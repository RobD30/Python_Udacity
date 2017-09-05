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

#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

