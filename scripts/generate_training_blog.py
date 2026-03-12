import datetime

# Read metrics
with open("reports/metrics.txt") as f:
    metrics = f.read()

# Create blog content
blog = f"""
# Crop Recommendation Model Training Report

Date: {datetime.date.today()}

## Model
Random Forest Classifier

## Features
- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH_Value

## Results
{metrics}

## Pipeline
This report was automatically generated using a GitHub CI/CD pipeline.
"""

# Save blog
with open("blogs/training_report.md", "w") as f:
    f.write(blog)

print("Training blog generated")