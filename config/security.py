"""
Security configuration for the Prokrastinations-Agent.
Centralized security settings for CSRF, rate limiting, headers, etc.
"""

import os
from datetime import timedelta


# ============================================================================
# CSRF Protection Configuration
# ============================================================================

CSRF_ENABLED = True
CSRF_TIME_LIMIT = None  # No time limit for research sessions (participants may take breaks)


# ============================================================================
# Rate Limiting Configuration
# ============================================================================

# Global rate limits (per IP address)
RATE_LIMIT_STORAGE_URL = "memory://"  # Use Redis in production: "redis://localhost:6379"
RATE_LIMIT_GLOBAL = "100 per hour"

# Endpoint-specific rate limits
RATE_LIMITS = {
    "chat": "20 per hour",  # Limit Claude API calls
    "save_questionnaire": "5 per hour",  # Prevent spam submissions
    "health_check": "60 per minute",  # Monitoring can check frequently
}

# Per-session API call limits
MAX_MESSAGES_PER_SESSION = 50  # Maximum chat messages per session
MAX_TOKENS_PER_MESSAGE = 1024  # Maximum tokens per Claude API call


# ============================================================================
# Session Security Configuration
# ============================================================================

SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production'  # HTTPS only in production
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookie
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)  # Session expires after 2 hours


# ============================================================================
# Security Headers Configuration (Flask-Talisman)
# ============================================================================

# Content Security Policy
CSP = {
    'default-src': ["'self'"],
    'script-src': ["'self'", "'unsafe-inline'"],  # unsafe-inline needed for inline scripts
    'style-src': ["'self'", "'unsafe-inline'"],  # unsafe-inline needed for inline styles
    'img-src': ["'self'", 'data:'],
    'font-src': ["'self'"],
    'connect-src': ["'self'"],  # For AJAX requests
    'frame-ancestors': ["'none'"],  # Prevent clickjacking
}

# Force HTTPS in production
FORCE_HTTPS = os.getenv('FLASK_ENV') == 'production'

# Strict Transport Security (HSTS) - only in production
HSTS_ENABLED = os.getenv('FLASK_ENV') == 'production'
HSTS_MAX_AGE = 31536000  # 1 year
HSTS_INCLUDE_SUBDOMAINS = True


# ============================================================================
# Input Validation Configuration
# ============================================================================

# Chat message validation
MAX_CHAT_MESSAGE_LENGTH = 1000  # Maximum characters per message
MIN_CHAT_MESSAGE_LENGTH = 1  # Minimum characters per message

# Questionnaire validation
VALID_SCALE_VALUES = [1, 2, 3, 4, 5, 6, 7]  # Valid Likert scale values
PRE_QUESTIONNAIRE_COUNT = 7  # Expected number of pre-questionnaire questions
POST_QUESTIONNAIRE_COUNT = 12  # Expected number of post-questionnaire questions

# Request size limits
MAX_CONTENT_LENGTH = 16 * 1024  # 16 KB maximum request size


# ============================================================================
# File Security Configuration
# ============================================================================

# JSON file permissions (owner read/write only)
FILE_PERMISSIONS = 0o600  # -rw-------


# ============================================================================
# Logging Configuration
# ============================================================================

# Log security events
SECURITY_LOG_ENABLED = True
SECURITY_LOG_LEVEL = "INFO"

# Events to log
LOG_EVENTS = {
    "rate_limit_exceeded": True,
    "invalid_input": True,
    "csrf_failure": True,
    "session_created": True,
    "session_expired": True,
    "api_error": True,
    "suspicious_activity": True,
}


# ============================================================================
# API Protection Configuration
# ============================================================================

# Claude API circuit breaker
API_CIRCUIT_BREAKER_THRESHOLD = 5  # Number of failures before opening circuit
API_CIRCUIT_BREAKER_TIMEOUT = 60  # Seconds to wait before retrying

# API error handling
GENERIC_API_ERROR_MESSAGE = "Entschuldigung, es gab einen technischen Fehler. Bitte versuche es erneut."


# ============================================================================
# Development vs Production Settings
# ============================================================================

def is_production():
    """Check if running in production environment."""
    return os.getenv('FLASK_ENV') == 'production'


def get_security_config():
    """
    Returns a dictionary of security configuration settings.
    Useful for initializing Flask app.
    """
    secret_key = os.getenv('SECRET_KEY')

    # In development, allow fallback but warn
    if not secret_key and not is_production():
        import warnings
        warnings.warn(
            "SECRET_KEY not set! Using temporary key for development. "
            "Set SECRET_KEY environment variable for production!",
            UserWarning
        )
        secret_key = os.urandom(32).hex()

    return {
        # Session
        'SESSION_COOKIE_SECURE': SESSION_COOKIE_SECURE,
        'SESSION_COOKIE_HTTPONLY': SESSION_COOKIE_HTTPONLY,
        'SESSION_COOKIE_SAMESITE': SESSION_COOKIE_SAMESITE,
        'PERMANENT_SESSION_LIFETIME': PERMANENT_SESSION_LIFETIME,

        # Request
        'MAX_CONTENT_LENGTH': MAX_CONTENT_LENGTH,

        # CSRF
        'WTF_CSRF_ENABLED': CSRF_ENABLED,
        'WTF_CSRF_TIME_LIMIT': CSRF_TIME_LIMIT,

        # Security
        'SECRET_KEY': secret_key,
    }
