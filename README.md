# The Investigator — AI Security & Network Copilot

The Investigator turns raw security logs into evidence-backed incident reports and can autonomously choose investigation steps while keeping its tool trail visible for review.

🔗 [Live app](https://the-investigator-ocv93sntztrbdc2bsjq8zm.streamlit.app/) · 📂 [GitHub repository](https://github.com/micahmajerus/the-investigator) · 🐳 [Docker Hub](https://hub.docker.com/r/micahmajerus/investigator-agent)

![The Investigator app](docs/screenshot.png)

## What it does

- **Correlate & Triage:** Upload one or more log files and generate one incident report with a timeline, severity, response plan, and MITRE ATT&CK mapping.
- **Ask the Investigator:** Chat with an AI security analyst about an active case or a general SOC question.
- **Case Files:** Browse previously generated Markdown investigation reports.
- **Autonomous Investigation:** Give the agent a goal and watch it choose evidence and MITRE lookup tools before producing a verdict.
- **Scheduled triage:** GitHub Actions checks the evidence every hour and runs the local Ollama pipeline only when the evidence has changed.

AI output is a starting point, not a final security decision. The app asks the model to cite evidence and expose uncertainty, and the autonomous mode shows its tool trail so an analyst can verify the result.

## Tech stack

- Python and Streamlit for the web app
- Groq-hosted Llama 3.3 70B for correlation, chat, and tool-calling
- Ollama with Llama 3.2 3B for the automated pipeline
- GitHub Actions for event-driven and hourly triage
- Docker for the containerized command-line agent
- MITRE ATT&CK for technique mapping

## Run the web app locally

Prerequisites: Python 3.12+ and a [Groq API key](https://console.groq.com/keys).

```bash
git clone https://github.com/micahmajerus/the-investigator.git
cd the-investigator
python -m venv .venv
```

Activate the environment:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install and configure:

```bash
pip install -r requirements.txt
mkdir .streamlit
```

Create `.streamlit/secrets.toml` (this file is ignored by Git):

```toml
GROQ_API_KEY = "your-groq-api-key"
```

Then start the app:

```bash
streamlit run app.py
```

## Run the autonomous CLI agent

```bash
# macOS/Linux
export GROQ_API_KEY="your-groq-api-key"

# Windows PowerShell
$env:GROQ_API_KEY="your-groq-api-key"

python agent.py
```

## Run with Docker

The image runs the autonomous CLI agent against the bundled `evidence/` files:

```bash
docker pull micahmajerus/investigator-agent:latest
docker run --rm -e GROQ_API_KEY="your-groq-api-key" micahmajerus/investigator-agent:latest
```

Or build it from this repository with `docker build -t investigator-agent .`.

## Scheduled pipeline

`.github/workflows/triage.yml` runs after evidence changes, once per hour, or on manual dispatch. `triage.py` hashes the current evidence and exits without calling the model when nothing changed. When new evidence is present, it uses local Ollama in the Actions runner, writes a Markdown report to `reports/`, and commits the report and evidence digest.
