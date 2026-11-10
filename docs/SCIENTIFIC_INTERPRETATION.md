# Scientific interpretation and reproducibility

## Data-generating process

- **Predictors (X):** cancer cohort and clinical annotations, gene-level copy-number alterations and DNA-derived somatic mutation calls.
- **Outcomes (y):** expression of ten tumor-associated antigen genes measured from RNA-seq, transformed as log2(TPM + 1).
- RNA expression columns must **never** be included in X. The same cohort can contain both expression targets and independent DNA/clinical features without making RNA expression a predictor.

## Biological figure interpretation

| Visualization | What it answers | Important limitation |
| --- | --- | --- |
| Mean RNA expression heatmap | Where is each TAA transcript abundant on average? | RNA is not cell-surface protein |
| Within-gene z-score heatmap | In which cancer cohorts is each TAA **relatively** enriched? | Z-scores are relative to each gene's cohort mean |
| Cohort expression boxplots | How heterogeneous is transcript abundance across patients? | Individual tumors are bulk tissue mixtures |
| Feature-group ablation heatmap | Which sets of **non-RNA** predictors provide signal for each TAA? | Predictive contributions are not causal |
| Observed-versus-predicted scatterplots | How close are held-out sample-level model predictions to measured RNA expression? | One train/test split does not establish clinical utility |

## Feature ablation audit

The original ad-hoc ablation code risked inadvertently assigning `project_id_cn` or `project_id_mut` (cohort metadata) to gene-level feature groups. The revised `09_Feature_Group_Ablation.ipynb` uses the explicit `copy_number_feature_genes` and `mutation_feature_genes` lists in `config/genes.json`. Clinical/cancer type is isolated into its own group. Consequently, earlier and new ablation heatmaps should not be compared as identical analyses.

All ablation variants use one held-out split and fit imputation, encoding, and target scaling on training data. Random seeds are set before model initialization. Repeat across multiple seeds and split designs for reliable comparative inference.

## Reporting boundaries

These outputs cannot establish causal mechanisms regulating TAA expression, tumor-specific cell-surface protein, on-target/off-tumor toxicity, patient eligibility for therapy, or clinical treatment response. Consider independent protein-level assays, normal-tissue expression, immune/microenvironment annotations and held-out cancer validation.

## Verification status

Notebook syntax/structure and branch contents can be inspected on GitHub. Real-data end-to-end execution and the revised ablation figures have not yet been independently rerun inside GitHub; a fully validated claim requires executing the workflows in the project's Python environment.
