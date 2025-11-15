# Prokrastinations-Interventions-Agent - Technical Documentation

**Project:** Prokrastinations-Interventions-Agent (Research MVP)
**Version:** 3.0 (Flask + Streaming)
**Tech Stack:** Python 3.11, Flask, Anthropic Claude API (Sonnet 4.5), Gunicorn, Railway
**Authors:** Yves, Nathalie, Eileen & Jara
**Institution:** Zurich School of Applied Sciences

---

## 📋 Project Overview

A conversational AI agent that helps people understand and overcome procrastination through a structured therapeutic conversation.

### User Flow (5 Screens)

1. **WELCOME** - Landing page with project information and privacy notice
2. **PRE-QUESTIONNAIRE** - 7 baseline questions (1-7 Likert scale)
3. **CHAT** - Conversational AI intervention with 4 phases
4. **POST-QUESTIONNAIRE** - 12 questions (7 repeated + 5 evaluation)
5. **THANK YOU** - Completion message with data information

### Chat State Machine (4 Phases)

```
INTAKE → HYPOTHESES → STRATEGIES → COMPLETION
```

1. **INTAKE**: Gathers information about the procrastinated task
2. **HYPOTHESES**: Develops psychologically-grounded hypotheses about causes
3. **STRATEGIES**: Provides evidence-based intervention strategies
4. **COMPLETION**: Wraps up with encouragement and next steps

---

## 🏗️ Architecture

### Tech Stack

- **Backend:** Flask (Python 3.11)
- **Frontend:** Jinja2 templates with vanilla JavaScript
- **AI:** Anthropic Claude API with Server-Sent Events (SSE) streaming
- **Production Server:** Gunicorn (2 workers, 120s timeout)
- **Deployment:** Railway.app (Nixpacks auto-detection)
- **Data Storage:** JSON files (pseudonymized session data)
- **Session Management:** Flask sessions with environment-based secret key

### Application Structure

```
procrastination_agent/
├── app_flask.py              # Main Flask application (production)
├── templates/                # Jinja2 HTML templates
│   ├── base.html            # Base template with CSS imports
│   ├── welcome.html         # Landing page
│   ├── pre_questionnaire.html  # Pre-questionnaire with scale selectors
│   ├── chat.html            # Chat interface with SSE streaming
│   ├── post_questionnaire.html # Post-questionnaire
│   └── thank_you.html       # Completion page
├── static/
│   └── css/
│       └── styles.css       # Complete CSS from HTML prototype
├── config/
│   └── questions.py         # Questionnaire definitions
├── utils/
│   ├── storage.py          # JSON data persistence
│   └── session.py          # Session management utilities
├── data/
│   └── responses/          # JSON session files (*.json)
├── nixpacks.toml           # Railway build configuration
├── .railwayignore          # Deployment exclusions
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (local, gitignored)
└── CLAUDE.md              # This file
```

---

## 🎯 Key Features

### 1. Real-Time Streaming (SSE)

**Implementation:**
- Claude API streaming via `client.messages.stream()`
- Server-Sent Events (SSE) for incremental text delivery
- Text appears word-by-word as Claude generates responses
- Provides ChatGPT-like user experience

**Technical Details:**
- Backend: Generator function yields SSE-formatted chunks
- Frontend: JavaScript `ReadableStream` reader
- Format: `data: {"text": "chunk"}\n\n`
- Metadata event at end: `data: {"type": "metadata", ...}\n\n`

**Code Location:**
- Backend: `app_flask.py` lines 312-403 (`/api/chat` endpoint)
- Frontend: `templates/chat.html` lines 99-208 (event handler)

### 2. State Machine Logic

**How It Works:**
1. Agent decides when to transition between states
2. Signals transitions with marker: `[TRANSITION:state_name]`
3. `check_for_state_transition()` detects and removes marker
4. State stored in Flask session, persists across requests

**Transition Rules:**
- **Intake → Hypotheses:** After collecting all 4 key pieces of information
- **Hypotheses → Strategies:** After user validates one or more hypotheses
- **Strategies → Completion:** After user confirms they have a good plan
- **Completion:** No further transitions (final state)

**Interaction Counter:**
- Tracks exchanges in `strategies` state
- Prevents endless loops
- Agent automatically prompts satisfaction check after 2-3 exchanges
- Counter sent to Claude as part of system prompt

**Code Location:**
- State transitions: `app_flask.py` lines 209-215, 367-396
- System prompts: `app_flask.py` lines 44-174
- Counter logic: `app_flask.py` lines 329-331, 381-382

### 3. Session & Data Management

**Session Tracking:**
- UUID generated on first visit
- Stored in Flask session (encrypted with SECRET_KEY)
- Links questionnaire data and chat messages

**Data Persistence:**
- Pre-questionnaire → `data/responses/{session_id}.json`
- Post-questionnaire → Appends to same JSON file
- Chat completion timestamp marked in JSON
- All data pseudonymized (no personal information)

**JSON Structure:**
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

**Code Location:**
- Storage utilities: `utils/storage.py`
- Session management: `utils/session.py`
- API endpoints: `app_flask.py` lines 263-430

---

## 🔬 Psychological Framework

### Procrastination Factors (Used in Hypotheses)

1. **Perfectionism** - Fear of mistakes, unrealistic standards
2. **Task Aversion** - Task is unpleasant, boring, frustrating
3. **Overwhelm** - Task seems too big or complex
4. **Deadline Problem** - Too much time, lack of urgency
5. **Lack of Clarity** - Unclear how/where to start
6. **Emotional Dysregulation** - Avoidance of negative feelings
7. **Self-Efficacy Doubts** - Doubts about own abilities

### Evidence-Based Strategies (Used in Intervention)

- **Perfectionism** → "Good Enough" mindset, Timeboxing, Prototyping
- **Task Aversion** → Temptation Bundling, 2-Minute Rule
- **Overwhelm** → Task Chunking, Pomodoro Technique, Micro-Goals
- **Deadline Problem** → Artificial deadlines, Accountability partners
- **Lack of Clarity** → 5-minute clarity session, Question lists
- **Emotional Dysregulation** → Emotion labeling, Self-compassion
- **Self-Efficacy Doubts** → Success journal, Past-wins list

**Code Location:**
- System prompts: `app_flask.py` lines 88-163

---

## 🚀 Running the Application

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# Run Flask development server
python3 app_flask.py

# Open browser
open http://localhost:8501
```

### Local Testing with Production Server

```bash
# Test with Gunicorn (what Railway uses)
gunicorn app_flask:app --bind 0.0.0.0:8501 --workers 2 --timeout 120

# Open browser
open http://localhost:8501
```

### Environment Variables

Required:
- `ANTHROPIC_API_KEY` - Claude API key (sk-ant-...)
- `SECRET_KEY` - Flask session encryption (generate with `python -c "import os; print(os.urandom(24).hex())"`)

Optional:
- `PORT` - Server port (default: 8501, auto-set by Railway)

---

## 🚂 Deployment (Railway)

### Quick Deploy

```bash
# Install Railway CLI
brew install railway

# Login and initialize
railway login
railway init

# Set secrets
railway variables set ANTHROPIC_API_KEY=sk-ant-...
railway variables set SECRET_KEY=your-generated-key

# Deploy
railway up

# Get URL
railway domain
```

### GitHub Auto-Deploy (Recommended)

1. Push code to GitHub
2. Go to railway.app → New Project → Deploy from GitHub
3. Select repository
4. Set environment variables in Railway dashboard
5. Generate domain
6. Auto-deploys on every push to main!

**Deployment Configuration:**
- `nixpacks.toml` - Defines Gunicorn start command
- `.railwayignore` - Excludes unnecessary files
- See `RAILWAY_DEPLOYMENT.md` for full guide

---

## 📡 API Endpoints

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

data: {"type": "metadata", "full_text": "Hello! How can I help?", "new_state": null, "session_completed": false}

data: [DONE]
```

**Error Response:**
```
data: {"type": "error", "message": "Error description"}
```

---

## 🎨 Frontend Implementation

### CSS Architecture

All styles extracted from HTML prototype into `static/css/styles.css`:

- **CSS Variables:** Color palette, spacing, typography
- **Components:** Cards, buttons, forms, scale selectors
- **Chat:** Sidebar timeline, message bubbles, input
- **Responsive:** Mobile-friendly breakpoints

**Key CSS Classes:**
- `.landing-card` - White cards on purple background
- `.info-box` - Gradient info boxes
- `.primary-btn` - Gradient buttons with lift effect
- `.scale-option` - Questionnaire scale buttons (1-7)
- `.chat-message` - Chat message bubbles
- `.timeline-dot` - Sidebar phase indicators

### JavaScript Functionality

**Pre/Post Questionnaires:**
- Scale button selection (1-7)
- Progress counter
- Form validation (all questions required)
- JSON submission to API

**Chat Interface:**
- SSE stream reading with `ReadableStream`
- Incremental text rendering
- Auto-scrolling
- State transition handling
- Error recovery

**Code Locations:**
- Questionnaires: `templates/*_questionnaire.html` (bottom script tags)
- Chat streaming: `templates/chat.html` lines 99-208

---

## 🔧 Key Functions Reference

### Backend (`app_flask.py`)

**Session Management:**
- `get_or_create_session_id()` - Get/create UUID session ID
- `initialize_chat_session()` - Initialize chat state variables

**State Machine:**
- `check_for_state_transition(message)` - Detect `[TRANSITION:...]` markers
- Returns: `(cleaned_message, new_state)`

**Chat Endpoint:**
- `chat_api()` - Main streaming endpoint (lines 312-403)
- Generator function yields SSE chunks
- Handles state transitions
- Updates Flask session

**Storage (`utils/storage.py`):**
- `save_pre_questionnaire(session_id, answers)` - Save pre-Q data
- `save_post_questionnaire(session_id, answers)` - Save post-Q data
- `mark_chat_complete(session_id)` - Mark chat completion timestamp
- `get_session_status(session_id)` - Check completion status

---

## 🧪 Testing Checklist

### Full Flow Test

- [ ] Welcome page loads with gradient icon
- [ ] Info boxes show correct colors (not white text on white)
- [ ] Button navigates to pre-questionnaire
- [ ] Scale buttons (1-7) are clickable and turn purple when selected
- [ ] Progress counter updates as questions answered
- [ ] Submit button enables when all questions answered
- [ ] Data saves to `data/responses/{uuid}.json`
- [ ] Chat page loads with sidebar timeline
- [ ] Welcome message appears
- [ ] **Type message and see text stream word-by-word** ✨
- [ ] Timeline dots update as states progress
- [ ] State transitions work (intake → hypotheses → strategies → completion)
- [ ] Auto-redirect to post-questionnaire after completion
- [ ] Post-questionnaire saves to same JSON file
- [ ] Thank you page displays

### Health Check

```bash
curl http://localhost:8501/_health
```

Expected:
```json
{
  "status": "healthy",
  "service": "procrastination-agent",
  "version": "2.0-flask"
}
```

---

## 🐛 Common Issues & Solutions

### Issue: Streaming Not Working

**Symptoms:** Text appears all at once instead of word-by-word

**Check:**
1. Browser console for JavaScript errors
2. Network tab shows `text/event-stream` content type
3. Flask endpoint returns `Response(generate(), ...)` not `jsonify()`

**Fix:**
- Ensure chat.html uses `response.body.getReader()` (not `.json()`)
- Check backend yields SSE format: `data: {...}\n\n`

### Issue: Session Lost After Restart

**Symptoms:** Users logged out, chat history gone

**Cause:** SECRET_KEY changes if using `os.urandom(24)`

**Fix:**
- Set `SECRET_KEY` environment variable
- Already implemented: `app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))`

### Issue: Claude API Timeout

**Symptoms:** 502 errors, stream cuts off

**Fix:**
- Increase Gunicorn timeout (already 120s in nixpacks.toml)
- Check ANTHROPIC_API_KEY is valid
- Check Railway logs for specific API errors

---

## 📊 Performance & Scaling

### Current Configuration

- **Workers:** 2 (optimal for SSE connections)
- **Timeout:** 120 seconds (handles slow Claude responses)
- **Port:** Dynamic (`$PORT` from Railway)

### Why 2 Workers?

SSE requires persistent connections. Too many workers can cause:
- Connection blocking
- Resource exhaustion
- Streaming reliability issues

2 workers balance concurrency and reliability.

### Scaling Options

If more capacity needed:
1. Increase to 4 workers (test streaming still works)
2. Add Railway Redis for distributed sessions
3. Add Railway PostgreSQL for data persistence
4. Implement connection pooling

---

## 📁 Important Files

**Core Application:**
- `app_flask.py` - Main Flask app (450+ lines)
- `templates/*.html` - 6 HTML templates
- `static/css/styles.css` - Complete CSS (400+ lines)

**Configuration:**
- `config/questions.py` - Pre/post questionnaire definitions
- `nixpacks.toml` - Railway build config
- `.env` - Local environment variables (gitignored)
- `requirements.txt` - Python dependencies

**Utilities:**
- `utils/storage.py` - JSON data persistence
- `utils/session.py` - Session management

**Documentation:**
- `CLAUDE.md` - This file (technical docs)
- `RAILWAY_DEPLOYMENT.md` - Deployment guide
- `STREAMING_RAILWAY_IMPLEMENTATION.md` - Implementation details
- `README.md` - User-facing documentation

---

## 🔒 Security Considerations

**Implemented:**
- ✅ SECRET_KEY from environment variable (not hardcoded)
- ✅ `.env` in `.gitignore` (no secrets in Git)
- ✅ HTTPS only on Railway (automatic)
- ✅ Session encryption with Flask's built-in crypto
- ✅ Pseudonymized data (no personal information)

**Best Practices:**
- Use strong SECRET_KEY (24+ bytes random)
- Rotate API keys periodically
- Monitor logs for suspicious activity
- Limit worker count to prevent DoS

---

## 📈 Future Enhancement Ideas

### Short-term
- [ ] Add loading spinner during stream
- [ ] Implement retry logic for failed API calls
- [ ] Add "Export conversation" button in completion state
- [ ] Email summary to participants (optional)

### Medium-term
- [ ] Migrate to PostgreSQL for data (Railway add-on)
- [ ] Add admin dashboard for data analysis
- [ ] Implement rate limiting per session
- [ ] Add support for multiple languages

### Long-term
- [ ] A/B test different prompting strategies
- [ ] Machine learning for hypothesis prediction
- [ ] Integration with calendar apps
- [ ] Follow-up messages after 1 week

---

## 🛠️ Development Workflow

### Making Changes

1. **Edit code locally**
2. **Test with Flask dev server:** `python3 app_flask.py`
3. **Test with Gunicorn:** `gunicorn app_flask:app --bind 0.0.0.0:8501 --workers 2`
4. **Commit and push:** Git commands
5. **Auto-deploy to Railway** (if GitHub integration enabled)

### Debugging

**View logs locally:**
```bash
# Flask dev server shows logs in terminal
python3 app_flask.py
```

**View logs on Railway:**
```bash
railway logs
railway logs --follow  # Live tail
```

**Check health:**
```bash
# Local
curl http://localhost:8501/_health

# Production
curl https://your-app.up.railway.app/_health
```

---

## 🎓 Research Data

### Data Collection

**Stored in:** `data/responses/{session_id}.json`

**Contents:**
- Session ID (UUID)
- Timestamps (created, completed)
- Pre-questionnaire answers (7 questions, 1-7 scale)
- Post-questionnaire answers (12 questions, 1-7 scale)

**Privacy:**
- Pseudonymized (UUID, no names/emails)
- No chat transcripts stored (privacy by design)
- No IP addresses or tracking

### Data Analysis

Export all sessions:
```python
from utils.storage import get_all_session_data
import json

sessions = get_all_session_data()
with open('export.json', 'w') as f:
    json.dump(sessions, f, indent=2)
```

Or access directly:
```bash
ls data/responses/
cat data/responses/{session-id}.json | python -m json.tool
```

---

## 📞 Quick Reference

### Start Development
```bash
python3 app_flask.py
# → http://localhost:8501
```

### Deploy to Railway
```bash
railway up
railway domain
railway logs
```

### Generate Secret Key
```bash
python -c "import os; print(os.urandom(24).hex())"
```

### Check Health
```bash
curl http://localhost:8501/_health
```

### View Session Data
```bash
ls data/responses/
cat data/responses/*.json | python -m json.tool
```

---

## 💡 Tips for Future Development

1. **Always test streaming locally** before deploying
2. **Monitor Railway logs** after deployment
3. **Keep worker count at 2-4** for SSE reliability
4. **Use environment variables** for all secrets
5. **Test full flow** (welcome → post-questionnaire) before sharing with participants
6. **Back up session data** regularly (copy `data/responses/` folder)
7. **Check `/_health`** endpoint for uptime monitoring

---

## 🎉 Success Metrics

**Technical:**
- ✅ Real-time streaming (word-by-word text)
- ✅ State machine reliability (no loops)
- ✅ Data persistence (JSON storage)
- ✅ Production server (Gunicorn)
- ✅ Health monitoring (endpoint)

**User Experience:**
- ✅ Perfect UI (matches HTML prototype)
- ✅ Fast perceived response time (streaming)
- ✅ Smooth transitions (no page reloads in chat)
- ✅ Mobile-friendly (responsive CSS)

**Research:**
- ✅ Pre/post questionnaire data collection
- ✅ Pseudonymized storage
- ✅ Easy data export for analysis

---

**Version:** 3.0 (Flask + Streaming)
**Last Updated:** November 2025
**Maintainers:** Yves, Nathalie, Eileen & Jara

**Tech Stack Summary:**
Python 3.11 | Flask | Claude Sonnet 4.5 | Server-Sent Events | Gunicorn | Railway | Jinja2 | Vanilla JS

🚀 **Ready for production research deployment!**
