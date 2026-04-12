def prepare_input(data, feature_list):
    processed = []

    for feature in feature_list:

        if feature not in data:
            print(f"⚠️ Missing feature: {feature}")

        value = data.get(feature, 0)

        # Handle empty values
        if value == "" or value is None:
            value = 0

        try:
            value = float(value)
        except:
            print(f"⚠️ Invalid value for {feature}: {value}")
            value = 0

        processed.append(value)

    print("✅ Final Feature Vector:", processed)

    return [processed]