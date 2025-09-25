def ascending_sequence(arr):
    def is_increasing(seq):
        for i in range(len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return False
        return True

    if is_increasing(arr):
        return True

    for i in range(len(arr)):
        temp = arr[:i] + arr[i + 1:]
        if is_increasing(temp):
            return True

    return False
