if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
pass

if 18.5 <= weight_in_kg / (height_in_m) ** 2 < 25:
    print("BMI is considered 'normal'.")

if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

def garden_calendar(season):
    if season == "spring":
        print("time to plant the garden!")
    elif season == "summer":
        print("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("time to harvest the garden!")
    elif season == "winter":
        print("time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season")


#First Example - uncomment lines or change values to test the code
phone_balance = 7.62
bank_balance = 104.39
#phone_balance = 12.34
#bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)

#Second Example

#change the number to experiment!
number = 145346334
#number = 5 #3 sir
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

#Third Example

#change the age to experiment with the pricing
age = 35

#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message)

def which_prize(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

def punctuate(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create.
                "exclamation", "question" and "aside" are known values.
    """
    if phrase_type == "exclamation":
        sentence_punct = sentence + "!"
    elif phrase_type == "question":
        sentence_punct = sentence + "?"
    elif phrase_type == "aside":
        sentence_punct = "(" + sentence + ".)"
    else:
        sentence_punct = sentence + "."
    return sentence_punct

def which_pize():
    if not prize:
        return "Oh dear, no prize this time."
    elif points <= 50:
        return "Congratulatoins! You have won a wooden rabbit"
    elif points >= 150 and <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"