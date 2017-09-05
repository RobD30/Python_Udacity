# Break the function down into 3-5 steps and write them in words in the box, in the order in which they will get
# performed on the input data. Include the input and the output of each step. This answer will not get graded but we'll
# share what we think afterwards. There is not a single right answer to a question like this, so just give it a try!
# Your reflection
# take in input, discard outliers, combine data, take the mean, output return
# Things to think about
# Thanks for thinking about this design decision!
#
# Here are our four steps:
#
# Take each of the raw scores and convert each of them to a numerical type.
# Input: score as string/float/int. Output: score as float or int.
# Choose the middle 3 values from the set of 5 scores.
# Input: 5 scores as float or int. Output: 3 scores (same type).
# Take the average of three scores.
# Input: 3 scores as float or int. Output: 1 average score (float).
# Choose the correct word rating for the average score.
# Input: average score as float. Output: Rating as a string.
def convert_to_numeric(score):
    """
    Converts the scores into a numerical value
    """
    return float(score)

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Gives the sum
    """
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5,
    into a string rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "Ok"
    elif av_score < 4:
        rating = "Good"
    else:
        rating = "Excellent"
    return rating


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # Convert Scores to numbers
    score1 = float(score1)
    score2 = float(score2)
    score3 = float(score3)
    score4 = float(score4)
    score5 = float(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
