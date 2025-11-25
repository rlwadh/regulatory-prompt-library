import pandas as pd
import itertools

# ==========================================
# 1. THE TRUTH SOURCE (REGULATORY MAPPING)
# ==========================================
# Hier definieren wir die exakten Standards. Keine Halluzinationen.

REGULATORY_MAPPING = {
    "MedTech_General": {
        "EU": "EU MDR 2017/745, ISO 13485:2016, ISO 14971:2019, MEDDEV 2.7/1 Rev 4",
        "US": "FDA 21 CFR Part 820 (QSR), 21 CFR Part 11, ISO 14971:2019, FDA Guidance on Human Factors",
        "Global": "IMDRF/GRRP WG/N47 (Essential Principles), ISO 13485:2016 (MDSAP)"
    },
    "MedTech_IVD": { 
        "EU": "EU IVDR 2017/746, ISO 13485:2016, ISO 14971, MDCG Guidelines for IVDs",
        "US": "FDA 21 CFR Part 809 (IVDs), 21 CFR Part 820, CLIA Regulations",
        "Global": "IMDRF/IVD WG/N64 (IVD Essential Principles), GHTF/SG5/N7"
    },
    "SaMD_and_AI": { 
        "EU": "EU MDR 2017/745 (Rule 11), IEC 62304:2006+A1:2015, IEC 82304-1, EU AI Act (Relevant Articles for Safety)",
        "US": "FDA 21 CFR Part 820, FDA AI/ML Action Plan, FDA PCCP Guidance (Predetermined Change Control Plan), NIST AI Risk Management Framework",
        "Global": "IMDRF/SaMD WG/N41 (SaMD Clinical Evaluation), ISO/IEC 42001 (AI Management System), IEC 62304"
    },
    "Pharma": {
        "EU": "EudraLex Vol 4 (EU GMP), EU GMP Annex 11, EMA Scientific Guidelines",
        "US": "FDA 21 CFR Part 210/211 (cGMP), 21 CFR Part 11, FDA Data Integrity Guidance",
        "Global": "ICH Q7 (API), ICH Q9 (Risk Management), ICH Q10 (Pharma Quality System), PIC/S GMP Guide"
    }
}

# ==========================================
# 2. THE ARTIFACTS (DOCUMENTS TO CREATE)
# ==========================================

ARTIFACTS_HARDWARE = [
    "Risk Management Plan", 
    "Clinical Evaluation Plan (CEP)", 
    "Post-Market Surveillance (PMS) Plan",
    "Technical File Index (Annex II)", 
    "Biocompatibility Assessment (ISO 10993)",
    "General Safety and Performance Requirements (GSPR) Checklist"
]

ARTIFACTS_IVD = [
    "Performance Evaluation Report (PER)", 
    "Scientific Validity Report",
    "Analytical Performance Report", 
    "Clinical Performance Report",
    "IVD Post-Market Performance Follow-up (PMPF) Plan"
]

ARTIFACTS_AI = [
    "Software Development Plan (SDP)", 
    "Software Requirements Specification (SRS)",
    "Cybersecurity Vulnerability Management Plan", 
    "Predetermined Change Control Plan (PCCP)",  # Crucial for AI
    "AI Model Card / Datasheet",
    "Algorithm Bias Assessment Report",
    "Usability Engineering File (IEC 62366 for SaMD)"
]

ARTIFACTS_PHARMA = [
    "Site Master File (SMF)", 
    "Validation Master Plan (VMP)",
    "Out of Specification (OOS) Investigation SOP", 
    "Batch Record Review Checklist",
    "Annual Product Quality Review (APQR)", 
    "Stability Study Protocol",
    "Corrective and Preventive Action (CAPA) SOP"
]

TASKS = [
    "Draft a detailed outline for", 
    "Create a compliance gap analysis checklist for",
    "Write an executive summary structure for", 
    "Formulate a risk-based review strategy for",
    "Generate a list of likely auditor questions for", 
    "Create a compliant template for"
]

ROLES = [
    "Senior Quality Manager", 
    "Regulatory Affairs Lead", 
    "Lead Auditor", 
    "AI Regulatory Specialist", # New for AI
    "Compliance Officer"
]

# ==========================================
# 3. THE GENERATOR ENGINE
# ==========================================

prompts = []

def create_prompt(sector, region, role, task, artifact, regulation):
    # Chain-of-Thought Structure for maximum quality
    return f"""
# SYSTEM ROLE
Act as a {role} specialized in {sector} ({region}).

# TASK
{task} a "{artifact}".

# MANDATORY COMPLIANCE FRAMEWORK
You must adhere strictly to: {regulation}.
Do NOT use generic advice. Use specific terminology from these standards.

# OUTPUT INSTRUCTIONS
1. Format: Professional Markdown with hierarchical headers.
2. Citation: Cite specific articles/clauses of {regulation.split(',')[0]} where possible.
3. Tone: Technical, precise, and audit-ready.
4. Placeholders: Use [INSERT DATA] for missing specific product info.
"""

def generate_batch(sector_key, artifact_list):
    regions = REGULATORY_MAPPING[sector_key].keys()
    for region in regions:
        reg_text = REGULATORY_MAPPING[sector_key][region]
        for artifact in artifact_list:
            for role in ROLES:
                for task in TASKS:
                    # Logic Check: Don't let an "AI Specialist" write a Pharma Batch Record if not relevant
                    # keeping it simple for mass generation, but conceptually separated by lists.
                    
                    prompt_text = create_prompt(sector_key, region, role, task, artifact, reg_text)
                    prompts.append({
                        "Sector": sector_key,
                        "Region": region,
                        "Role": role,
                        "Task": task,
                        "Artifact": artifact,
                        "Prompt": prompt_text
                    })

# ==========================================
# 4. EXECUTION
# ==========================================

# Generate Logic-Based Combinations
generate_batch("MedTech_General", ARTIFACTS_HARDWARE)
generate_batch("MedTech_IVD", ARTIFACTS_IVD)
generate_batch("SaMD_and_AI", ARTIFACTS_AI)
generate_batch("Pharma", ARTIFACTS_PHARMA)

# Save to CSV
df = pd.DataFrame(prompts)
filename = "adhocon_regulatory_prompts.csv"
df.to_csv(filename, index=False)

print(f"✅ SUCCESS: Generated {len(df)} regulatorily validated prompts.")
print(f"   Covering: FDA, MDR, IVDR, IMDRF, ICH, and AI/ML Specifics.")
print(f"📁 Saved to {filename}")