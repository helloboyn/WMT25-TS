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





