# 2490. Circular Sentence

def isCircularSentence(sentence: str) -> bool:
    check = False

    if ' ' not in sentence:
        check = sentence[0] == sentence[-1]

    for i in range(len(sentence)):
        if ((sentence[i] == ' ') and (sentence[i-1] == sentence[i+1])):
            check = True
    return check
        
if __name__ == "__main__":
    sentence = "eetcode"
    print(isCircularSentence(sentence))