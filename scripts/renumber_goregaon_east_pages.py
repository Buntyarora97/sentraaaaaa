"""Give the remaining unnumbered Goregaon East pages numbers 105–109."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = {
    "best-eye-hospital-in-goregaon-east.html": "105-best-eye-hospital-in-goregaon-east.html",
    "eye-clinic-and-checkup-in-goregaon-east.html": "106-eye-clinic-and-checkup-in-goregaon-east.html",
    "eye-doctor-in-goregaon-east.html": "107-eye-doctor-in-goregaon-east.html",
    "eye-hospital-in-goregaon-east.html": "108-eye-hospital-in-goregaon-east.html",
    "ophthalmologist-in-goregaon-east.html": "109-ophthalmologist-in-goregaon-east.html",
}


def text_files():
    yield from ROOT.glob("*.html")
    yield from ROOT.glob("*.py")
    yield from (ROOT / "scripts").glob("*.py")


def main():
    staged = {}
    for old, new in MAPPING.items():
        source = ROOT / old
        if source.exists():
            temporary = ROOT / f".east-renumber-{old}"
            source.rename(temporary)
            staged[temporary] = ROOT / new
    for temporary, destination in staged.items():
        temporary.rename(destination)

    replacements = []
    for old, new in MAPPING.items():
        replacements.append((old, new))
        replacements.append((f"/{old}", f"/{new}"))
        old_slug = old.removesuffix(".html")
        new_slug = new.removesuffix(".html")
        replacements.append((f"/{old_slug}/", f"/{new_slug}/"))

    for path in text_files():
        if path.resolve() == Path(__file__).resolve() or not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")

    index = ROOT / "index.html"
    index_text = index.read_text(encoding="utf-8")
    entries = "\n".join(
        f'    <li><a href="/{filename}">{number}. {label}</a></li>'
        for number, (filename, label) in enumerate(
            (
                (MAPPING["best-eye-hospital-in-goregaon-east.html"], "Best Eye Hospital in Goregaon East"),
                (MAPPING["eye-clinic-and-checkup-in-goregaon-east.html"], "Eye Clinic & Checkup in Goregaon East"),
                (MAPPING["eye-doctor-in-goregaon-east.html"], "Eye Doctor in Goregaon East"),
                (MAPPING["eye-hospital-in-goregaon-east.html"], "Eye Hospital in Goregaon East"),
                (MAPPING["ophthalmologist-in-goregaon-east.html"], "Ophthalmologist in Goregaon East"),
            ),
            start=105,
        )
    )
    if "105-best-eye-hospital-in-goregaon-east.html" not in index_text:
        index_text = index_text.replace("</ul>", entries + "\n  </ul>", 1)
    else:
        for line in entries.splitlines():
            href = line.split('href="', 1)[1].split('"', 1)[0]
            index_text = "\n".join(
                line if href in current else current
                for current in index_text.splitlines()
            )
    index.write_text(index_text, encoding="utf-8")
    print("Renumbered five Goregaon East pages as 105–109.")


if __name__ == "__main__":
    main()