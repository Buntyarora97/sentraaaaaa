"""Clean up duplicated numbering introduced while updating post-56 links."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGET_LABELS = {
    "82-best-eye-hospital-in-goregaon-west.html": "82. Best Eye Hospital in Goregaon West",
    "83-eye-clinic-in-goregaon-west.html": "83. Eye Clinic in Goregaon West",
    "84-cataract-surgery-in-goregaon-west.html": "84. Cataract Surgery in Goregaon West",
    "85-retina-specialist-in-goregaon-west.html": "85. Retina Specialist in Goregaon West",
    "86-eye-checkup-in-goregaon-west.html": "86. Eye Checkup in Goregaon West",
    "87-eye-hospital-in-kandivali.html": "87. Eye Hospital in Kandivali",
    "88-eye-doctor-in-kandivali.html": "88. Eye Doctor in Kandivali",
    "89-ophthalmologist-in-kandivali.html": "89. Ophthalmologist in Kandivali",
    "90-best-eye-hospital-in-kandivali.html": "90. Best Eye Hospital in Kandivali",
    "91-eye-clinic-in-kandivali.html": "91. Eye Clinic in Kandivali",
    "92-cataract-surgery-in-kandivali.html": "92. Cataract Surgery in Kandivali",
    "93-retina-specialist-in-kandivali.html": "93. Retina Specialist in Kandivali",
    "94-lasik-surgery-in-kandivali.html": "94. LASIK Surgery in Kandivali",
    "95-eye-checkup-in-kandivali.html": "95. Eye Checkup in Kandivali",
    "96-eye-hospital-in-borivali.html": "96. Eye Hospital in Borivali",
    "97-eye-doctor-in-borivali.html": "97. Eye Doctor in Borivali",
    "98-ophthalmologist-in-borivali.html": "98. Ophthalmologist in Borivali",
    "99-best-eye-hospital-in-borivali.html": "99. Best Eye Hospital in Borivali",
    "100-eye-clinic-in-borivali.html": "100. Eye Clinic in Borivali",
    "101-cataract-surgery-in-borivali.html": "101. Cataract Surgery in Borivali",
    "102-retina-specialist-in-borivali.html": "102. Retina Specialist in Borivali",
    "103-lasik-surgery-in-borivali.html": "103. LASIK Surgery in Borivali",
    "104-eye-checkup-in-borivali.html": "104. Eye Checkup in Borivali",
}


def project_files():
    yield from ROOT.glob("*.html")
    yield from (ROOT / "scripts").glob("*.py")


def main():
    replacements = {}
    for filename in TARGET_LABELS:
        number, rest = filename.split("-", 1)
        replacements[f"{number}-{filename}"] = filename
        replacements[f"/{number}-{filename}"] = f"/{filename}"
    replacements.update({
        "90-best-eye-hospital-in-kandivali.html": "90-best-eye-hospital-in-kandivali.html",
        "/90-best-eye-hospital-in-kandivali.html": "/90-best-eye-hospital-in-kandivali.html",
        "90-best-eye-hospital-in-kandivali": "90-best-eye-hospital-in-kandivali",
        "/90-best-eye-hospital-in-kandivali": "/90-best-eye-hospital-in-kandivali",
        "99-best-eye-hospital-in-borivali.html": "99-best-eye-hospital-in-borivali.html",
        "/99-best-eye-hospital-in-borivali.html": "/99-best-eye-hospital-in-borivali.html",
        "99-best-eye-hospital-in-borivali": "99-best-eye-hospital-in-borivali",
        "/99-best-eye-hospital-in-borivali": "/99-best-eye-hospital-in-borivali",
    })

    for path in project_files():
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")

    index = ROOT / "index.html"
    lines = index.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        for filename, label in TARGET_LABELS.items():
            if filename in line:
                lines[i] = f'    <li><a href="/{filename}">{label}</a></li>'
                break
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Cleaned numbered filenames in HTML, index and generators.")


if __name__ == "__main__":
    main()