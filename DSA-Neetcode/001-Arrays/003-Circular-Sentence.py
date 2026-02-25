# 2490. Circular Sentence

def isCircularSentence(sentence: str) -> bool:
    check = True

    if sentence[0] != sentence[-1]:
        check = False

    for i in range(1,len(sentence)-1):
        if ((sentence[i] == ' ') and (sentence[i-1] != sentence[i+1])):
            check = False
    return check
        
if __name__ == "__main__":
    sentence = "EDZVVYaYimHThFLmoHFGKCVPJTjVnBUnjhvFWijkHPxtWSWXAXXwDOjiTsPvRQIkxQZcGuKwWnctUjRwAibDlpfjZCYZdJFbjfUhffFdRhSRCcfJkCqYcPHYXhdOIzXdVwrxAKVXXQVSvMkIlfAbuKkyseWwAOLEnpMrcnDcWYcflAhAflHvJxgBYUKmeFHmrDZccVhtUEnVAwqnpUMgwtcFlsSddrzhOPLnjbzvmeMrCvqBJlAABUAdijMtebKTZMmNxtWqLIcsDsaepkmcOtVyBPR QMBUHrwRdOFsuIvjXLmnmpafbPPXXxWUWSGnhxjKOKH LhACwgqyvoaDmDgKAnmAAfJwnHsppIYrHxqEAFhAawCcHMHC WFOXITzBeNSgXBvRnwbTxogHKgbHBCylFSjjgkOMTHYoJdJLmHvXePjyGEALDI WgdgsRo o x"
    print(isCircularSentence(sentence))