# TCGA TAA Deep Learning Pipeline — Notebook Edition

This repository contains a Jupyter-notebook-based deep learning pipeline for predicting tumor-associated antigen (TAA) RNA expression from TCGA multi-omic features.

The project is intentionally deep-learning focused. It evaluates neural network architectures rather than treating linear/logistic regression as the center of the project.

## Project goal

Predict RNA expression for 10 TAA genes:

```text
ERBB2, FOLR1, MUC16, CD276, NECTIN4, TACSTD2, CLDN6, EPCAM, MSLN, MUC1
```

from:

```text
clinical/cancer type features + mutation features + gene-level copy-number features
```

## Experiments

| Experiment | Notebook | Purpose |
|---|---|---|
| 1 | `02_Experiment_1_Standard_MLP.ipynb` | Baseline feedforward neural network |
| 2 | `03_Experiment_2_Dropout_Comparison.ipynb` | Dropout/no-dropout regularization comparison |
| 3 | `04_Experiment_3_BatchNorm_Comparison.ipynb` | Batch normalization vs no batch normalization |
| 4 | `05_Experiment_4_Residual_MLP.ipynb` | Residual MLP with skip connections |
| 5 | `06_Experiment_5_MultiBranch_MultiTask.ipynb` | Multi-branch, multi-task model with clinical, mutation, and copy-number branches |

## Expected data layout

Raw data is **not included** in this repo because the GDC download is very large.

After adding your data, the repo should look like this:

```text
tcga-taa-deep-learning/
  data/
    raw/
      copy_number/
        files/
        download_info/
      mutation/
        files/
        download_info/
      clinical/
        biospecimen.cart.2026-07-09/
        clinical.cart.2026-07-09/
      rna_expression/
        files/
        download_info/
    processed/
```

The code assumes this structure but does not require hardcoded Mac paths.

## Important GitHub note

Do **not** commit the 40GB raw GDC data to GitHub. This repo's `.gitignore` excludes `data/raw/**`.

For GitHub/class submission, include code and notebooks. Locally, add raw data under `data/raw/` before running data processing.

## Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

Start Jupyter from the repo root:

```bash
jupyter notebook
```

## How to run

Run notebooks in this order:

```text
00_Project_Setup_and_Validation.ipynb
01_Data_Processing_Pipeline.ipynb
02_Experiment_1_Standard_MLP.ipynb
03_Experiment_2_Dropout_Comparison.ipynb
04_Experiment_3_BatchNorm_Comparison.ipynb
05_Experiment_4_Residual_MLP.ipynb
06_Experiment_5_MultiBranch_MultiTask.ipynb
07_Results_Excel_and_Visuals.ipynb
```

The shared training/modeling code is in:

```text
notebooks/_Shared_Training_Utilities.ipynb
```

Each experiment notebook loads this shared notebook with `%run` logic.

## Output folders

```text
data/processed/
  modeling_table.csv
  rna_taa_case_level.csv
  copy_number_case_level.csv
  mutation_case_level.csv
  clinical_features_case_level.csv

results/
  metrics/
  predictions/
  histories/
  configs/
  models/

reports/
  figures/
  tcga_taa_experiment_summary.xlsx
```

## Re-running experiments only

If `data/processed/modeling_table.csv` already exists, you can skip raw data processing and run only the experiment notebooks.

## Course-module alignment

This project directly connects to:

- Feedforward neural networks
- Backpropagation
- Regularization
- Batch normalization
- Residual connections
- Representation learning
- Multi-task learning
- Biologically motivated multi-branch neural networks
