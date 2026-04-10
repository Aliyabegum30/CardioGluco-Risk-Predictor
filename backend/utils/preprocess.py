def prepare_input(data, feature_list):
    processed = []

    for feature in feature_list:
        value = data.get(feature, 0)

        # handle empty values
        if value == "" or value is None:
            value = 0

        try:
            value = float(value)
        except:
            value = 0

        processed.append(value)

    return [processed]