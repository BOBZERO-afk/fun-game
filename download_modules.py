import subprocess
import sys
from pathlib import Path

# Path to needs.txt (same directory as this script)
BASE_DIR = Path(__file__).resolve().parent
NEEDS_FILE = BASE_DIR / "needs.txt"

def read_needs():
    if not NEEDS_FILE.exists():
        print("needs.txt not found:", NEEDS_FILE)
        sys.exit(1)

    modules = []
    with NEEDS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # ignore empty lines
                continue
            modules.append(line)
    return modules

def install_missing(modules):
    for module in modules:
        try:
            __import__(module)
            print(f"[OK] {module}")
        except ImportError:
            print(f"[MISSING] {module} — installing...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", module
            ])

def main():
    modules = read_needs()
    if not modules:
        print("No modules listed in needs.txt")
        return

    install_missing(modules)
    print("All required modules are installed.")

if __name__ == "__main__":
    main()
