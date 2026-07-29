Ransomware Incident Response Runbook

Organized by NIST SP 800-61 phases. Work through each phase in order; check off steps as completed.

Phase 1 — Preparation
 1. Maintain offline, verified-clean backups. Keep backups isolated (offline or immutable) and routinely test restoration so recovery doesn't depend on trusting a decryptor.
 2. Keep the IR plan and contacts current. Maintain an up-to-date contact list (IR team, legal, leadership, cyber insurance, law enforcement, outside forensics) and pre-approve escalation/communication paths.
 3. Ensure logging and detection coverage. Confirm EDR/AV, network monitoring, and centralized logging are deployed and retained long enough to support investigation.
 4. Pre-stage response tooling and access. Have forensic imaging tools, isolated analysis systems, and out-of-band communication channels ready before they're needed.
Phase 2 — Detection & Analysis
 1. Confirm and scope the incident. Verify it really is ransomware (ransom note, mass file encryption, changed file extensions) and determine the blast radius (affected hosts, accounts, shares, backups).
 2. Preserve evidence before you change anything. Capture volatile data first (memory, active network connections, logged-in users) and collect relevant logs.
 3. Do not power off encrypted machines. Powering off can destroy in-memory evidence (e.g., encryption keys); isolate instead (see Phase 3).
Phase 3 — Containment, Eradication & Recovery
 4. Isolate, don't destroy. Disconnect affected hosts from the network (disable the switch port or pull the cable) rather than shutting them down.
 5. Identify and eradicate the root cause. Remove attacker footholds (malware, persistence mechanisms, compromised accounts/credentials) before reconnecting or rebuilding systems.
 6. Recover from known-good backups. Restore from offline backups you have verified are clean; rebuild rather than trust decryptors where possible. Do not pay the ransom as a first resort.
Phase 4 — Post-Incident Activity
 7. Document everything. Record the full timeline, every action taken, all indicators of compromise, and the MITRE ATT&CK techniques observed (e.g., T1110 Brute Force, T1071 C2 over Web Protocols, T1486 Data Encrypted for Impact).
 8. Conduct lessons learned. Hold a review, fix the root cause (the entry vector), tune detections, and update this runbook. Make any required notifications (legal, regulators, affected parties) according to policy.****
