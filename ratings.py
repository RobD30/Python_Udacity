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
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # THE CODE GOES HERE!

    return rating