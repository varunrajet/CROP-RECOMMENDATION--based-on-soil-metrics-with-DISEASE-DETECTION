import subprocess
import datetime

# Get latest commit info
commit_msg = subprocess.check_output(
    ["git", "log", "-1", "--pretty=%B"]
).decode().strip()

files_changed = subprocess.check_output(
    ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"]
).decode().strip()

date = datetime.datetime.now().strftime("%Y-%m-%d")

blog = f"""
# Project Update - {date}

## Commit Summary
{commit_msg}

## Files Changed
{files_changed}

## Pipeline Update
The CI/CD pipeline executed successfully and the model training workflow was triggered.

## Impact
This update improves the crop recommendation AI pipeline.
"""

file_path = f"blogs/update-{date}.md"

with open(file_path, "w") as f:
    f.write(blog)

print("Blog generated:", file_path)