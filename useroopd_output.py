"""
Jordan Wheeler 22 Jan 2023
Domain= Fitness
We will use PyBuddy to get the user
fitness information. 


Build a PyBuddy to extend a welcome.

Uses:

- new Python 3.7 data classes
- list compreshensions for concise processing
- multiline strings -
- some are indented because all the way left seems ugly.

"""

# import from dataclasses to make our job even easier
from dataclasses import dataclass, field

import datetime
from enum import Enum
import statistics


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4

reps = [ 
     1,
     4,
     6,
     8,
     10,
     12,
     16,
     18,
     20,
     24,
     24,
     ]

# Add central tendicies

mean = statistics.mean(reps)
median = statistics.median(reps)
mode = statistics.mode(reps)

# Add the @dataclass decorator to let Python do more of the work
# Notice what changes.


@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy."""

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Unknown"
    species: Species = 1
    num_legs: int = 4
    weight_kgs: float = 9.999999999
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()
    num_eyes: int = 2
    
    def get_num_eyes_string(self):
        """Return a string with number of eyes."""
        return str(self.num_eyes)

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn proper form."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy. I can tell you
the mean, median, and mode of the most common rep ranges: 
{self.get_mean()}, {self.get_median()}, {self.get_mode()}.

{self.to_string()}

You'll need curiousity, the ability to get to a gym, 
and the tenacity and resourcefulness
to power through all kinds of challenges.
Let's get started! 

        """
        )

    def get_mean(self):
        """Return mean to user"""
        return mean
    
    def get_median(self):
        """Return median to user."""
        return median
    
    def get_mode(self):
        """Return mode to user"""
        return mode
                   
                      
    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
I have {self.get_num_eyes_string()} eyes.
I'm a {self.species} with {self.num_legs} legs.
I weigh {self.weight_kgs:.2f} kgs.
I've been alive for {self.get_age_string()}.
I know workouts for:
{self.get_skills_string()}
"""


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run, do this:
if __name__ == "__main__":

    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "Alice",
        Species.CAT,
        4,
        8.123456,
        True,
        ["Legs", "Chest", "Shoulders", "Arms", "Back"],
    )

    # Call the buddy's welcome() method
    alice.display_welcome()

    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Rex",
        species=Species.DOG,
        num_legs=4,
        weight_kgs=10.437241,
        is_available=True,
        skill_list=["Legs", "Chest", "Shoulders", "Arms", "Back"],
    )

    rex.display_welcome()
