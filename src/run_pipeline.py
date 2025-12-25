import subprocess
import sys

scripts = [
    "data_prep.py",
    "features.py",
    "train.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error running {script}")
        break

print("\nPipeline finished.")
