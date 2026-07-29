import ollama, os
from datetime import datetime
 
# 1. Read every file in evidence/ (the logs), concatenated with filename headers
evidence_text = ""
for filename in sorted(os.listdir("evidence")):
    filepath = os.path.join("evidence", filename)
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            evidence_text += f"--- FILE: {filename} ---\n{f.read()}\n\n"
 
# 2. Read the incident-response runbook
with open("ir_runbook.md", "r", encoding="utf-8", errors="replace") as f:
    runbook_text = f.read()
 
# Build the prompt: ask for summary, timeline, root cause, ATT&CK mapping,
# runbook step status, and next actions
prompt_text = f"""Using the runbook and evidence below, write a Markdown
incident report with these sections: Summary, Timeline, Root Cause,
MITRE ATT&CK Mapping (tactic, technique name, technique ID per finding),
Runbook Step Status (which steps were completed vs. missed), and
Recommended Next Actions.
 
RUNBOOK:
{runbook_text}
 
EVIDENCE:
{evidence_text}"""
 
# 3. Send both to the local Llama 3.2 model via Ollama
resp = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a senior SOC analyst. "
            "Map findings to MITRE ATT&CK with technique IDs and cite the runbook."},
        {"role": "user", "content": prompt_text},
    ],
)
report = resp.message.content
 
# 4. Write the result to a timestamped file in reports/ so re-runs don't overwrite
os.makedirs("reports", exist_ok=True)               # folder may not exist on the runner
stamp = datetime.now().strftime("%Y-%m-%d_%H%M")    # unique per run, not just per day
open(f"reports/report_{stamp}.md", "w").write(report)
 
