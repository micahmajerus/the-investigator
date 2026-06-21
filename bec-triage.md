# BEC Triage Report — Meridian Group Wire-Transfer Email

## Verdict
**Spoofed (Impersonation)** **Confidence:** High

* **Definitive Authentication Triple-Failure:** DKIM, SPF, and DMARC all failed. A legitimate email from `marcus.webb@meridiangroup.com` sent through Meridian's own servers would pass all three. Failing all three means this email never touched Meridian's corporate email infrastructure.
* **Unauthorized Delivery Path:** The delivery path confirms Gmail as the sending platform. The `Received:` chain shows the message entered the internet via `smtp.gmail.com`. No executive with legitimate access to their corporate account needs to use a personal Gmail server to send official company correspondence.
* **Geographic Discrepancy & Technical Fingerprint:** The originating IP directly contradicts the email's narrative. The network address `41.223.57.188` belongs to a West African (likely Nigerian) mobile ISP, whereas the email body claims the sender is currently located in Singapore. Furthermore, the private address `192.168.43.7` within the headers fingerprints a mobile phone hotspot—a known signature of Nigerian Business Email Compromise (BEC) operators.
* **The "Money Trap" Reply-To Header:** The `Reply-To` header is explicitly set to `mwebb.ceo2026@gmail.com`, which serves as the attacker's actual inbox. The display `From` field is purely cosmetic and can be easily faked. No legitimate executive routes wire transfer replies to a personal Gmail account. This single field provides sufficient grounds to quarantine the message and escalate the incident without further forensic analysis.
* **Compromised Account Ruled Out:** A true account takeover (ATO) would route traffic through Meridian's authorized servers, thereby passing SPF and DKIM checks. The forensic signatures present here—external relay, foreign mobile IP, and Gmail infrastructure—are mutually exclusive with a legitimate compromise failure mode.
* **Playbook Alignment:** Every qualitative and quantitative element—CEO impersonation, Friday afternoon timing, phone-blocking excuses, strict secrecy mandates, artificial deadlines, and a generic vendor profile—perfectly maps onto the documented BEC attacker playbook. The header evidence definitively closes the case.

---

## Red Flags Found

### Technical & Header Indicators
* **Spoofed Identities:** `Reply-To` points to a personal Gmail address (`mwebb.ceo2026@gmail.com`) rather than the official corporate domain.
* **Authentication Failure:** Severe SPF softfail, DKIM failure, and DMARC failure indicate the sender is completely unauthorized.
* **Geographic Anomaly:** The originating IP address (`41.223.x.x`) resolves to an African mobile ISP instead of Singapore.
* **Device Fingerprint:** The private IP `192.168.43.7` in the headers reveals a mobile phone hotspot connection, exposing that the attacker was working from a phone rather than a corporate boardroom.

### Social Engineering & Contextual Indicators
* **Calculated Timing:** Sent at **4:31 PM on a Friday**. This is a deliberate tactic engineered to compress the verification window to under 30 minutes before the weekend, a time when senior staff are difficult to reach and employees are mentally checked out.
* **Pre-emptive Communication Block:** The claim of being "unreachable until Monday" is not just an excuse for urgency—it is a strategic barrier designed to eliminate the single verification step (a phone call) that would immediately compromise the attack.
* **Targeted Secrecy:** The instruction to *"not discuss with anyone else on the team"* specifically targets the approval chain. It is designed to prevent the recipient from looping in the CFO, compliance officers, or a secondary approver who would recognize the scam.
* **Flattering Pretext:** The "confidential acquisition" narrative is a psychological upgrade. It provides a plausible reason for the secrecy mandate and applies subtle pressure by implying the target has been trusted with highly sensitive corporate information.
* **Unverifiable Vendor Profile:** The vendor name **"Apex Consulting Group"** is generic and lacks an existing historical footprint or purchasing relationship to cross-check against. A legitimate corporate acquisition of this scale would require extensive, multi-departmental legal and financial documentation.
* **Evading Compliance Thresholds:** The requested transfer amount (**$84,000**) sits strategically below common $100,000 corporate reporting and compliance thresholds to avoid triggering automated review workflows.
* **Geographic Inconsistency:** Routing a transaction for a Singapore-based deal involving a generic consulting group to the **"First National Bank of Nevada"** introduces an erratic, high-risk banking profile with no prior history.

---

## Verification Checklist
*Complete these mandatory steps before executing any wire transfer.*

1. **Verify via Out-of-Band Voice Confirmation** Do not reply directly to the email thread. Call the requestor using a trusted phone number extracted from your internal corporate directory or an established historical contact card. A text message or email confirmation from the same thread is invalid.  
   * **⚠️ Current Case Context:** *The email explicitly claims the sender is unreachable. This claim is the red flag, not a valid excuse.*
2. **Inspect the Full Reply-To Header** Hover over or expand the sender information inside your email client. If the `Reply-To` field differs from the `From` domain, treat the email as fraudulent.  
   * **⚠️ Current Case Context:** *The hidden Reply-To address is `mwebb.ceo2026@gmail.com` instead of the company domain.*
3. **Independently Confirm Vendor Bank Details** Contact the receiving vendor directly using a phone number retrieved from their official corporate website or internal historical database records—never use contact details provided within the suspect email. Attackers frequently embed fraudulent contact numbers alongside fake account numbers.
4. **Enforce Dual-Authorization Controls** Any wire transfer exceeding designated corporate thresholds (typically $10,000+) requires a second authorized internal signatory. A request to bypass standard operating procedures or maintain total confidentiality is an immediate disqualifier.  
   * **⚠️ Current Case Context:** *The instruction "Do not discuss with anyone else" should halt the transfer immediately.*
5. **Reconcile Against an Approved Invoice or PO** Cross-reference the payment request against an existing Purchase Order (PO), executed contract, or verified invoice inside the internal ERP or accounting system. If there is no documented paper trail, do not authorize the transfer. "Confidential acquisitions" do not supersede financial controls.
6. **Resist Artificial Urgency** Artificial deadlines are designed to force errors. If conducting thorough verifications (Steps 1–5) causes you to miss a stated deadline, **miss the deadline**. Legitimate vendors will happily accommodate verification delays; fraudsters will disappear when forced to wait 24 hours.  
   * **⚠️ Current Case Context:** *A "hard deadline of 5 PM today" on a Friday afternoon is intentionally engineered to force the bypass of security protocols.*
