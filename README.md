# Procrastination Intervention Agent

An evidence-based AI-powered conversational agent for procrastination intervention, built on Claude by Anthropic.

**Version:** 3.0 (Flask + Security Hardening + Streaming)
**Tech Stack:** Python 3.11, Flask, Anthropic Claude API (Sonnet 4.5), Gunicorn, Railway
**Research Team:** Yves, Nathalie, Eileen & Jara
**Institution:** Zurich School of Applied Sciences

---

## 🎯 Project Overview

This research MVP provides evidence-based psychological intervention for procrastination through a structured 4-phase conversational flow. The agent combines insights from **clinical psychology**, **behavioral economics**, and **cognitive science** to deliver personalized strategies.

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

This agent is built on **decades of peer-reviewed research** across multiple disciplines:

### Procrastination Psychology (Steel, 2007)
- **Meta-analysis of 691 correlations** validating 7 procrastination factors
- Temporal Motivation Theory (TMT) framework
- Conscientiousness correlation: **r = -0.62** (strong effect)

### Therapeutic Approach
- **Person-Centered Therapy** (Carl Rogers) - Unconditional positive regard, empathy, congruence
- **Motivational Interviewing** - Meta-analysis shows **OR: 1.55** vs. traditional advice-giving
- **Self-Determination Theory** - Autonomy support predicts sustained behavior change

### Evidence-Based Interventions
- **Implementation Intentions** (Gollwitzer) - Effect size **d = .65** (medium-large)
- **WOOP Model** (Oettingen) - **2x improvement** in physical activity
- **Temptation Bundling** (Milkman) - **10-14% increase** in gym attendance
- **Self-Compassion** (Neff) - Meta-analysis of **94 studies**
- **Task Chunking** - Cognitive Load Theory, Zeigarnik Effect
- **Pomodoro Technique** - **25-35% productivity improvement** (32 studies, N=5,270)

### Conversation Design
- **Fogg Behavior Model** - Motivation + Ability + Prompt
- **Transtheoretical Model** - Stage-matched intervention (Prochaska & DiClemente)
- **Cognitive Load Management** - One question at a time, worked examples
- **Observational Learning** (Bandura) - Concrete strategy examples

📖 **[Read Full Scientific Documentation](docs/psychological-foundations.md)** - Comprehensive evidence base with citations

---

## 📊 The Seven Procrastination Factors

Based on **Piers Steel's Temporal Motivation Theory** (2007 meta-analysis):

1. **Perfectionism** - Fear of mistakes, unrealistically high standards
2. **Task Aversion** - Unpleasant, boring, or frustrating tasks (r = 0.40 correlation)
3. **Overwhelm** - Tasks feel too big or complex (cognitive load)
4. **Deadline Problems** - Too much time, lack of urgency (hyperbolic discounting)
5. **Lack of Clarity** - Unclear how/where to start (analysis paralysis)
6. **Emotional Dysregulation** - Avoidance of negative feelings (short-term mood repair)
7. **Self-Efficacy Doubts** - Doubts about own abilities (Bandura)

Each factor is addressed with **matched, evidence-based intervention strategies**.

---

## 🔬 Evidence-Based Intervention Strategies

| Procrastination Factor | Intervention Strategy | Research Support |
|------------------------|----------------------|------------------|
| **Perfectionism** | "Good Enough" Mindset, Timeboxing | Simon (Satisficing), HBR #1 productivity hack |
| **Task Aversion** | Temptation Bundling, 2-Minute Rule | Milkman (10-14% improvement), Fogg (3x maintenance) |
| **Overwhelm** | Task Chunking, Pomodoro, Micro-Goals | Cognitive Load Theory, 25-35% productivity gain |
| **Deadline Problems** | Artificial Deadlines, Accountability | Ariely & Wertenbroch, temporal discounting research |
| **Lack of Clarity** | 5-Minute Clarity Session, Question Lists | Analysis paralysis research, decision-making studies |
| **Emotional Dysregulation** | Emotion Labeling, Self-Compassion | Neff (94-study meta-analysis), ER training (medium effect) |
| **Self-Efficacy Doubts** | Success Journal, Past-Wins List | Bandura's Social Cognitive Theory |

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

### Phase 1: INTAKE (Assessment)
**Goal:** Understand the procrastinated task
**Approach:** Empathetic, one question at a time (Cognitive Load Management)
**Collects:** Task description, deadline, emotional load (1-10), attempted solutions

**Evidence Base:** Rogers' therapeutic assessment, Motivational Interviewing rapport-building

---

### Phase 2: HYPOTHESES (Collaborative Formulation)
**Goal:** Identify psychological causes collaboratively
**Approach:** 2-3 specific, evidence-based hypotheses with supporting evidence
**Validation:** User confirms which hypotheses resonate (MI principle)

**Evidence Base:** Steel's 7 procrastination factors, validation before intervention (SDT autonomy support)

---

### Phase 3: STRATEGIES (Intervention Planning)
**Goal:** Provide matched, actionable strategies
**Approach:** 2-3 concrete strategies directly addressing validated hypotheses
**Format:** What + How (step-by-step) + Why it works

**Evidence Base:** Implementation Intentions (Gollwitzer d=.65), WOOP Model, observational learning

---

### Phase 4: COMPLETION (Consolidation & Next Steps)
**Goal:** Reinforce learning and build confidence
**Approach:** Summarize (mental contrasting), provide smallest next step, encourage
**Outcome:** User feels understood, equipped, and motivated

**Evidence Base:** Relapse prevention, self-efficacy building (Bandura), WOOP conclusion

---

### ✨ Auto-Continuation Feature

**UX Innovation:** When transitioning between states, the agent **automatically generates a continuation message** in the new state, creating seamless conversational flow without requiring user input.

**Before:**
```
Agent: "I have enough information. Let me develop hypotheses..."
[TRANSITION] *User must type something* ❌
```

**After:**
```
Agent: "I have enough information. Let me develop hypotheses..."
[AUTOMATIC CONTINUATION]
Agent: "I see a few patterns here. Hypothesis 1: ..." ✅
```

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
SECRET_KEY=<generate-with-python>
```

**Generate SECRET_KEY:**
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
    └── psychological-foundations.md  # Scientific documentation
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

### GitHub Auto-Deploy (Recommended)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select repository
4. Set environment variables in Railway dashboard
5. Generate domain
6. 🎉 Auto-deploys on every push to main!

**Deployment files:**
- `nixpacks.toml` - Defines Gunicorn start command
- `.railwayignore` - Excludes unnecessary files

---

## 📖 Documentation

### For Developers
- **[CLAUDE.md](CLAUDE.md)** - Technical documentation, architecture, API endpoints
- **[FRAMEWORK_COMPARISON.md](FRAMEWORK_COMPARISON.md)** - Streamlit vs. Flask comparison
- **[FLASK_MIGRATION_COMPLETE.md](FLASK_MIGRATION_COMPLETE.md)** - Migration guide
- **[RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)** - Deployment guide
- **[STREAMING_RAILWAY_IMPLEMENTATION.md](STREAMING_RAILWAY_IMPLEMENTATION.md)** - SSE implementation details

### For Researchers
- **[docs/psychological-foundations.md](docs/psychological-foundations.md)** - Scientific evidence base, citations, research support

### For Users
- **[README.de.md](README.de.md)** - German version of this README

---

## 🎓 Scientific Credibility

### Research Validation

This agent's design is supported by:
- **50+ peer-reviewed studies** across clinical psychology, behavioral economics, and cognitive science
- **Multiple meta-analyses** (Steel: 691 correlations; Gollwitzer: 94 studies; Neff: 94 studies)
- **Randomized controlled trials** (Milkman, Oettingen, etc.)
- **Well-validated theories** (TMT, SDT, Social Cognitive Theory, Cognitive Load Theory)

### Key Research Citations

**Procrastination Psychology:**
- Steel, P. (2007). The nature of procrastination: A meta-analytic and theoretical review. *Psychological Bulletin*, 133(1), 65-94.

**Intervention Effectiveness:**
- Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement. *Advances in Experimental Social Psychology*, 38, 69-119. [d = .65]
- Rubak, S., et al. (2005). Motivational interviewing: A systematic review and meta-analysis. *British Journal of General Practice*, 55(513), 305-312. [OR: 1.55]

**Therapeutic Alliance:**
- Rogers, C. (1957). The necessary and sufficient conditions of therapeutic personality change. *Journal of Consulting Psychology*, 21(2), 95-103.

**Behavior Change:**
- Fogg, B. J. (2009). A behavior model for persuasive design. *Persuasive Technology*, 40.

📖 **[Full References in Scientific Documentation](docs/psychological-foundations.md#7-references)**

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
**Project Type:** Research MVP for Procrastination Intervention

---

## 📄 License

MIT License

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

## 📞 Contact

For research inquiries or collaboration opportunities, please contact the research team at Zurich School of Applied Sciences.

---

_With ❤️ by Yves, who had a little too much caffeine, and some spare time._

**🔗 [German Version / Deutsche Version](README.de.md)**