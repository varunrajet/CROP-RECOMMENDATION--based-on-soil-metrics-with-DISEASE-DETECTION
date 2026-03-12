import os

# Read accuracy from metrics file
with open("reports/metrics.txt") as f:
    content = f.read()

accuracy = float(content.split(":")[1].strip())

print("Model accuracy:", accuracy)

# Threshold check
threshold = 0.90

if accuracy < threshold:
    print("WARNING: Model accuracy below threshold!")

    # Create issue message
    issue_text = f"""
Model performance dropped.

Accuracy: {accuracy}

Threshold: {threshold}

Action Required:
Review dataset or retrain model.
"""

    with open("reports/issue.txt", "w") as f:
        f.write(issue_text)

else:
    print("Model performance is acceptable.")