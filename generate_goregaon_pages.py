from html import escape
import json
from pathlib import Path
import re

OUT = Path(".")
PHONE = "9372947075"
PHONE_DISPLAY = "93729 47075"
WHATSAPP = "https://wa.me/919372947075"
ADDRESS = "Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097"
BASE = "https://sentraclinic.com"

IMAGES = {
    "doctors": "https://sentraclinic.com/wp-content/uploads/2025/04/Doctors-image.png",
    "rohit": "https://sentraclinic.com/wp-content/uploads/2025/04/Dr.-Rohit-Modi-min.png",
    "shraddha": "https://sentraclinic.com/wp-content/uploads/2025/04/Dr.-Shraddha-Surekha-min-1.png",
    "lasik": "https://sentraclinic.com/wp-content/uploads/2025/04/Lasik-Surgery-min-1-scaled.jpg",
    "cataract": "https://sentraclinic.com/wp-content/uploads/2025/04/Cataract-surgery-min-scaled.jpg",
    "retina": "https://sentraclinic.com/wp-content/uploads/2025/04/Retina-care-min-scaled.jpg",
    "clear": "https://sentraclinic.com/wp-content/uploads/2025/04/clear-vision-min-scaled.jpg",
}

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');
.sc-wrap{--navy:#0a2540;--navy2:#071b30;--cream:#f2eee1;--gold:#c9932c;--gold2:#a97814;--teal:#1f7a6c;--ink:#16202c;--muted:#5c6b7c;--line:#e6e2d6;font-family:Inter,'Segoe UI',Arial,sans-serif;color:var(--ink);font-size:17px;line-height:1.75;max-width:1180px;margin:auto;padding:0 22px;isolation:isolate}
.sc-wrap *{box-sizing:border-box}.sc-wrap h1,.sc-wrap h2,.sc-wrap h3{font-family:'Playfair Display',Georgia,serif}.sc-wrap h1{font-size:clamp(31px,4.4vw,52px);line-height:1.14;color:var(--navy2);margin:0 0 16px}.sc-wrap h2{font-size:clamp(25px,3.2vw,35px);line-height:1.2;color:var(--navy2);margin:48px 0 20px;padding-left:20px;position:relative}.sc-wrap h2:before{content:"";position:absolute;left:0;top:5px;bottom:5px;width:5px;border-radius:6px;background:linear-gradient(var(--gold),var(--gold2))}.sc-wrap h3{font-size:22px;line-height:1.3;color:var(--navy);margin:22px 0 9px}.sc-wrap p{margin:0 0 17px}.sc-wrap a{color:var(--navy);font-weight:700}.sc-breadcrumb{font-size:13px;color:var(--muted);padding:20px 0 8px}.sc-breadcrumb a{font-weight:600}.sc-hero{display:grid;grid-template-columns:1.05fr .95fr;gap:34px;align-items:center;background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:22px;padding:46px;margin:14px 0 36px;overflow:hidden;position:relative}.sc-hero:after{content:"";position:absolute;width:380px;height:380px;right:-120px;top:-130px;border-radius:50%;background:radial-gradient(circle,rgba(201,147,44,.34),transparent 68%)}.sc-hero>div{position:relative;z-index:1}.sc-hero h1{color:#fff}.sc-hero p{color:#edf3f8}.sc-eyebrow{display:inline-block;background:rgba(255,255,255,.12);border:1px solid rgba(246,232,201,.35);color:#f6e8c9;padding:7px 14px;border-radius:999px;font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;margin-bottom:16px}.sc-img{width:100%;height:100%;max-height:360px;object-fit:cover;border-radius:17px;display:block;box-shadow:0 16px 35px rgba(0,0,0,.18)}.sc-hero .sc-img{min-height:290px;position:relative}.sc-btn-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:21px}.sc-btn,.sc-btn-outline{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:12px 20px;text-decoration:none!important;font-size:15px}.sc-btn{background:var(--gold);color:#fff!important}.sc-btn-outline{border:1px solid rgba(255,255,255,.45);color:#fff!important}.sc-cta{background:linear-gradient(110deg,var(--cream),#fff);border:1px solid var(--line);border-radius:18px;padding:24px 28px;margin:26px 0}.sc-cta p{font-weight:800;color:var(--navy);margin:0}.sc-grid-2,.sc-grid-3{display:grid;gap:22px}.sc-grid-2{grid-template-columns:1fr 1fr;align-items:center}.sc-grid-3{grid-template-columns:repeat(3,1fr);margin:25px 0}.sc-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:21px;box-shadow:0 7px 18px rgba(10,37,64,.06)}.sc-card h3{margin-top:0}.sc-card p{font-size:15px;color:var(--muted);margin-bottom:0}.sc-note{background:#fff8ec;border:1px solid #f1d5a1;color:#684c13;border-radius:14px;padding:18px 21px;margin:22px 0}.sc-table{width:100%;border-collapse:collapse;border:1px solid var(--line);margin:20px 0;background:#fff}.sc-table th,.sc-table td{padding:13px 15px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.sc-table th{background:var(--navy);color:#fff}.sc-table tr:last-child td{border-bottom:0}.sc-steps{counter-reset:step;padding:0;list-style:none}.sc-steps li{counter-increment:step;position:relative;padding:8px 0 8px 56px;margin:0 0 18px}.sc-steps li:before{content:counter(step);position:absolute;left:0;top:0;width:38px;height:38px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:800;background:var(--gold)}.sc-faq details{border:1px solid var(--line);border-radius:13px;margin:0 0 13px;padding:17px 20px;background:#fff}.sc-faq summary{cursor:pointer;font-weight:800;color:var(--navy);display:flex;justify-content:space-between;gap:14px}.sc-faq summary:after{content:'+';color:var(--gold);font-size:23px}.sc-faq details[open] summary:after{content:'−'}.sc-faq p{color:var(--muted);margin:12px 0 0}.sc-related{background:var(--cream);border-radius:19px;padding:25px;margin:35px 0}.sc-related h2{margin-top:0}.sc-related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}.sc-related-grid a{background:#fff;border:1px solid var(--line);border-radius:11px;padding:15px;text-decoration:none!important;font-size:15px}.sc-disclaimer{font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding:22px 0 34px;margin-top:34px}.sc-float{position:fixed;right:20px;bottom:20px;background:#c0392b;color:#fff!important;border-radius:999px;padding:13px 18px;text-decoration:none!important;font-weight:800;box-shadow:0 8px 25px rgba(192,57,43,.35);z-index:99}@media(max-width:760px){.sc-hero,.sc-grid-2{grid-template-columns:1fr}.sc-hero{padding:27px 20px}.sc-grid-3,.sc-related-grid{grid-template-columns:1fr}.sc-wrap{padding:0 14px;font-size:16px}.sc-hero .sc-img{min-height:220px}.sc-table{font-size:14px}.sc-table th,.sc-table td{padding:10px}.sc-float{right:12px;bottom:12px;font-size:13px;padding:11px 14px}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
"""

COMMON_INTRO = {
    "hospital": (
        "Searching for an eye hospital in Goregaon East often means comparing a neighbourhood clinic, a diagnostic centre and a surgical facility. Sentra Clinic gives families a clear local option in Malad East for consultations, investigations and planned eye procedures. The clinic is on Rani Sati Road, with care led by Dr. Rohit Modi and Dr. Shraddha Surekha. Patients from Goregaon East can discuss routine vision concerns as well as cataract, LASIK, retina, cornea and glaucoma needs in one coordinated setting.",
        "A hospital should not be judged only by a large signboard. Look for the quality of examination, the clarity of the diagnosis, the surgeon’s involvement, the explanation of alternatives and the follow-up plan. Sentra Clinic’s approach is to begin with the patient’s symptoms and history, use the tests that are actually relevant, and then explain what needs attention now versus what can be monitored. This is useful for Goregaon East families who want accessible care without losing the personal attention of a doctor-led practice.",
    ),
    "doctor": (
        "When someone types eye doctor in Goregaon East, they may be looking for help with a new prescription, irritation, headaches, cataract symptoms or a report that needs explanation. The right first visit is not always the one with the shortest waiting time. It is the one where a doctor listens, examines the eye properly and tells you what the next step means. Sentra Clinic welcomes patients travelling from Goregaon East to its Malad East location for focused consultations and ongoing eye care.",
        "An eye doctor’s role is broader than checking whether a patient can read the smallest line on a chart. A consultation can connect changing vision with the cornea, lens, retina, optic nerve, eye pressure, tear film or general health. It can also identify when a symptom needs prompt review rather than another pair of glasses. At Sentra Clinic, patients are encouraged to bring previous reports, medication details and their questions so the consultation becomes a useful health decision, not a rushed transaction.",
    ),
    "ophthalmologist": (
        "An ophthalmologist in Goregaon East should be able to assess the whole eye, not just update spectacle power. Sentra Clinic provides access to ophthalmic consultation and surgical guidance from its Malad East centre on Rani Sati Road. People from Goregaon East visit for cataract opinions, refractive surgery screening, retina concerns, corneal problems, glaucoma evaluation and everyday symptoms such as watering or dryness. The aim is to match the examination to the problem instead of offering the same test package to everyone.",
        "The word ophthalmologist can sound technical, but the patient experience should be understandable. After examining the eyes, the doctor should explain what has been found, what has not been found, what is uncertain and when the next review is needed. If a procedure is discussed, a responsible consultation includes benefits, limitations, alternatives, recovery and possible additional tests. That conversation helps Goregaon East patients make a decision based on their eyes and lifestyle rather than on a generic promise of perfect vision.",
    ),
    "best": (
        "People searching for the best eye hospital in Goregaon East are usually trying to avoid guesswork. “Best” is not a universal medical label; it depends on the patient’s condition, the doctor’s experience, the quality of assessment, the suitability of the treatment and the reliability of follow-up. Sentra Clinic offers Goregaon East residents a transparent, doctor-led option a short journey away in Malad East, where the focus is on careful evaluation and treatment decisions that fit the individual.",
        "A trustworthy comparison should include more than online ratings. Ask whether the doctor personally reviews the case, whether the facility can coordinate the next investigation, whether the price and recovery expectations are explained, and whether urgent symptoms are directed appropriately. Sentra Clinic’s two eye surgeons support patients across routine and surgical eye care, while the team helps families understand reports and plan follow-up. This page is designed to help you compare care thoughtfully rather than make an unsupported medical superlative claim.",
    ),
    "clinic": (
        "An eye clinic in Goregaon East can be the right first stop for a regular vision review, but convenience should not come at the cost of a proper examination. Sentra Clinic in nearby Malad East sees patients from Goregaon East for comprehensive checkups, glasses-related concerns, dry eye, cataract planning, retina screening and refractive surgery discussions. A visit is organised around the person’s symptoms, age, work, existing conditions and previous reports, so the plan is practical for everyday life.",
        "An eye checkup in Goregaon East is useful even when there is no pain. Many eye conditions develop quietly, while children, contact-lens users, people with diabetes and adults over 40 may have changing needs that are easy to miss in a quick vision test. A full consultation can identify whether the issue is refractive, surface-related, lens-related or deeper inside the eye. Sentra Clinic can explain which examination steps are relevant and what follow-up interval makes sense for you.",
    ),
}

PAGES = [
    {
        "file": "eye-hospital-in-goregaon-east.html",
        "slug": "eye-hospital-in-goregaon-east",
        "kind": "hospital",
        "title": "Eye Hospital in Goregaon East | Sentra Clinic",
        "h1": "Eye Hospital in Goregaon East for Complete, Doctor-Led Eye Care",
        "desc": "Looking for an eye hospital in Goregaon East? Sentra Clinic in nearby Malad East offers doctor-led checkups, cataract, LASIK, retina, cornea and glaucoma care.",
        "eyebrow": "Eye hospital near Goregaon East · Sentra Clinic",
        "hero_img": "doctors",
        "hero_alt": "Eye hospital care team at Sentra Clinic serving Goregaon East patients",
        "sections": [
            ("Why the first examination matters", [
                "A patient may arrive with blurred vision and assume that new glasses will solve it. Another may have watering that feels like an allergy, while an older family member quietly stops reading because the words appear hazy. These symptoms can come from very different parts of the eye. A hospital-level evaluation starts by understanding the pattern: one eye or both, sudden or gradual, constant or intermittent, worse at night or after screen use, and associated with pain, flashes, discharge or headache.",
                "The aim is not to order every possible investigation. It is to choose examinations that answer useful clinical questions. Refraction assesses focusing power, slit-lamp examination looks at the front of the eye, pressure measurement supports glaucoma assessment and a dilated retinal review may be important for diabetes, flashes, floaters or unexplained vision change. When a test is advised, ask what it is checking and how its result will change the plan.",
                "For a Goregaon East family, this organised approach can reduce repeated visits to different providers. It also creates a baseline that can be compared at a future appointment. Keep copies of prescriptions, scans and discharge notes; eye care becomes safer when the next doctor can see the history rather than relying on memory."
            ]),
            ("Services available for Goregaon East families", [
                "Sentra Clinic supports a broad range of eye-care conversations. A routine visit may address distance or near vision, changing glasses, computer-related discomfort, dry eye, redness or recurrent watering. A surgical discussion may concern cataract, LASIK or another refractive option. Patients with diabetes, flashes, floaters or a history of retinal treatment may need a retina-focused assessment. Corneal, glaucoma, paediatric and ocular-surface concerns also benefit from a structured review.",
                "The service that is appropriate depends on the findings, not on the search phrase used to reach this page. A person looking for cataract surgery may first need measurements and a health review. Someone asking about LASIK may need corneal mapping, stable power and a discussion of expectations. Someone with a red eye may need diagnosis before any drop is started. The clinic’s role is to explain those steps in plain language and refer or coordinate when a different level of care is needed.",
                "If you are travelling from Goregaon East with an older patient, allow enough time for tests and questions. Bring glasses, contact-lens details, prior scans, diabetes or blood-pressure reports and a list of medicines. If dilation is possible, consider arranging a companion and avoid scheduling a demanding drive immediately afterwards."
            ]),
            ("Cataract, LASIK and retina care under one roof", [
                "Cataract is a clouding of the natural lens that can make faces, steps, signs and night lights look less clear. Surgery is not decided by age alone. The important question is whether the reduced vision is affecting safety, work, reading or independence, and whether the examination confirms that cataract is the main cause. A consultation should cover lens choices, measurements, recovery, glasses expectations and follow-up rather than presenting one implant as suitable for everyone.",
                "LASIK and other vision-correction procedures are elective decisions. A detailed screening considers the stability of the prescription, corneal shape and thickness, tear-film health, age, eye history and the patient’s reasons for wanting less dependence on glasses. Good candidacy is about suitability, not just a desire to remove spectacles. The doctor should explain alternatives and the possibility that glasses may still be useful for some tasks.",
                "Retina symptoms deserve a different level of attention. New flashes, a sudden increase in floaters, a curtain-like shadow or sudden loss of vision should not be managed by waiting for a routine appointment. Contact the clinic for guidance and seek urgent medical assessment when symptoms are severe or sudden. Online content cannot identify a retinal emergency."
            ]),
            ("A calm process for investigations and decisions", [
                "The first step at a local eye hospital should feel structured, not intimidating. Registration is followed by a discussion of the complaint, relevant history and any immediate warning signs. Vision is checked, the front of the eye is examined and additional tests are selected when they are clinically useful. If the pupil needs to be dilated, the team can explain why and what temporary effects to expect.",
                "Once the results are available, ask for a simple summary. What is the diagnosis or working diagnosis? Is treatment needed today? What happens if you observe it? Which symptoms should bring the review forward? If surgery is being considered, ask for an itemised estimate and a written list of pre-operative tests. A family member can take notes, especially when an older patient is anxious or several options are discussed.",
                "The best plan is one a patient can follow. If cost, work hours, transport, language or caregiver availability affects your choices, mention it early. The clinical team can then explain realistic timing and follow-up. Do not stop prescribed medicine or begin someone else’s eye drops without medical advice."
            ]),
            ("How Sentra Clinic serves Goregaon East", [
                "Sentra Clinic is located at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Patients from Goregaon East can call before travelling to confirm appointment availability, the expected consultation type and whether they should bring a particular report. The journey is manageable for families who prefer a doctor-led clinic with surgical and diagnostic discussions in the same setting.",
                "When booking, share the main reason for the visit: routine checkup, cataract opinion, LASIK screening, retina symptom, child’s vision, contact-lens problem or a second opinion. This helps the team guide the appointment appropriately. For urgent symptoms, say that clearly rather than describing them only as “number problem.” If a patient has sudden vision loss, severe pain or an eye injury, prioritise emergency medical care.",
                "Goregaon East is a busy residential and commercial area, so many patients try to combine appointments with work or school schedules. Plan extra time if several family members need evaluation. Carry water, a mask if needed, and a companion for an elderly person. The clinic can be reached on 93729 47075 or via WhatsApp for appointment-related communication."
            ]),
            ("Questions to ask before choosing an eye hospital", [
                "Ask who will examine you and whether the doctor will explain the reports personally. Ask whether a recommended test is essential, what it measures and whether dilation is required. For surgery, ask about the surgeon’s role, the type of procedure, alternatives, recovery restrictions, follow-up schedule and what is included in the estimate. These questions are not confrontational; they help you consent with a clear understanding.",
                "Also ask what to do if symptoms change after the visit. A clinic should tell you which warning signs require a call or urgent assessment. Keep the answer with your discharge notes. If a treatment plan includes multiple drops, write the timing in large letters and set reminders. If instructions are unclear, call rather than guessing.",
                "A health-care decision should be based on clinical fit and communication. Reviews can offer context, but they cannot replace an examination or guarantee a particular result. Choose the provider that explains your actual findings, avoids pressure and gives you a practical path for follow-up."
            ]),
            ("What to bring for a productive visit", [
                "Bring your current glasses and, if relevant, the boxes or prescription for contact lenses. Carry previous eye reports, scans, surgery notes and a list of medicines. Mention diabetes, thyroid disease, blood-pressure problems, autoimmune illness, migraine, allergies and any earlier eye injury. Tell the doctor if you are pregnant, breastfeeding or using medicines that affect bleeding or immunity.",
                "Write down when the problem started and what makes it better or worse. A short phone note can include whether the blur is near or far, whether one eye is affected, how long screens are used each day and whether there is pain, light sensitivity, discharge, flashes or floaters. Children may not describe blur, so note squinting, sitting close to the screen, closing one eye or avoiding reading.",
                "These details help the ophthalmologist interpret the examination and avoid treating a symptom in isolation. They also make a follow-up more efficient because the team can compare today’s findings with the original concern."
            ]),
        ],
        "faq": [
            ("Is Sentra Clinic an eye hospital near Goregaon East?", "Sentra Clinic is in Malad East on Rani Sati Road and accepts patients travelling from Goregaon East. Call 93729 47075 before visiting for directions and appointment availability."),
            ("What eye problems can I discuss at the clinic?", "You can ask about routine vision, cataract, LASIK screening, retina symptoms, glaucoma, cornea, dry eye, children’s vision and second opinions. The doctor will advise which examination is appropriate."),
            ("Should I book a routine visit for sudden floaters?", "New floaters, flashes, a curtain-like shadow or sudden vision loss should be treated as time-sensitive symptoms. Contact the clinic promptly and seek urgent assessment rather than waiting for a routine slot."),
            ("How do I prepare for a cataract consultation?", "Bring old reports, glasses, medicine details and questions about daily activities. The doctor will assess whether cataract explains the symptoms and discuss measurements, lens choices, recovery and follow-up."),
            ("How can I book an appointment from Goregaon East?", "Call 93729 47075 or message the clinic on WhatsApp at +91 93729 47075. Share the reason for the visit so the team can guide you.")
        ],
        "related": [("Eye specialist in Goregaon East", "/eye-specialist-goregaon-east/"), ("Cataract surgery in Goregaon East", "/cataract-surgery-goregaon-east/"), ("Retina specialist in Goregaon East", "/retina-specialist-goregaon-east/"), ("LASIK surgery in Goregaon East", "/lasik-surgery-goregaon-east/"), ("Dr. Rohit Modi", "/dr-rohit-modi/"), ("Comprehensive eye checkup", "/comprehensive-eye-checkup-malad/")],
    },
    {
        "file": "eye-doctor-in-goregaon-east.html",
        "slug": "eye-doctor-in-goregaon-east",
        "kind": "doctor",
        "title": "Eye Doctor in Goregaon East | Sentra Clinic",
        "h1": "Eye Doctor in Goregaon East for Clear Answers, Not Just a New Prescription",
        "desc": "Need an eye doctor in Goregaon East? Sentra Clinic in Malad East offers thoughtful eye examinations, second opinions, cataract, LASIK, retina and family eye care.",
        "eyebrow": "Eye doctor for Goregaon East families",
        "hero_img": "rohit",
        "hero_alt": "Dr. Rohit Modi, eye doctor serving patients from Goregaon East at Sentra Clinic",
        "sections": [
            ("When to see an eye doctor", [
                "A doctor’s appointment is useful when vision changes gradually as well as when a symptom appears suddenly. Difficulty reading a phone, increasing glare while driving, headaches after near work, frequent changes in glasses, watering or a gritty feeling can all justify an examination. Children may show the problem by sitting close to the television, tilting the head, covering one eye or losing interest in reading. Older adults may simply adapt to blur and call it normal ageing.",
                "An eye doctor looks for patterns that a self-test cannot capture. The complaint may come from refractive error, dry eye, cataract, corneal irritation, retinal disease, eye pressure or a general health condition. The first consultation is therefore about more than selecting lenses. It is an opportunity to record a baseline, identify risk factors and decide whether observation, drops, glasses, further testing or a procedure is appropriate.",
                "Patients from Goregaon East can use Sentra Clinic in Malad East for this kind of doctor-led review. Call ahead with the main concern so the appointment is planned around the patient’s age, symptoms and previous treatment."
            ]),
            ("What makes a consultation useful", [
                "A good consultation has three parts: listening, examining and explaining. Listening means understanding the patient’s routine, occupation, screen time, driving needs, family history and previous eye care. Examining means checking vision and the health of the eye rather than assuming the complaint is only a power change. Explaining means describing the finding in words that make sense and setting out the next action.",
                "Take an active role in the conversation. Tell the doctor if symptoms are worse in one eye, if they fluctuate through the day or if they appear after contact-lens wear. Mention medicines, allergies and conditions such as diabetes or high blood pressure. Ask whether the pupils need to be dilated and whether temporary blur or light sensitivity will affect your return journey.",
                "Before you leave, repeat the plan in your own words. Confirm how to use every drop, how long to use it, when to return and what warning signs should prompt an earlier call. If the diagnosis is uncertain, ask what information or test will clarify it. Clear communication is part of safe eye care."
            ]),
            ("A doctor-led approach to common complaints", [
                "For changing glasses, the examination should separate a simple refractive adjustment from a problem that needs medical attention. For dryness, the doctor may consider screen habits, airflow, contact lenses, eyelid health and the tear film rather than recommending a random redness-relief drop. For cataract, the decision to operate is connected to the patient’s function and examination findings, not only to a number on a report.",
                "For diabetes, a retinal assessment can be important even when vision seems normal. For glaucoma risk, pressure is only one part of the picture; the optic nerve, field of vision and other findings may matter. For children, the doctor may need to consider visual development, eye alignment and the possibility that one eye is doing more work than the other.",
                "This is why online symptom searches should be a starting point, not a diagnosis. A local eye doctor can connect the history with what is seen on examination and explain when a specialist test is needed. If there is severe pain, injury or sudden loss of vision, seek urgent medical assessment."
            ]),
            ("Meet the doctors at Sentra Clinic", [
                "Sentra Clinic’s care is supported by Dr. Rohit Modi and Dr. Shraddha Surekha. Patients can learn more about the doctors through the clinic’s profile pages and discuss which appointment is most suitable when they call. A consultation is not a promise that surgery will be recommended; it is a professional assessment of what the eye needs.",
                "For a second opinion, bring the original reports and the exact recommendation you were given. Avoid showing only a phone photograph if the original scan or prescription is available. Ask the doctor to explain whether the proposed treatment is urgent, optional, or one of several reasonable choices. This helps families from Goregaon East make decisions without feeling pressured by unfamiliar terminology.",
                "If more than one family member needs care, mention that while booking. A parent may need a child’s vision check, an adult may need a cataract review and another family member may need diabetes screening. The team can advise whether to arrange separate consultations so every person receives enough attention."
            ]),
            ("What happens at your first visit", [
                "At the beginning, the team records the main complaint and relevant history. Vision is checked with and without current correction where appropriate. The doctor examines the eye and considers whether additional evaluation is useful. Some patients need only a focused review; others benefit from a more detailed assessment because of diabetes, age, surgery planning or a complex history.",
                "If a procedure is discussed, slow the conversation down. Ask what problem it is intended to solve, what alternatives exist, how long recovery may take and what result is realistic for your lifestyle. A written estimate should be clear about professional fees, tests, medicines and follow-up. Never feel obliged to decide about elective treatment in the same moment.",
                "Afterwards, keep the written plan accessible. Use alarms for drops, avoid sharing medication and contact the clinic if the eye becomes more painful, vision worsens or an unexpected reaction develops. A follow-up is part of treatment, not an optional extra."
            ]),
            ("Eye doctor visits for working adults", [
                "Many Goregaon East residents work on screens, travel through traffic and postpone appointments until a deadline forces action. A consultation can be more useful when you describe the actual workday: hours on a laptop, air-conditioning, late-night phone use, contact lenses, outdoor exposure and whether you drive after dark. The doctor can then distinguish a focusing problem from surface irritation or another eye condition.",
                "Do not use someone else’s glasses or old prescription as a permanent solution. The number may have changed, or the old lenses may hide an issue that needs medical review. Take breaks from near work, blink fully and keep screens at a comfortable distance, but understand that habits do not replace an examination when symptoms persist.",
                "If the doctor dilates your pupils, bright light may feel uncomfortable for a while. Bring sunglasses and consider a companion if you are not sure how you will travel home. Ask before driving."
            ]),
            ("Family eye care and prevention", [
                "A family approach is helpful because different ages have different risks. Children need attention to visual development and eye alignment. Adults may need regular review for refractive change, dry eye or occupational strain. Around middle age, near focus commonly changes. Later in life, cataract, glaucoma and retinal conditions become more important, while diabetes and blood pressure can affect the eye at any age.",
                "Prevention is practical: wear protective eyewear for risky work, avoid using steroid eye drops without medical supervision, control diabetes and blood pressure with your physician, wash hands before handling lenses and attend review appointments even when a symptom improves. Ask the eye doctor how often you should return based on your own history.",
                "Early assessment does not mean every patient needs a procedure. It means the decision is made with better information. That is especially valuable for families who want a trusted eye doctor near Goregaon East rather than treating each new symptom in isolation."
            ]),
        ],
        "faq": [
            ("Where can I find an eye doctor for Goregaon East?", "Sentra Clinic is located in Malad East and serves patients from Goregaon East. Call 93729 47075 for appointment guidance and directions."),
            ("Can I visit for a glasses power check only?", "You can book for a power concern, but the doctor may recommend a broader examination if symptoms, age or medical history suggest that more than refraction is involved."),
            ("What should I bring to an eye doctor appointment?", "Bring current glasses, old prescriptions, reports, scans, contact-lens details and a list of medicines. Note when the symptom began and whether one or both eyes are affected."),
            ("Can the doctor give a second opinion?", "Yes. Bring the original reports and recommendation so the doctor can review the evidence, explain alternatives and tell you whether the situation is urgent or can be planned."),
            ("When is an eye symptom an emergency?", "Sudden vision loss, new flashes, a curtain-like shadow, severe eye pain, chemical injury or significant trauma needs urgent medical attention. Do not wait for online advice.")
        ],
        "related": [("Ophthalmologist in Goregaon East", "/ophthalmologist-in-goregaon-east/"), ("Eye clinic and checkup", "/eye-clinic-and-checkup-in-goregaon-east/"), ("Dr. Rohit Modi", "/dr-rohit-modi/"), ("Dr. Shraddha Surekha", "/dr-shraddha-surekha/"), ("Dry eye treatment", "/dry-eye-treatment-malad/"), ("Children’s eye specialist", "/children-eye-specialist-malad-mumbai/")],
    },
    {
        "file": "ophthalmologist-in-goregaon-east.html",
        "slug": "ophthalmologist-in-goregaon-east",
        "kind": "ophthalmologist",
        "title": "Ophthalmologist in Goregaon East | Sentra Clinic",
        "h1": "Ophthalmologist in Goregaon East for Medical and Surgical Eye Problems",
        "desc": "Find an ophthalmologist for Goregaon East at Sentra Clinic, Malad East. Get clear guidance for cataract, LASIK, retina, glaucoma, cornea and routine eye problems.",
        "eyebrow": "Ophthalmic consultation near Goregaon East",
        "hero_img": "shraddha",
        "hero_alt": "Dr. Shraddha Surekha, ophthalmologist serving Goregaon East patients at Sentra Clinic",
        "sections": [
            ("Ophthalmologist versus a routine vision test", [
                "A routine vision test can tell you whether a lens makes letters clearer. An ophthalmologist goes further by examining the structures and health of the eye. This matters when the patient has pain, recurrent redness, light sensitivity, flashes, floaters, diabetes, a family history of glaucoma, a previous injury or a recommendation for surgery. It also matters when a new prescription does not explain the symptoms.",
                "The value of an ophthalmology consultation is the connection between symptom and anatomy. A hazy view may be cataract, corneal change, tear-film instability or a retinal problem. Headache may be related to focusing, but it should not be assumed to be an eye-number issue without an examination. A child’s poor school performance may involve vision development or alignment. Each pattern requires a different conversation.",
                "Sentra Clinic gives Goregaon East patients a nearby Malad East option for that conversation. The doctor can explain whether a focused check is enough or whether investigations, monitoring, treatment or another specialist referral is appropriate."
            ]),
            ("Conditions an ophthalmologist can evaluate", [
                "Ophthalmic care can include refractive error and changing glasses, dry eye and ocular-surface complaints, cataract, glaucoma risk, corneal disease, retina symptoms, diabetic eye changes, paediatric vision concerns and screening before refractive procedures. The list is broad because the eye is a small but complex organ, and different tissues can create similar complaints.",
                "A patient with cataract may need lens measurements and a discussion of daily visual priorities. Someone considering LASIK may need corneal mapping, stable power and an honest discussion of limitations. A person with flashes or a sudden shower of floaters may need prompt retinal assessment. Someone with gradual peripheral-vision concerns may need glaucoma-focused testing. The appropriate pathway emerges from the examination.",
                "Do not start antibiotic, steroid or another person’s prescription drops based on a message or social-media post. Drops can mask signs, worsen some infections or delay the correct diagnosis. If you have already used a product, bring the bottle or a clear photograph and tell the doctor how often it was used."
            ]),
            ("How a specialist examination is planned", [
                "The appointment begins with questions about the complaint, health history, family history and previous eye care. The doctor then decides which parts of the examination are most relevant. Vision and refraction are common starting points, while slit-lamp examination helps assess the front of the eye. Eye pressure, dilation or imaging may be considered according to symptoms and risk.",
                "A test result is not meaningful in isolation. The doctor interprets it with age, symptoms, previous measurements and the appearance of the eye. If monitoring is advised, ask what change would trigger treatment and when the next review should happen. If a procedure is proposed, ask what problem it will address and what it cannot change.",
                "Bring enough time for questions. If language or anxiety makes medical explanations difficult, bring a family member or ask the team to repeat the plan. It is reasonable to take notes. The goal is informed care, not simply leaving with a report."
            ]),
            ("Cataract and refractive surgery guidance", [
                "Cataract surgery replaces the cloudy natural lens after a detailed assessment. The decision is individual: some people need surgery when reading becomes difficult, while others choose to wait until glare, mobility or work is affected. The ophthalmologist considers the lens, retina, cornea, eye pressure, general health and the patient’s visual priorities before discussing options.",
                "Refractive surgery is elective and requires a different kind of honesty. A patient may want to play sport without glasses, work more comfortably or reduce dependence on contact lenses. Screening should confirm that the cornea and tear film are suitable and that expectations are realistic. A procedure may reduce dependence on glasses without guaranteeing that glasses will never be needed.",
                "Ask about alternatives, recovery, restrictions, future reading vision, night-vision symptoms, dry-eye symptoms and follow-up. If the advice is not clear, pause and request a second explanation. A good ophthalmologist will support an informed decision even when the best choice is to wait."
            ]),
            ("Retina and glaucoma symptoms need attention", [
                "Retinal problems can be silent in their early stages, which is why people with diabetes or a history of retinal disease should follow a review schedule advised by their doctor. New flashes, a sudden increase in floaters, a dark curtain, missing areas of vision or sudden loss of sight require prompt attention. These symptoms should not be self-treated as simple eye strain.",
                "Glaucoma can also progress without obvious pain or early blur. Assessment may include pressure, optic-nerve evaluation, visual-field testing and other measurements. One normal pressure reading does not answer every glaucoma question, and one borderline reading does not automatically mean a patient has the disease. The ophthalmologist interprets the complete picture.",
                "If a report recommends repeat testing, keep the appointment even if you feel well. Comparing measurements over time can be more informative than reacting to a single number. Tell the clinic if you miss a review so the next step can be planned safely."
            ]),
            ("A specialist visit for children", [
                "Children do not always say that one eye is blurry. They may avoid books, lose their place, rub the eyes, tilt the head, close one eye in sunlight or struggle with classroom work. A child may also have a visible eye turn or a difference in how the eyes move. These signs deserve an age-appropriate ophthalmology assessment rather than waiting for the child to “grow out of it.”",
                "Parents should bring school observations, old prescriptions and information about birth history, developmental concerns and family eye conditions. Do not coach a child to guess letters; honest responses help the doctor understand how each eye is functioning. The doctor will explain whether glasses, observation, exercises, patching or further evaluation is relevant.",
                "A calm visit is easier when parents describe what they have noticed without blaming the child. Clear vision supports learning, but eye care is not a test of school performance. It is a health assessment with a plan that families can follow."
            ]),
            ("Why location and continuity matter", [
                "Eye care often involves more than one appointment. A pre-operative assessment, a scan, a procedure and follow-up may be separated by days or weeks. A clinic that is practical to reach from Goregaon East can make it easier to attend those visits and bring the same reports each time. Continuity also helps the doctor compare symptoms and measurements instead of beginning from zero at every appointment.",
                "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 to ask about the appointment type, expected tests and route. If you are bringing an older person, a child or someone who may need dilation, plan the journey and companion support in advance.",
                "The clinic can also guide you about whether a complaint sounds routine or requires quicker assessment. However, telephone guidance is not a replacement for emergency care when vision changes suddenly, there is severe pain or the eye has been injured."
            ]),
        ],
        "faq": [
            ("What does an ophthalmologist examine?", "An ophthalmologist can assess vision and the health of the cornea, lens, retina, optic nerve, eye pressure and other structures according to symptoms and risk."),
            ("Is an ophthalmologist the right doctor for cataract?", "Yes. Cataract diagnosis, surgical suitability, lens discussion and follow-up are part of ophthalmic care. The need and timing of surgery depend on the examination and daily impact."),
            ("Can I see an ophthalmologist for dry eye?", "Yes. Persistent dryness, burning or watering deserves an assessment of the tear film, eyelids, contact-lens habits and other possible causes instead of repeated self-medication."),
            ("Do flashes and floaters require urgent review?", "New flashes, a sudden increase in floaters, a curtain-like shadow or sudden vision loss can be urgent. Contact a medical provider promptly and do not wait for a routine check."),
            ("How do I book from Goregaon East?", "Call Sentra Clinic at 93729 47075 or use WhatsApp at +91 93729 47075. The clinic is in Malad East on Rani Sati Road.")
        ],
        "related": [("Eye doctor in Goregaon East", "/eye-doctor-in-goregaon-east/"), ("Eye hospital in Goregaon East", "/eye-hospital-in-goregaon-east/"), ("Retina specialist", "/retina-specialist-goregaon-east/"), ("LASIK surgery", "/lasik-surgery-goregaon-east/"), ("Glaucoma treatment", "/glaucoma-treatment-malad-mumbai/"), ("Eye examination guide", "/eye-examination-test-malad.html")],
    },
    {
        "file": "best-eye-hospital-in-goregaon-east.html",
        "slug": "best-eye-hospital-in-goregaon-east",
        "kind": "best",
        "title": "Best Eye Hospital in Goregaon East: How to Choose | Sentra Clinic",
        "h1": "Best Eye Hospital in Goregaon East: Choose Care That Fits Your Eyes",
        "desc": "Looking for the best eye hospital in Goregaon East? Compare doctor involvement, diagnostics, surgery guidance and follow-up with Sentra Clinic in nearby Malad East.",
        "eyebrow": "Choosing eye care near Goregaon East",
        "hero_img": "clear",
        "hero_alt": "Clear vision and patient-focused eye care at Sentra Clinic near Goregaon East",
        "sections": [
            ("What “best” should mean in eye care", [
                "The phrase best eye hospital in Goregaon East is a useful search starting point, but it is not a medical diagnosis or a guarantee of a particular result. The most suitable provider depends on the patient’s condition. Someone with cataract needs a careful lens and eye-health assessment. Someone with diabetes needs retinal surveillance. Someone considering LASIK needs candidacy screening. A child needs attention to visual development, while a person with a painful red eye needs the correct diagnosis before any drop is chosen.",
                "Look beyond a polished website. Find out who examines the patient, how findings are explained, what tests are available or coordinated, how treatment alternatives are discussed and what happens after a procedure. A facility can be impressive yet unsuitable for a particular condition; a smaller doctor-led clinic can be a better fit when communication and continuity matter.",
                "Sentra Clinic in Malad East gives Goregaon East residents a nearby option for comprehensive consultation and planned eye care. The clinic’s approach is to match the service to the evidence and help patients make decisions without pressure."
            ]),
            ("A practical comparison checklist", [
                "Before booking, ask five questions. Is the doctor qualified to assess the problem? Will the examination look beyond spectacle power? Can the clinic explain which tests are needed and why? Will the surgeon discuss alternatives and limitations if a procedure is considered? Is there a clear route for follow-up or urgent concerns? The answers tell you more than a single star rating.",
                "You can also check whether the clinic publishes a complete address and contact number, whether the doctors are named, whether patient information avoids exaggerated promises and whether the language is respectful. Be cautious about claims of guaranteed perfect vision, universal painless treatment or a single “best” procedure for every person. Eye outcomes depend on anatomy, health, healing and adherence to aftercare.",
                "Take the same questions to a second opinion if you are uncertain. A second opinion is most useful when you carry the original reports and ask the new doctor to review the evidence, not when you collect disconnected opinions from short advertisements."
            ]),
            ("Why doctor involvement matters", [
                "A technician can record measurements, but a doctor must place them in context. The same eye-power change can be routine in one patient and a reason for further evaluation in another. A pressure reading can be normal for one person and concerning when combined with optic-nerve appearance or family history. A cataract scan may not explain poor vision if the retina or cornea has another problem.",
                "Sentra Clinic’s consultation model gives patients an opportunity to discuss what the findings mean with an ophthalmic doctor. Ask for a plain-language summary and write down the plan. If you do not understand a medical term, say so; a clear explanation is part of professional care.",
                "Doctor involvement also matters after treatment. Recovery questions, drop schedules and new symptoms need timely answers. Confirm the follow-up schedule before you leave and keep the clinic’s number available."
            ]),
            ("Matching the hospital to the problem", [
                "For routine vision, a comprehensive eye examination may be enough to identify refractive needs and common surface complaints. For cataract, look for an assessment that includes the lens and the rest of the eye, because visual improvement depends on more than the cloudy lens alone. For LASIK, insist on proper screening and a discussion of alternatives rather than choosing based only on a promotional price.",
                "For retina concerns, ask how urgent symptoms are handled and whether retinal evaluation or referral can be arranged. For glaucoma risk, understand that pressure alone is not the full diagnosis. For children, ask whether the examination is designed for the child’s age and whether eye alignment and visual development will be considered.",
                "The best provider is the one whose process fits the clinical question. Sentra Clinic can help Goregaon East patients identify the right starting appointment when they call, but urgent symptoms should be treated as urgent rather than waiting for a marketing promise."
            ]),
            ("Transparent decisions for surgery", [
                "A surgical consultation should feel like a decision conversation, not a sales presentation. Ask what the procedure is intended to improve, what it cannot improve, which alternatives exist and what happens if you do nothing for now. Cataract discussions may include lens choices and the patient’s reading, driving and work priorities. LASIK discussions may include corneal suitability, dryness, night vision and the possibility of future reading glasses.",
                "Ask for recovery instructions in writing. Understand restrictions on water, rubbing, work, screens, travel and driving. Confirm the number of follow-ups and how medicines are supplied. If the estimate has packages, ask what is included and what could cost extra. These questions help families plan financially and practically.",
                "Never allow urgency created by a discount to replace clinical suitability. Elective treatment can usually be considered after you have understood the findings. If a symptom is genuinely urgent, the team should explain that urgency in medical terms and direct you to timely care."
            ]),
            ("A better experience for Goregaon East families", [
                "A short, convenient route is valuable when a patient needs repeat visits, but convenience is only one part of quality. Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. When you call 93729 47075, share whether you need a checkup, second opinion, surgery consultation, retina review or a child’s assessment.",
                "If an older patient may need dilation, take sunglasses and arrange a companion. If a child is coming, bring school observations and previous glasses. If a person has diabetes, carry recent medical reports and medication details. If you have already used eye drops, bring the bottles so the doctor can identify them.",
                "Good preparation reduces time spent repeating history and helps the doctor focus on the patient’s actual question. It also creates a more useful record for future visits, particularly when different members of a family use the same clinic."
            ]),
            ("How to judge online eye-care information", [
                "Useful patient information explains symptoms, uncertainty, alternatives and warning signs. It does not diagnose every reader or promise identical results. Look for a named medical team, a real clinic address, a way to contact the provider and language that encourages examination when symptoms persist. A page should also distinguish educational content from personalised medical advice.",
                "Use online reviews to learn about communication, waiting experience and general organisation, but do not treat them as proof that a particular operation is right for you. Ask for the findings from your own examination. Compare written estimates and recovery plans rather than only prices.",
                "Sentra Clinic’s pages can help you decide what to ask, but the final treatment decision belongs in a consultation. If you have sudden vision loss, severe pain, a penetrating injury or chemical exposure, seek urgent medical assistance immediately."
            ]),
        ],
        "faq": [
            ("Is there one universally best eye hospital in Goregaon East?", "No. The right hospital depends on the patient’s condition, required tests, doctor expertise, communication and follow-up. Compare care on those factors rather than a superlative alone."),
            ("Why do patients from Goregaon East visit Sentra Clinic?", "Sentra Clinic in Malad East offers doctor-led consultations and planned care for routine vision, cataract, LASIK, retina, cornea, glaucoma and family eye concerns."),
            ("What should I compare before cataract surgery?", "Compare the diagnosis, surgeon involvement, lens options, expected visual goals, alternatives, recovery instructions, follow-up and a complete written estimate."),
            ("Can reviews prove that a treatment will work for me?", "No. Reviews describe other people’s experiences. Your suitability and likely outcome depend on your own eye examination, health, anatomy and adherence to aftercare."),
            ("How can I contact Sentra Clinic?", "Call 93729 47075 or WhatsApp +91 93729 47075. The address is Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East.")
        ],
        "related": [("Eye hospital in Goregaon East", "/eye-hospital-in-goregaon-east/"), ("Eye doctor in Goregaon East", "/eye-doctor-in-goregaon-east/"), ("Ophthalmologist in Goregaon East", "/ophthalmologist-in-goregaon-east/"), ("Cataract surgery", "/cataract-surgery-goregaon-east/"), ("LASIK surgery", "/lasik-surgery-goregaon-east/"), ("Eye clinic and checkup", "/eye-clinic-and-checkup-in-goregaon-east/")],
    },
    {
        "file": "eye-clinic-and-checkup-in-goregaon-east.html",
        "slug": "eye-clinic-and-checkup-in-goregaon-east",
        "kind": "clinic",
        "title": "Eye Clinic & Eye Checkup in Goregaon East | Sentra Clinic",
        "h1": "Eye Clinic and Eye Checkup in Goregaon East for Every Age",
        "desc": "Book an eye checkup in Goregaon East at Sentra Clinic, Malad East. Get comprehensive vision, cataract, dry eye, retina and family eye-care guidance.",
        "eyebrow": "Eye clinic and checkup near Goregaon East",
        "hero_img": "cataract",
        "hero_alt": "Patient-focused eye clinic and checkup care near Goregaon East",
        "sections": [
            ("Why a checkup is useful even without pain", [
                "Many people search for an eye clinic in Goregaon East only after vision becomes uncomfortable. But an eye checkup can be useful before a problem interferes with work, study or driving. Some conditions develop gradually and may not hurt. A child may not know that one eye is weaker. An adult may assume that night glare is just tiredness. A person with diabetes may see normally while retinal changes develop in the background.",
                "A comprehensive visit begins with the reason for booking and then considers age, symptoms, health, family history, work and previous prescriptions. The doctor can decide whether the patient needs a routine vision review, a dilated retinal assessment, eye-pressure evaluation, dry-eye examination, cataract opinion or another focused pathway. This avoids treating every patient as if the same checklist is appropriate.",
                "Sentra Clinic in Malad East welcomes Goregaon East patients who want a clear plan. Call before travelling to confirm the appointment and tell the team whether the visit is for a child, an older adult, a contact-lens user, a diabetes review or a new symptom."
            ]),
            ("What a comprehensive eye checkup can include", [
                "The exact examination varies, but a checkup may include visual acuity, refraction, eye movement and alignment, assessment of the front of the eye, pressure measurement and a review of the retina when indicated. The doctor may ask about glare, reading comfort, headaches, screen use, dryness, watering, family history and medicines. If a test is recommended, ask what clinical question it answers.",
                "A glasses-power check does not always equal a medical eye examination. A new lens can improve clarity while an underlying condition remains unnoticed. Conversely, a patient may have a normal eye health examination but need a different prescription or advice about near focus. The distinction helps avoid both unnecessary anxiety and false reassurance.",
                "If dilation is advised, the team can explain why. Pupils may remain larger and near vision may be temporarily blurred, so carry sunglasses and arrange a companion if needed. Ask when it is safe to drive and return to close work."
            ]),
            ("Checkup guidance for children and students", [
                "Children often adapt to blurred vision, especially when the stronger eye is doing more work. Parents may notice sitting very close to screens, frequent blinking, rubbing, closing one eye, tilting the head, losing place while reading or avoiding tasks that need distance vision. A school screening can be helpful, but a persistent concern deserves a proper examination.",
                "Bring the child’s previous glasses, school observations and information about family eye conditions. Be honest about how often the glasses are worn; the doctor needs the real routine to understand progress. Do not turn the visit into an exam that the child must pass. Calm reassurance helps the child respond naturally.",
                "The doctor may discuss glasses, visual development, eye alignment, follow-up or further assessment. Parents should ask how to monitor the child at home and which changes should prompt an earlier review. Early guidance can support learning without assuming that every child needs treatment beyond glasses."
            ]),
            ("Checkups for adults, screens and contact lenses", [
                "Adults who use laptops and phones for long periods may experience dryness, fluctuating focus, burning or forehead discomfort. Breaks, complete blinking, a comfortable screen position and avoiding direct air-conditioning can help, but symptoms that continue should be assessed. The doctor may need to consider the tear film, eyelids, contact-lens habits, prescription and other causes.",
                "Contact-lens users should bring the lens brand or details, wearing schedule and cleaning products. Do not wear lenses longer than advised and never sleep in them unless specifically instructed. Pain, light sensitivity, marked redness or reduced vision while using lenses needs prompt medical advice because some corneal problems can worsen quickly.",
                "For adults over 40, near focus commonly changes and reading glasses may become useful. That does not mean every change is harmless. Mention glare, night-driving difficulty, one-sided blur, new floaters and difficulty recognising faces so the doctor can decide what to examine."
            ]),
            ("Diabetes, blood pressure and preventive eye care", [
                "People with diabetes benefit from eye reviews advised by their physician and eye doctor, even when vision feels normal. Retinal changes can be symptom-free at first. Bring recent blood-sugar reports, medicines and previous retinal scans. Tell the doctor about blood-pressure problems, kidney disease, pregnancy or any earlier laser or injection treatment.",
                "Blood pressure and other health conditions can also affect eye risk. Eye care works best alongside general medical care: continue the plan from your physician, do not stop medicines because an eye report looks normal and ask how often your eye review should happen. A clinic can identify findings, but long-term health management is a shared process.",
                "A checkup is not a promise that disease will be found or prevented. It is a chance to identify risk, create a baseline and receive advice matched to the patient. Keep the next due date in a calendar and carry reports to future appointments."
            ]),
            ("Cataract, retina and dry-eye conversations", [
                "Cataract can cause hazy vision, glare, faded colours and difficulty with steps or night travel. An examination confirms whether the lens is the main cause and whether another part of the eye also needs attention. Surgery timing is based on daily impact and findings, while lens discussions should reflect reading, driving and work needs.",
                "Flashes, new floaters, a curtain-like shadow or sudden vision loss are not routine checkup symptoms. Contact a doctor promptly and seek urgent care. A scheduled appointment may not be appropriate if the change is sudden. Take the onset seriously even if there is no pain.",
                "Dry eye may cause burning, gritty sensation, fluctuating clarity and watering. Treatment depends on the cause, including screen habits, tear evaporation, eyelid health, allergy, medicines and contact lenses. Avoid using steroid or antibiotic drops without medical supervision."
            ]),
            ("Planning your visit to a local eye clinic", [
                "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. When you call 93729 47075, tell the team the patient’s age, the reason for the visit and whether any report or surgery recommendation already exists. This makes it easier to suggest a suitable appointment.",
                "Carry current glasses, old prescriptions, reports, scan images, medicine names and contact-lens details. Write down symptoms, their start date, screen habits and any warning signs. For a child, bring a parent who knows the school concern. For an elderly patient, arrange help with travel and notes.",
                "Allow time for a proper consultation rather than scheduling it between two rushed commitments. If dilation or additional testing is needed, the visit may take longer. Ask whether a companion should drive and when the patient can return to close work."
            ]),
        ],
        "faq": [
            ("Where can I book an eye checkup in Goregaon East?", "Sentra Clinic is located in nearby Malad East and serves Goregaon East patients. Call 93729 47075 to ask about appointment availability and the most suitable checkup."),
            ("Is a spectacle test the same as a full eye checkup?", "No. Refraction measures focusing power, while a comprehensive examination may also assess the front of the eye, pressure, alignment and retina according to the patient’s needs."),
            ("How often should children have an eye checkup?", "The appropriate interval depends on age, symptoms, visual development, glasses and medical history. Ask the ophthalmologist for a schedule specific to the child."),
            ("Can contact-lens users visit this eye clinic?", "Yes. Bring lens details and cleaning products, and report pain, light sensitivity, redness or reduced vision promptly. Do not self-treat a painful contact-lens eye."),
            ("What is the address and phone number?", "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 or WhatsApp +91 93729 47075.")
        ],
        "related": [("Eye doctor in Goregaon East", "/eye-doctor-in-goregaon-east/"), ("Ophthalmologist in Goregaon East", "/ophthalmologist-in-goregaon-east/"), ("Eye hospital in Goregaon East", "/eye-hospital-in-goregaon-east/"), ("Diabetic eye checkup", "/diabetic-eye-checkup-malad-west/"), ("Dry eye treatment", "/dry-eye-treatment-malad/"), ("Children’s eye care", "/children-eye-specialist-malad-mumbai/")],
    },
]

EXTRAS = {
    "hospital": [("A useful long-term eye-care relationship", [
        "Eye health is rarely a single transaction. A patient may first visit with changing glasses, return for a cataract opinion years later and need a retina review if diabetes changes. Keeping reports together and returning to a clinic that knows the history can make those decisions easier. Ask for copies of important prescriptions, scans and procedure notes, and tell the team if another doctor has changed the treatment.",
        "Families should also discuss practical safety. An older adult with glare may need help on stairs or while driving at night before surgery is planned. A child who cannot see the board may need school support while glasses are being arranged. A working adult with persistent dryness may need a realistic screen and contact-lens plan rather than a temporary drop. A doctor-led hospital can connect the examination to the patient’s real routine.",
        "If a symptom changes between visits, do not wait for the next annual checkup. Call and describe what changed, when it began and whether vision, pain or light sensitivity is involved. Early communication helps the team decide whether a routine appointment is appropriate or whether urgent assessment is safer."
    ])],
    "doctor": [("Getting more value from follow-up", [
        "Follow-up is where a doctor checks whether the diagnosis and treatment plan are working. Bring the previous prescription and describe what improved, what stayed the same and what became worse. If you used drops, note the actual schedule rather than an ideal schedule. This is not a test; honest information helps the doctor adjust the plan safely.",
        "Ask whether you should continue the same glasses or lens routine, whether screen breaks are enough, and what the next review is meant to measure. For a surgery discussion, ask how the result will be assessed and which temporary symptoms are expected. For an older patient, ask a family member to listen and help with reminders. Written instructions are useful when several medicines are involved.",
        "A local eye doctor can become a reliable first contact for future concerns, but urgent changes still need urgent action. Keep the clinic number saved and mention the patient’s previous diagnosis when calling. Do not send private medical records over an unconfirmed channel; ask the team how to share them."
    ])],
    "ophthalmologist": [("Making a shared treatment decision", [
        "The patient’s preference is important in ophthalmology, especially when more than one safe option exists. Tell the doctor what matters most: reading small print, driving at night, playing sport, working on a screen, caring for family or avoiding frequent drops. These priorities help the ophthalmologist explain trade-offs in a way that is relevant, rather than giving a generic recommendation.",
        "Ask for the diagnosis, the evidence for it and the uncertainty that remains. If observation is reasonable, ask what would change the plan. If treatment is recommended, ask about timing, alternatives, recovery and the consequences of delaying. A family member can help record the answers, but the patient should have space to ask questions directly.",
        "Good consent is a process. It includes enough time to read instructions, understand the estimate and decide freely. If you feel rushed, request another explanation or a follow-up discussion. Patients travelling from Goregaon East can call Sentra Clinic to plan the appointment around the reports and questions they need to review."
    ]), ("Questions that improve a specialist review", [
        "Before the appointment, write down the main visual task that has become difficult and the time of day when it happens. Mention whether the issue is stable, progressing or different between the two eyes. This gives the ophthalmologist a clearer starting point than a general description such as “my eyesight is weak.”",
        "At the end, ask which result matters most, what should be monitored and whether the next visit needs a particular test. Understanding the reason for follow-up helps patients attend on time and notice meaningful changes without checking the eyes anxiously every hour."
    ])],
    "best": [("A patient-centred definition of quality", [
        "Quality is also visible in small details: the clinic asks about allergies before advising a drop, checks whether an elderly patient understood dilation instructions, gives a contact number for follow-up and avoids making a patient feel guilty for seeking another opinion. These behaviours do not replace clinical skill, but they make good care easier to use.",
        "For families comparing providers, write down the same questions and compare the answers. What is the suspected problem? What examination supports it? Is treatment urgent? What are the alternatives? What will recovery require? Who should be contacted if something changes? A provider who answers clearly gives you a better foundation for a safe decision.",
        "Sentra Clinic cannot promise that every procedure is suitable or that every patient will have the same result. It can offer an examination, a discussion of options and a practical route to follow-up. That honest boundary is more useful than a slogan because it keeps the focus on the patient’s own eyes."
    ]), ("The right fit matters more than a ranking", [
        "A patient with a straightforward glasses change may need a different service from somebody with a complex retinal history. Families should therefore describe the actual need when they call rather than asking only for the “best” package. The team can explain whether a routine appointment, a surgical opinion or quicker guidance is the sensible first step.",
        "Take time to read instructions, understand the expected follow-up and decide with the people who will support recovery. A confident choice is one where the patient knows what is being treated, what remains uncertain and how to ask for help after the visit."
    ])],
    "clinic": [("After the checkup: turning advice into action", [
        "A checkup becomes valuable when the advice is followed. If glasses are prescribed, wear them in the situations discussed and notice whether clarity, headaches or school performance changes. If lubricating drops are advised, use them as directed and ask when to review. If the examination is normal, keep the recommended interval rather than assuming another visit is never needed.",
        "Put the next appointment date in a calendar and store reports in one folder. Families can take a photograph of the prescription for reference, but keep the original document safe. If a child loses glasses, if a contact lens causes pain or if an older adult suddenly sees less, contact the clinic instead of waiting for the next scheduled visit.",
        "Good eye care also includes protecting the eyes during dusty work, using appropriate safety eyewear, washing hands before touching lenses and avoiding unverified home remedies. These steps support, but do not replace, professional examination. Share any change in symptoms when you call Sentra Clinic so the team can guide you accurately."
    ]), ("Small habits that protect a checkup baseline", [
        "Keep a note of when your last prescription changed and whether the change helped. If you use screens for work, notice whether blur improves after blinking or continues even after rest. These observations can help the clinician distinguish a temporary comfort issue from a persistent vision complaint.",
        "Parents and caregivers should keep the clinic’s instructions with the child’s or older adult’s medicines. A simple written schedule prevents missed reviews and makes it easier to explain the history if another doctor is needed. When the eyes feel suddenly different, use the saved contact number instead of relying on an old internet answer."
    ])],
}

def words(html: str) -> int:
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return len(re.findall(r"\b[\w’'-]+\b", text))

def faq_schema(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }

def render(page):
    first, second = COMMON_INTRO[page["kind"]]
    image = IMAGES[page["hero_img"]]
    sections = [
        ("A local starting point for Goregaon East", [first, second]),
        *page["sections"],
        *EXTRAS[page["kind"]],
    ]
    parts = [f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(page["title"])}</title>
<meta name="description" content="{escape(page["desc"])}">
<link rel="canonical" href="{BASE}/{page["slug"]}/">
<meta property="og:type" content="website"><meta property="og:title" content="{escape(page["title"])}">
<meta property="og:description" content="{escape(page["desc"])}"><meta property="og:url" content="{BASE}/{page["slug"]}/">
<meta property="og:image" content="{image}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg">
<style>{CSS}</style></head><body>
<main class="sc-wrap">
<p class="sc-breadcrumb"><a href="/">Home</a> / <a href="/areas-we-serve/">Areas We Serve</a> / {escape(page["h1"])}</p>
<section class="sc-hero"><div>
<span class="sc-eyebrow">{escape(page["eyebrow"])}</span>
<h1>{escape(page["h1"])}</h1>
<p>{escape(first)}</p>
<div class="sc-btn-row"><a class="sc-btn" href="{WHATSAPP}">WhatsApp {PHONE_DISPLAY}</a><a class="sc-btn-outline" href="tel:{PHONE}">Call {PHONE_DISPLAY}</a></div>
</div><div><img class="sc-img" src="{image}" alt="{escape(page["hero_alt"])}" width="1200" height="800"></div></section>
<div class="sc-cta"><p>Planning an eye visit from Goregaon East? Call {PHONE_DISPLAY} for appointment guidance and directions to Sentra Clinic, Malad East.</p><div class="sc-btn-row"><a class="sc-btn" href="tel:{PHONE}">Book by phone</a><a class="sc-btn-outline" style="color:var(--navy)!important;border-color:var(--navy)" href="{WHATSAPP}">Message on WhatsApp</a></div></div>
"""]
    for index, (heading, paras) in enumerate(sections):
        cls = "sc-section"
        parts.append(f'<section class="{cls}"><h2>{escape(heading)}</h2>')
        for p in paras:
            parts.append(f"<p>{escape(p)}</p>")
        if index in (1, 3, 5):
            key = ["lasik", "retina", "shraddha"][index // 2 - 1]
            alt = {
                "lasik": "LASIK vision correction information for Goregaon East patients at Sentra Clinic",
                "retina": "Retina care consultation for patients from Goregaon East at Sentra Clinic",
                "shraddha": "Ophthalmology consultation with Dr. Shraddha Surekha at Sentra Clinic",
            }[key]
            parts.append(f'<img class="sc-img" src="{IMAGES[key]}" alt="{alt}" loading="lazy" width="1200" height="800">')
        parts.append("</section>")
    parts.append("""<section class="sc-section"><h2>Services patients commonly ask about</h2>
<div class="sc-grid-3">
<article class="sc-card"><h3>Vision and glasses</h3><p>Assessment for changing power, reading comfort, screen strain and everyday visual needs.</p></article>
<article class="sc-card"><h3>Cataract planning</h3><p>Examination-led guidance about lens clouding, measurements, treatment timing and recovery.</p></article>
<article class="sc-card"><h3>Retina and diabetes</h3><p>Symptom-aware guidance for diabetes reviews, flashes, floaters and retinal concerns.</p></article>
</div></section>""")
    parts.append('<section class="sc-related"><h2>Helpful Sentra Clinic resources</h2><div class="sc-related-grid">')
    for label, href in page["related"]:
        parts.append(f'<a href="{href}">{escape(label)} <span aria-hidden="true">→</span></a>')
    parts.append("</div></section>")
    parts.append('<section class="sc-section"><h2>Frequently asked questions</h2><div class="sc-faq">')
    for q, a in page["faq"]:
        parts.append(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>")
    schema_json = escape(json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "MedicalClinic", "@id": f"{BASE}/#clinic", "name": "Sentra Clinic", "url": BASE, "telephone": f"+91 {PHONE_DISPLAY}", "image": image, "address": {"@type": "PostalAddress", "streetAddress": "Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road", "addressLocality": "Malad East", "addressRegion": "Maharashtra", "postalCode": "400097", "addressCountry": "IN"}, "areaServed": ["Goregaon East", "Malad East", "Mumbai"]},
            {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}, {"@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": BASE + "/areas-we-serve/"}, {"@type": "ListItem", "position": 3, "name": page["h1"], "item": f"{BASE}/{page['slug']}/"}]},
            faq_schema(page["faq"]),
        ],
    }), quote=False)
    parts.append(f"""</div></section>
<section class="sc-grid-2">
<div><img class="sc-img" src="{IMAGES["doctors"]}" alt="Sentra Clinic doctors providing eye care to families from Goregaon East" loading="lazy" width="1200" height="800"></div>
<div><h2>Plan your visit</h2><p>Sentra Clinic is at <strong>{ADDRESS}</strong>. Call <a href="tel:{PHONE}">{PHONE_DISPLAY}</a> or use <a href="{WHATSAPP}">WhatsApp</a> to ask about an appointment. Please share the main concern when booking so the team can guide you to the right consultation.</p><p>This page is educational and does not replace a medical examination. Sudden vision loss, severe eye pain, major trauma, chemical exposure, new flashes or a curtain-like shadow require prompt medical assessment.</p></div>
</section>
<p class="sc-disclaimer"><strong>Medical information note:</strong> Individual treatment, investigation and follow-up decisions depend on the patient’s examination and history. Do not start, stop or share eye drops without medical advice.</p>
<a class="sc-float" href="tel:{PHONE}">Call eye clinic</a>
</main>
<script type="application/ld+json">{schema_json}</script>
</body></html>""")
 
    return "\n".join(parts)

if __name__ == "__main__":
    for page in PAGES:
        html = render(page)
        count = words(html)
        if count < 2000:
            raise SystemExit(f"{page['file']} only has {count} words")
        (OUT / page["file"]).write_text(html, encoding="utf-8")
        print(f"{page['file']}: {count} words, {html.count('<img ')} images, {html.count('<h2>')} H2s")