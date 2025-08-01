import os, requests, sys, time

VERSION = "1.0.0"
UPDATE_URL = "https://raw.githubusercontent.com/AsiMglobal/AsiMglobal/main/asim_core.py"

def check_for_updates():
    try:
        r = requests.get(UPDATE_URL)
        if r.status_code == 200:
            new_code = r.text
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(new_code)
            print("Updated to latest version!")
            os.execv(sys.executable, ['python'] + sys.argv)
    except Exception as e:
        print("Update check failed:", e)

def asim_ai():
    print("🚀 AsiM AI Core Activated: Version", VERSION)
    while True:
        cmd = input("Command: ")
        if cmd.lower() in ["exit", "quit"]:
            break
        print("Processing:", cmd)
        time.sleep(1)
        print("✅ Done!")

if __name__ == "__main__":
    check_for_updates()
    asim_ai()
