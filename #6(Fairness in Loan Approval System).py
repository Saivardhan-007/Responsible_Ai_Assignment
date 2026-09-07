"""Fairness-aware loan approval example.

The first model intentionally demonstrates why sensitive attributes must not
influence lending decisions.  The revised model uses only relevant financial
information.
"""


def biased_decision(applicant):
	"""An unsafe example: gender, race, and religion affect the outcome."""
	score = 0
	score += applicant["credit_score"] >= 650
	score += applicant["income"] >= 40000
	score += applicant["employment_status"] == "employed"
	score += applicant["loan_amount"] <= applicant["income"] * 3

	# These rules are discriminatory and are included only to expose the risk.
	if applicant["gender"] == "female":
		score -= 1
	if applicant["race"] == "minority":
		score -= 1
	if applicant["religion"] == "minority_religion":
		score -= 1
	return "Approved" if score >= 3 else "Rejected"


def fair_decision(applicant):
	"""Approve using financial capacity and credit history only."""
	score = 0
	score += applicant["credit_score"] >= 650
	score += applicant["income"] >= 40000
	score += applicant["employment_status"] == "employed"
	score += applicant["loan_amount"] <= applicant["income"] * 3
	return "Approved" if score >= 3 else "Rejected"


def main():
	applicants = [
		{"name": "Alex", "income": 50000, "age": 35, "employment_status": "employed",
		 "credit_score": 700, "loan_amount": 100000, "gender": "male",
		 "religion": "religion_a", "race": "majority"},
		{"name": "Sam", "income": 50000, "age": 35, "employment_status": "employed",
		 "credit_score": 700, "loan_amount": 100000, "gender": "female",
		 "religion": "minority_religion", "race": "minority"},
		{"name": "Jordan", "income": 30000, "age": 29, "employment_status": "employed",
		 "credit_score": 620, "loan_amount": 60000, "gender": "nonbinary",
		 "religion": "religion_a", "race": "majority"},
	]

	print("FAIRNESS AND LOAN APPROVAL ANALYSIS")
	print("\nRisks identified:")
	print("- Sensitive attributes can create disparate treatment and proxy discrimination.")
	print("- Biased historical training data can reproduce past lending inequality.")
	print("- Unrelated attributes reduce transparency and may violate lending rules.")
	print("\nExample: Alex and Sam have identical financial information, but the biased")
	print("rules may reject Sam because of gender, race, or religion.")
	print("\nDecisions:")
	for applicant in applicants:
		print(f"{applicant['name']}: biased={biased_decision(applicant)}, "
			  f"fair={fair_decision(applicant)}")
	print("\nThe revised system ignores gender, religion, race, and age. It considers")
	print("only income, employment, credit score, and loan affordability, making")
	print("the decision more relevant, explainable, and consistent across applicants.")


if __name__ == "__main__":
	main()
