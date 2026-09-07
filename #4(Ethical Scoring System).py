"""Task 4: Transparent and ethical employee performance scoring.

The system uses only job-relevant, employee-controlled measures.  Scores are
normalised to 0-100 and the weights are published before evaluation.
"""


WEIGHTS = {
	"project_completion": 0.40,
	"teamwork": 0.35,
	"attendance": 0.25,
}


def _validate_score(name, value):
	"""Return a numeric score, rejecting missing or out-of-range values."""
	if isinstance(value, bool) or not isinstance(value, (int, float)):
		raise ValueError(f"{name} must be a number from 0 to 100")
	if not 0 <= value <= 100:
		raise ValueError(f"{name} must be a number from 0 to 100")
	return float(value)


def evaluate_employee(project_completion, teamwork, attendance):
	"""Calculate a weighted score and an interpretable performance band."""
	scores = {
		"project_completion": _validate_score(
			"project_completion", project_completion
		),
		"teamwork": _validate_score("teamwork", teamwork),
		"attendance": _validate_score("attendance", attendance),
	}
	total = sum(scores[key] * WEIGHTS[key] for key in WEIGHTS)

	if total >= 90:
		band = "Outstanding"
	elif total >= 75:
		band = "Strong"
	elif total >= 60:
		band = "Developing"
	else:
		band = "Needs support"

	return {"score": round(total, 2), "band": band, "breakdown": scores}


def print_evaluation(project_completion, teamwork, attendance):
	result = evaluate_employee(project_completion, teamwork, attendance)
	print(f"Overall score: {result['score']}/100 ({result['band']})")
	print("Breakdown:")
	for criterion, score in result["breakdown"].items():
		print(f"  {criterion}: {score:g}/100 (weight {WEIGHTS[criterion]:.0%})")


if __name__ == "__main__":
	print_evaluation(project_completion=88, teamwork=92, attendance=95)


ANALYSIS = """
Ethical analysis:
- The criteria are job-related and the weights (40%, 35%, 25%) are explicit,
  so no factor is hidden or allowed to dominate the result.
- Project completion and teamwork measure outcomes and collaboration; attendance
  has the smallest weight because raw presence is not the same as performance.
- The score is not inherently biased by protected characteristics, but managers
  should validate that each measure is defined consistently and audit outcomes
  across demographic groups.
- Approved leave, disability accommodations, remote work, and other legally
  protected circumstances must be excluded or adjusted before scoring. Employees
  should be able to review evidence, request corrections, and appeal a result.
- This is decision support, not an automatic employment decision; a trained
  human should consider role-specific context and documented feedback.
"""

print(ANALYSIS)
