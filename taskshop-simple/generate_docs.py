import subprocess
import os

os.makedirs("docs/pdoc", exist_ok=True)
subprocess.run(["pdoc", "src/taskshop", "-o", "docs/pdoc"])
print("✅ Documentación generada en docs/pdoc/")