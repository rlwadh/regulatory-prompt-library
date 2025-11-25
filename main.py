import pandas as pd
import itertools

# ==========================================
# 1. THE TRUTH SOURCE (REGULATORY MAPPING)
# ==========================================

REGULATORY_MAPPING = {
    "MedTech_Hardware": {
        "EU": "EU MDR 2017/745, ISO 13485:2016, ISO 14971:2019, MEDDEV 2.7/1 Rev 4",
        "US": "FDA 21 CFR Part 820 (QSR), 21 CFR Part 11, ISO 14971:2019",
        "Global": "ISO 13485:2016, MDSAP Requirements"
    },
    "MedTech_SaMD": { # Software as a Medical Device
        "EU": "EU MDR 2017/745, IEC 62304:2006+A1:2015, IEC 82304-1, ISO 14971",
        "US": "FDA 21 CFR Part 820, FDA Guidance on Cybersecurity, IEC 62304",
        "Global": "IMDRF SaMD Guidelines (N10/N12/N41), IEC 62304"
    },
    "IVD": { # In Vitro Diagnostics (The Pain Point!)
        "EU": "EU IVDR 2017/746, ISO 13485:2016, ISO 14971, MDCG Guidelines for IVDs",
        "US": "FDA 21 CFR Part 809 (IVDs), 21 CFR Part 820, CLIA Regulations",
    },
    "Pharma": {
        "EU": "EudraLex Vol 4 (GMP), EU GMP Annex 11, ICH Q10 (PQS)",
        "US": "FDA 21 CFR Part 210/211 (cGMP), 21 CFR Part 11, FDA Data Integrity Guidance",
        "Global": "ICH Q7 (API), ICH Q9 (Risk), PIC/S GMP Guide"
    }
}

# ==========================================
# 2. THE ARTIFACTS (DOCUMENTS)
# ==========================================

ARTIFACTS_HARDWARE = [
    "Risk Management Plan", "Clinical Evaluation Plan (CEP)", "Post-Market Surveillance (PMS) Plan",
    "Technical File Index (Annex II)", "Labeling Checklist", "Biocompatibility Assessment Report (ISO 10993)",
    "General Safety and Performance Requirements (GSPR) Checklist", "EU MDR", "usability", "validation", "design", "verification", "manufacturing", "ISO13485", "Quality Management System"
]

ARTIFACTS_SAMD = [
    "Software Development Plan (SDP)", "Software Requirements Specification (SRS)",
    "Cybersecurity Vulnerability Management Plan", "Algorithm Change Protocol",
    "Usability Engineering File (IEC 62366)", "Software Architecture Design Chart", "EU MDR", "usability", "validation", "design", "verification", "manufacturing", "ISO13485", "Quality Management System"
]

ARTIFACTS_IVD = [
    "Performance Evaluation Report (PER)", "Scientific Validity Report",
    "Analytical Performance Report", "Clinical Performance Report",
    "IVD Post-Market Performance Follow-up (PMPF) Plan", "EU IVDR", "usability", "validation", "design", "verification", "manufacturing", "ISO13485", "Quality Management System", "specificity", "Sensitivity"
]

ARTIFACTS_PHARMA = [
    "Site Master File (SMF)", "Validation Master Plan (VMP)",
    "Out of Specification (OOS) SOP", "Batch Record Review Checklist",
    "Annual Product Quality Review (APQR)", "Stability Study Protocol", "clinical study", "ICH", "Qbd", "Quality by design"
]

TASKS = [
    "Draft a detailed outline for", "Create a gap analysis checklist for",
    "Write an executive summary structure for", "Formulate a risk-based review strategy for",
    "Generate a list of likely audit questions for", "Create a compliance template for", "compile the document for", "generate the training for", "generate a record for", "check for compliance", 
]

ROLES = [
    "Senior Quality Manager", "Regulatory Affairs Lead", "Lead Auditor", "Compliance Officer", "safety office", "clinical lead"
]

# ==========================================
# 3. THE GENERATOR ENGINE
# ==========================================

prompts = []

def create_prompt(sector, region, role, task, artifact, regulation):
    # This structure ensures high-quality LLM outputs (Chain-of-Thought)
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
generate_batch("MedTech_Hardware", ARTIFACTS_HARDWARE)
generate_batch("MedTech_SaMD", ARTIFACTS_SAMD)
generate_batch("IVD", ARTIFACTS_IVD)
generate_batch("Pharma", ARTIFACTS_PHARMA)

# Save to CSV
df = pd.DataFrame(prompts)
filename = "adhocon_regulatory_prompts.csv"
df.to_csv(filename, index=False)

print(f"✅ SUCCESS: Generated {len(df)} regulatorily validated prompts.")
print(f"📁 Saved to {filename}")