"""Renumber every SEO page after page 56 without breaking internal links."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# Pages 56–62 are already correct. The remaining numbered pages are compacted
# first, followed by the keyword-led pages created in later batches.
RENUMBER = {
    "64-cataract-surgery-goregaon-east.html": "63-cataract-surgery-goregaon-east.html",
    "65-cataract-surgery-malad-east.html": "64-cataract-surgery-malad-east.html",
    "68-retina-specialist-goregaon-east.html": "65-retina-specialist-goregaon-east.html",
    "69-retina-specialist-malad-east.html": "66-retina-specialist-malad-east.html",
    "70-eye-hospital-malad-east.html": "67-eye-hospital-malad-east.html",
    "71-eye-doctor-malad-east.html": "68-eye-doctor-malad-east.html",
    "72-ophthalmologist-malad-east.html": "69-ophthalmologist-malad-east.html",
    "73-best-eye-hospital-malad-east.html": "70-best-eye-hospital-malad-east.html",
    "74-eye-clinic-malad-east.html": "71-eye-clinic-malad-east.html",
    "75-eye-hospital-malad-west.html": "72-eye-hospital-malad-west.html",
    "76-eye-doctor-malad-west.html": "73-eye-doctor-malad-west.html",
    "77-ophthalmologist-malad-west.html": "74-ophthalmologist-malad-west.html",
    "78-best-eye-hospital-malad-west.html": "75-best-eye-hospital-malad-west.html",
    "79-cataract-surgery-malad-west.html": "76-cataract-surgery-malad-west.html",
    "80-retina-specialist-malad-west.html": "77-retina-specialist-malad-west.html",
    "81-lasik-surgery-malad-west.html": "78-lasik-surgery-malad-west.html",
    "82-eye-checkup-malad-west.html": "79-eye-checkup-malad-west.html",
    "83-diabetic-eye-checkup-malad-west.html": "80-diabetic-eye-checkup-malad-west.html",
    "84-eye-clinic-malad-west.html": "81-eye-clinic-malad-west.html",
    "best-eye-hospital-in-goregaon-west.html": "82-best-eye-hospital-in-goregaon-west.html",
    "eye-clinic-in-goregaon-west.html": "83-eye-clinic-in-goregaon-west.html",
    "cataract-surgery-in-goregaon-west.html": "84-cataract-surgery-in-goregaon-west.html",
    "retina-specialist-in-goregaon-west.html": "85-retina-specialist-in-goregaon-west.html",
    "eye-checkup-in-goregaon-west.html": "86-eye-checkup-in-goregaon-west.html",
    "eye-hospital-in-kandivali.html": "87-eye-hospital-in-kandivali.html",
    "eye-doctor-in-kandivali.html": "88-eye-doctor-in-kandivali.html",
    "ophthalmologist-in-kandivali.html": "89-ophthalmologist-in-kandivali.html",
    "best-eye-hospital-in-kandivali.html": "90-best-eye-hospital-in-kandivali.html",
    "eye-clinic-in-kandivali.html": "91-eye-clinic-in-kandivali.html",
    "cataract-surgery-in-kandivali.html": "92-cataract-surgery-in-kandivali.html",
    "retina-specialist-in-kandivali.html": "93-retina-specialist-in-kandivali.html",
    "lasik-surgery-in-kandivali.html": "94-lasik-surgery-in-kandivali.html",
    "eye-checkup-in-kandivali.html": "95-eye-checkup-in-kandivali.html",
    "eye-hospital-in-borivali.html": "96-eye-hospital-in-borivali.html",
    "eye-doctor-in-borivali.html": "97-eye-doctor-in-borivali.html",
    "ophthalmologist-in-borivali.html": "98-ophthalmologist-in-borivali.html",
    "best-eye-hospital-in-borivali.html": "99-best-eye-hospital-in-borivali.html",
    "eye-clinic-in-borivali.html": "100-eye-clinic-in-borivali.html",
    "cataract-surgery-in-borivali.html": "101-cataract-surgery-in-borivali.html",
    "retina-specialist-in-borivali.html": "102-retina-specialist-in-borivali.html",
    "lasik-surgery-in-borivali.html": "103-lasik-surgery-in-borivali.html",
    "eye-checkup-in-borivali.html": "104-eye-checkup-in-borivali.html",
}


def all_project_text_files():
    yield from ROOT.glob("*.html")
    yield from (ROOT / "scripts").glob("*.py")
    yield ROOT / "replit.md"


def update_references():
    # Replace both file links and pretty-preview links.
    replacements = []
    for old, new in RENUMBER.items():
        replacements.append((old, new))
        replacements.append((old.removesuffix(".html"), new.removesuffix(".html")))
    for path in all_project_text_files():
        if path.resolve() == Path(__file__).resolve():
            continue
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def rename_files():
    staged = {}
    for old, new in RENUMBER.items():
        source = ROOT / old
        if source.exists():
            temporary = ROOT / f".renumber-staging-{old}"
            source.rename(temporary)
            staged[temporary] = ROOT / new
    for temporary, destination in staged.items():
        temporary.rename(destination)


def update_index_labels():
    index = ROOT / "index.html"
    text = index.read_text(encoding="utf-8")
    for old, new in RENUMBER.items():
        # The link target has already been updated; make the visible label
        # numeric as well, including the previously "New." keyword batches.
        old_num = re.match(r"^(\d+)-", old)
        new_num = re.match(r"^(\d+)-", new)
        if old_num and new_num:
            text = re.sub(
                rf'(href="/{re.escape(new)}"[^>]*>){re.escape(old_num.group(1))}\.',
                rf'\g<1>{new_num.group(1)}.',
                text,
            )
        elif "goregaon-west" in old or "kandivali" in old or "borivali" in old:
            text = text.replace(f'href="/{new}">New. ', f'href="/{new}">{new_num.group(1)}. ')
    index.write_text(text, encoding="utf-8")


def main():
    rename_files()
    update_references()
    update_index_labels()
    print(f"Renumbered {len(RENUMBER)} pages after page 56.")


if __name__ == "__main__":
    main()