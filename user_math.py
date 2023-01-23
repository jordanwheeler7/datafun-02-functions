"""
Jordan Wheeler
21 Jan 2023
Ftiness 
This formula should help the user calculate and track their last 3 sets of the squat.
We will find the mean, median, and mode for the squat.
"""
# Start creating a list of the last 3 lifts and weight for those
import math
import statistics
import webbrowser

# Welcome the user and gather their inputs
print()
print()
print("Welcome! We will utilize this opportunity to record your last 3 sets of squats")
print("To begin, we will start with your last 3 sets of squats weight beginning with the most recent.")
print()

is1 = input("Please enter the weight of your first set of squats: ")
is2 = input("Please enter the weight of your second set of squats: ")
is3 = input("Please enter the weight of your third set of squats: ")
print()
print()
ir1 = input("Please enter the number of reps for your first set: ")
ir2 = input("Please enter the number of reps for your second set: ")
ir3 = input("Please enter the number of reps for your third set: ")
print()
print()

#string to numbers

s1 = float(is1)
s2 = float(is2)
s3 = float(is3)
r1 = float(ir1)
r2 = float(ir2)
r3 = float(ir3)

#get sum
sum = s1 + s2 + s3
sumr = r1 + r2 + r3

#find average to the 3 decimal
average = round(sum/3, 3)
averager = round(sumr/3, 3)

#find the product
product = s1 * s2 * s3
productr = r1 * r2 * r3

#lightest rep
Light = min(s1, s2, s3)
Lightr = min(r1, r2, r3)

#heaviest reps
Heavy = max(s1, s2, s3)
Heavyr = max(r1, r2, r3)

#find the range
range = Heavy - Light
ranger = Heavyr - Lightr

#find 1 rep max
one_rep_max = round((Heavy * (36 / (37-averager)) ), 2)

#show user their results
print({sum},"was your total weight.")
print({average},"was your average weight.")
print({product},"was the product of your lifts.")
print({Light},"was your lightest rep.")
print({Heavy},"was your heaviest rep.")
print({range},"was the range of your lifts")
print({one_rep_max},"is your new one rep max")

#Wording for the user

try_harder = "Push yourself a little harder."
on_par = "You are right where you should be. Keep working."
getting_it = "You are above average. Keep up the progress!"
below_average = 135
average_2 = 225
above_average = 315

if Light < below_average:
    print(try_harder)
if average == average_2:
    print(on_par)
if Heavy > above_average:
    print(getting_it)

str_response = input("Would you like to see how to improve your squats? (Y/N)")

if str_response == "y":
    webbrowser.open ("https://www.topfitness.com/blogs/blog/14-tips-for-improving-your-back-squat")
