def normalize(lst):
    normalized = {}

    for obj in lst:
        normalized[obj['id']] = obj
    return normalized
