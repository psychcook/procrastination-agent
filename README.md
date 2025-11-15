# Procrastination Intervention Agent

An evidence-based AI-powered conversational agent for procrastination intervention, built on Claude by Anthropic.

**Version:** 3.0  
**Tech Stack:** Python 3.11, Flask, Anthropic Claude API (claude-sonnet-4-5-20250929)  
**Research Team:** Yves, Nathalie, Eileen & Jara  
**Institution:** Zurich School of Applied Sciences  

---

## 🎯 Project Overview

This group project provides evidence-based psychological intervention for procrastination through a structured 4-phase conversational flow. The agent combines insights from **clinical psychology**, **behavioral economics**, and **cognitive science** to deliver personalized strategies.

### Key Features

✅ **Evidence-Based Psychology** - Grounded in peer-reviewed research (Temporal Motivation Theory, Motivational Interviewing, Implementation Intentions)  
✅ **Therapeutic Alliance** - Warm, non-judgmental tone based on Rogers' Person-Centered Therapy  
✅ **State-Based Conversation** - Mirrors therapeutic process: Intake → Hypothesis → Strategies → Completion  
✅ **Real-Time Streaming** - Server-Sent Events (SSE) for ChatGPT-like word-by-word response  
✅ **Auto-Continuation** - Seamless state transitions without user interruption  
✅ **Privacy-First** - Pseudonymized data collection, no personal information  
✅ **Production-Ready** - Security hardening, rate limiting, CSRF protection  

---

## 🧠 Scientific Foundation

Built on **50+ peer-reviewed studies** across clinical psychology, behavioral economics, and cognitive science:

**Core Frameworks:**
- **Temporal Motivation Theory** (Steel, 2007) - Meta-analysis of 691 correlations
- **Person-Centered Therapy** (Rogers) - Therapeutic alliance & unconditional positive regard
- **Motivational Interviewing** - Validation before intervention
- **Self-Determination Theory** - Autonomy support for sustained change

**Key Interventions:**
- Implementation Intentions (d = .65), WOOP Model (2x activity improvement)
- Temptation Bundling (10-14% increase), Self-Compassion (r = .47 well-being)
- Pomodoro Technique (25-35% productivity gain), Task Chunking (Cognitive Load Theory)

📖 **[Full Scientific Documentation](docs/psychological-foundations.md)** - Evidence base with citations

---

## 🛡️ Why Anthropic Claude?

For a sensitive therapeutic application like procrastination intervention, we chose **Anthropic's Claude API** over other LLM providers based on their industry-leading AI safety practices:

### Constitutional AI Framework
Anthropic pioneered **Constitutional AI (CAI)** - a structured approach to AI alignment that guides model behavior using predefined ethical principles derived from:
- The UN Declaration of Human Rights
- Trust and safety best practices from multiple research labs
- Transparent, auditable rules rather than opaque training processes

### Superior Safety Performance
In joint safety evaluations with OpenAI (2025), Claude models demonstrated:
- **Perfect instruction hierarchy scores** - Critical for maintaining therapeutic boundaries
- **Stronger resistance to jailbreaking** - Protected by Constitutional Classifiers
- **Safer behavior out-of-the-box** - Minimal need for extensive prompt engineering to ensure appropriate responses

### High-Stakes Use Case Alignment
Claude's design prioritizes **predictability and trust**, making it particularly well-suited for applications involving:
- Vulnerable users seeking help
- Psychological interventions requiring empathy and care
- Sensitive topics where harmful outputs could cause real damage

### Ongoing Safety Commitment
Anthropic maintains rigorous safety standards through:
- **AI Safety Levels (ASL-3)** protections for advanced models
- Active support for AI safety regulation (endorsed California SB 53)
- Continuous iteration on safety through the Responsible Scaling Policy

For therapeutic AI applications where user wellbeing is paramount, these safety guarantees provide essential peace of mind that the agent will remain helpful, harmless, and aligned with therapeutic principles throughout the intervention.

---

## 📊 The Seven Procrastination Factors

Based on **Piers Steel's Temporal Motivation Theory** (2007 meta-analysis of 691 correlations):

1. **Perfectionism** - Fear of mistakes, unrealistic standards
2. **Task Aversion** - Unpleasant/boring tasks (r = 0.40)
3. **Overwhelm** - Tasks feel too big/complex
4. **Deadline Problems** - Distant deadlines, lack of urgency
5. **Lack of Clarity** - Unclear starting point
6. **Emotional Dysregulation** - Avoidance of negative feelings
7. **Self-Efficacy Doubts** - Doubts about abilities (Bandura)

---

## 🌊 User Flow (5 Screens)

1. **WELCOME** - Landing page with project information and privacy notice
2. **PRE-QUESTIONNAIRE** - 7 baseline questions (1-7 Likert scale)
3. **CHAT** - AI-guided conversation with 4 therapeutic phases
4. **POST-QUESTIONNAIRE** - 12 questions (7 repeated + 5 evaluation)
5. **THANK YOU** - Completion message with data information

---

## 🔄 Chat State Machine (4 Phases)

```
INTAKE → HYPOTHESES → STRATEGIES → COMPLETION
```

1. **INTAKE** - Understand the procrastinated task (empathetic assessment, one question at a time)
2. **HYPOTHESES** - Identify psychological causes collaboratively (user validates hypotheses)
3. **STRATEGIES** - Provide matched, evidence-based interventions (implementation intentions)
4. **COMPLETION** - Reinforce learning and next steps (build self-efficacy)

**Auto-Continuation Feature:** Agent seamlessly transitions between states without requiring user input, creating natural conversational flow

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Anthropic API Key ([console.anthropic.com](https://console.anthropic.com))

### Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create `.env` file:**
```bash
cp .env.example .env
```

3. **Add your secrets to `.env`:**
```
ANTHROPIC_API_KEY=sk-ant-...
SECRET_KEY=<generate_with_python_os_urandom>
ADMIN_TOKEN=<generate_secure_token_for_data_download>
```

**Generate SECRET_KEY and ADMIN_TOKEN:**
```bash
python3 -c "import os; print(os.urandom(32).hex())"
```

### Run Locally

**Flask Development Server:**
```bash
python3 app_flask.py
```

**Or with Gunicorn (Production Server):**
```bash
gunicorn app_flask:app --bind 0.0.0.0:8501 --workers 2 --timeout 120
```

The app will be available at `http://localhost:8501`.

---

## 📁 Project Structure

```
procrastination_agent/
├── app_flask.py                  # Main Flask application
├── requirements.txt              # Python dependencies
├── nixpacks.toml                # Railway build configuration
│
├── config/
│   ├── questions.py             # Questionnaire definitions
│   ├── security.py              # Security configuration
│   └── prompts/                 # AI system prompts (extracted)
│       ├── intake.txt           # Phase 1: Assessment
│       ├── hypotheses.txt       # Phase 2: Formulation
│       ├── strategies.txt       # Phase 3: Intervention
│       └── completion.txt       # Phase 4: Consolidation
│
├── templates/                   # Jinja2 HTML templates
├── static/css/                  # CSS styles
├── utils/
│   ├── storage.py              # JSON data persistence
│   └── session.py              # Session management
│
├── data/responses/             # Anonymized session data (JSON)
│
└── docs/
    ├── psychological-foundations.md  # Scientific documentation
    └── ux-design-specification.md    # UX Design Specification
```

---

## 🔒 Security & Privacy

### Implemented Security Measures
✅ **CSRF Protection** - Flask-WTF token-based protection  
✅ **Rate Limiting** - Per-endpoint limits (20 chat requests/hour)  
✅ **Input Sanitization** - Bleach library for XSS prevention  
✅ **Session Encryption** - Flask sessions with SECRET_KEY  
✅ **HTTPS Only** - Talisman security headers (production)  
✅ **Content Security Policy** - Strict CSP headers  
✅ **Input Validation** - Length limits, type checking, value ranges  

### Privacy-First Design
- **Pseudonymized Data** - UUID session IDs, no personal information
- **No Chat Transcripts Stored** - Only questionnaire responses saved
- **No IP Tracking** - Minimal logging, no user tracking
- **Local Data Storage** - JSON files, not cloud databases

---

## 🧪 Research Data Collection

### What is Collected
- **Session ID:** UUID (pseudonymized)
- **Timestamps:** Created, pre-questionnaire completed, chat completed, post-questionnaire completed
- **Pre-Questionnaire:** 7 questions (1-7 Likert scale)
- **Post-Questionnaire:** 12 questions (7 repeated + 5 evaluation)

### What is NOT Collected
❌ Chat transcripts
❌ Personal information (names, emails)
❌ IP addresses
❌ Device information

### Data Format
```json
{
  "session_id": "uuid-here",
  "created_at": "2025-11-15T10:30:00Z",
  "pre_questionnaire": {
    "completed_at": "2025-11-15T10:32:00Z",
    "answers": [{"question_id": 1, "value": 5}, ...]
  },
  "chat_completed_at": "2025-11-15T10:45:00Z",
  "post_questionnaire": {
    "completed_at": "2025-11-15T10:50:00Z",
    "answers": [{"question_id": 1, "value": 3}, ...]
  }
}
```

---

## 💾 Data Access & Persistence

### Quick Data Access (Download Endpoint)

1. **Set Admin Token on Railway:**
```bash
# Generate secure token
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Set on Railway
railway variables set ADMIN_TOKEN=your-generated-token
```

2. **Download Data:**
Visit: `https://your-app.up.railway.app/api/download-data?token=YOUR_ADMIN_TOKEN`

This downloads a timestamped JSON file with all session data (rate limited, secure).

---

## 🚂 Deployment (Railway)

### One-Click Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

### Manual Deployment

1. **Install Railway CLI:**
```bash
brew install railway
```

2. **Login and initialize:**
```bash
railway login
railway init
```

3. **Set environment variables:**
```bash
railway variables set ANTHROPIC_API_KEY=sk-ant-...
railway variables set SECRET_KEY=your-generated-key
```

4. **Deploy:**
```bash
railway up
```

5. **Get URL:**
```bash
railway domain
```

**Deployment files:**
- `nixpacks.toml` - Defines Gunicorn start command
- `.railwayignore` - Excludes unnecessary files

---

## 📖 Documentation

**For Developers:**
- **[CLAUDE.md](CLAUDE.md)** - Complete technical documentation, architecture, API endpoints
- **[docs/ux-design-specification.md](docs/ux-design-specification.md)** - User experience design principles and guidelines

**For Researchers:**
- **[docs/psychological-foundations.md](docs/psychological-foundations.md)** - Complete scientific evidence base

---

## 🎓 Research Validation

Supported by **50+ peer-reviewed studies** including:
- **Meta-analyses:** Steel (691 correlations), Gollwitzer (94 studies), Neff & Zessin (79 studies)
- **RCTs:** Milkman (Temptation Bundling), Oettingen (WOOP), Eckert (Emotion Regulation)
- **Validated theories:** Temporal Motivation Theory, Self-Determination Theory, Social Cognitive Theory

📖 **[Full References](docs/psychological-foundations.md#7-references)** - Complete citations and DOIs in scientific documentation

---

## 🛠️ Technology Stack

### Backend
- **Framework:** Flask (Python 3.11)
- **AI:** Anthropic Claude API (Sonnet 4.5) with Server-Sent Events (SSE)
- **Production Server:** Gunicorn (2 workers, 120s timeout)
- **Security:** Flask-WTF (CSRF), Flask-Limiter (rate limiting), Flask-Talisman (HTTPS/CSP)
- **Session Management:** Flask sessions with encrypted SECRET_KEY

### Frontend
- **Templates:** Jinja2
- **Styling:** Custom CSS (extracted from HTML prototype)
- **JavaScript:** Vanilla JS with ReadableStream for SSE
- **Responsive:** Mobile-friendly design

### Deployment
- **Platform:** Railway.app
- **Auto-Deploy:** GitHub integration
- **Health Monitoring:** `/_health` endpoint

### Data Storage
- **Format:** JSON files
- **Location:** `data/responses/` directory
- **Persistence:** File-based (pseudonymized)

---

## 🔍 API Endpoints

### Public Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Welcome landing page |
| `/pre-questionnaire` | GET | Pre-questionnaire form |
| `/chat` | GET | Chat interface |
| `/post-questionnaire` | GET | Post-questionnaire form |
| `/thank-you` | GET | Completion page |

### API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/api/save-pre-questionnaire` | POST | Save pre-questionnaire answers |
| `/api/chat` | POST | Chat endpoint with SSE streaming |
| `/api/save-post-questionnaire` | POST | Save post-questionnaire answers |
| `/_health` | GET | Health check for monitoring |

### Chat API (SSE Streaming)

**Request:**
```json
POST /api/chat
Content-Type: application/json

{
  "message": "User message here"
}
```

**Response (SSE Stream):**
```
data: {"text": "Hello"}

data: {"text": "!"}

data: {"text": " How"}

data: {"text": " can"}

data: {"text": " I"}

data: {"text": " help"}

data: {"text": "?"}

data: {"type": "metadata", "full_text": "Hello! How can I help?", "new_state": null, "session_completed": false, "auto_continued": false}

data: [DONE]
```

---

## 👥 Team

**Authors:** Yves, Nathalie, Eileen & Jara  
**Institution:** Zurich School of Applied Sciences  
**Project Type:** Research group project for Procrastination Intervention  

---

## 📄 License

[MIT License](LICENSE)

---

## 🙏 Acknowledgments

This project builds on decades of research by:
- **Piers Steel** (Temporal Motivation Theory)
- **Carl Rogers** (Person-Centered Therapy)
- **Peter Gollwitzer** (Implementation Intentions)
- **Gabriele Oettingen** (WOOP Model)
- **Katherine Milkman** (Temptation Bundling)
- **Kristin Neff** (Self-Compassion)
- **BJ Fogg** (Behavior Model)
- **Albert Bandura** (Social Cognitive Theory)
- **James Prochaska & Carlo DiClemente** (Transtheoretical Model)

---

_With ❤️ by Yves, who had a little too much caffeine, and some spare time._
