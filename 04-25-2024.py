__author__ = 'Markell Thornton'
import random
# Please evaluate me!
# https://urldefense.com/v3/__https://uw.iasystem.org/survey/288992__;!!K-Hz7m0Vt54!nd-pzveeXmTesU89Q5kQMA9dL667PWar6a0qnA6_P5anJ_L_K_Ma1PgnPOQiEtsUEHyjNPd3SY99F3-RB0s$

#-------------------------------------
# Programming acitivity 1

# Using the random module, flip some coins
# Assume 0 is tails and 1 is heads

# TODO: Use random.choices(),
#  Flip 1,000 coins and count how many heads or tails your get, Calculate the probability of getting heads and tails
#  Flip 1,000 more and compare your results, Calculate the probability of getting heads and tails

#Example of flipping one coin:
for _ in range(1000):
    flip = random.choices([0, 1], k=1)[0]
    if flip == 1:
        heads_count += 1
    else:
        tails_count += 1

#Now try writing a code to flip 1000 times:

# TODO: If you have more time, for a challenge:
# create an unfair coin,
# i.e., one where heads and tails are not equally probable
# Hint: Give more options to random.choices
# and rethink what numbers correspond to heads and tails

#-------------------------------------
# Programming acitivity 2
# TODO: Write a for loop to approximate the value of θ that maximizes P(D) = {HHHTT}
#  Think about how to loop over evenly-spaced numbers between 0 to 1
#  Then loop over the numbers and calculate the value of θ^3 * (1-θ)^2
#  Then compare the product with the existing highest P(D) value to update the smallest value
#  Feel free to come up with your own numerical approximation method

curr_max_p = 0
curr_max_x = 0
for x in range(0, 1000, 1):
    pass
