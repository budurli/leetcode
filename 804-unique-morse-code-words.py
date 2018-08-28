morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
mapping = {chr(ord('a') + i): morze for i, morze in enumerate(morze)}


def to_morze(word):
    return ''.join(mapping[c] for c in word)


def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    morzed = [to_morze(word) for word in words]
    return len(set(morzed))


tests = (
    (["gin", "zen", "gig", "msg"], 2),
)

for _input, expected_result in tests:
    actual_result = uniqueMorseRepresentations(_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
