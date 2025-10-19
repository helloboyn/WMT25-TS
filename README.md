## 📄 Research Paper
[Evaluation of LLM for English to Hindi Legal Domain Machine Translation Systems(WMT25)]([https://arxiv.org/new-id](https://www2.statmt.org/wmt25/pdf/2025.wmt-1.57.pdf))

# Test Suite Submission – WMT-TS

**Test Suite Name**: Legal Domain English-Hindi Test Suite  
**Institution**: AI & NLP Research Group, IIT Patna  
**Contact Email**: boynfrancis[at]gmail[.]com  


# WMT-TS Test Suite Submission – English to Hindi (Legal Domain)

## Overview

This repository contains a test dataset prepared for the **WMT-TS Shared Task** on English to Hindi Machine Translation, specifically targeting the **Legal domain**.

- **Language Pair:** [English](https://github.com/helloboyn/AACL25-MT/blob/main/eng-hin-test.eng.txt) → [Hindi](https://github.com/helloboyn/AACL25-MT/blob/main/eng-hin-test.hin.txt)  
- **Domain:** Legal  
- **Total Sentences:** 5,000  
- **Word Count Distribution:** 100 sentences each for word lengths from **5 to 54** words

---

## Objective

The goal of this test suite is to benchmark machine translation systems' performance in the legal domain across varying sentence lengths. This allows for fine-grained analysis of model behavior and robustness in legal language contexts.

---

## Dataset Structure

| Word Count | Number of Sentences |
|------------|---------------------|
| 5          | 100                 |
| 6          | 100                 |
| 7          | 100                 |
| ...        | ...                 |
| 54         | 100                 |
| **Total**  | **5000**            |

Each group contains 100 English-Hindi parallel sentence pairs from legal texts such as:
- Court judgments
- Contracts
- Legal notices
- Statutory documents

---

## Data Preparation

- **Source Collection:** Public domain and open-licensed legal corpora
- **Cleaning & Filtering:** Tokenized, length-filtered (5–54 words), de-duplicated
- **Alignment:** English-Hindi aligned with semi-automatic tools + manual verification
- **Validation:** 10% of the dataset manually reviewed for quality and domain accuracy

---

## Intended Use

- For **testing and evaluation** only (not training)
- Suitable for assessing translation quality across sentence lengths in the legal domain
- Recommended for use in WMT-TS Shared Task submissions

---

Cite this Paper:
```
@InProceedings{singh-kumar-ekbal:2025:WMT2,
  author    = {Singh, Kshetrimayum Boynao  and  Kumar, Deepak  and  Ekbal, Asif},
  title     = {Evaluation of LLM for English to Hindi Legal Domain Machine Translation Systems},
  booktitle      = {Proceedings of the Tenth Conference on Machine Translation (WMT 2025)},
  month          = {November},
  year           = {2025},
  address        = {Suzhou, China},
  publisher      = {Association for Computational Linguistics},
  pages     = {823--833},
  abstract  = {The study critically examines various Machine Translation systems, particularly focusing on Large Language Models, using the WMT25 Legal Domain Test Suite for translating English into Hindi. It utilizes a dataset of 5,000 sentences designed to capture the complexity of legal texts based on word frequency ranges from 5 to 54. Each frequency range contains 100 sentences, collectively forming a corpus that spans from simple legal terms to intricate legal provisions. Six metrics were used to evaluate the performance of the system: BLEU, METEOR, TER, CHRF++, BERTScore and COMET. The findings reveal diverse capabilities and limitations of LLM architectures in handling complex legal texts. Notably, Gemini-2.5-Pro, Claude-4, and ONLINE-B topped the performance charts in terms of human evaluation, showcasing the potential of LLMs for nuanced translation. Despite these advances, the study identified areas for further research, especially in improving robustness, reliability, and explainability for use in critical legal contexts. The study also supports the WMT25 subtask focused on evaluating the weaknesses of large language models (LLMs). The dataset and related resources are publicly available at https://github.com/helloboyn/WMT25-TS.},
  url       = {https://aclanthology.org/2025.wmt-1.57}
}

```






