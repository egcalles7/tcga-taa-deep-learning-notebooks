#!/usr/bin/env python3
"""Update the original UNC ABRCMS editable poster.

Usage:
    python scripts/update_abrcms_poster.py \
      "poster/source/UNC_ABRCMS_4_Column(1).pptx" \
      "poster/UNC_ABRCMS_4_Column_QR_Expanded_Findings.pptx"
"""
import argparse
from io import BytesIO
from pathlib import Path

import qrcode
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

REPOSITORY_URL = "https://github.com/egcalles7/tcga-taa-deep-learning-notebooks"

FINDINGS = [
    "Non-RNA tumor features predict TAA RNA expression, but accuracy varies across antigens.",
    "Copy-number features often outperform mutation-only inputs, suggesting complementary predictive information.",
    "ERBB2 is relatively enriched in BRCA; FOLR1/MUC16/MSLN in OV; EPCAM in COAD/READ.",
    "EPCAM shows stronger agreement (R² ≈ 0.64) than CD276/B7-H3 (R² ≈ 0.19); protein-level validation remains essential.",
]

def update(input_path: Path, output_path: Path) -> None:
    prs = Presentation(str(input_path))
    if len(prs.slides) != 1:
        raise ValueError("Expected one poster slide")
    slide = prs.slides[0]

    def find(text):
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text.strip().startswith(text):
                return shape
        raise ValueError(f"Could not locate text shape: {text}")

    key = find("Non-RNA tumor features predict")
    old_followup = find("RNA predictions can guide")
    key.left, key.top = Inches(1.72), Inches(32.01)
    key.width, key.height = Inches(24.55), Inches(2.33)
    tf = key.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(.04)
    tf.margin_right = Inches(.03)
    tf.margin_top = Inches(.02)
    tf.margin_bottom = Inches(.02)
    for idx, finding in enumerate(FINDINGS):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = "▪  " + finding
        p.font.name = "Arial"
        p.font.size = Pt(21)
        p.font.color.rgb = RGBColor(17, 43, 77)
        p.space_before = Pt(1)
        p.space_after = Pt(4)
    old_followup.text = ""

    for prefix in ("Validate in independent", "Jonathan Schlosser:",
                   "Future work", "Acknowledgments"):
        find(prefix).width = Inches(11.85)

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14, border=4
    )
    qr.add_data(REPOSITORY_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    slide.shapes.add_picture(buffer, Inches(43.35), Inches(31.65),
                             width=Inches(2.80), height=Inches(2.80))

    label = slide.shapes.add_textbox(Inches(40.05), Inches(31.45), Inches(3.15), Inches(.45))
    p = label.text_frame.paragraphs[0]
    p.text = "Code & Repository"
    p.font.name = "Arial"
    p.font.bold = True
    p.font.size = Pt(24)
    p.font.color.rgb = RGBColor(17, 43, 77)

    caption = slide.shapes.add_textbox(Inches(40.05), Inches(32.12), Inches(3.10), Inches(1.20))
    p = caption.text_frame.paragraphs[0]
    p.text = "Scan to view\nGitHub project"
    p.font.name = "Arial"
    p.font.size = Pt(21)
    p.font.color.rgb = RGBColor(17, 43, 77)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_path))
    print(f"Saved editable poster: {output_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    update(args.input, args.output)
