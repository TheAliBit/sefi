# For Django 3.2+ only, add this to settings.py
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Theme customization
ADMIN_INTERFACE_CONFIG = {
    'TITLE': 'My Admin Site',
    'FAVICON': 'path/to/favicon',
    'LOGO': 'path/to/logo',
    'MAIN_BG_COLOR': '#2a3547',
    'MAIN_HOVER_COLOR': '#3a4b5f',
    'SHOW_THEMES': True,
    'SHOW_COUNTS': True,
    'LIST_FILTER_HIGHLIGHT': True,
}
