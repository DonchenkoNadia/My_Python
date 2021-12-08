'''
30 карт и каждая обозначена цифрой от 0 до 9 и буквой R, G, B
и есть правила которые могут дополнятся
например выигрышная комбинация, если выпало три карты одного числового значения, либо одного цвета
'''
#кодирование ответа

rules = { 1: ["color", "color", "color"], # color - 5, digit - 10, any - 0
          2: ["digit", "digit", "digit"],
          3: ["color", "color", "any"]
}

cards = ["1R", "2R", "3R"]

def checkIfDigitsSame(cards):
    #R 0 - 0
    #G 3 - 9
    #B 6 - 18
    digit = cards[0][0]
    for i in range(1, len(cards)):
        if cards[i][0] == digit:
            continue
        else:
            return False
    return True

print(checkIfDigitsSame(cards))
