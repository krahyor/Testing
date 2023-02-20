import itertools

def alternate(s):
    # Get all distinct characters in the string
    distinct_chars = set(s)

    # Try all possible pairs of distinct characters
    max_length = 0
    for pair in itertools.combinations(distinct_chars, 2):
        # Remove all characters that are not in the pair
        filtered = ''.join(c for c in s if c in pair)

        # Check if the resulting string is alternating
        is_alternating = all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1))

        # Update the maximum length if the string is alternating and longer than the current maximum
        if is_alternating and len(filtered) > max_length:
            max_length = len(filtered)

    return max_length