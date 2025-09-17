def missing_statues(statues):
    if not statues:
        return 0
    unique_sorted = sorted(set(statues))
    full_range = unique_sorted[-1] - unique_sorted[0] + 1
    return full_range - len(unique_sorted)