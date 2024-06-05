__author__ = 'Yuan Chai'
import random #Part 1
import import numpy as np #part 2
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
flip = random.choi
ces([0, 1], k = 1)
n_H = sum(flip)

#Now try writing a code to flip 1000 times:
flips_2 = random.choices([0, 1], k=1000)
heads_count_2 = flips_2.count(1)
tails_count_2 = flips_2.count(0)

flips_2 = random.choices([0, 1], k=1000)
heads_count_2 = flips_2.count(1)
tails_count_2 = flips_2.count(0)

print("\nSecond 1,000 flips:")
print(f"Heads: {heads_count_2}, Tails: {tails_count_2}")
print(f"Probability of Heads: {prob_heads_2}")
print(f"Probability of Tails: {prob_tails_2}")

# TODO: If you have more time, for a challenge:
# create an unfair coin,
# i.e., one where heads and tails are not equally probable
# Hint: Give more options to random.choices
# and rethink what numbers correspond to heads and tails
flips_unfair = random.choices([0, 1], weights=[0.3, 0.7], k=1000)
heads_count_unfair = flips_unfair.count(1)
tails_count_unfair = flips_unfair.count(0)

prob_heads_unfair = heads_count_unfair / 1000
prob_tails_unfair = tails_count_unfair / 1000

print("\nUnfair coin (1,000 flips):")
print(f"Heads: {heads_count_unfair}, Tails: {tails_count_unfair}")
print(f"Probability of Heads: {prob_heads_unfair}")
print(f"Probability of Tails: {prob_tails_unfair}")
#-------------------------------------
# Programming acitivity 2
# TODO: Write a for loop to approximate the value of θ that maximizes P(D) = {HHHTT}
#  Think about how to loop over evenly-spaced numbers between 0 to 1
#  Then loop over the numbers and calculate the value of θ^3 * (1-θ)^2
#  Then compare the product with the existing highest P(D) value to update the smallest value
#  Feel free to come up with your own numerical approximation method

curr_max_p = 0
curr_max_theta = 0
for x in range(0, 1000, 1):
    pass

theta_values = np.linspace(0, 1, 1000)

for theta in theta_values:
    p_d = theta**3 * (1 - theta)**2 #probability: P(D) = θ^3 * (1-θ)^2

        if p_d > curr_max_p:
        curr_max_p = p_d
        curr_max_theta = theta

print(f"Maximum P(D) is {curr_max_p} at θ = {curr_max_theta}")
