<div align="center">

# 🏛️ The Regulatory Prompt Library
### Programmatically Validated Intelligence for MedTech, Pharma & AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/rlwadh)
[![Sector](https://img.shields.io/badge/Sector-MedTech%20%7C%20Pharma%20%7C%20AI-blue)](https://adhocon.com)
[![Validation](https://img.shields.io/badge/Validation-High-red)](https://adhocon.com)

<p align="center">
  <b>10,000+ Prompts. Zero Hallucinations. 100% Open Source.</b><br>
  Stop guessing. Start engineering your Regulatory Compliance.
</p>

[Report Bug](https://github.com/rlwadh/regulatory-prompt-library/issues) · [Request Feature](https://github.com/rlwadh/regulatory-prompt-library/issues) · [Visit ADHOCON](https://adhocon.com)

</div>

---

## ⚡ The Mission

> **"Prompt Engineering shouldn't cost $10,000. It is a commodity. Regulatory Intelligence is the asset."** — Rudolf Wagner, CEO ADHOCON

We see consultants charging thousands for "AI Workshops" that teach basic prompting. We believe this knowledge belongs to the community. 

This repository provides a massive database of **context-aware, regulatorily validated prompts** designed for:
* **MedTech** (MDR, FDA, ISO 13485)
* **IVD** (IVDR, 21 CFR 809)
* **Pharma** (GMP, ICH, FDA)
* **SaMD & AI** (IEC 62304, FDA PCCP, EU AI Act)

---

## 🛡️ "Compliance by Design" (How it works)

Unlike random prompt lists found on the internet, this library is generated via a logical Python Matrix (`main.py`). We use **Conditional Logic** to ensure regulatory safety:

| Sector | If you select... | The Prompt enforces... |
| :--- | :--- | :--- |
| **MedTech** | Risk Management | **ISO 14971:2019** (Not ICH Q9) |
| **Pharma** | Risk Management | **ICH Q9** (Not ISO 14971) |
| **AI / SaMD** | Change Control | **FDA PCCP & IEC 62304** |
| **IVD** | Performance Eval | **EU IVDR 2017/746 & MDCG** |

❌ **No Cross-Contamination:** The script ensures a Pharma prompt never accidentally cites a MedTech standard.

---

## 📂 Repository Contents

* `adhocon_regulatory_prompts.csv` 💾  
  **The Database.** A CSV file containing thousands of rows. 
  * **Columns:** Sector, Region, Role, Task, Artifact, The_Prompt.
  * *Usage:* Import this into your own tools, Excel, or internal LLM wrappers.

* `main.py` 🐍  
  **The Generator.** The Python script used to generate the CSV. We published the source code to prove the validation logic.

---

## 🚀 How to Use

### Option A: The "Copy-Paste" Method (Simple)
1. **Download** the `adhocon_regulatory_prompts.csv` file above.
2. Open it in **Excel** or Google Sheets.
3. **Filter** column A ("Sector") for your industry (e.g., `MedTech_IVD`).
4. **Filter** column D ("Task") for what you need (e.g., `Gap Analysis`).
5. Copy the content of the **"Prompt"** column.
6. Paste it into **ChatGPT Enterprise**, **Microsoft Copilot**, or **Claude**.

### Option B: The "Power User" Method (Python)
Clone the repo and generate your own custom batches:

```bash
git clone [https://github.com/rlwadh/regulatory-prompt-library.git](https://github.com/rlwadh/regulatory-prompt-library.git)
cd regulatory-prompt-library
python main.py

🤖 Coverage & Standards
We cover the most critical global standards. The generator includes logic for:

🏥 MedTech (General)
EU: MDR 2017/745, ISO 13485:2016, MEDDEV 2.7/1

US: FDA 21 CFR Part 820 (QSR), 21 CFR Part 11

Global: IMDRF Essential Principles, MDSAP

🧬 IVD (In Vitro Diagnostics)
EU: IVDR 2017/746, MDCG Guidelines

US: 21 CFR Part 809, CLIA

🧠 SaMD & AI (Artificial Intelligence)
Frameworks: FDA AI/ML Action Plan, PCCP (Predetermined Change Control Plan)

Standards: IEC 62304, IEC 82304, EU AI Act (Safety Articles)

💊 Pharma
EU: EudraLex Vol 4 (GMP), Annex 11

US: 21 CFR 210/211 (cGMP)

Global: ICH Q7, Q9, Q10

⚠️ Disclaimer
Human-in-the-Loop Required. While these prompts are structurally validated, the output of any LLM (AI) must be reviewed by a qualified professional.

These prompts do not constitute legal advice.

Always verify outputs against the latest official regulatory texts (e.g., EUR-Lex, FDA.gov).

🔗 About ADHOCON
We don't just write prompts. We build Autonomous Regulatory Systems.

ADHOCON specializes in deploying "Agentic QMS Frameworks" directly into your Azure/AWS cloud environment. No new servers. No data transfer. Just validated automation.

Website: adhocon.com

Author: Rudolf Wagner (ISO 17024 Certified Expert)

<div align="center">


<i>If this library saves you time, give it a ⭐ Star!</i> </div>


-----

### Teil 2: Step-by-Step Anleitung (Upload)

Hier ist der Prozess, um das Repo genau so live zu schalten.

#### 1\. Vorbereitung (Auf deinem PC)

1.  Geh in deinen Ordner `adhocon-prompts`.
2.  Stelle sicher, dass dort die **neueste** `main.py` (mit dem AI/IMDRF Update von vorhin) liegt.
3.  Lösche die alte CSV (falls vorhanden) und führe das Skript nochmal aus: `python main.py`.
4.  Jetzt hast du eine frische `adhocon_regulatory_prompts.csv`.

#### 2\. GitHub Repo erstellen

1.  Geh auf [github.com/new](https://github.com/new).
2.  **Repository name:** `regulatory-prompt-library`
3.  **Description:** `10,000+ Validated Regulatory Prompts for MedTech, IVD, Pharma & AI. Open Source by ADHOCON.`
4.  **Public:** Auswählen.
5.  **Initialize with README:** [x] Ja (Ankreuzen).
6.  **License:** MIT License.
7.  Klicke **Create repository**.

#### 3\. Dateien hochladen

1.  Im neuen Repo, klicke auf **Add file** -\> **Upload files**.
2.  Zieh die `main.py` und die `adhocon_regulatory_prompts.csv` rein.
3.  Commit message: `Initial release v1.0`.
4.  Button: **Commit changes**.

#### 4\. Das Readme "schön" machen

1.  Klicke in der Dateiliste auf `README.md`.
2.  Klicke auf das **Stift-Icon** (Edit).
3.  **Lösche alles**, was drin steht.
4.  **Kopiere den kompletten Markdown-Code** aus "Teil 1" (siehe oben in meiner Antwort) und füge ihn ein.
5.  Scrolle runter und klicke **Commit changes**.

#### 5\. Check

Geh auf die Hauptseite des Repos (`Code`-Tab).
Du solltest jetzt:

  * Ein zentriertes Logo/Header sehen.
  * Bunte Badges (License, Sector).
  * Eine klare Tabelle und schöne Emojis sehen.

Das sieht dann genauso professionell aus wie *ReguWatch*.

**Bist du bereit? Los geht's\!** Sag Bescheid, wenn der Link steht – das wird auf LinkedIn Wellen schlagen.
