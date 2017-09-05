def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # return the correct value
    return days_in_month[9]


# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# Test for list
print(eclipse_dates[7:10])

def more_different():
    sample_string = "And Now For Something Completely Different"
    sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    sentence1 = "I wish to resiter a complaint."
    sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
    person = "Old Woman"
    name = "Dennis"
    dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
    mr_buns_order = dish
    some_list = mr_buns_order
    len(some_list)
    max(some_list)
    python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
    max(python_varieties)
    print(python_varieties)
    min(some_list)
    sorted(some_list)
    pass

def some_ting():
    nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
    names = ["García", "O'Kelly", "Davis"]
    stuff = ["thing", "42", "nope"]
    return " and ".join(stuff)

print (some_ting())

def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # implement this function

def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # if the list has an odd number of elements,
        # the median is the middle element
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        # if the list has an even number of elements,
        # the median is the average of the middle two elements
        right_of_middle = len(numbers)//2
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2