# Model Evaluation Metrics

This document outlines the **objective metrics** used to evaluate segmentation models trained on brain tumor datasets (BraTS‑23, BraTS‑24, Doctor‑65), ensuring **consistent benchmarking**, **traceable progress**, and **clinical relevance**.

---

## Core Metrics

### 1. **Dice Similarity Coefficient (DSC)**

- **Purpose**: Measures overlap between predicted and ground truth masks.
- **Range**: 0 (no overlap) to 1 (perfect overlap).
- **Reported For**:
  - **Whole Tumor (WT)**
  - **Tumor Core (TC)**
  - **Enhancing Tumor (ET)**
- **Formula**:

```text
Dice = (2 × |P ∩ G|) / (|P| + |G|)
```

where `P` = prediction, `G` = ground truth.

---

### 2. **Hausdorff Distance (95th percentile) – HD95**

- **Purpose**: Captures boundary alignment between predictions and ground truth, robust to outliers.
- **Interpretation**: Lower is better (in mm).
- **Reported For**:
- WT, TC, ET (if available)

---

### 3. **Recall / Sensitivity**

- **Purpose**: Measures how much of the actual tumor is correctly detected.
- **Important for**: Clinical safety – avoiding missed tumor regions.
- **Reported For**:
- Doctor‑65 → recall for WT on 10‑patient test set.

---

## Dataset-Specific Requirements

| Dataset      | Metric(s) Required                                          | Evaluation Method            |
|--------------|-------------------------------------------------------------|-------------------------------|
| **BraTS‑23** | Dice (WT/TC/ET), HD95 (WT/TC/ET)                             | 5‑fold Cross‑Validation       |
| **BraTS‑24** | Same as above, **stratified** for treatment-naïve vs post-treatment cases | 5‑fold Cross‑Validation |
| **Doctor‑65**| Dice (WT), **Recall (WT)** on 10‑patient hold‑out set       | Single test split             |
