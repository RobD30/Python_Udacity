def name_changer():
    names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
             'nigel incubator-jones', 'philip diplodocus mallory']
    for name in names:
        print(name.title())


print(name_changer())


def list_sum(input_list):
    total = 0
    for element in input_list:
        total += element
    return total


# These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box


# Test Cases
print("Test 1:")
starbox(5, 5)  # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)