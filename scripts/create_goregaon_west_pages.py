"""Create the five Goregaon West SEO pages from the clinic's finished templates.

The source pages are intentionally different topics.  Location wording, metadata,
canonical URLs, navigation labels and a topic-specific Goregaon West section are
updated here so future edits can be regenerated without hand-editing five HTML
files.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PHONE = "9372947075"
WHATSAPP = "https://wa.me/919372947075"
SHARED_CSS = (ROOT / "malad-west-seo-pages.css").read_text(encoding="utf-8")

PAGES = [
    {
        "source": "75-best-eye-hospital-malad-west.html",
        "output": "82-best-eye-hospital-in-goregaon-west.html",
        "title": "Best Eye Hospital in Goregaon West | Sentra Clinic",
        "description": "Looking for the best eye hospital in Goregaon West? Compare doctor-led diagnosis, cataract, retina, LASIK guidance and follow-up at Sentra Clinic, Malad East.",
        "section": (
            "A thoughtful choice for Goregaon West patients",
            [
                "Families in Goregaon West often compare a neighbourhood eye clinic, an optical store and a larger hospital before booking. The right choice depends on the problem that needs attention, not simply on the size of the building or the strongest online claim. Someone looking for cataract advice needs lens and retina assessment; a person with diabetes needs retinal surveillance; a child needs age-appropriate visual evaluation. Sentra Clinic gives patients travelling from Goregaon West a doctor-led starting point in nearby Malad East.",
                "A useful first appointment should answer practical questions. Who will examine the eyes? Which investigation is relevant and why? Is the recommended treatment urgent, optional or something that can be monitored? What alternatives and follow-up are available? Patients should be able to ask these questions without feeling pressured to purchase a package or decide about elective surgery immediately. Clear explanations are a meaningful part of quality eye care.",
                "The journey from Goregaon West to Rani Sati Road, Malad East is also relevant when follow-up may be needed. Before travelling, call the clinic with the patient’s age, symptoms and previous recommendation. Carry original reports, current glasses and medicine details. A convenient, continuous care plan is more useful than a one-time consultation that leaves the family unsure about what to do next.",
            ],
        ),
    },
    {
        "source": "81-eye-clinic-malad-west.html",
        "output": "83-eye-clinic-in-goregaon-west.html",
        "title": "Eye Clinic in Goregaon West | Sentra Clinic",
        "description": "Find an eye clinic in Goregaon West for comprehensive checkups, cataract, retina, LASIK screening, dry eye and family eye care at Sentra Clinic near Malad East.",
        "section": (
            "An accessible eye clinic for Goregaon West families",
            [
                "An eye clinic should do more than issue a spectacle number. Goregaon West residents may arrive with burning after screen use, frequent watering, night glare, a child who sits close to the television, or an older parent who has started avoiding stairs. These complaints can have different causes. At Sentra Clinic, the consultation begins with the patient’s story and then connects symptoms with an examination of the relevant eye structures.",
                "Patients can ask for help with routine vision, dry eye, contact-lens discomfort, cataract symptoms, diabetes-related screening, flashes and floaters, glaucoma risk, corneal concerns or a second opinion. Not every visitor needs every test. The doctor explains whether refraction, pressure measurement, dilation, imaging or another focused investigation is useful for the question being asked.",
                "If you are coming from Bangur Nagar, Jawahar Nagar, Motilal Nagar, the Link Road corridor or another part of Goregaon West, confirm the route and appointment timing before leaving. Bring old prescriptions and reports, and allow extra time if dilation or several family members are involved. Call 93729 47075 or WhatsApp the clinic to describe the main concern.",
            ],
        ),
    },
    {
        "source": "76-cataract-surgery-malad-west.html",
        "output": "84-cataract-surgery-in-goregaon-west.html",
        "title": "Cataract Surgery in Goregaon West | Sentra Clinic",
        "description": "Explore cataract surgery in Goregaon West with examination-led lens counselling, measurements, recovery guidance and follow-up at Sentra Clinic, Malad East.",
        "section": (
            "Cataract surgery planning for Goregaon West",
            [
                "Cataract can make a familiar Goregaon West route look hazy, turn oncoming headlights into glare, reduce reading comfort and make faces or steps less distinct. Surgery is not decided by age alone or by a single scan. The important questions are how much vision affects daily life, whether the cloudy lens explains the symptoms, and whether the retina, cornea or eye pressure also needs attention. Sentra Clinic starts with that complete assessment.",
                "A cataract consultation should give the patient time to discuss reading, driving, screen work, outdoor activities and the kind of glasses dependence they consider acceptable. Lens options have different benefits, limitations and suitability criteria. The surgeon should explain measurements, the proposed procedure, expected recovery, possible risks, alternatives and the consequences of waiting. A recommendation should be based on the patient’s eyes and priorities rather than a generic package.",
                "For a senior citizen travelling from Goregaon West, plan the visit with a companion who can note instructions and help with transport if the pupils are dilated. Bring all reports, medicines, diabetes and blood-pressure information, and previous operation details. Call 93729 47075 before booking so the team can suggest the appropriate cataract consultation and explain the clinic location in Malad East.",
            ],
        ),
    },
    {
        "source": "77-retina-specialist-malad-west.html",
        "output": "85-retina-specialist-in-goregaon-west.html",
        "title": "Retina Specialist in Goregaon West | Sentra Clinic",
        "description": "Need a retina specialist in Goregaon West? Sentra Clinic near Malad East offers doctor-led retinal evaluation, diabetic eye screening and treatment planning.",
        "section": (
            "Retina evaluation for Goregaon West residents",
            [
                "Retina symptoms are easy to dismiss when they appear as a few floaters or a brief flash after a long day. Goregaon West patients should take a new shower of floaters, repeated flashes, a dark curtain, a missing patch of vision or sudden loss of sight seriously. These symptoms can require prompt assessment. A routine online answer cannot tell whether the change is harmless, vitreous-related or connected with a retinal tear or detachment.",
                "A retina consultation also matters for people with diabetes, high blood pressure, previous retinal treatment, high short-sightedness or a family history of eye disease. Retinal changes may develop before a person notices reduced vision. The doctor interprets the examination alongside blood-sugar history, previous scans and symptoms, and may recommend dilation, retinal imaging, OCT or another test when it will clarify the diagnosis.",
                "Sentra Clinic on Rani Sati Road, Malad East gives Goregaon West families a practical location for planned retinal reviews and treatment discussions. Bring previous scans rather than only screenshots, plus medicine details and recent medical reports. If the change is sudden or severe, do not wait for a convenient appointment slot—call promptly and seek urgent medical care when advised.",
            ],
        ),
    },
    {
        "source": "79-eye-checkup-malad-west.html",
        "output": "86-eye-checkup-in-goregaon-west.html",
        "title": "Eye Checkup in Goregaon West | Sentra Clinic",
        "description": "Book an eye checkup in Goregaon West for vision, eye pressure, cataract, glaucoma and retina screening at Sentra Clinic, Malad East.",
        "section": (
            "A complete eye checkup near Goregaon West",
            [
                "A clear vision chart result is useful, but it is not the same as a complete eye checkup. A Goregaon West student, office worker, contact-lens user, person with diabetes and senior citizen may each need a different examination. The doctor may consider visual acuity, refraction, eye alignment, the cornea and lens, pressure, tear-film symptoms and the retina according to age, history and the reason for the visit.",
                "Preventive review is valuable because some eye conditions progress quietly. A person can read the chart and still need retinal screening for diabetes, glaucoma risk assessment or a cataract review. Conversely, headaches or fluctuating focus may be related to prescription, dry eye or near-work habits without indicating a serious disease. The purpose of a full checkup is to replace assumptions with an examination and a sensible follow-up interval.",
                "When booking from Goregaon West, tell the clinic whether the visit is for a routine baseline, a child’s school concern, new glasses, diabetes, cataract symptoms or a report review. Carry current spectacles, older prescriptions, scans and medicines. If dilation may be needed, take sunglasses and arrange help with travel. Call 93729 47075 for appointment guidance at Sentra Clinic, Malad East.",
            ],
        ),
    },
]


def replace_location(text: str) -> str:
    replacements = [
        ("malad-west", "goregaon-west"),
        ("Malad West", "Goregaon West"),
        ("malad west", "Goregaon West"),
        ("MALAD WEST", "GOREGAON WEST"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    # The project has one shared stylesheet; the filename is not a location slug.
    text = text.replace("/goregaon-west-seo-pages.css", "/malad-west-seo-pages.css")
    # Point transformed related links at the five new, canonical preview files.
    link_map = {
        "/best-eye-hospital-goregaon-west.html": "/82-best-eye-hospital-in-goregaon-west.html",
        "/eye-clinic-goregaon-west.html": "/83-eye-clinic-in-goregaon-west.html",
        "/eye-checkup-goregaon-west.html": "/86-eye-checkup-in-goregaon-west.html",
        "/cataract-surgery-goregaon-west.html": "/84-cataract-surgery-in-goregaon-west.html",
        "/retina-specialist-goregaon-west.html": "/85-retina-specialist-in-goregaon-west.html",
        "/75-eye-hospital-goregaon-west.html": "/82-best-eye-hospital-in-goregaon-west.html",
        "/76-eye-doctor-goregaon-west.html": "/83-eye-clinic-in-goregaon-west.html",
        "/77-ophthalmologist-goregaon-west.html": "/85-retina-specialist-in-goregaon-west.html",
        "/82-eye-checkup-goregaon-west.html": "/86-eye-checkup-in-goregaon-west.html",
        "/80-retina-specialist-goregaon-west.html": "/85-retina-specialist-in-goregaon-west.html",
        "/81-lasik-surgery-goregaon-west.html": "/83-eye-clinic-in-goregaon-west.html",
    }
    for old, new in link_map.items():
        text = text.replace(old, new)
    return text


def metadata(html: str, page: dict) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>{page['title']}</title>", html, count=1, flags=re.S | re.I)
    desc = f'<meta name="description" content="{page["description"]}">'
    if re.search(r'<meta name="description"', html, flags=re.I):
        html = re.sub(r'<meta name="description"[^>]*>', desc, html, count=1, flags=re.I)
    else:
        html = html.replace("</title>", f"</title>{desc}", 1)
    canonical = f'<link rel="canonical" href="https://sentraclinic.com/{page["output"].removesuffix(".html")}/">'
    if re.search(r'<link rel="canonical"', html, flags=re.I):
        html = re.sub(r'<link rel="canonical"[^>]*>', canonical, html, count=1, flags=re.I)
    else:
        html = html.replace("</title>", f"</title>{canonical}", 1)
    html = re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{page["title"]}">', html, count=1, flags=re.I)
    html = re.sub(r'<meta property="og:description"[^>]*>', f'<meta property="og:description" content="{page["description"]}">', html, count=1, flags=re.I)
    return html


def inline_shared_css(html: str) -> str:
    css_tag = f'<style data-sentra-page-css="inline">\n{SHARED_CSS}\n</style>'
    pattern = r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\'][^"\']*malad-west-seo-pages\.css[^"\']*["\'][^>]*>\s*'
    return re.sub(pattern, css_tag + "\n", html, count=1, flags=re.I)


def unique_section(page: dict) -> str:
    heading, paragraphs = page["section"]
    body = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f'<section class="sc-section sc-section-alt"><h2>{heading}</h2>{body}</section>'


def main() -> None:
    for page in PAGES:
        source = ROOT / page["source"]
        html = source.read_text(encoding="utf-8")
        html = replace_location(html)
        html = metadata(html, page)
        html = inline_shared_css(html)
        marker = '<div class="sc-cta">'
        if marker not in html:
            raise RuntimeError(f"Could not find CTA insertion point in {source}")
        html = html.replace(marker, unique_section(page) + "\n\n" + marker, 1)
        # Keep this exact keyword prominent in browser metadata and the visible page.
        html = html.replace("Serving Goregaon West", "Serving Goregaon West", 1)
        out = ROOT / page["output"]
        out.write_text(html, encoding="utf-8")
        text = re.sub(r"<(script|style)[^>]*>.*?</\\1>", " ", html, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        count = len(re.findall(r"\b[\w’'-]+\b", text))
        if count < 2000:
            raise RuntimeError(f"{page['output']} has only {count} visible words")
        print(f"{page['output']}: {count} words, {html.count('<img')} images")


if __name__ == "__main__":
    main()