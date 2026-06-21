# BEC Triage — Meridian Group wire-transfer email

## Verdict
Spoofed (impersonation). Confidence: high.
-The authentication triple-failure is definitive. DKIM, SPF, and DMARC all failed. A legitimate email from marcus.webb@meridiangroup.com sent through Meridian's own servers would pass all three. Failing all three means this email never touched Meridian's infrastructure.
-The delivery path confirms Gmail as the sending platform. The Received: chain shows the message entered the internet at smtp.gmail.com. Nobody with legitimate access to a corporate account needs Gmail to send company email.
-The originating IP contradicts the email's own story. 41.223.57.188 is a West African (likely Nigerian) mobile ISP address. The email claims the sender is in Singapore. The IP doesn't lie; the email body does. The private address 192.168.43.7 further fingerprints a phone hotspot — a known signature of Nigerian BEC operators.
-The Reply-To is the money trap. mwebb.ceo2026@gmail.com is the attacker's actual inbox. The From field is cosmetic — anyone can type any address there. No legitimate executive routes wire transfer replies to a personal Gmail account. This single field is sufficient to quarantine and escalate without any further forensic analysis.
-"Compromised account" is ruled out because a real account takeover would send through Meridian's servers, passing DKIM and SPF. The forensic signature here is completely different — external relay, foreign IP, Gmail infrastructure. These are mutually exclusive failure modes.
-Every element — CEO impersonation, Friday afternoon timing, phone-blocking excuse, secrecy instruction, artificial deadline, generic vendor — maps onto the documented BEC playbook. The header evidence closes it.

## Red flags found
- Reply-To is a Gmail address, not the company domain
- SPF softfail, DKIM fail, DMARC fail — sender not authorized
- Originating IP (41.223.x.x) is an African ISP, not Singapore
- Urgency (5 PM deadline), secrecy ("don't tell the team"),
  authority (the CEO)
-Timing — sent at 4:31 PM on a Friday. This is deliberate: it compresses the verification window to under 30 minutes before the weekend, when senior staff are harder to reach and people are mentally checked out.
-The "unreachable until Monday" claim — this isn't just urgency, it's a pre-emptive block on the one verification step (a phone call) that would kill the attack instantly. Conveniently, the attacker needs to be unreachable for exactly as long as the deadline is active.
-The secrecy instruction targets the approval chain specifically — "don't discuss with anyone else on the team" isn't generic discretion, it's designed to prevent Sandra from looping in the exact people (CFO, compliance, a second approver) who would catch this.
"Confidential acquisition" is a social engineering upgrade — it gives the secrecy instruction a plausible, flattering reason. It also implies Sandra has been trusted with sensitive information, which creates psychological pressure to comply rather than question.
-The vendor name "Apex Consulting Group" is generic and unverifiable at a glance — unlike a known supplier, there's no existing relationship to cross-check against. A real acquisition payment of this size would go through legal and finance with extensive prior documentation.
-The amount — $84,000 — sits just under common $100K reporting thresholds — this may be intentional to avoid triggering automatic compliance reviews.
-The bank is "First National Bank of Nevada" — for a supposed Singapore-based deal with a consulting group, wiring to a Nevada bank with no prior relationship is geographically and contextually inconsistent.
-The private IP 192.168.43.7 in the headers — as noted in the forensic report, this is a mobile hotspot signature. The attacker was literally on their phone, not in a Singapore boardroom.

## Verification checklist (before wiring money)
1. Verify by voice — not by replying to the email. Call the requestor on a number from your internal directory or a previous known contact. A text or email "confirmation" from the same thread does not count. ⚠️ This email claims the sender is unreachable — that is the red flag, not the excuse.
2. Check the Reply-To address — is it different from From? Hover over or expand the sender details in your email client. If Reply-To differs from From, treat the email as fraudulent until proven otherwise. ⚠️ This email's Reply-To is mwebb.ceo2026@gmail.com — not a company address.
3. Confirm the bank account with the vendor directly. Call the vendor using a number from your records or their official website — not a number provided in the email. Fraudsters sometimes supply fake contact info alongside fake account numbers.
4. Get a second approver — especially if told to keep it secret. Any wire above your threshold (typically $10K+) requires a second authorized signatory. A request to skip this step or keep the transfer confidential is itself a disqualifying red flag. ⚠️ "Do not discuss with anyone else" should stop the transfer immediately.
5. Match the request to a known invoice or PO. Locate the original purchase order, signed contract, or invoice in your accounting system. No paper trail = no wire. "Confidential acquisition" is not a substitute for documentation.
6. Slow down on urgency — artificial deadlines are a tactic. If completing steps 1–5 would miss the stated deadline, the answer is to miss the deadline. Legitimate vendors reschedule. Fraudsters disappear when you ask for 24 hours. ⚠️ "Hard deadline of 5 PM today" on a Friday is engineered to skip verification.
