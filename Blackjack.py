import random


def generate_deck(_suits, _cards):
    random.seed(0)
    n = 0
    deck = [(i, j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n == 52:
            random.shuffle(deck)
            n = 0


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shuffled_deck = generate_deck(suits, cards)


def get_next_card():
    return next(shuffled_deck)


# DO NOT EDIT ABOVE THIS LINE
# BELOW THIS LINE WILL BE YOUR SOLUTION

money_sages = int(input("Sage's money:\n"))
numberofgames = int(input("Number of games:\n"))

def get_valueofcard(cardabbreviation,suitofcard):
    if cardabbreviation.isdigit():
            valueofcard = int(cardabbreviation)
    elif cardabbreviation == "A" or cardabbreviation == "J" or cardabbreviation == "Q":
            valueofcard = 10
    elif cardabbreviation == "K":
        if suitofcard == "Hearts" or suitofcard == "Diamonds":
              valueofcard = 1
        elif suitofcard == "Clubs" or suitofcard == "Spades":
             valueofcard = 11
    return valueofcard

did_gameend=False
valueofkingscards=0
valueofsagescards=0
k=0
def gameofsage():
    global valueofsagescards,money_sages,did_gameend,valueofkingscards,k
    if valueofsagescards == 21:
        if k==0:
            print("It is Blackking! You won!")
            
            money_sages +=50
            did_gameend = True
            return
        else:
            k+=1
            return
    elif valueofsagescards > 21:
        k+=1
        print("You busted! You lost!")
        money_sages -= 50
        did_gameend = True
        return
    elif valueofsagescards < 21:
        k+=1
        while True:
            hitorstay = input("Do you want to hit or stand? [H/S]\n")
            if hitorstay == "S":
                break
            elif hitorstay == "H":
                sagescards.append(get_next_card())
                #sagescards.append(("Diamonds","7"))
                valueofsagescards += get_valueofcard(sagescards[-1][1],sagescards[-1][0])
                stringsagescards = ""
                for _ in range(len(sagescards)):
                    stringsagescards += str(sagescards[_])
                print(f"Sage's cards: {stringsagescards}")
                print(f"Total value: {valueofsagescards}")
                if did_gameend == False:
                    gameofsage()
                break
def gameofking():
    global valueofsagescards,money_sages,did_gameend,valueofkingscards
    stringkingscards = ""
    for _ in range(len(kingscards)):
        stringkingscards += str(kingscards[_])
    print(f"King's cards: {stringkingscards}")
    print(f"Total value: {valueofkingscards}")
    if valueofkingscards > 21:
        print("King busted! You won!")
        money_sages += 50
    elif valueofkingscards >= 17:
        if valueofkingscards > valueofsagescards:
            money_sages -=50
            print("King has higher value. You lost!")
        elif valueofsagescards > valueofkingscards:
            money_sages +=50
            print("You have higher value. You won!")
        elif valueofkingscards == valueofsagescards:
            print("It is a tie!")
    elif valueofkingscards < 17:
        kingscards.append(get_next_card())
        valueofkingscards += get_valueofcard(kingscards[-1][1],kingscards[-1][0])
        gameofking()
            

for i in range(1,numberofgames+1):
    print(f"Game {i}")
    kingscards = []
    sagescards = []
    did_gameend = False
    valueofkingscards=0
    valueofsagescards=0
    k=0
    sagescards.append(get_next_card())
    sagescards.append(get_next_card())
    kingscards.append(get_next_card())
    kingscards.append(get_next_card())
    print("King's cards: "+"(*)"+str(kingscards[1]))
    valueofkingscards += get_valueofcard(kingscards[1][1],kingscards[1][0])
    print(f"Total value: {valueofkingscards}")
    valueofkingscards += get_valueofcard(kingscards[0][1],kingscards[0][0])
    stringsagescards = ""
    for _ in range(len(sagescards)):
        stringsagescards += str(sagescards[_])
    stringkingscards = ""
    for _ in range(len(kingscards)):
        stringkingscards += str(kingscards[_])
    print(f"Sage's cards: {stringsagescards}")
    valueofsagescards += get_valueofcard(sagescards[0][1],sagescards[0][0]) + get_valueofcard(sagescards[1][1],sagescards[1][0])
    print(f"Total value: {valueofsagescards}")
    if did_gameend == False:
        gameofsage()
    if did_gameend == False:
        gameofking()
print(f"Final money is {money_sages}")
         