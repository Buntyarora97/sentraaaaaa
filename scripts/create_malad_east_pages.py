"""Generate the five Malad East landing pages from the existing Sentra design system.

The project is a WordPress-ready static content pack. Keeping the content in a
small generator makes future medical/team-detail corrections less error-prone.
Run: python3 scripts/create_malad_east_pages.py
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "57-eye-specialist-malad-east.html"

IMAGES = {
    "team": "https://sentraclinic.com/wp-content/uploads/2025/04/Doctors-image.png",
    "rohit": "https://sentraclinic.com/wp-content/uploads/2025/04/Dr.-Rohit-Modi-min.png",
    "shraddha": "https://sentraclinic.com/wp-content/uploads/2025/04/Dr.-Shraddha-Surekha-min-1.png",
    "lasik": "https://sentraclinic.com/wp-content/uploads/2025/04/Lasik-Surgery-min-1-scaled.jpg",
    "vision": "https://sentraclinic.com/wp-content/uploads/2025/04/sharper-vision-min-scaled.jpg",
    "sports": "https://sentraclinic.com/wp-content/uploads/2025/04/Active-life-sports-min-scaled.jpg",
    "clear": "https://sentraclinic.com/wp-content/uploads/2025/04/clear-vision-min-scaled.jpg",
    "cataract": "https://sentraclinic.com/wp-content/uploads/2025/04/Cataract-surgery-min-scaled.jpg",
    "cornea": "https://sentraclinic.com/wp-content/uploads/2025/04/Cornea-care-min-scaled.jpg",
    "retina": "https://sentraclinic.com/wp-content/uploads/2025/04/Retina-care-min-scaled.jpg",
    "retina2": "https://sentraclinic.com/wp-content/uploads/2025/04/retina-treatment-image-2-min-scaled.jpg",
    "family": "https://sentraclinic.com/wp-content/uploads/2025/04/convinence-min-scaled.jpg",
}


PAGES = [
    {
        "file": "70-eye-hospital-malad-east.html",
        "slug": "eye-hospital-malad-east",
        "title": "Eye Hospital in Malad East | Sentra Clinic",
        "description": "Looking for an eye hospital in Malad East? Sentra Clinic offers comprehensive eye checkups, cataract, LASIK, cornea, glaucoma and retina care on Rani Sati Road.",
        "eyebrow": "Complete eye hospital care · Malad East",
        "h1": "Eye Hospital in Malad East for Complete, Connected Eye Care",
        "hero": "team",
        "hero_alt": "Eye hospital team at Sentra Clinic serving Malad East patients",
        "image_keys": ["team", "retina2", "rohit", "shraddha"],
        "intro": [
            "Finding an eye hospital in Malad East should not mean visiting one place for a test, another for a specialist opinion and a third for surgery. Sentra Clinic brings consultation, diagnostic evaluation, treatment planning and follow-up together at Shah Arcade 2 on Rani Sati Road. Patients from Malad East, Dindoshi, Kurar, Pathanwadi, Raheja Township and nearby Thakur Village can begin with a conversation about what has changed in their vision and receive a clear next step.",
            "Our eye hospital approach is deliberately personal. A routine eye checkup in Malad East may be all that is needed for one patient, while another may need a retina assessment, cataract discussion or cornea evaluation. The purpose of a detailed examination is not to sell a procedure; it is to identify the reason behind blurred vision, pain, redness, glare or fluctuating sight and explain sensible options in plain language. If you need urgent attention, call before travelling so the team can guide you to the right care pathway."
        ],
        "stats": [("01", "single care address"), ("04+", "core eye specialties"), ("60–90", "minutes for a full checkup"), ("1", "clear next step")],
        "sections": [
            ("Why an eye hospital is different from a basic optical visit", [
                "An optical store can help with a spectacle prescription, but an eye hospital is designed to look beyond the number on a pair of glasses. A complete evaluation can consider the cornea, lens, retina, optic nerve, eye pressure, eye movements and the health of both eyes. This matters when a person says that new glasses are not helping, night driving has become uncomfortable or one eye sees differently from the other. Early disease can be quiet, so a normal-looking eye is not always proof that every structure is healthy.",
                "At Sentra Clinic, the consultation begins with your history: diabetes, blood pressure, medicines, previous surgery, family history and the time pattern of your symptoms. Testing is selected around that history rather than performed as a meaningless checklist. When dilation is useful, the doctor explains the temporary blur and how to plan your day. The result is a practical report: what is normal, what needs monitoring, what treatment is reasonable and when to return."
            ]),
            ("Services available for Malad East families", [
                "People search for an eye hospital in Malad East for many different reasons. Children may need a first vision assessment, myopia monitoring, squint evaluation or advice about screen habits. Adults often come for dry eye, headaches, contact-lens discomfort, computer vision symptoms or a changing spectacle number. Older adults may notice glare, faded colours, difficulty reading, halos or slower adaptation in dim light, which can be associated with cataract or other age-related conditions.",
                "The clinic’s wider care pathway includes comprehensive eye checkups, cataract counselling, LASIK and refractive evaluation, cornea care, glaucoma assessment, retina and diabetic-eye review, paediatric eye care and selected surgical procedures. A service name is never a diagnosis. The right route depends on your examination, medical history and expectations. If a condition needs a hospital or subspecialist not available here, the team can explain that openly instead of delaying appropriate care."
            ]),
            ("What happens during your first visit", [
                "Bring old prescriptions, previous scan reports, discharge papers, a list of medicines and your glasses or contact lenses. Tell the team whether the issue is sudden or gradual, whether it affects one eye or both, and whether there is pain, redness, light sensitivity, flashes, floaters or a curtain-like shadow. These details can change the urgency of the visit. Parents should mention birth history, school complaints and whether a child avoids reading or closes one eye in sunlight.",
                "A typical visit may include vision measurement, refraction, eye alignment and movement assessment, slit-lamp examination and pressure or retina evaluation when indicated. Some patients need dilation or additional imaging. Do not drive yourself if dilation has been advised, especially for a first visit. A complete eye checkup in Malad East commonly takes 60–90 minutes, although a focused follow-up may be shorter. Ask for the written plan before leaving and keep it for future comparisons."
            ]),
            ("Cataract and surgical care with a planned pathway", [
                "Cataract is not simply a foggy spectacle number. The natural lens becomes less clear and may cause glare, reduced contrast, faded colours and difficulty with night travel. Surgery is discussed when the vision change interferes with work, mobility, reading or independence—not only when a chart reaches a particular line. During the consultation, the doctor examines the eye, reviews health conditions and explains what an intraocular lens is intended to achieve. The decision remains yours after understanding benefits, limits and recovery.",
                "For LASIK or another refractive procedure, the first step is eligibility testing, not a promise. Corneal thickness, shape, tear film, stable prescription, age, eye health and general expectations all matter. Retina, cornea or glaucoma findings may need attention before elective vision correction. A safe eye hospital in Malad East should be willing to say “not yet” or “not suitable” when that is the medically responsible answer. Pre-operative instructions, consent, medicines and follow-up should be documented clearly."
            ]),
            ("Retina, glaucoma and diabetic-eye awareness", [
                "Retina conditions can threaten vision without pain. People with diabetes should not wait for blurred vision before arranging a dilated retinal examination, because diabetic changes can develop quietly. New flashes, a sudden shower of floaters, a dark curtain or an abrupt drop in sight are urgent symptoms. They need prompt medical guidance rather than home remedies or a wait for the next routine appointment. Call the clinic and describe the exact timing and symptoms.",
                "Glaucoma is another reason regular eye checkups matter. Eye pressure is only one part of the assessment; the optic nerve, visual field, cornea and family history also influence risk. A single normal pressure reading does not rule out every form of glaucoma. Sentra Clinic can help with assessment and follow-up planning for Malad East residents, including when a repeat test or specialist review is sensible. Carry old reports because trends over time are often more useful than one isolated result."
            ]),
            ("A calmer experience for children and older adults", [
                "An eye hospital can feel intimidating to a child, so the first visit should be explained as a set of simple games and pictures rather than a punishment. Parents can bring the child’s school diary or teacher note and avoid saying that an examination will hurt. If glasses are prescribed, fit and wearing habits matter. Regular review is useful because children’s eyes change as they grow, and a missed visual problem can affect classroom confidence.",
                "Older adults may need extra time, assistance with forms and a plan for travelling after dilation. Keep a current medicine list and bring a family member if the treatment decision is complex. Ask how cataract, glaucoma, macular or diabetic changes could affect daily tasks such as stairs, cooking, reading labels and crossing a road. Good eye care includes practical safety advice, not only a diagnosis. The team can help organise the next visit around the patient’s mobility and support needs."
            ]),
            ("Location, appointment planning and transparent communication", [
                "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. The location is convenient for residents around Dindoshi, Kurar and the eastern side of Malad, but traffic and parking conditions can vary. Use the map link or call 93729 47075 before leaving if you need directions, wheelchair assistance or a particular appointment slot. WhatsApp is also available for appointment coordination at +91 93729 47075.",
                "Fees and procedure costs depend on the examination and the treatment plan, so a responsible estimate should be based on your case rather than a generic internet number. Ask what is included: consultation, investigations, surgeon fees, medicines, lens or device, follow-up and any possible additional test. A clear written estimate helps families compare care fairly. If you are anxious, bring your questions; the best consultation is one where you understand the reasoning before agreeing to treatment."
            ]),
            ("When to book an eye checkup in Malad East", [
                "Book a routine examination if your glasses no longer feel right, you are getting frequent headaches while reading, you have persistent dryness or you have not had an eye health review for several years. People with diabetes, high blood pressure, a strong family history of glaucoma, previous eye injury or long-term steroid use may need a personalised schedule. Contact-lens users should not ignore pain, discharge or light sensitivity; remove lenses and seek advice promptly.",
                "Do not wait for a routine slot for sudden vision loss, severe eye pain, a chemical injury, a penetrating injury, a new curtain or a sudden cluster of flashes and floaters. Avoid putting someone else’s drops in the eye, especially steroid drops, unless a doctor has prescribed them for that episode. Call Sentra Clinic on 93729 47075 for direction. This page is educational and does not replace an in-person examination."
            ]),
        ],
        "cards": [
            ("🔎 Comprehensive checkup", "A structured look at vision, pressure, front-of-eye and retinal health.", "/comprehensive-eye-checkup-malad/"),
            ("💎 Cataract pathway", "Understand when cataract surgery may improve daily function.", "/cataract-surgery-malad-mumbai/"),
            ("🔬 Retina review", "Diabetic-eye and retinal symptoms deserve timely assessment.", "/retina-specialist-malad-mumbai/"),
        ],
        "faqs": [
            ("Where is the eye hospital in Malad East?", "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 for directions and current appointment availability."),
            ("Can I book an eye checkup in Malad East without knowing which specialist I need?", "Yes. Start with a comprehensive consultation and explain your symptoms and history. The doctor can recommend the appropriate examination or subspecialty pathway after assessing you."),
            ("Do you treat cataract and retina problems at the same location?", "The clinic provides evaluation and treatment planning for cataract, retina and other eye conditions. The exact procedure or referral depends on the examination and the patient’s medical needs."),
            ("How long does a full eye examination take?", "A comprehensive examination commonly takes 60–90 minutes, especially if dilation or additional tests are needed. A focused follow-up may take less time."),
            ("Should a person with diabetes get an eye examination even without symptoms?", "Yes. Diabetic retinal changes may be present before vision becomes noticeably blurred. The doctor will suggest a review interval based on diabetes control and retinal findings."),
            ("Can children visit this eye hospital?", "Yes. Children can be assessed for vision, myopia, squint, lazy eye and other concerns. Bring school observations and previous prescriptions when available."),
            ("What should I bring to my first appointment?", "Bring current glasses, old reports, medicine details, diabetes or blood-pressure records and information about when the symptoms started. Contact-lens users should bring their lens details."),
        ],
    },
    {
        "file": "71-eye-doctor-malad-east.html",
        "slug": "eye-doctor-malad-east",
        "title": "Eye Doctor in Malad East | Sentra Clinic",
        "description": "Book an eye doctor in Malad East for blurred vision, dry eye, cataract, children’s eye concerns, retina screening and a complete eye checkup on Rani Sati Road.",
        "eyebrow": "Personalised consultation · Malad East",
        "h1": "Eye Doctor in Malad East Who Starts With Listening",
        "hero": "rohit",
        "hero_alt": "Eye doctor Dr Rohit Modi at Sentra Clinic for Malad East patients",
        "image_keys": ["rohit", "sports", "shraddha", "team"],
        "intro": [
            "When you search for an eye doctor in Malad East, you may already know the symptom but not the cause. Blurred vision can be a spectacle number, dry eye, cataract, corneal irregularity, retinal change or a problem that needs urgent attention. A useful consultation begins by listening to the full story: when the symptom started, whether it changes during the day, what makes it better or worse and how it affects work, travel and family life.",
            "Sentra Clinic offers eye consultations on Rani Sati Road for adults, children and older family members. The first appointment is not a race to prescribe a stronger lens. It is an opportunity to check the health of both eyes, explain what the tests mean and build a follow-up plan that matches your risk. For appointment coordination, call 93729 47075 or WhatsApp +91 93729 47075 before visiting."
        ],
        "stats": [("1:1", "doctor discussion"), ("360°", "history-led assessment"), ("7", "common symptom groups"), ("60–90", "minutes for full review")],
        "sections": [
            ("How to choose the right eye doctor", [
                "A good eye doctor should be comfortable with routine vision care and know when a symptom needs a deeper evaluation. Look for a consultation that includes questions about your medical history, medicines, family history and previous eye procedures, not only a quick refraction. You should be able to ask why a test is needed, what the result means and what happens if you choose monitoring instead of immediate treatment.",
                "Location matters too. A doctor near Malad East makes it easier to attend follow-ups, compare reports over time and bring a parent or child when needed. Sentra Clinic serves patients around Dindoshi, Kurar, Pathanwadi, Thakur Village and nearby neighbourhoods. The right doctor-patient relationship is not based on a “best” label alone; it is built through careful examination, honest expectations and instructions you can actually follow."
            ]),
            ("Symptoms that deserve an appointment", [
                "Arrange an eye consultation for recurring headaches after screen work, squinting, trouble reading road signs, glare around lights, eye fatigue, dry or gritty eyes, watering, a change in colour perception or a spectacle number that changes repeatedly. Children may show signs indirectly: holding a book close, sitting too near the television, tilting the head, closing one eye, avoiding homework or losing place while reading. Teachers’ observations can be valuable.",
                "Some symptoms should not be treated as a routine glasses problem. Sudden loss of sight, severe pain, an eye injury, chemical exposure, a new curtain or shadow, or sudden flashes with many floaters needs prompt advice. Do not self-medicate with leftover antibiotics or steroid drops. Remove contact lenses if the eye is painful and call the clinic. If the symptom is time-critical, the doctor or team can guide you to emergency care rather than asking you to wait."
            ]),
            ("What your consultation may include", [
                "A complete eye checkup in Malad East may include visual acuity, refraction, alignment, eye movements, the front-of-eye examination, eye pressure and a retinal assessment when indicated. The doctor chooses the sequence based on age and symptoms. Dilation can help view the retina more thoroughly, but it may temporarily blur near vision and increase light sensitivity. Plan transport and sunglasses if dilation is likely, and never feel embarrassed to ask for the reason behind it.",
                "The most important part is the explanation after the tests. You should leave knowing whether the issue is optical, surface-related, lens-related, retinal, pressure-related or still uncertain. Ask for copies or photographs of important reports, the name of any prescribed drop, how often to use it and what warning signs should trigger a call. Keeping a simple timeline of symptoms and medicines makes the next consultation more useful."
            ]),
            ("Common reasons adults visit an eye doctor", [
                "Working adults in Malad East often postpone eye care because the symptom seems manageable. Screen-related dryness, changing focus between phone and distance, contact-lens intolerance and glare can gradually reduce productivity and comfort. An examination can distinguish a correctable prescription problem from an ocular-surface issue or another cause. Breaks, blinking, a sensible screen distance and adequate sleep support comfort, but they do not replace an examination when symptoms persist.",
                "Adults may also seek advice before LASIK, while considering cataract surgery, after an eye injury or because a parent had glaucoma. Elective procedures require realistic expectations and stable eye health. The eye doctor should review corneal shape, tear film and other findings before discussing refractive correction. Cataract decisions similarly depend on daily function and overall eye health, not only on the word “mature” or an internet price."
            ]),
            ("Children, parents and school vision", [
                "Children do not always report blur because they assume the world looks the same to everyone. A paediatric eye consultation checks whether each eye is developing useful vision and whether the eyes work together. Myopia, squint, focusing difficulty, colour-vision concerns and lazy eye can influence classroom participation. Early assessment is especially important if a child sits close, rubs the eyes, complains of headaches or has a close relative with high myopia.",
                "Prepare a child by describing the appointment as looking at pictures and lights. Bring school notes, previous glasses and details about screen time or outdoor activity. If glasses are prescribed, fit, comfort and consistent use matter. Follow-up is not only about increasing or reducing a number; it lets the doctor see whether vision is developing as expected and whether the plan needs to change."
            ]),
            ("Eye care for diabetes, blood pressure and ageing", [
                "Diabetes and high blood pressure can affect the retina and the small blood vessels that support vision. A person may feel completely normal while changes are developing, which is why screening is part of responsible health care. Share recent blood reports and medicines with the eye doctor. The eye examination cannot replace diabetes or blood-pressure management, but it can identify ocular changes that deserve closer coordination with your physician.",
                "With ageing, glare, poor contrast, slower adaptation in the dark and faded colours may be more important than a simple reduction in the letter chart. Cataract is common, but not every change is cataract. Glaucoma and macular or retinal conditions need different evaluation. Bring a family member if the consultation involves a treatment decision, and ask how findings may affect driving, stairs, reading and independent living."
            ]),
            ("Making a follow-up plan that works", [
                "A prescription or eye drop is only useful when the plan is clear. Before leaving, confirm the dose, timing, duration and whether both eyes are involved. Ask whether you should return after a particular number of days, when the next routine checkup is due and what symptoms should bring the appointment forward. Use a phone reminder for drops and keep a current list in your wallet or health app.",
                "For long-term conditions, compare today’s reports with earlier results instead of judging progress from one good or bad day. Bring the same glasses and medication list to follow-ups. If cost, travel, language or family support makes adherence difficult, tell the clinic team. A practical plan may be safer than a theoretically perfect plan that a patient cannot maintain. Call 93729 47075 if you are unsure whether a change needs review."
            ]),
            ("Book a local consultation with confidence", [
                "Sentra Clinic is located at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 for an appointment, directions or help deciding whether a routine consultation or urgent guidance is more appropriate. You can also use WhatsApp at +91 93729 47075 to share appointment preferences; do not send sensitive medical records until the team tells you the correct channel.",
                "The fee for an examination or procedure depends on what your eyes need, and the clinic can explain the expected investigations and follow-up before treatment. This page is educational, not a diagnosis. If you have sudden vision change or severe symptoms, prioritise timely medical assessment. For routine concerns, bring your questions and allow enough time for a proper evaluation rather than trying to fit it into a rushed errand."
            ]),
        ],
        "cards": [
            ("🩺 Retina screening", "A symptom-led assessment for diabetes, flashes, floaters and retinal concerns.", "/retina-specialist-malad-east/"),
            ("👓 Checkup guide", "Understand what to bring and what a comprehensive examination covers.", "/comprehensive-eye-checkup-malad/"),
            ("👶 Children’s vision", "Support clear vision development with age-appropriate evaluation.", "/children-eye-specialist-malad-mumbai/"),
        ],
        "faqs": [
            ("How do I book an eye doctor in Malad East?", "Call Sentra Clinic on 93729 47075 or WhatsApp +91 93729 47075 to ask about available consultation slots and directions to Rani Sati Road."),
            ("Can an eye doctor check more than my spectacle number?", "Yes. A comprehensive consultation can assess the front of the eye, eye pressure, alignment and retina when indicated, in addition to refraction."),
            ("What should I do if my eye is suddenly painful and red?", "Call promptly for medical guidance. Avoid contact lenses and leftover or steroid eye drops unless prescribed for this episode. Severe pain, injury or vision loss may require urgent care."),
            ("Is a complete eye checkup useful if I can see clearly?", "Yes. Some retinal, pressure-related and early eye-health changes may not cause noticeable blur. The review interval depends on age and health risks."),
            ("Can children be seen for a changing spectacle number?", "Yes. Children can be evaluated for myopia, focusing problems, squint and lazy eye, with follow-up based on age and findings."),
            ("How long does a doctor appointment take?", "A focused consultation can be shorter, while a full assessment commonly takes 60–90 minutes if dilation or additional tests are needed."),
            ("Should I bring old eye reports?", "Yes. Previous prescriptions, scans, surgery notes and medicine lists help the doctor identify changes over time and avoid repeating unnecessary tests."),
        ],
    },
    {
        "file": "72-ophthalmologist-malad-east.html",
        "slug": "ophthalmologist-malad-east",
        "title": "Ophthalmologist in Malad East | Sentra Clinic",
        "description": "Consult an ophthalmologist in Malad East for cornea, refractive, cataract, glaucoma, retina and comprehensive eye care. Find a careful, evidence-led evaluation at Sentra Clinic.",
        "eyebrow": "Ophthalmology consultation · Malad East",
        "h1": "Ophthalmologist in Malad East for Diagnosis Beyond Glasses",
        "hero": "cornea",
        "hero_alt": "Cornea care at Sentra Clinic for ophthalmology patients in Malad East",
        "image_keys": ["cornea", "retina", "rohit", "shraddha"],
        "intro": [
            "An ophthalmologist is a medical eye specialist who can evaluate eye disease as well as vision and glasses. That distinction matters when symptoms are persistent, when a routine prescription is not improving sight, or when a condition may need drops, monitoring or surgery. Sentra Clinic provides ophthalmology consultations in Malad East for people who want a reasoned assessment of the eye—not just a quick number written on a prescription.",
            "The clinic on Rani Sati Road is a practical starting point for cornea, refractive, cataract, glaucoma, retina, diabetic-eye and general eye-health concerns. You do not need to diagnose yourself before calling. Explain the symptom, its timing and any health conditions; the team can help schedule the appropriate appointment. Call 93729 47075 or WhatsApp +91 93729 47075 for current availability."
        ],
        "stats": [("MD", "medical eye care"), ("06+", "care pathways"), ("2", "eyes assessed"), ("1", "documented plan")],
        "sections": [
            ("Ophthalmologist versus optometrist or optical store", [
                "Optometrists and optical professionals play valuable roles in measuring vision and helping with spectacles or contact lenses. An ophthalmologist is a medical doctor trained to examine the eye for disease and manage medical or surgical problems. Depending on the practice, care may involve several professionals working together. Knowing which level of care you need prevents a person with pain, retinal symptoms or cataract from treating the problem as only a lens issue.",
                "A referral is sensible when there is a mismatch between symptoms and the prescription, reduced vision in one eye, recurrent redness, unexplained headaches, diabetes, a family history of glaucoma, previous surgery or a need for a procedure. The goal is not to make every visit complicated. It is to make sure the examination is proportional to the risk and that the patient understands what has been ruled out."
            ]),
            ("Cornea and refractive evaluation", [
                "The cornea is the clear front window of the eye and contributes much of its focusing power. Dryness, infection, scars, keratoconus, irregular shape and contact-lens complications can all affect vision. A person may describe fluctuating blur that gets worse after blinking less or wearing lenses for long hours. An ophthalmologist can examine the surface and shape of the cornea and decide whether lubrication, lens changes, monitoring or a specialist pathway is appropriate.",
                "People considering LASIK or other refractive procedures need more than enthusiasm and a stable glasses number. Corneal thickness and topography, tear-film health, prescription stability, age, pupil considerations and the rest of the eye are relevant. A safe recommendation may be to proceed, to treat the surface first, to monitor or to avoid surgery. A good consultation respects that “not a candidate” is a useful medical answer."
            ]),
            ("Cataract and lens decisions", [
                "Cataract can make a familiar neighbourhood look hazy, reduce contrast on stairs and produce glare while driving at night. Some people notice that colours look less bright or that reading becomes tiring even after a new prescription. The decision about surgery is based on how the change affects your daily life and what the examination shows. There is no single correct date for every patient, and a rushed decision can create unnecessary anxiety.",
                "During a cataract consultation, ask about the health of the cornea, retina and optic nerve, the purpose of the proposed lens, expected spectacle dependence and recovery restrictions. Share diabetes, blood-pressure, heart, blood-thinning and other medicine details. The ophthalmologist should distinguish what surgery can improve from what may remain because of another eye condition. A written plan and a chance to ask questions are part of informed consent."
            ]),
            ("Glaucoma: why pressure is not the whole story", [
                "Glaucoma can damage the optic nerve gradually, often without pain or an obvious change in everyday vision. Eye pressure is important, but risk assessment also considers the optic-nerve appearance, corneal thickness, visual field, family history and other findings. Some people with apparently normal pressure can still have glaucoma, while a higher reading does not automatically mean permanent damage. Repeated, properly interpreted examinations help clarify risk.",
                "If drops are prescribed, ask whether they are for pressure control, inflammation, infection or another reason; different medicines are not interchangeable. Learn the correct technique, the schedule and what side effects need a call. Do not stop long-term glaucoma treatment because vision feels normal. Bring prior fields, scans and pressure records to follow-up because trends and consistency help the ophthalmologist make safer decisions."
            ]),
            ("Retina and diabetic-eye assessment", [
                "The retina converts light into signals for the brain, and changes there can be vision-threatening even when the eye is not painful. Diabetes, high blood pressure, age-related macular problems, high myopia and previous vascular events can increase the need for surveillance. A dilated examination may be recommended, and imaging can document the macula or optic nerve. Ask how often you should return instead of relying on a general annual rule.",
                "Flashes, a sudden increase in floaters, a dark curtain, a missing area of vision or sudden distortion require timely advice. Do not wait to see whether the symptom disappears after sleep. Contact the clinic and describe which eye is affected and exactly when the change began. For people with diabetes, keeping glucose, blood pressure and cholesterol under medical care supports eye health, but does not replace retinal screening."
            ]),
            ("Children and family ophthalmology", [
                "An ophthalmologist can assess children when parents notice a squint, a drifting eye, one eye closing in bright light, difficulty copying from the board or frequent rubbing. Children may not know how to describe double vision or blur. Assessment looks at each eye, how the eyes work together and whether the visual system is developing normally. Earlier treatment is often easier than waiting until a child has adapted to seeing poorly.",
                "Family history can guide attention: high myopia, glaucoma, retinal disease and childhood squint are worth mentioning. Parents should bring school feedback, previous glasses and a timeline of changes. Explain that the visit is not a test the child can fail. Comfort, trust and a follow-up interval that the family can attend are essential to useful paediatric eye care."
            ]),
            ("What to expect from a specialist consultation", [
                "Start with an honest symptom history, including what you have already tried. Bring contact-lens details, old prescriptions, scans, discharge summaries and a complete medicine list. The ophthalmologist may check vision, refraction, pupils, alignment, eye movements, the cornea and lens, pressure and the retina. Dilation is not automatically required for every person, but it may be recommended when a view of the back of the eye is important.",
                "Before the appointment ends, repeat the plan in your own words: working diagnosis, tests completed, treatment, warning signs and follow-up. Ask what improvement should look like and when to call if it does not happen. If surgery is discussed, ask about alternatives, likely benefits, limitations, recovery and total costs. Specialist care is most valuable when the patient can make an informed decision rather than simply agreeing to a technical term."
            ]),
            ("Local access for Malad East patients", [
                "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. It is accessible for families living on the eastern side of Malad and nearby areas, but travel time can change with traffic. Call 93729 47075 to confirm the appointment, ask about the current clinic schedule or request directions. WhatsApp coordination is available at +91 93729 47075.",
                "Keep your reports in one folder and write down your top three questions. If dilation is likely, arrange transport and sunglasses. If you are seeking a second opinion, bring the original reports rather than only a phone photograph. This page provides general information and cannot diagnose an individual. Sudden sight loss, serious injury or severe pain should be treated as urgent and not postponed for a routine booking."
            ]),
            ("Questions that make the appointment more useful", [
                "Patients often remember the main complaint but forget the details that help a doctor find the pattern. Before you leave home, note whether the blur is worse at distance or near, whether blinking changes it, whether one eye is affected, and whether the symptom is linked to a new medicine, illness or long screen session. Write down how often it happens and what you were doing at the time. A short timeline is more useful than trying to remember everything under pressure.",
                "Also note the outcome you hope for. You may want to read comfortably, drive with less glare, understand whether cataract has started, or know whether a child needs glasses. Sharing that goal helps the eye doctor explain realistic options. It is appropriate to ask for a second explanation, an estimate of the follow-up schedule and a copy of important reports. The consultation works best when the patient and doctor make the plan together."
            ]),
        ],
        "cards": [
            ("🫧 Cornea care", "Surface, contact-lens and corneal-shape concerns need careful examination.", "/cornea-keratoconus-treatment-malad/"),
            ("✨ Refractive options", "Learn why eligibility assessment comes before LASIK planning.", "/lasik-eye-surgery-malad-mumbai/"),
            ("🩺 Glaucoma awareness", "Understand why pressure, nerve and field findings are reviewed together.", "/glaucoma-treatment-malad-mumbai/"),
        ],
        "faqs": [
            ("What does an ophthalmologist do?", "An ophthalmologist is a medical eye specialist who evaluates vision and eye disease and can manage medical or surgical eye problems when appropriate."),
            ("When should I see an ophthalmologist instead of only getting glasses?", "Book a medical eye evaluation for persistent blur, pain, recurrent redness, reduced vision in one eye, diabetes, previous surgery, flashes, floaters or a family history of glaucoma."),
            ("Is every blurred-vision problem suitable for LASIK?", "No. Corneal shape, tear film, stable prescription, age and overall eye health determine suitability. Some people need surface treatment, monitoring or another option."),
            ("Does a glaucoma check only measure eye pressure?", "No. A risk assessment may include the optic nerve, visual field, cornea, family history and repeated pressure readings."),
            ("How often should people with diabetes have a retinal check?", "The interval depends on diabetes control and the retinal examination. An ophthalmologist can recommend a personalised schedule; screening should not wait for symptoms."),
            ("Can I bring a child for an ophthalmology consultation?", "Yes. Children can be assessed for squint, myopia, lazy eye, focusing concerns and other vision-development issues."),
            ("Where can I find an ophthalmologist in Malad East?", "Sentra Clinic is on Rani Sati Road at Shah Arcade 2, 002, First Floor, B Wing. Call 93729 47075 before visiting."),
        ],
    },
    {
        "file": "73-best-eye-hospital-malad-east.html",
        "slug": "best-eye-hospital-malad-east",
        "title": "Best Eye Hospital in Malad East | Sentra Clinic",
        "description": "Searching for the best eye hospital in Malad East? Compare what matters: specialist evaluation, safe diagnostics, clear estimates, follow-up and patient-first eye care at Sentra Clinic.",
        "eyebrow": "What good eye care should feel like · Malad East",
        "h1": "Best Eye Hospital in Malad East? Start With Safety, Clarity and Follow-up",
        "hero": "cataract",
        "hero_alt": "Cataract eye care treatment image for patients looking for an eye hospital in Malad East",
        "image_keys": ["cataract", "clear", "rohit", "shraddha"],
        "intro": [
            "The phrase “best eye hospital in Malad East” is easy to search and difficult to define. The most suitable centre is not necessarily the one with the loudest claim, the lowest headline price or the longest list of procedures. For a patient, quality means the problem is evaluated properly, the doctor explains reasonable options, safety is prioritised and follow-up is available when it matters. Sentra Clinic is designed around those practical standards.",
            "Whether you need a routine eye checkup in Malad East, cataract guidance, LASIK eligibility, a diabetic retina review or help with a child’s vision, the first step should be an appropriate assessment. The clinic is located at Shah Arcade 2 on Rani Sati Road. Call 93729 47075 or WhatsApp +91 93729 47075 to discuss an appointment rather than selecting a treatment from a search result alone."
        ],
        "stats": [("01", "honest assessment"), ("04+", "specialty pathways"), ("100%", "case-specific planning"), ("24/7", "symptom awareness")],
        "sections": [
            ("What “best” should mean for an eye patient", [
                "A good eye hospital makes the diagnosis and the patient’s priorities visible. Can the team explain why a test is necessary? Are both eyes assessed when relevant? Are risks and alternatives discussed before a procedure? Do you know who to contact if symptoms change? These questions matter more than a generic promise of perfect vision. Medical decisions should be based on examination findings, not on a keyword, celebrity story or a copied testimonial.",
                "Sentra Clinic’s care model connects evaluation with a documented next step. That may be reassurance and a routine review, a prescription and surface-care advice, a retina screening schedule, a cataract conversation or a referral. Sometimes the safest plan is to wait. A trustworthy centre does not turn every visit into surgery. It helps you understand the trade-offs and choose care that fits your eyes, health and daily life."
            ]),
            ("Doctors, technology and judgement work together", [
                "Modern eye care uses instruments to measure details that cannot be judged by symptoms alone. Yet a machine printout is not a diagnosis. The doctor must interpret it alongside your age, history, medicines, previous procedures and the examination of the eye. An impressive test list does not help if no one explains which result matters. Ask what the test is assessing and whether it changes the treatment decision.",
                "For refractive surgery, corneal mapping and tear-film assessment can be part of eligibility. For cataract, the health of the retina and optic nerve affects expected visual improvement. For glaucoma, pressure is interpreted with nerve and field findings. For diabetes, retinal examination and imaging can document change. The best eye hospital is therefore a combination of qualified clinical judgement, appropriate technology and a willingness to communicate uncertainty honestly."
            ]),
            ("A safe pathway for cataract patients", [
                "Cataract affects people differently. One person may manage comfortably with brighter light while another cannot drive at night or read medication labels. The right time to discuss surgery is when the visual change affects function and the examination supports it. During a consultation, ask what part of your vision is likely to improve, what may remain because of retina or cornea findings and what recovery restrictions apply to your routine.",
                "Lens selection should be a shared decision. Your work, reading habits, night driving, astigmatism, budget and expectations all matter. The total estimate should identify what is included and what could create an additional charge. Never choose an intraocular lens only because an advertisement calls it premium. Ask the ophthalmologist to explain the likely benefits and compromises in your own case, then take time to decide."
            ]),
            ("Refractive surgery without pressure", [
                "LASIK and other refractive procedures can reduce dependence on glasses for suitable patients, but they are elective. A responsible evaluation looks at prescription stability, corneal thickness and shape, tear-film health, eye pressure, retinal health and general expectations. A person who wants to stop wearing glasses for every activity may have a different priority from someone who needs precise night vision for driving. Those priorities should be discussed before consent.",
                "A low price is not a complete comparison. Ask who performs the procedure, what technology is used, what pre-operative tests are included, how many follow-ups are planned, what happens if the result needs enhancement and which symptoms require urgent contact. If you are not suitable, the answer protects your vision. Sentra Clinic can explain the next option, whether that means glasses, contact-lens review, treatment of dryness or a different surgical discussion."
            ]),
            ("Retina and glaucoma: quality means timely attention", [
                "Retinal problems and glaucoma often require a different kind of quality than a one-time prescription. The important things are baseline documentation, the correct interval for review, coordination with diabetes or blood-pressure care and a clear warning-sign plan. Sudden flashes, a burst of floaters, a curtain or abrupt vision loss should be reported promptly. A routine online booking form should not become a reason to delay urgent symptoms.",
                "For glaucoma risk, the eye hospital should explain that pressure is one piece of the puzzle. For diabetic retinopathy, a person should understand why screening matters even when vision is clear. Carry older scans and field reports to appointments. Consistent follow-up makes it easier to recognise change and avoid both false reassurance and unnecessary alarm. Good care is measured across months and years, not only by the experience of one day."
            ]),
            ("Patient experience is part of clinical safety", [
                "Directions, appointment timing and accessible communication may sound like administrative details, but they influence whether a patient returns for care. A family should know where the clinic is, how long the visit may take, whether dilation could blur vision and what records to bring. Older adults may need a companion; children need a calm explanation; working patients may need help choosing a realistic follow-up slot.",
                "At the consultation, write down the name and purpose of each drop. Confirm whether it goes in one eye or both, whether contact lenses must be stopped and when driving is safe. Ask for an estimate that separates consultation, investigations, medicines, surgery, lens and follow-up. If you do not understand the plan, request another explanation. Clear communication is not a luxury; it helps prevent avoidable medication and follow-up errors."
            ]),
            ("Local access in Malad East", [
                "Sentra Clinic is located at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. The location serves people from Malad East and neighbouring areas such as Dindoshi, Kurar and Pathanwadi. Traffic and parking can change, so call 93729 47075 for directions and appointment confirmation. WhatsApp at +91 93729 47075 can be used for basic coordination.",
                "If you are comparing centres, make a written list of questions and take the same list to each consultation. Ask about diagnosis, alternatives, expected improvement, limitations, total cost and follow-up. Do not share passwords or financial information in a chat. This page is general information and does not declare that one centre is right for every person; the best decision depends on a proper examination and informed choice."
            ]),
            ("A practical checklist before you book", [
                "For a routine appointment, bring your current glasses, old prescriptions, reports, medicines and a note of your symptoms. For cataract or LASIK, add details of previous surgery, contact-lens wear, diabetes, blood pressure and any eye drops. For a child, bring school feedback. If you are seeking a second opinion, ask for the original scan files where possible, because a compressed photograph may hide important detail.",
                "Seek urgent guidance instead of a routine appointment for sudden sight loss, severe eye pain, chemical injury, penetrating trauma, a new curtain or a sudden shower of flashes and floaters. Do not put household substances, someone else’s drops or leftover steroids into the eye. Call Sentra Clinic for direction, and use emergency services when the injury or vision change is severe. The safest hospital is the one you reach in time with the right information."
            ]),
        ],
        "cards": [
            ("📋 Compare care", "Questions to ask about tests, treatment, cost, recovery and follow-up.", "/eye-specialist-malad-east/"),
            ("💡 Cataract clarity", "Make a lens and surgery decision based on your daily visual needs.", "/cataract-surgery-malad-mumbai/"),
            ("🚨 Emergency signs", "Know when flashes, floaters, pain or sudden blur cannot wait.", "/emergency-contact/"),
        ],
        "faqs": [
            ("How can I choose the best eye hospital in Malad East?", "Compare the quality of examination, specialist access, explanation of alternatives, safety process, written estimate and follow-up—not only advertising or price."),
            ("Does the best eye hospital need to perform every procedure?", "No. Responsible care includes recognising when another facility or subspecialist is more appropriate and arranging the next step without unnecessary delay."),
            ("Can I visit for a routine eye checkup before deciding on surgery?", "Yes. Start with an examination and consultation. Surgery should only be discussed after the doctor confirms that it is medically suitable and matches your goals."),
            ("What questions should I ask before LASIK?", "Ask about eligibility, corneal and tear-film findings, expected improvement, limitations, risks, follow-ups, enhancement policy and the complete cost."),
            ("What makes cataract care patient-friendly?", "Clear explanation of timing, lens options, expected benefits, limitations, recovery instructions and a written cost and follow-up plan."),
            ("Do emergency eye symptoms need a regular appointment?", "Sudden sight loss, severe pain, injury, chemical exposure, a curtain or sudden flashes and floaters need prompt guidance rather than a delayed routine slot."),
            ("Where is Sentra Clinic in Malad East?", "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 before travelling."),
        ],
    },
    {
        "file": "74-eye-clinic-malad-east.html",
        "slug": "eye-clinic-malad-east",
        "title": "Eye Clinic in Malad East | Sentra Clinic",
        "description": "Sentra Clinic is an eye clinic in Malad East for routine checkups, dry eye, children’s vision, contact-lens advice, cataract, retina and surgical consultations.",
        "eyebrow": "Everyday eye care · Malad East",
        "h1": "Eye Clinic in Malad East for Routine Care and Specialist Support",
        "hero": "family",
        "hero_alt": "Family eye care consultation at a modern eye clinic in Malad East",
        "image_keys": ["family", "vision", "rohit", "shraddha"],
        "intro": [
            "A neighbourhood eye clinic should make it easier to look after your eyes before a small concern becomes a disruption. Sentra Clinic in Malad East offers a convenient starting point for a vision review, dry-eye symptoms, changing glasses, children’s concerns, contact-lens advice, cataract questions and specialist assessment when needed. The aim is simple: understand what brought you in, examine the eyes carefully and give you a plan that fits real life.",
            "The clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road. Residents of Dindoshi, Kurar, Pathanwadi, Thakur Village and nearby parts of Malad East can call 93729 47075 for an appointment or WhatsApp +91 93729 47075 for basic scheduling help. If your symptom is sudden or severe, mention that when you call so you are guided appropriately."
        ],
        "stats": [("01", "neighbourhood clinic"), ("05+", "routine pathways"), ("2", "eyes in every plan"), ("12", "care questions answered")],
        "sections": [
            ("Why choose a local eye clinic?", [
                "Eye care is rarely a single appointment. A child may need a repeat vision check, a contact-lens wearer may need a surface review, and a person with diabetes may need a planned retinal schedule. A clinic near home reduces the practical friction of returning with old reports, bringing a parent or attending a follow-up after drops or treatment. It also lets the doctor compare findings over time instead of treating every visit as a fresh story.",
                "Local convenience should not mean shallow evaluation. Sentra Clinic combines a calm outpatient experience with access to assessment for cataract, cornea, refractive, retina, glaucoma and general eye-health concerns. Not every patient needs every test. The doctor selects what is useful and explains when an additional scan, dilation or referral would change the decision."
            ]),
            ("What a routine eye checkup can cover", [
                "A routine checkup is more than reading letters from a chart. Depending on age and history, it may include visual acuity, refraction, eye alignment, eye movements, the front surface, lens, eye pressure and a view of the retina. A comprehensive eye checkup in Malad East is especially useful when your glasses are old, you have diabetes or high blood pressure, you have a family history of glaucoma or you have not had an eye-health review recently.",
                "Bring your glasses even if you do not like wearing them. The old prescription helps show whether the number is stable. Tell the doctor about screen use, contact lenses, headaches, glare, watering, itching and any medicines. Dilation may be recommended for a better retinal view and can temporarily blur near vision. Ask how to plan transport and work after the examination."
            ]),
            ("Dry eye, allergy and screen comfort", [
                "Burning, gritty sensation, watering and fluctuating blur are common reasons people visit an eye clinic. Long screen sessions, reduced blinking, air conditioning, smoke, dust, contact lenses and an unstable tear film can all contribute. A watery eye can still be dry because irritation triggers reflex watering. A surface examination helps separate dryness from allergy, infection, lid-margin disease or a corneal problem.",
                "Comfort measures such as regular breaks, deliberate blinking, keeping a sensible screen distance and avoiding direct fan or air-conditioner flow can help some people. They are not a substitute for review when pain, light sensitivity, discharge or reduced vision is present. Do not use someone else’s antibiotic or steroid drops. The doctor can explain which lubricant or treatment is suitable, how long to try it and when the result should be reassessed."
            ]),
            ("Children’s eye clinic care", [
                "A child’s eye check should consider how the eyes work together, not only whether the child can read a large letter. Myopia, astigmatism, squint, lazy eye, focusing difficulty and colour-vision concerns can be missed when a child has learned to cope. Parents may notice sitting close to a screen, closing one eye, head tilting, losing place while reading or avoiding outdoor games. School feedback can help the doctor understand the impact.",
                "Make the first appointment positive. Tell children they will look at pictures and lights, and bring their existing glasses. If spectacles are prescribed, comfort and consistent wearing are part of the treatment. Follow the advised review interval because a prescription and the visual system can change during growth. If there is a sudden change, pain, injury or a white pupil, call promptly rather than waiting for a routine slot."
            ]),
            ("Contact lenses, glasses and work vision", [
                "Contact lenses are medical devices, not only a fashion choice. Incorrect cleaning, sleeping in lenses, over-wearing or using water can increase the risk of irritation and infection. A clinic review is important if lenses feel dry, move around, cause redness or make vision fluctuate. Remove the lens when the eye is painful or unusually light-sensitive and seek advice; do not continue wearing it to finish the day.",
                "For glasses users, an accurate prescription is only one part of comfortable vision. Frame fit, working distance, lighting, dry eye and the need for separate distance or near correction may all matter. People who work on computers can discuss task-specific habits and whether a medical examination is needed. Frequent headaches should not automatically be blamed on “eye number”; the cause needs to be assessed."
            ]),
            ("Cataract, retina and glaucoma support", [
                "An eye clinic can be the first place to discuss a cataract when reading, night travel or recognising faces becomes difficult. The doctor examines the lens and the rest of the eye before explaining whether stronger glasses, observation or surgery makes sense. If the retina or optic nerve has another condition, expectations from cataract surgery may need to be adjusted. A complete plan is more useful than a rushed yes or no.",
                "People with diabetes should arrange retinal screening even if sight feels normal. People at risk of glaucoma should keep recommended follow-up because early disease may be quiet. Flashes, a new shower of floaters, a curtain-like shadow or sudden blur are different: call promptly. Keep old reports and bring them to each visit; comparison is particularly valuable for long-term eye conditions."
            ]),
            ("A comfortable visit for seniors and caregivers", [
                "Older adults may have several medicines, hearing difficulty or reduced mobility. Bring a family member when possible, write down the reason for the visit and carry the full medicine list. Tell the clinic if the patient needs help with stairs, forms or transport after dilation. Ask how findings affect practical activities: reading labels, using the kitchen, walking outside, taking medicines and recognising obstacles in low light.",
                "Caregivers should not assume that a patient’s statement “I can see” means both eyes are functioning equally. Some people adapt by relying on the stronger eye. A checkup can identify differences that matter for safety and independence. Use large-print instructions or phone reminders for drops, and ask for a demonstration if hand strength or vision makes the bottle difficult to manage."
            ]),
            ("Visit details and a simple booking plan", [
                "Sentra Clinic is located at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 to confirm available slots, directions and whether you should allow extra time for dilation or testing. WhatsApp at +91 93729 47075 is available for basic coordination. Appointment times and clinical advice should be confirmed with the team before you travel.",
                "For a productive visit, bring glasses, contact-lens information, old reports, medicine details and your top questions. Note which eye is affected and whether the change is sudden. Fees vary by the consultation and investigations required; ask what is included before agreeing to treatment. This educational page does not replace a medical examination. If there is severe pain, trauma, chemical exposure or sudden loss of vision, seek urgent guidance."
            ]),
        ],
        "cards": [
            ("🔎 Eye checkup", "Plan a complete examination instead of guessing from a glasses number.", "/comprehensive-eye-checkup-malad/"),
            ("💧 Dry eye care", "Get help when burning, watering or screen discomfort continues.", "/dry-eye-treatment-malad/"),
            ("👓 Contact lenses", "Review comfort, hygiene and safe wearing habits.", "/contact-lens-consultation-malad/"),
        ],
        "faqs": [
            ("What services are available at an eye clinic in Malad East?", "Sentra Clinic provides routine eye evaluations and guidance for dry eye, changing prescriptions, children’s vision, contact lenses, cataract, cornea, glaucoma, retina and refractive concerns."),
            ("How do I prepare for an eye checkup?", "Bring current glasses, old reports, medicines, contact-lens details and a note of your symptoms. Allow extra time if dilation or additional testing is recommended."),
            ("Can screen use cause dry eyes?", "Long screen sessions can reduce blinking and contribute to discomfort, but persistent symptoms need an examination to rule out other surface or eye conditions."),
            ("Should I stop wearing contact lenses before an appointment?", "Ask when booking because the timing depends on the purpose of the visit. Remove a lens promptly if the eye is painful, red or light-sensitive."),
            ("Do older adults need a regular eye clinic visit?", "Yes. Regular review can identify cataract, glaucoma, retinal and prescription changes and help maintain safe daily activities."),
            ("Can I bring my child for a first eye test?", "Yes. Children can be assessed for myopia, squint, lazy eye and focusing concerns in an age-appropriate way."),
            ("Where is the clinic located?", "Sentra Clinic is at Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call 93729 47075 for directions."),
        ],
    },
]


def extract_assets() -> tuple[str, str]:
    source = SOURCE.read_text(encoding="utf-8")
    style_match = re.search(r"<style>(.*?)</style>", source, flags=re.S)
    script_matches = re.findall(r"<script>\s*\(function\(\)\{.*?</script>", source, flags=re.S)
    if not style_match or not script_matches:
        raise RuntimeError("Could not extract the existing Sentra style and reveal script")
    extra = """
  .sc-page-shell{max-width:1180px;margin:0 auto;padding:0 22px;}
  body{margin:0;background:#fffdf8;}
  .sc-footer-note{font-size:13px;color:#66717d;border-top:1px solid var(--sc-line);padding:22px 0 34px;margin-top:24px;}
  .sc-hero .sc-img{width:100%;height:360px;object-fit:cover;border-radius:16px;box-shadow:0 18px 36px rgba(0,0,0,.22);}
  .sc-card img{width:100%;height:185px;object-fit:cover;border-radius:12px;margin-bottom:14px;}
  .sc-image-caption{font-size:13px;color:var(--sc-muted);margin-top:-8px;}
  @media(max-width:820px){.sc-page-shell{padding:0 14px;}.sc-hero .sc-img{height:280px;}}
"""
    return style_match.group(1) + extra, script_matches[-1]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def paragraph_html(texts: list[str]) -> str:
    return "\n".join(f"  <p>{text}</p>" for text in texts)


def page_html(page: dict, style: str, script: str) -> str:
    extra_sections = {
        "71-eye-doctor-malad-east.html": [
            ("Preparing for your eye doctor visit", [
                "If you have used eye drops recently, write down their names and how often you used them. Mention allergies, pregnancy or breastfeeding when relevant, and tell the doctor about medicines that affect blood pressure or blood thinning. Contact-lens users should share the type and wearing schedule. These details can change how the cornea, tear film and eye pressure are interpreted.",
                "After the appointment, keep the plan visible at home. Mark the day for a review, set a reminder for drops and ask a family member to repeat the instructions if the patient is older. If the symptom gets worse, the treatment causes a worrying reaction or the diagnosis is unclear, call rather than changing the plan yourself. Good follow-up turns one consultation into ongoing eye health."
            ]),
        ],
        "73-best-eye-hospital-malad-east.html": [
            ("A fair comparison for families", [
                "When comparing an eye hospital, write down the same questions for every centre: who will examine you, what tests are needed, what alternatives exist, what is included in the estimate and how follow-up is handled. Ask for medical terms to be explained in everyday language. A family should never feel that asking about risk, cost or a second opinion is disrespectful.",
                "Also compare access. A centre that is practical to reach may make it easier to attend post-operative reviews or bring an older parent for repeat testing. Keep copies of reports and consent documents. The strongest choice is the one that combines appropriate expertise with a plan you understand and can follow."
            ]),
        ],
        "74-eye-clinic-malad-east.html": [
            ("A useful routine for healthier eyes", [
                "Between visits, protect comfort by taking regular screen breaks, blinking fully, wearing prescribed glasses and avoiding unapproved drops. Sunglasses and a hat can reduce bright-light discomfort, while outdoor time is helpful for children’s general visual habits. These everyday measures support eye health but cannot diagnose glaucoma, cataract or retinal disease, so keep the review recommended for your age and medical history.",
                "Make the next appointment easier by saving your current prescription, recording when symptoms occurred and bringing the same medicines and glasses. Tell the clinic if you could not follow an instruction because of cost, work or difficulty using a bottle. The team can only improve a plan when they know what happened at home. A simple folder or phone note with the date, eye affected and treatment response can prevent confusion when several family members share care."
            ]),
        ],
    }.get(page["file"], [])
    sections = []
    for heading, paragraphs in page["sections"] + extra_sections:
        sections.append(f"  <h2>{heading}</h2>\n{paragraph_html(paragraphs)}")
    section_html = "\n\n".join(sections)

    stat_html = "\n".join(
        f'      <div class="sc-stat"><span class="num">{esc(number)}</span><span>{esc(label)}</span></div>'
        for number, label in page["stats"]
    )
    card_html = "\n".join(
        f'      <a class="sc-card" href="{esc(href)}"><span class="sc-card-icon">{esc(title[:2])}</span><h3>{esc(title[2:].strip())}</h3><p>{copy}</p></a>'
        for title, copy, href in page["cards"]
    )
    faq_html = "\n".join(
        f"    <details><summary>{question}</summary><p>{answer}</p></details>"
        for question, answer in page["faqs"]
    )

    images = page["image_keys"]
    image_alts = [
        page["hero_alt"],
        f"Eye examination and consultation at Sentra Clinic, {page['slug'].replace('-', ' ')}",
        "Eye specialist consultation at Sentra Clinic, Malad East Mumbai",
        "Sentra Clinic eye care team serving families in Malad East",
    ]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalClinic",
                "@id": f"https://sentraclinic.com/{page['slug']}/#clinic",
                "name": "Sentra Clinic",
                "url": f"https://sentraclinic.com/{page['slug']}/",
                "telephone": "+919372947075",
                "image": IMAGES[page["hero"]],
                "description": page["description"],
                "medicalSpecialty": ["Ophthalmology", "Cornea and Refractive Surgery", "Vitreoretinal Surgery"],
                "areaServed": [{"@type": "Place", "name": name} for name in ["Malad East, Mumbai", "Dindoshi, Mumbai", "Kurar, Mumbai", "Pathanwadi, Mumbai"]],
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road",
                    "addressLocality": "Malad East",
                    "addressRegion": "Mumbai, Maharashtra",
                    "postalCode": "400097",
                    "addressCountry": "IN",
                },
                "geo": {"@type": "GeoCoordinates", "latitude": "19.1874", "longitude": "72.8693"},
                "hasMap": "https://maps.google.com/?q=Sentra+Clinic+Malad+East+Mumbai",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sentraclinic.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Malad East Eye Care", "item": "https://sentraclinic.com/eye-specialist-malad-east/"},
                    {"@type": "ListItem", "position": 3, "name": page["title"].split(" | ")[0], "item": f"https://sentraclinic.com/{page['slug']}/"},
                ],
            },
        ],
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in page["faqs"]
        ],
    }

    related = [
        ("/eye-hospital-malad-east/", "🏥 Eye Hospital in Malad East"),
        ("/eye-doctor-malad-east/", "🩺 Eye Doctor in Malad East"),
        ("/ophthalmologist-malad-east/", "👁 Ophthalmologist in Malad East"),
        ("/best-eye-hospital-malad-east/", "⭐ Best Eye Hospital in Malad East"),
        ("/eye-clinic-malad-east/", "📍 Eye Clinic in Malad East"),
        ("/comprehensive-eye-checkup-malad/", "🔎 Comprehensive Eye Checkup"),
        ("/cataract-surgery-malad-mumbai/", "💎 Cataract Surgery"),
        ("/retina-specialist-malad-east/", "🔬 Retina Specialist"),
    ]
    related_html = "\n".join(f'      <a href="{href}">{label}</a>' for href, label in related if href.strip("/") != page["slug"])

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page["title"])}</title>
  <meta name="description" content="{esc(page["description"])}">
  <link rel="canonical" href="https://sentraclinic.com/{page["slug"]}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(page["title"])}">
  <meta property="og:description" content="{esc(page["description"])}">
  <meta property="og:url" content="https://sentraclinic.com/{page["slug"]}/">
  <meta property="og:image" content="{IMAGES[page["hero"]]}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%230a2540'/%3E%3Cpath d='M12 32s8-14 20-14 20 14 20 14-8 14-20 14S12 32 12 32Z' fill='none' stroke='%23f6e8c9' stroke-width='4'/%3E%3Ccircle cx='32' cy='32' r='6' fill='%23c9932c'/%3E%3C/svg%3E">
  <style>{style}</style>
</head>
<body>
<main class="sc-page-shell">
<div class="sc-wrap">
  <p class="sc-breadcrumb"><a href="/">Home</a> / <a href="/eye-specialist-malad-east/">Malad East Eye Care</a> / {esc(page["title"].split(" | ")[0])}</p>
  <div class="sc-hero">
    <div>
      <span class="sc-eyebrow">{esc(page["eyebrow"])}</span>
      <h1>{esc(page["h1"])}</h1>
      <p>{page["intro"][0]}</p>
      <div class="sc-btn-row" style="margin-top:22px;">
        <a href="tel:9372947075" class="sc-btn">📞 Call 93729 47075</a>
        <a href="https://wa.me/919372947075" class="sc-btn-outline">💬 WhatsApp for an appointment</a>
      </div>
    </div>
    <div>
      <img class="sc-img" src="{IMAGES[page["hero"]]}" alt="{esc(image_alts[0])}" loading="eager">
    </div>
  </div>
  <p>{page["intro"][1]}</p>
  <div class="sc-stats">
{stat_html}
  </div>
  <div class="sc-note">📍 <strong>Visit Sentra Clinic:</strong> Shah Arcade 2, 002, First Floor, B Wing, Rani Sati Road, Malad East, Mumbai 400097. Call <a href="tel:9372947075">93729 47075</a> before travelling for appointment and direction confirmation.</div>
  <div class="sc-grid-2">
    <div>
      <h2>A thoughtful local starting point</h2>
      <p>Eye problems can be simple, ongoing or urgent. A careful first assessment helps separate them and avoids guessing with random drops or stronger glasses. Sentra Clinic serves Malad East families with a doctor-led plan and clear next steps.</p>
      <p>Bring your records, list your symptoms and ask questions. If the examination suggests a different level of care, the team can explain the reason and the next step instead of delaying it.</p>
    </div>
    <div>
      <img class="sc-img" src="{IMAGES[images[1]]}" alt="{esc(image_alts[1])}" loading="lazy">
      <p class="sc-image-caption">Representative eye-care image; the doctor selects tests according to each patient’s history and findings.</p>
    </div>
  </div>

{section_html}

  <div class="sc-grid-3">
{card_html}
  </div>
  <div class="sc-grid-2">
    <div><img class="sc-img" src="{IMAGES[images[2]]}" alt="{esc(image_alts[2])}" loading="lazy"></div>
    <div>
      <h2>Bring your questions</h2>
      <p>A good consultation is a conversation, not only a test result. Ask what has been found, what remains uncertain, what treatment is optional, how soon to return and which symptoms should prompt an earlier call.</p>
      <p>If surgery is discussed, ask for expected benefits, limitations, recovery, alternatives and a complete written estimate. Informed decisions are safer decisions.</p>
    </div>
  </div>
  <div class="sc-cta">
    <p>Need an eye consultation in Malad East?</p>
    <div class="sc-btn-row">
      <a href="tel:9372947075" class="sc-btn">Call 93729 47075</a>
      <a href="https://wa.me/919372947075" class="sc-btn-outline">WhatsApp the clinic</a>
    </div>
  </div>
  <div class="sc-grid-2">
    <div>
      <h2>Care that continues after the visit</h2>
      <p>Keep your prescription, investigation reports and medicine list together. Follow the timing written by the doctor and return when advised. If a symptom changes suddenly, do not wait for a routine follow-up.</p>
      <p>This page is general educational information, not a diagnosis or a substitute for emergency care. Clinical recommendations, timings and fees are confirmed after an in-person assessment.</p>
    </div>
    <div><img class="sc-img" src="{IMAGES[images[3]]}" alt="{esc(image_alts[3])}" loading="lazy"></div>
  </div>
  <h2>Frequently asked questions</h2>
  <div class="sc-faq">
{faq_html}
  </div>
  <div class="sc-related">
    <h3 style="margin-top:0;">More Malad East eye-care pages</h3>
    <div class="sc-related-grid">
{related_html}
    </div>
  </div>
  <div class="sc-footer-note">Medical information on this page is for education and does not replace a clinical examination. Contact the clinic for current timings, fees and appointment availability. Last reviewed: August 2026.</div>
</div>
</main>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>
{script}
</body>
</html>
"""


def visible_word_count(text: str) -> int:
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    return len(re.findall(r"\b[\w’'-]+\b", html.unescape(body)))


def main() -> None:
    style, script = extract_assets()
    counts = []
    for page in PAGES:
        output = page_html(page, style, script)
        words = visible_word_count(output)
        if words < 2000:
            raise RuntimeError(f"{page['file']} has only {words} visible words; add unique content before publishing")
        (ROOT / page["file"]).write_text(output, encoding="utf-8")
        counts.append(f"{page['file']}: {words} words")
    print("\n".join(counts))


if __name__ == "__main__":
    main()