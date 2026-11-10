# Figure guide

## Biological notebook: `notebooks/10_Biological_Results.ipynb`

1. **Mean TAA RNA expression by cancer type:** each cell is a cohort-average log2(TPM+1) for a given TAA.
2. **Relative expression heatmap:** values are cohort-mean z-scores **within each gene** across cancer cohorts.
3. **Within- and between-cohort RNA heterogeneity:** boxplots of individual tumor expression values.
4. **Feature-group ablation:** held-out R² by TAA and data modality. Requires `09_Feature_Group_Ablation.ipynb` results.
5. **Predicted vs observed:** paired held-out test predictions for EPCAM, FOLR1, ERBB2 and CD276. A dot is one tumor, and the dashed line denotes equality of axes.

## Deep learning notebook: `notebooks/07_Deep_Learning_Results.ipynb`

- Mean R² by neural network experiment.
- Per-target R² by experiment.
- Validation loss by experiment.
- Per-target metrics, best models and spreadsheet export are also available.

**Reference scope:** Based on public TCGA/GDC tumor cohorts and conventional expression-unit definitions. No citations to individual papers have been verified here; add independently verified primary citations before formal publication.
