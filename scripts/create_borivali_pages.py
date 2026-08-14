"""Create the nine Borivali SEO pages from the verified Kandivali topic set."""

from pathlib import Path

from create_kandivali_pages import (
    PAGES,
    ROOT,
    replace_location,
    update_metadata,
    inline_css,
    visible_words,
)


def borivali_text(value: str) -> str:
    value = (
        value.replace("Kandivali", "Borivali")
        .replace("kandivali", "borivali")
        .replace("KANDIVALI", "BORIVALI")
    )
    return value.replace("/14-eye-specialist-borivali.html", "/15-eye-specialist-borivali.html")


def main():
    for source_name, output_name, title, description, heading, paragraphs in PAGES:
        output_name = output_name.replace("kandivali", "borivali")
        title = borivali_text(title)
        description = borivali_text(description)
        heading = borivali_text(heading)
        paragraphs = [borivali_text(p) for p in paragraphs]

        html = (ROOT / source_name).read_text(encoding="utf-8")
        html = replace_location(html)
        html = borivali_text(html)
        html = update_metadata(html, output_name, title, description)
        html = inline_css(html)
        section = f'<section class="sc-section sc-section-alt"><h2>{heading}</h2>'
        section += "".join(f"<p>{p}</p>" for p in paragraphs) + "</section>"
        marker = '<div class="sc-cta">'
        if marker not in html:
            raise RuntimeError(f"CTA marker missing in {source_name}")
        html = html.replace(marker, section + "\n\n" + marker, 1)
        count = visible_words(html)
        if count < 2000:
            raise RuntimeError(f"{output_name} has only {count} visible words")
        (ROOT / output_name).write_text(html, encoding="utf-8")
        print(f"{output_name}: {count} words, {html.count('<img')} images")


if __name__ == "__main__":
    main()