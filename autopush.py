import os
import time
import datetime
import subprocess

def update_file():
    os.system("sourcedefender encrypt ../main_run.py")
    os.system("mv ../main_run.pye .")

def git_commit_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-update: {datetime.datetime.now()}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}")

if __name__ == "__main__":
   update_file()
   git_commit_push()
