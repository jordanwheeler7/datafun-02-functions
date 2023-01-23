"""
Jordan Wheeler, 21 Jan 2023

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics


# define a variable with some univariant data 
# (one varabile, many readings)
weight = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xreps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ypounds = [405, 385, 365, 315, 295, 275, 225, 225, 205, 185, 185, 135]

#print error if both lists are not the same size
if len(xreps) != len(ypounds):
    print("ERROR: The two lists are not the same size.")
    print(f"    {len(xreps)}!={ypounds}")
    quit()
try:
    xx_coor = statistics.correlation(xreps, xreps)
    xy_coor = statistics.correlation(xreps, ypounds)
    
except Exception as e:
    print(f"ERROR:  {e}")
    print("Try updating to Python 3.10 or greater.")
    print("Or select your updated conda environment in VS Code.")
    print("VS Code Menu / View / Command Palette / Python: Select Interpretor")
    quit()
    
    
    
#central tendency

mean = statistics.mean(weight)
median = statistics.median(weight)
mode = statistics.mode(weight)

#measure of spread

variance = statistics.variance(weight)
std_deviation =statistics.stdev(weight)
lowest = min(weight)
highest = max(weight)

print()
print("=============================================================")
print()
print(f"Here's some weight data: {weight}")
print()
print("Descriptive statistics include measures of central tendancy:")
print(f"   mean={mean:.2f}")
print(f"   median={median:.2f}")
print(f"   mode={mode:.2f}")
print()
print("Descriptive statistics include measures of spread:")
print(f"   var={variance:.2f}")
print(f"   stddev={std_deviation:.2f}")
print()
print()
print("=============================================================")
print()
print("See the following for weight and rep data:")
print()
print(f"xtimes:{xreps}")
print()
print(f"yvalues:{ypounds}")
print()
print(
    "These stats will show the correlation between the reps and weight",
)
print()
print(f"   correlation between xreps and xreps = {xx_coor:.2f}")
print(f"   correlation between xtimes and yvalues = { xy_coor:.2f}")
print()


#calculate slope/intercept

slope, intercept = statistics.linear_regression(xreps, ypounds)
futurex = 14
future_y = round(slope * futurex + intercept)

print()
print()
print("Now we will see some of our data combined.")
print()
print(f"x (reps):{xreps}")
print()
print(f"y (pounds):{ypounds}")
print()
print("We will calculate for the best fit straight line: ")
print()
print(f"   slope = {slope:.2f}")
print(f"   intercept = { intercept:.2f}")
print()
print("Now we will predict our future weight using the best fit line: ")
print()
print(f"   At {futurex:d}, reps,")
print(f"   your predicted weight will be { future_y:d}.")
print()
print()

