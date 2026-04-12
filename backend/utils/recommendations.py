def heart_risk_factors(data):
    factors = []

    if float(data.get("chol", 0)) > 240:
        factors.append("High cholesterol increases heart disease risk")

    if float(data.get("trestbps", 0)) > 140:
        factors.append("High blood pressure puts strain on the heart")

    if float(data.get("thalach", 0)) < 100:
        factors.append("Low maximum heart rate detected")

    if float(data.get("age", 0)) > 50:
        factors.append("Age is a contributing risk factor")

    if int(data.get("exang", 0)) == 1:
        factors.append("Exercise-induced chest pain present")

    if int(data.get("cp", 0)) > 0:
        factors.append("Chest pain symptoms observed")

    if float(data.get("oldpeak", 0)) > 2:
        factors.append("ST depression indicates possible heart stress")

    return factors


def diabetes_risk_factors(data):
    factors = []

    if float(data.get("Glucose", 0)) > 140:
        factors.append("High glucose level")

    if float(data.get("BMI", 0)) > 30:
        factors.append("High BMI (Obesity risk)")

    if float(data.get("Age", 0)) > 45:
        factors.append("Age increases diabetes risk")

    if float(data.get("Insulin", 0)) > 150:
        factors.append("High insulin resistance")

    if float(data.get("BloodPressure", 0)) > 90:
        factors.append("Elevated blood pressure")

    return factors


def generate_recommendations(factors):
    recs = []

    for f in factors:
        f = f.lower()

        if "cholesterol" in f:
            recs.append("Reduce oily and fried foods")
            recs.append("Increase fiber intake")

        if "pressure" in f:
            recs.append("Reduce salt intake")
            recs.append("Practice stress management")

        if "glucose" in f:
            recs.append("Limit sugar and refined carbs")
            recs.append("Monitor blood sugar regularly")

        if "bmi" in f or "obesity" in f:
            recs.append("Start weight loss plan")
            recs.append("Increase physical activity")

        if "age" in f:
            recs.append("Schedule regular medical checkups")

        if "insulin" in f:
            recs.append("Follow low-carb diet")
            recs.append("Exercise regularly")

        if "chest pain" in f:
            recs.append("Consult a cardiologist immediately")

        if "heart rate" in f:
            recs.append("Start moderate cardio exercise")

    if not recs:
        recs.append("Maintain a balanced diet")
        recs.append("Exercise regularly")
        recs.append("Stay hydrated and sleep well")

    return list(set(recs))