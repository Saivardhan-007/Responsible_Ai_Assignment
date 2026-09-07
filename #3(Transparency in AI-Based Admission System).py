"""
Task 3 - Version B (Revised, transparent version)
Predicts admission and EXPLAINS the decision: shows each factor's
contribution and states in plain language why the student was
selected or rejected.
"""

WEIGHTS = {
    "entrance_score": 0.50,
    "academic_marks": 0.35,
    "extracurricular_score": 0.15,
}
THRESHOLD = 60


def predict_admission(entrance_score, academic_marks, extracurricular_score):
    contributions = {
        "entrance_score": entrance_score * WEIGHTS["entrance_score"],
        "academic_marks": academic_marks * WEIGHTS["academic_marks"],
        "extracurricular_score": extracurricular_score * WEIGHTS["extracurricular_score"],
    }
    total = sum(contributions.values())
    decision = "Selected" if total >= THRESHOLD else "Rejected"

    # rank factors by how much they contributed to the outcome
    ranked = sorted(contributions.items(), key=lambda x: x[1], reverse=True)
    top_factor, top_value = ranked[0]
    weakest_factor, weakest_value = ranked[-1]

    explanation = (
        f"Decision: {decision} (total score: {total:.1f}/{THRESHOLD} required)\n"
        f"Breakdown of contributing factors:\n"
        f"  - Entrance score contributed {contributions['entrance_score']:.1f} points "
        f"(weight {WEIGHTS['entrance_score']*100:.0f}%)\n"
        f"  - Academic marks contributed {contributions['academic_marks']:.1f} points "
        f"(weight {WEIGHTS['academic_marks']*100:.0f}%)\n"
        f"  - Extracurricular score contributed {contributions['extracurricular_score']:.1f} points "
        f"(weight {WEIGHTS['extracurricular_score']*100:.0f}%)\n"
        f"Most influential factor: {top_factor.replace('_', ' ')} "
        f"({top_value:.1f} points).\n"
        f"Least influential factor: {weakest_factor.replace('_', ' ')} "
        f"({weakest_value:.1f} points)."
    )

    return decision, explanation


if __name__ == "__main__":
    decision, explanation = predict_admission(
        entrance_score=55, academic_marks=70, extracurricular_score=40
    )
    print(explanation)
