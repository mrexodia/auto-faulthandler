#!/usr/bin/env python3
"""
Test script to verify auto-faulthandler is working.
This will cause a segfault, and you should see a traceback in stderr.
"""

import ctypes

print("About to cause a segfault...")
print("If auto-faulthandler is working, you'll see a traceback below:")
print("-" * 60)

# Cause a segfault by dereferencing a null pointer
ctypes.string_at(0)

print("This line will never be reached")
