"""Create the nine Kandivali SEO pages as standalone Elementor-ready HTML files."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SHARED_CSS = (ROOT / "malad-west-seo-pages.css").read_text(encoding="utf-8")

PAGES = [
    ("75-eye-hospital-malad-west.html", "eye-hospital-in-kandivali.html",
     "Eye Hospital in Kandivali | Sentra Clinic",
     "Looking for an eye hospital in Kandivali? Sentra Clinic near Malad East offers doctor-led checkups, cataract, LASIK, retina and family eye care.",
     "A practical eye hospital option for Kandivali families",
     [
         "Kandivali families often compare a neighbourhood clinic, an optical store and a larger hospital before choosing eye care. The right starting point depends on the patient’s concern: cataract, diabetes, a child’s vision, a changing prescription, retina symptoms or a planned procedure. Sentra Clinic gives patients travelling from Kandivali a doctor-led option in nearby Malad East where the examination, explanation and follow-up can be connected.",
         "A useful hospital visit should answer more than whether a patient can read a chart. The team should understand the history, examine the relevant parts of the eye, recommend only purposeful tests and explain what the findings mean. If surgery is discussed, families should receive information about alternatives, recovery, limitations and follow-up before making a decision.",
         "When booking from Kandivali, share the patient’s age, main symptom and any previous recommendation. Bring current glasses, old reports, scans and medicine details. The clinic is at Shah Arcade 2, Rani Sati Road, Malad East; confirm the route and appointment timing on 93729 47075 before travelling, especially for a senior patient who may need dilation.",
     ]),
    ("76-eye-doctor-malad-west.html", "eye-doctor-in-kandivali.html",
     "Eye Doctor in Kandivali | Sentra Clinic",
     "Find an eye doctor in Kandivali for changing vision, dry eye, cataract, retina, LASIK screening and family eye care at Sentra Clinic near Malad East.",
     "An eye doctor for clear answers in Kandivali",
     [
         "People searching for an eye doctor in Kandivali may be dealing with headaches, a new glasses number, burning after screen use, watering, night glare or an older parent whose vision is slowly becoming hazy. These symptoms should not automatically be treated as a simple power change. A doctor-led consultation connects the complaint with the cornea, lens, tear film, eye pressure, optic nerve and retina when appropriate.",
         "Bring the actual question you want answered. Tell the doctor whether one eye or both are affected, when the change began, whether it fluctuates, and whether there is pain, discharge, light sensitivity, flashes or floaters. Mention diabetes, blood pressure, thyroid disease, allergies, previous operations and all eye drops. This history helps the examination become more useful than a rushed prescription check.",
         "Sentra Clinic serves patients from Kandivali at its Malad East location. Call before visiting so the team can guide you to the right appointment for a routine consultation, second opinion, child’s vision, cataract assessment or sudden symptom. Carry your current spectacles and old prescriptions, and arrange a companion if dilation could make the return journey uncomfortable.",
     ]),
    ("77-ophthalmologist-malad-west.html", "ophthalmologist-in-kandivali.html",
     "Ophthalmologist in Kandivali | Sentra Clinic",
     "Consult an ophthalmologist near Kandivali for cataract, retina, cornea, glaucoma, LASIK screening and routine eye problems at Sentra Clinic, Malad East.",
     "Ophthalmology guidance for Kandivali patients",
     [
         "An ophthalmologist looks beyond spectacle power and assesses the health of the eye. This matters when a Kandivali patient has recurring redness, persistent dryness, diabetes, flashes, floaters, a family history of glaucoma, a previous injury or a recommendation for surgery. Similar symptoms can come from different structures, so the diagnosis should follow an examination rather than an online guess.",
         "The right consultation may include vision and refraction, slit-lamp examination, eye-pressure assessment, dilation, retinal imaging, corneal mapping or another focused investigation. A test is useful when it answers a clinical question and changes the plan. Ask what each test is checking, what the result means and when a repeat review is required.",
         "Patients travelling from Kandivali should bring reports in their original format, not only a cropped phone photograph. Tell the team if the appointment is for cataract, refractive surgery, glaucoma risk, a child or a retinal symptom. Sentra Clinic is at Shah Arcade 2, Rani Sati Road, Malad East; call 93729 47075 for appointment guidance and directions.",
     ]),
    ("78-best-eye-hospital-malad-west.html", "best-eye-hospital-in-kandivali.html",
     "Best Eye Hospital in Kandivali | Sentra Clinic",
     "Looking for the best eye hospital in Kandivali? Compare doctor involvement, diagnostics, cataract, retina, LASIK guidance and follow-up at Sentra Clinic.",
     "How Kandivali families can compare eye hospitals",
     [
         "“Best” is not a universal medical label. The most suitable eye hospital in Kandivali depends on the patient’s condition, the quality of diagnosis, the doctor’s involvement, the suitability of treatment and the reliability of follow-up. Cataract, diabetic eye disease, a child’s visual development and LASIK candidacy each require a different conversation.",
         "Before booking, ask who will examine you, whether the doctor reviews the reports personally, which tests are needed and why, what alternatives exist, and what happens after treatment. Be cautious of guaranteed results, one procedure promoted for everyone or a low headline price that does not explain what is included. A clear estimate and written recovery plan are more useful than a slogan.",
         "Sentra Clinic gives Kandivali residents a nearby Malad East option for comprehensive consultation and planned eye care. Bring previous reports and write down your questions. If an elective procedure is recommended, take time to understand it. If you have sudden vision loss, severe pain, a major injury or a curtain-like shadow, seek prompt medical attention instead of waiting for a routine comparison appointment.",
     ]),
    ("84-eye-clinic-malad-west.html", "eye-clinic-in-kandivali.html",
     "Eye Clinic in Kandivali | Sentra Clinic",
     "Find an eye clinic in Kandivali for comprehensive checkups, dry eye, cataract, retina, LASIK screening and family eye care at Sentra Clinic near Malad East.",
     "A connected eye clinic experience for Kandivali",
     [
         "An eye clinic should help a patient understand the next step, not only print a prescription. Kandivali residents may visit for burning after screen use, contact-lens discomfort, blurred vision, a child who sits close to the television or an older adult who has stopped reading. The same symptom can have several causes, so the consultation begins with the person’s routine and history.",
         "Sentra Clinic can guide patients about routine vision, dry eye, corneal concerns, cataract symptoms, diabetes-related screening, flashes and floaters, glaucoma risk and second opinions. The doctor decides whether refraction, pressure measurement, dilation, imaging or another examination is relevant. This focused approach helps families avoid both unnecessary testing and false reassurance from a quick power check.",
         "When travelling from Kandivali, tell the team the patient’s age and reason for the visit. Bring glasses, old prescriptions, medicines and previous scans. Allow more time if dilation or several family members are involved. The clinic is located at Shah Arcade 2, Rani Sati Road, Malad East; call or WhatsApp 93729 47075 before leaving.",
     ]),
    ("79-cataract-surgery-malad-west.html", "cataract-surgery-in-kandivali.html",
     "Cataract Surgery in Kandivali | Sentra Clinic",
     "Explore cataract surgery in Kandivali with detailed evaluation, lens counselling, measurements, recovery guidance and follow-up at Sentra Clinic, Malad East.",
     "Cataract surgery planning for Kandivali residents",
     [
         "Cataract can make signs, faces, steps and night traffic look hazy for a Kandivali resident. Glare and faded colours may gradually change how a person reads, works, travels or manages the home. Surgery is not decided by age alone. The doctor first confirms that the cloudy lens explains the symptoms and checks whether the retina, cornea or eye pressure also needs attention.",
         "A useful cataract consultation connects lens choices with daily priorities. Tell the surgeon whether you read small print, drive after dark, use a computer, enjoy outdoor activities or want to reduce dependence on glasses. Measurements, the proposed procedure, expected recovery, risks, alternatives and limitations should be explained in language the patient understands. No lens is automatically right for every eye.",
         "For a senior citizen coming from Kandivali, arrange a companion who can note instructions and help with transport if the pupils are dilated. Carry diabetes and blood-pressure reports, medicines, previous surgery notes and current glasses. Call 93729 47075 to confirm the cataract appointment at Sentra Clinic, Shah Arcade 2, Rani Sati Road, Malad East.",
     ]),
    ("80-retina-specialist-malad-west.html", "retina-specialist-in-kandivali.html",
     "Retina Specialist in Kandivali | Sentra Clinic",
     "Need a retina specialist in Kandivali? Sentra Clinic near Malad East offers doctor-led retinal evaluation, diabetic eye screening and treatment planning.",
     "Retina care and timely assessment for Kandivali",
     [
         "A new shower of floaters, repeated flashes, a curtain-like shadow, a missing area of vision or sudden loss of sight should not be dismissed as ordinary eye strain. Kandivali patients with these symptoms may need prompt retinal assessment. A website cannot identify a retinal tear, detachment, vitreous change or another cause; urgency is decided after understanding the timing and examining the eye.",
         "Planned retina review is also important for diabetes, high blood pressure, high short-sightedness, previous retinal treatment and a family history of retinal disease. Changes can be present before vision feels different. The doctor may consider dilation, retinal photographs, OCT or another investigation according to the patient’s history and examination, then explain whether observation, treatment or referral is appropriate.",
         "Bring previous scans, medication details, diabetes reports and the exact date a symptom began. Patients from Kandivali can call Sentra Clinic on 93729 47075 for appointment guidance at Rani Sati Road, Malad East. Sudden or severe changes should be described clearly on the call and treated as time-sensitive rather than waiting for a convenient routine slot.",
     ]),
    ("81-lasik-surgery-malad-west.html", "lasik-surgery-in-kandivali.html",
     "LASIK Surgery in Kandivali | Sentra Clinic",
     "Considering LASIK surgery in Kandivali? Get candidacy screening, corneal evaluation, alternatives, recovery guidance and doctor-led counselling at Sentra Clinic.",
     "LASIK suitability conversations for Kandivali",
     [
         "Many Kandivali adults consider LASIK because they want less dependence on spectacles for work, sport, travel or daily routines. Wanting freedom from glasses is understandable, but the decision should follow a detailed screening. Stable power, corneal shape and thickness, tear-film health, age, eye history and the patient’s expectations all influence suitability.",
         "A responsible refractive consultation explains what LASIK can improve and what it cannot promise. Ask about dry-eye symptoms, night glare, reading vision after the usual age-related change, possible alternatives and the chance that glasses may still be useful for specific activities. Corneal mapping and other tests are meaningful when the doctor interprets them with the complete examination.",
         "Do not choose an elective procedure only because of a limited-time offer. Bring old prescriptions, contact-lens details, previous eye reports and a list of medicines. Patients from Kandivali can call 93729 47075 to schedule a screening at Sentra Clinic, Shah Arcade 2, Rani Sati Road, Malad East, and plan enough time for questions before deciding.",
     ]),
    ("82-eye-checkup-malad-west.html", "eye-checkup-in-kandivali.html",
     "Eye Checkup in Kandivali | Sentra Clinic",
     "Book an eye checkup in Kandivali for vision, eye pressure, cataract, glaucoma and retina screening at Sentra Clinic, Malad East.",
     "A complete eye checkup near Kandivali",
     [
         "A spectacle test is useful but is not the same as a complete eye checkup. A Kandivali student, screen-based professional, contact-lens user, person with diabetes and older adult may each need a different assessment. The doctor may consider vision, refraction, eye alignment, the cornea and lens, pressure, tear-film symptoms and the retina according to age, history and the reason for the visit.",
         "Preventive review matters because some retinal and glaucoma changes can be quiet early. A person may read a chart and still need a diabetes-related retinal assessment or cataract review. On the other hand, fluctuating focus may relate to dry eye or near-work habits. The purpose of a full checkup is to replace assumptions with an examination and a sensible review interval.",
         "When booking from Kandivali, tell the clinic whether the visit is a baseline, a child’s school concern, a new glasses problem, diabetes screening, cataract symptoms or a report review. Carry spectacles, previous prescriptions, scans and medicines. If dilation is possible, take sunglasses and arrange help with travel. Call 93729 47075 for appointment guidance at Sentra Clinic in Malad East.",
     ]),
]


def replace_location(html: str) -> str:
    for old, new in (
        ("malad-west", "kandivali"),
        ("Malad West", "Kandivali"),
        ("malad west", "Kandivali"),
        ("MALAD WEST", "KANDIVALI"),
    ):
        html = html.replace(old, new)
    link_map = {
        "/75-eye-hospital-kandivali.html": "/eye-hospital-in-kandivali.html",
        "/76-eye-doctor-kandivali.html": "/eye-doctor-in-kandivali.html",
        "/77-ophthalmologist-kandivali.html": "/ophthalmologist-in-kandivali.html",
        "/78-best-eye-hospital-kandivali.html": "/best-eye-hospital-in-kandivali.html",
        "/79-cataract-surgery-kandivali.html": "/cataract-surgery-in-kandivali.html",
        "/80-retina-specialist-kandivali.html": "/retina-specialist-in-kandivali.html",
        "/81-lasik-surgery-kandivali.html": "/lasik-surgery-in-kandivali.html",
        "/82-eye-checkup-kandivali.html": "/eye-checkup-in-kandivali.html",
        "/84-eye-clinic-kandivali.html": "/eye-clinic-in-kandivali.html",
        "/eye-hospital-kandivali.html": "/eye-hospital-in-kandivali.html",
        "/eye-doctor-kandivali.html": "/eye-doctor-in-kandivali.html",
        "/ophthalmologist-kandivali.html": "/ophthalmologist-in-kandivali.html",
        "/best-eye-hospital-kandivali.html": "/best-eye-hospital-in-kandivali.html",
        "/cataract-surgery-kandivali.html": "/cataract-surgery-in-kandivali.html",
        "/retina-specialist-kandivali.html": "/retina-specialist-in-kandivali.html",
        "/lasik-surgery-kandivali.html": "/lasik-surgery-in-kandivali.html",
        "/eye-checkup-kandivali.html": "/eye-checkup-in-kandivali.html",
        "/eye-clinic-kandivali.html": "/eye-clinic-in-kandivali.html",
        "/59-eye-specialist-kandivali.html": "/14-eye-specialist-kandivali.html",
    }
    for old, new in link_map.items():
        html = html.replace(old, new)
    return html


def update_metadata(html: str, filename: str, title: str, description: str) -> str:
    slug = filename.removesuffix(".html")
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S | re.I)
    desc = f'<meta name="description" content="{description}">'
    if re.search(r'<meta name="description"', html, flags=re.I):
        html = re.sub(r'<meta name="description"[^>]*>', desc, html, count=1, flags=re.I)
    else:
        html = html.replace("</title>", f"</title>{desc}", 1)
    canonical = f'<link rel="canonical" href="https://sentraclinic.com/{slug}/">'
    if re.search(r'<link rel="canonical"', html, flags=re.I):
        html = re.sub(r'<link rel="canonical"[^>]*>', canonical, html, count=1, flags=re.I)
    else:
        html = html.replace("</title>", f"</title>{canonical}", 1)
    html = re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{title}">', html, count=1, flags=re.I)
    html = re.sub(r'<meta property="og:description"[^>]*>', f'<meta property="og:description" content="{description}">', html, count=1, flags=re.I)
    if re.search(r'<meta property="og:url"', html, flags=re.I):
        html = re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="https://sentraclinic.com/{slug}/">', html, count=1, flags=re.I)
    return html


def inline_css(html: str) -> str:
    style = f'<style data-sentra-page-css="inline">\n{SHARED_CSS}\n</style>'
    link = r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\'][^"\']*malad-west-seo-pages\.css[^"\']*["\'][^>]*>\s*'
    return re.sub(link, style + "\n", html, count=1, flags=re.I)


def visible_words(html: str) -> int:
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    return len(re.findall(r"\b[\w’'-]+\b", html))


def main():
    for source_name, output_name, title, description, heading, paragraphs in PAGES:
        html = (ROOT / source_name).read_text(encoding="utf-8")
        html = replace_location(html)
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