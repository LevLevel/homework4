def missing_statues(statues):
    if not statues:
        return 0
    return max(statues) - min(statues) - len(statues) + 1