def heart_risk_factors(data):
    factors = []

    if float(data.get("chol", 0)) > 240:
        factors.append("High cholesterol")

    if float(data.get("trestbps", 0)) > 140:
        factors.append("High blood pressure")

    if float(data.get("age", 0)) > 50:
        factors.append("Age-related risk")

    return factors


def diabetes_risk_factors(data):
    factors = []

    if float(data.get("Glucose", 0)) > 140:
        factors.append("High glucose")

    if float(data.get("BMI", 0)) > 30:
        factors.append("High BMI")

    return factors


def generate_recommendations(factors):
    recs = []

    for f in factors:
        if "cholesterol" in f.lower():
            recs.append("Reduce oily food")

        if "pressure" in f.lower():
            recs.append("Reduce salt intake")

        if "glucose" in f.lower():
            recs.append("Limit sugar intake")

    if not recs:
        recs.append("Maintain a healthy lifestyle")

    return list(set(recs))