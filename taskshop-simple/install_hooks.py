#!/usr/bin/env python3
"""Instalar hooks pre-commit simple."""
import os

hook = '''#!/bin/bash
python tests/test_basic.py
python todo_en_uno.py --help
'''

with open(".git/hooks/pre-commit", "w") as f:
    f.write(hook)

print("Hook instalado. Se ejecutaran tests antes de commit.")