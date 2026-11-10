# TCGA Tumor-Associated Antigen RNA Prediction

**Biology first, modeling as the tool.** This project investigates whether **non-RNA tumor features** predict expression of ten tumor-associated antigen (TAA) genes across ten TCGA cancer cohorts.

RNA sequencing (**RNA-seq**) provides the **observed response labels** (log2[TPM+1] TAA RNA expression); it is **not** used as an input feature. Inputs comprise cancer type and clinical annotations, DNA-derived copy number, and somatic mutation calls.

## Biological questions

1. Which TAA transcripts are relatively enriched in specific cancer cohorts?
2. How much does TAA expression vary among tumors within the same cancer type?
3. Which non-RNA feature groups have predictive associations with specific TAAs?
4. Which TAA RNA expression patterns can the neural network reproduce on held-out tumor samples?

Targets: `ERBB2`, `FOLR1`, `MUC16`, `CD276`, `NECTIN4`, `TACSTD2`, `CLDN6`, `EPCAM`, `MSLN`, `MUC1`.

Cohorts: TCGA-BRCA, OV, UCEC, LUAD, LUSC, BLCA, HNSC, STAD, COAD and READ.

## Notebook roadmap

| Notebook | Purpose |
| --- | --- |
| `00_Project_Overview.ipynb` | Study objectives |
| `00_Project_Setup_and_Validation.ipynb` | Environment and input checks |
| `01_Data_Processing_Pipeline.ipynb` | Optional raw GDC-to-modeling table pipeline |
| `02_Experiment_1_Standard_MLP.ipynb` | Standard multilayer perceptron |
| `03_Experiment_2_Dropout_Comparison.ipynb` | Regularization/dropout comparisons |
| `04_Experiment_3_BatchNorm_Comparison.ipynb` | Batch-normalization comparison |
| `05_Experiment_4_Residual_MLP.ipynb` | Residual architecture |
| `06_Experiment_5_MultiBranch_MultiTask.ipynb` | Multi-branch model |
| **`07_Deep_Learning_Results.ipynb`** | **Model metrics, per-target R² and validation loss** |
| **`08_Run_All_Notebooks.ipynb`** | **Connected runner: reports / train / full** |
| **`09_Feature_Group_Ablation.ipynb`** | **Retrain one multi-output MLP with five feature subsets** |
| **`10_Biological_Results.ipynb`** | **Five biological displays: mean and relative TAA expression; heterogeneity; ablation; observed vs predicted** |
| **`11_Export_Results_Tables.ipynb`** | **CSV and optional Excel reporting** |
| `_Shared_Training_Utilities.ipynb` | Common training functions |

## Quick start

1. Clone the repository and install `requirements.txt` in a Python environment.
2. Open Jupyter in VS Code; choose a kernel using that environment.
3. Use the already-tracked `data/processed/modeling_table.csv` for analysis, without downloading raw TCGA files.
4. Open `notebooks/08_Run_All_Notebooks.ipynb`. Set `MODE = "reports"` to render figures using existing saved model outputs. Missing prediction or ablation CSVs are reported without inventing results.
5. Set `MODE = "train"` to run all model comparisons, regenerate a **corrected ablation analysis**, and then render reports. `MODE = "full"` additionally executes the raw pipeline and requires the full raw GDC dataset.

The runner saves executed notebook copies under `notebooks/executed/`. Outputs are written under `reports/` and `results/`. No raw data are committed by the revised workflow.

## Scientific cautions

- RNA abundance is **not** measured cell-surface protein density or treatment response.
- Feature-group ablation compares predictive information from different modality subsets; **it is not evidence of causality**.
- Relative heatmaps are normalized separately for each gene, and must not be read as an absolute cross-gene comparison.
- If the earlier ablation code inadvertently used cohort identifier columns in gene-only models, **rerun notebook 09** before making conclusions from those legacy ablation plots.
- Shared train/validation/test splits, train-only imputation/scaling, and repeated independent evaluation remain important. Model superiority has not been established from a single random split alone.

More details are in [Scientific interpretation](docs/SCIENTIFIC_INTERPRETATION.md).

## Original files preserved

The original combined metrics/biology notebook, original run-all notebook and original README are copied to `archive/pre-report-split/`. Git history also retains prior commits. The new organization is proposed through a **draft pull request**; `main` remains unchanged until you merge.

### Data provenance

Source: TCGA/GDC public data. RNA-seq supplies the TAA expression target values; copy-number and somatic mutation features are DNA-derived. No patient-level protein, clinical response, or experimental validation is claimed.
