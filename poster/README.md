# UNC ABRCMS 2026 Poster

The editable PowerPoint is created **inside GitHub**, not downloaded from ChatGPT.

## Add the original once

1. In this repository, choose branch `chore/biological-deep-learning-report-split-2026`.
2. Open `poster/source/` and use **Add file → Upload files**.
3. Upload the **original**, unedited PowerPoint from your Mac, with the exact filename:
   `UNC_ABRCMS_4_Column(1).pptx`.
4. Choose **Commit changes** to this branch.
5. The **Build editable ABRCMS poster** GitHub Action should run on that upload and create `poster/UNC_ABRCMS_4_Column_QR_Expanded_Findings.pptx` automatically.
6. Open the new file in the GitHub repository and use its **Download raw file** icon.

The script preserves the original slide's other graphics and editable text, expands four key findings, and adds a scannable repository QR at the lower-right.

## Manual alternative inside Codespaces

```bash
python -m pip install python-pptx 'qrcode[pil]'
python scripts/update_abrcms_poster.py \
  'poster/source/UNC_ABRCMS_4_Column(1).pptx' \
  'poster/UNC_ABRCMS_4_Column_QR_Expanded_Findings.pptx'
```

Check the generated slide in PowerPoint/Keynote before submitting or printing. Existing biological result figures are retained as in the original uploaded slide.
