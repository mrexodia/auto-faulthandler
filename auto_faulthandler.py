"""
auto-faulthandler: Automatically enable Python's faulthandler for development.

This module is automatically imported via a .pth file and enables faulthandler
to dump tracebacks to stderr on crashes (segfaults, bus errors, etc.).
"""

import os
import sys

# Allow disabling via environment variable
if not os.environ.get("AUTO_FAULTHANDLER_DISABLE"):
    try:
        # Enable faulthandler with all threads
        import faulthandler

        faulthandler.enable(file=sys.stderr, all_threads=True)
    except Exception:
        # Silently fail if something goes wrong
        pass
