"""
Jordan Wheeler 22 Jan 2023
Domain= Fitness


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


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4


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

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn Python."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy.
{self.to_string()}
You'll need curiousity, the ability to search the web, 
and the tenacity and resourcefulness
to solve all kinds of challenges.
Let's get started! 

        """
        )

    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
I'm a {self.species} with {self.num_legs} legs.
I weigh {self.weight_kgs:.2f} kgs.
I've been alive for {self.get_age_string()}.
I know:
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
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
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
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    rex.display_welcome()
