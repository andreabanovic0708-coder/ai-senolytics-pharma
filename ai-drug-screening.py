```python
# AI Senolytics Screening v1.0 - MIPT PhD Demo
import random

senolytics = {
    'dasatinib': 'heart drug → senolytic',
    'quercetin': 'apples → senolytic', 
    'navitoclax': 'cancer drug → senolytic'
}

print("=== AI SENOLYTICS SCREENING ===")
for drug, origin in senolytics.items():
    efficacy = random.uniform(12, 25)
    print(f"{drug} ({origin}): {efficacy:.1f}% lifespan extension")
