"""
Task 2 - Version A (Initial AI-generated version)
Scholarship eligibility checker based on academic score, family income, and location.
"""

def check_eligibility(score, income, location):
    if location.lower() == "urban":
        if score >= 75 and income <= 300000:
            return "Eligible"
        else:
            return "Not Eligible"
    else:  # rural / other
        if score >= 85 and income <= 200000:
            return "Eligible"
        else:
            return "Not Eligible"


if __name__ == "__main__":
    print(check_eligibility(80, 250000, "Urban"))   # Eligible
    print(check_eligibility(80, 250000, "Rural"))   # Not Eligible (stricter score cutoff)
