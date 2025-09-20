import os
import pandas as pd
from evaluate import load
from bert_score import score
from tqdm import tqdm
import torch

# Optional: Enable COMET (set to True if needed)
use_comet = True
if use_comet:
    from comet import download_model, load_from_checkpoint

# Check GPU availability
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"🖥️  Using device: {device.upper()}")

# Load reference and system outputs
reference_file = "Hindi_Gold_Group1.txt"
systems_folder = "group1"

with open(reference_file, 'r', encoding='utf-8') as f:
    references = [line.strip() for line in f.readlines()]

# Load metric scorers
bleu = load("bleu")
meteor = load("meteor")
ter = load("ter")
chrf = load("chrf")

# Load COMET model (optional)
if use_comet:
    print("📦 Loading COMET model...")
    comet_model_path = download_model("Unbabel/wmt22-comet-da")
    comet_model = load_from_checkpoint(comet_model_path)

results = []

# Iterate through system outputs
print(f"\n🔍 Evaluating {len(os.listdir(systems_folder))} system outputs...\n")
for idx, filename in enumerate(tqdm(sorted(os.listdir(systems_folder))), 1):
    system_path = os.path.join(systems_folder, filename)

    with open(system_path, 'r', encoding='utf-8') as f:
        predictions = [line.strip() for line in f.readlines()]

    if len(predictions) != len(references):
        print(f" ⚠️  Skipping {filename}: mismatched line count.")
        continue

    # Compute BLEU
    bleu_score = bleu.compute(predictions=predictions, references=[[ref] for ref in references])["bleu"]

    # Compute METEOR
    meteor_score = meteor.compute(predictions=predictions, references=references)["meteor"]

    # Compute TER
    try:
        ter_result = ter.compute(predictions=predictions, references=references)
        ter_score = ter_result.get("ter", list(ter_result.values())[0])
    except Exception as e:
        print(f" ⚠️  TER failed for {filename}: {e}")
        ter_score = None

    # Compute CHRF++
    chrf_score = chrf.compute(predictions=predictions, references=references)["score"]

    # Compute BERTScore (with GPU)
    try:
        P, R, F1 = score(predictions, references, lang="hi", verbose=False, device=device)
        bert_score = F1.mean().item()
    except Exception as e:
        print(f" ⚠️  BERTScore failed for {filename}: {e}")
        bert_score = None

    # Compute COMET (with GPU)
    if use_comet:
        try:
            data = [{"src": "", "mt": pred, "ref": ref} for pred, ref in zip(predictions, references)]
            comet_output = comet_model.predict(data, batch_size=32, gpus=1, accelerator="gpu")
            comet_score = comet_output.system_score
        except Exception as e:
            print(f" ⚠️  COMET failed for {filename}: {e}")
            comet_score = None
    else:
        comet_score = "N/A"

    # Save results
    results.append({
        "System": filename,
        "BLEU": round(bleu_score * 100, 2),
        "METEOR": round(meteor_score * 100, 2),
        "TER": round(ter_score * 100, 2) if ter_score is not None else "N/A",
        "CHRF++": round(chrf_score, 2),
        "BERTScore": round(bert_score * 100, 2) if bert_score is not None else "N/A",
        "COMET": round(comet_score * 100, 2) if isinstance(comet_score, float) else "N/A"
    })

# Save to Excel
df = pd.DataFrame(results)
df.sort_values(by="BLEU", ascending=False, inplace=True)
df.to_excel("Group1-1.6k.xlsx", index=False)

print("\n✅ Evaluation completed and saved to 'MT_Evaluation_English_to_Hindi_GPU.xlsx'")
