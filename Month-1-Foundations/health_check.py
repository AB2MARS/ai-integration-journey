import sys
import platform
import datetime

def run_diagnostics():
    print(f"--- 🚀 AI AGENT HEALTH CHECK | {datetime.date.today()} ---")
    
    # Check Python version
    version = sys.version.split()[0]
    print(f"PYTHON VERSION: {version}")
    
    # Check OS
    system = platform.system()
    print(f"OPERATING SYSTEM: {system}")
    
    # Integration logic simulation
    if float(version[:4]) >= 3.10:
        print("STATUS: Environment is COMPATIBLE.")
    else:
        print("STATUS: Environment WARNING - Version below 3.10")
    
    print("------------------------------------------")

if __name__ == "__main__":
    run_diagnostics()