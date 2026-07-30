# The Investigator

An AI-powered security & network analyst I'm building across 8 weeks.

## Skills so far

- Week 1: Thinks like a security analyst (prompt library)
- Week 2: can triage suspicious emails — check headers
(SPF/DKIM/DMARC, Reply-To), flag urgency/secrecy/authority,
recommend out-of-band verification.
- Week 3: Can audit server logs for failed-login and brute-force patterns (see [audit.py](http://audit.py)).
- Week 4: *Can hunt network beaconing ([hunt.py](http://hunt.py)) and reconstruct an incident timeline from multiple logs to guide response ([timeline.py](http://timeline.py)).*
- Week 5: Runs an automated triage pipeline (GitHub Actions + a local Llama 3.2 model via Ollama) that reads the IR runbook, maps findings to MITRE ATT&CK, and writes a verified incident report.
- Week 6: A Streamlit SOC Copilot that correlates four telemetry sources (firewall, Sysmon, Windows, Suricata) via Groq and returns a triaged report with MITRE mapping, severity, and response plan.
- Week 7: The live Streamlit website lets analysts upload logs, correlate incidents, ask follow-up questions, and browse saved case reports.

## Streamlit website

The Streamlit site, **The Investigator v1.2 — SOC Copilot**, helps a security analyst investigate incidents in one workspace. It uses Groq's hosted Llama 3.3 70B model to:

- Accept one or more uploaded log files and correlate them into a single incident assessment, including the attack chain, involved hosts/accounts/IPs, MITRE ATT&CK mappings, severity, investigation steps, and a response plan.
- Provide an **Ask the Investigator** chat for follow-up questions about a case or SOC analysis.
- Display saved Markdown incident reports from the `reports/` directory in a **Case Files** tab.
- Keep the active report available across Streamlit reruns, allow it to be downloaded as a timestamped Markdown file, and start a fresh analysis when needed.

The app requires a `GROQ_API_KEY` in `.streamlit/secrets.toml` to run AI-powered correlation and chat.

More coming each week.
