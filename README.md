# Sentra Clinic — WordPress/Elementor Pages (All 3 Months)

Ye folder me 10 HTML files hain — client ke MS Word doc (Sentra Month 1 Content Pack) ka **exact wahi content**, sirf HTML tags me convert kiya gaya hai. Kahin se bhi extra content nahi add kiya gaya — sirf jo Word doc me likha tha wahi, structured HTML (h1/h2/h3/p/ul/table) me.

## Files (order wahi hai jo doc me diya gaya hai)

| # | File | WordPress URL/Slug |
|---|------|---------------------|
| 1 | `1-homepage.html` | `/` (homepage) |
| 2 | `2-lasik-eye-surgery-malad-mumbai.html` | `/lasik-eye-surgery-malad-mumbai` |
| 3 | `3-contoura-vision-malad-mumbai.html` | `/contoura-vision-malad-mumbai` |
| 4 | `4-icl-surgery-malad-mumbai.html` | `/icl-surgery-malad-mumbai` |
| 5 | `5-retina-specialist-malad-mumbai.html` | `/retina-specialist-malad-mumbai` |
| 6 | `6-diabetic-retinopathy-treatment-malad.html` | `/diabetic-retinopathy-treatment-malad` |
| 7 | `7-cataract-surgery-malad-mumbai.html` | `/cataract-surgery-malad-mumbai` |
| 8 | `8-lasik-surgery-cost-mumbai.html` | `/lasik-surgery-cost-mumbai` |
| 9 | `9-cataract-surgery-cost-mumbai.html` | `/cataract-surgery-cost-mumbai` |
| 10 | `10-dr-rohit-modi.html` | `/dr-rohit-modi` |

## WordPress + Elementor me kaise paste karein (step by step)

1. WordPress admin → **Pages → Add New**. Page ka title dalein (jaise "LASIK Eye Surgery in Malad, Mumbai") aur URL/slug upar table se set karein.
2. Since aapka **header aur footer already hai** — Elementor page template me "Elementor Canvas" ya "Default" (jo bhi aapke theme me header/footer already inherit karta ho) select karein. Naya header/footer is HTML me nahi hai — sirf body/content area ka content hai.
3. "Edit with Elementor" kholein.
4. Ek **HTML widget** (Elementor ke widget panel me search karein "HTML") page par drag karein.
5. Us HTML widget ke andar, respective `.html` file ka **poora content copy-paste** kar dein.
6. Isi tarah baaki 9 pages ke liye bhi alag-alag page banayein, respective HTML file paste karein.
7. Har page par **Title Tag aur Meta Description** ko HTML widget me paste NA karein — inhe apne SEO plugin (Yoast / RankMath / All in One SEO) ke SEO settings box me set karein. Har file ke top comment me title tag + meta description likha hai, wahan se copy kar lein.

## Publish karne se pehle — ye zaroor karein (doc ke "Non-Negotiables" section se)

1. **Har `[bracket]` ko fill karein** — jaise `[phone]`, `[number]`, `[Full address with landmark]`, `[Timings]`, `[X years]`, `[X,000+]` procedures, doctor ki degrees, etc. Maine inhe waise hi rakha hai jaise doc me tha kyunki aapne kaha ki doc se bahar kuch bhi nahi uthana — asli phone number/address/doctor credentials sirf aapke paas hain.
   - Sabse aasan tareeka: har file ko text editor me kholiye aur "Find & Replace" se `[phone]` ko apne real number se, `[number]` ko WhatsApp number se replace kariye.
2. **Prices** (Article 8 - LASIK Cost, Article 9 - Cataract Cost): doc ne clearly bola hai ki ye sirf indicative Mumbai market ranges hain, drafting ke liye. Clinic ke actual confirmed packages se replace karna zaroori hai — galat price publish karna trust todta hai aur advertising rules ke against hai.
3. **Dr. Modi se medical review lena zaroori hai** — har page live karne se pehle unhe padhna/approve karna chahiye, kyunki wo hi "author of record" hain (Google E-E-A-T ke liye).
4. Har page par **2-4 images** add karein, keyword-relevant alt text aur compressed filenames ke saath (jaise `lasik-surgery-malad-sentra.webp`) — ye HTML files me images nahi daali gayi hain kyunki doc me actual images provide nahi thi.
5. Har file me neeche **JSON-LD schema script** already diya gaya hai (FAQPage har page par, MedicalClinic+Physician homepage par, Physician doctor page par) — ye bhi HTML widget ke andar hi paste ho jayega, alag se kuch nahi karna. Bas [bracket] wale fields (phone, address) fill kar dein.
6. Internal links (jaise "LASIK page →", "About Dr. Modi →") already `<a href="...">` tags me correct slugs ke saath daal diye gaye hain — agar aapke actual permalink structure alag hai to sirf href check kar lein.

## Kya nahi kiya gaya (jaisa aapne bola)

- Doc se bahar koi naya content, extra paragraph, ya alag wording nahi likha gaya — jo bhi Word doc me tha, wahi content hai.
- Koi header/footer HTML nahi banaya — sirf page-body content hai, jo aapke existing Elementor header/footer ke beech me aayega.
- Sirf saade HTML tags use kiye hain (h1/h2/h3/p/ul/table/div) jo kisi bhi WordPress theme ke default style ke saath kaam karenge.

---

# Month 2 Content Pack (Files 12–24)

Ye 13 naye pages **Sentra_Month2_Content_Pack** doc se banaye gaye hain — 6 hyperlocal area pages, 4 condition/service pages, aur 3 blogs. In sabme wahi "luxury" design system use kiya gaya hai jo pages 2–9 me hai (`.sc-*` classes, floating icons, scroll-reveal animation, FAQ accordion) — koi shared CSS/JS file nahi, har page apne aap me self-contained hai (paste karte waqt kuch alag se add nahi karna).

| # | File | WordPress URL/Slug | Type |
|---|------|---------------------|------|
| 12 | `12-comprehensive-eye-checkup-malad.html` | `/comprehensive-eye-checkup-malad` | Service |
| 13 | `13-eye-specialist-goregaon.html` | `/eye-specialist-goregaon` | Hyperlocal |
| 14 | `14-eye-specialist-kandivali.html` | `/eye-specialist-kandivali` | Hyperlocal |
| 15 | `15-eye-specialist-borivali.html` | `/eye-specialist-borivali` | Hyperlocal |
| 16 | `16-eye-clinic-malad-west.html` | `/eye-clinic-malad-west` | Hyperlocal |
| 17 | `17-eye-clinic-near-kurar-dindoshi.html` | `/eye-clinic-near-kurar-dindoshi` | Hyperlocal |
| 18 | `18-glaucoma-treatment-malad-mumbai.html` | `/glaucoma-treatment-malad-mumbai` | Condition |
| 19 | `19-squint-pediatric-eye-care-malad.html` | `/squint-pediatric-eye-care-malad` | Condition |
| 20 | `20-cornea-keratoconus-treatment-malad.html` | `/cornea-keratoconus-treatment-malad` | Condition |
| 21 | `21-retinal-detachment-treatment-malad.html` | `/retinal-detachment-treatment-malad` | Condition (Emergency) |
| 22 | `22-blog-lasik-eligibility-checklist.html` | `/blog/lasik-eligibility-checklist` | Blog |
| 23 | `23-blog-diabetes-and-your-eyes.html` | `/blog/diabetes-and-your-eyes` | Blog |
| 24 | `24-blog-flashes-floaters-warning-signs.html` | `/blog/flashes-floaters-warning-signs` | Blog |
| 25 | `25-emergency-contact.html` | `/emergency-contact` | Emergency Contact |

Paste karne ka process bilkul same hai jo upar Month 1 me diya gaya hai (Elementor → HTML widget → poora content copy-paste, Title Tag/Meta Description ko SEO plugin me set karein).

---

# Month 3 Content Pack (Files 26–35)

Ye 10 naye pages **Sentra_Month3_Content_Pack** doc se banaye gaye hain — 6 blogs aur 4 service/condition pages. Same `.sc-*` luxury design system, fully self-contained.

| # | File | WordPress URL/Slug | Type |
|---|------|---------------------|------|
| 26 | `26-blog-is-lasik-safe-evidence.html` | `/blog/is-lasik-safe-evidence` | Blog |
| 27 | `27-blog-contoura-vs-lasik.html` | `/blog/contoura-vs-lasik` | Blog |
| 28 | `28-blog-smile-vs-lasik-vs-contoura.html` | `/blog/smile-vs-lasik-vs-contoura` | Blog |
| 29 | `29-blog-cataract-recovery-guide.html` | `/blog/cataract-recovery-guide` | Blog |
| 30 | `30-blog-sudden-vision-loss-emergency.html` | `/blog/sudden-vision-loss-emergency` | Blog (Emergency — red hero + floating call btn) |
| 31 | `31-blog-cataract-vs-glaucoma.html` | `/blog/cataract-vs-glaucoma` | Blog (Safed motia vs kala motia) |
| 32 | `32-dry-eye-treatment-malad.html` | `/dry-eye-treatment-malad` | Service — Dry Eye |
| 33 | `33-oculoplasty-malad-mumbai.html` | `/oculoplasty-malad-mumbai` | Service — Oculoplasty |
| 34 | `34-eye-flu-conjunctivitis-treatment-malad.html` | `/eye-flu-conjunctivitis-treatment-malad` | Service — Eye Flu (monsoon angle, steroid-warning danger box) |
| 35 | `35-blog-reduce-eye-number-naturally-truth.html` | `/blog/reduce-eye-number-naturally-truth` | Blog (myth-buster + LASIK funnel, bilingual FAQs) |

### Month 3 — Notes before publishing

1. **Schema types:** Blogs (26–31, 35) have `Article` (author: Dr. Rohit Modi) + `FAQPage` JSON-LD. Service/condition pages (32–34) have `MedicalCondition` or `MedicalProcedure` + `FAQPage`. All already embedded in the HTML — pasting into Elementor widget is sufficient.
2. **`[TEAM: ...]` placeholders:** File 33 (Oculoplasty) has one `[TEAM: ...]` note about insurance applicability — fill in your TPA/cashless details.
3. **File 30** (Sudden Vision Loss Emergency) has a red hero and always-visible floating call button — same treatment as the Retinal Detachment emergency page (#21).
4. **File 34** (Eye Flu) has a red-bordered `sc-danger` box listing the most harmful self-medication practices (especially the "no steroid drops without diagnosis" warning) — review with Dr. Modi before publishing, as it is strong clinical advice.
5. Phone number (93729 47075) and WhatsApp link (https://wa.me/919372947075) are already filled in throughout all 10 pages.

## Publish karne se pehle — ye zaroor karein

1. **`[TEAM: ...]` notes fill karein** — checkup fees, LASIK screening fee, statistics (Article — Diabetes & Your Eyes), parking info, aur exact route/landmark details har hyperlocal page par. Ye jagah-jagah chhode gaye hain kyunki asli numbers sirf clinic ke paas hain.
2. **Phone number (93729 47075) aur address already fill kiye gaye hain** — ye already site par existing verified contact details hain, doc ke generic `[phone]`/`[number]` placeholders ki jagah use kiye gaye hain. Confirm kar lein ki ye sahi hain.
3. **Dr. Modi se medical review lena zaroori hai** — especially Article 21 (Retinal Detachment) jaisa emergency-content page, jahan clinical accuracy critical hai.
4. Har page par **2-4 real images** add karein (abhi placeholder clinic photo use ho raha hai) — keyword-relevant alt text ke saath.
5. **Article 21 (Retinal Detachment)** me ek floating "Emergency — Call Now" button hai jo screen par hamesha visible rehta hai (page-local CSS, `.sc-float-call`) — isko intentionally rakha gaya hai kyunki ye ek time-critical emergency page hai.
6. **Links IN** (purane Month 1 pages se in naye pages ki taraf back-links add karna, jaisa doc me "Links IN" section me bola gaya hai) is pack me include nahi kiya gaya — ye 11 existing pages ko edit karega, jo ek alag, deliberate step hona chahiye. Naye pages ke andar "Links OUT" (related pages ki taraf) already daal diye gaye hain.
7. Doc me diye gaye kuch FAQ answers/statistics bilingual ya approximate the — publish se pehle Dr. Modi se factually verify karayein, especially numbers jaise "1 in 3 diabetics" (marked with a `[TEAM: verify]` note).

## Emergency Contact Page (File 25)

`25-emergency-contact.html` client ke diye gaye emergency contact list se banaya gaya hai — same `.sc-*` luxury design system, red/urgent color accent ke saath (kyunki ye emergency-purpose page hai):

- **Emergency contacts** (strictly emergencies ke liye): Ms. Anjali (Counselor) — 9769494046, Dr. Rohit Modi — 7718953978, Dr. Shraddha Sureka — 9820184038.
- **Appointments** (routine queries ke liye): 93729 47075 aur 022 4605 7489.
- Dr. Rohit Modi aur Dr. Shraddha Sureka ki existing site photos use ki gayi hain; Ms. Anjali ke liye koi photo site par available nahi thi, isliye icon use kiya gaya hai — **[TEAM: agar Ms. Anjali ki photo available ho, to `sc-avatar` img tag add kar dein unke card me, jaisa doctors ke cards me hai]**.
- Ek permanently visible floating "🚨 Eye Emergency — Call Now" button hai (Ms. Anjali ke number par call karta hai) — jaisa Article 21 (Retinal Detachment) me hai.
- FAQ me ek `[TEAM: ...]` note hai — emergency lines ki exact availability (24x7 ya specific hours) confirm karke fill karein.
