decksOfCards = ["TD", "TC", "6H", "5H", "KC", "JH", "QC", "4S", "2S", "8H", "JD", "2H", "AC", "7D", "6C", "5D", "AD", "TS", "4D", "KH", "3H", "9H", "3S", "2D", "5S", "6S", "AH", "JS", "6D", "9S", "4C", "7C", "8S", "AS", "KD", "7S", "4H", "KS", "7H", "9D", "8D", "3D", "5C", "9C", "QH", "JC", "8C", "TH", "QS", "3C", "QD", "2C"]
dict = {}
full_deck = {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}
all_suits = {"S", "C", "H", "D"}
for card in decksOfCards:
    suit = card[1]
    rank = card[0]
    if suit not in dict:
        dict[suit] = set()

    dict[suit].add(rank)


ans = 0
for suit, ranks in dict.items():
    if len(ranks) == len(full_deck):
        ans += 1

if dict.keys() == all_suits and ans % 4 == 0:
    print("one full deck")
