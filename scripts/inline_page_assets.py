"""Embed shared page CSS into every post-56 page for Elementor uploads."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SHARED_CSS = ROOT / "malad-west-seo-pages.css"


def target_files():
    numbered = []
    for path in ROOT.glob("*.html"):
        match = re.match(r"^(\d+)-", path.name)
        if match and int(match.group(1)) >= 56:
            numbered.append(path)
    # These five are the new post-84 Goregaon West pages and use the same
    # Elementor-ready page system, even though their filenames are keyword-led.
    numbered.extend(ROOT / name for name in (
        "best-eye-hospital-in-goregaon-west.html",
        "eye-clinic-in-goregaon-west.html",
        "cataract-surgery-in-goregaon-west.html",
        "retina-specialist-in-goregaon-west.html",
        "eye-checkup-in-goregaon-west.html",
    ))
    return sorted(set(numbered))


def inline_css(html: str, css: str) -> str:
    css_tag = f'<style data-sentra-page-css="inline">\n{css}\n</style>'
    pattern = r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\'][^"\']*malad-west-seo-pages\.css[^"\']*["\'][^>]*>\s*'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, css_tag + "\n", html, count=1, flags=re.I)
    return html


def main():
    css = SHARED_CSS.read_text(encoding="utf-8")
    for path in target_files():
        html = path.read_text(encoding="utf-8")
        updated = inline_css(html, css)
        path.write_text(updated, encoding="utf-8")
        print(f"{path.name}: inline_css={'yes' if updated != html else 'already-present'}")


if __name__ == "__main__":
    main()