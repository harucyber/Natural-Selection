# Import Packages
import random
import os
import json

# These settings you can modify to change how this simulation runs.
subject_count = 10
simulation_years = 100

# Create Test-Subject
class testsubject_class():
    def __init__(self, id, charstr):
        self.id = id
        self.charstr = charstr
    def returnstr(self):
        return (f"no{(self.id)}/{self.charstr}")

# Generate Properties
def char_generate():
    local_age = 0 # ref age factor which determines survivability (0 is best)
    local_gender = random.randint(0,1) # 0M 1F
    local_attractivelvl = random.randint(0,8) # determines reproduction level
    local_strength = random.randint(0,8) # ref strength factor which determines survivability (0 is best) 
    local_eyesight = random.randint(0,8) # ref eyesight factor which determines survivablity (0 is best)
    local_intuition = random.randint(0,8) # ref intuition factor which determines survivability (0 is best)
    local_survivability = (100 - (local_age + (local_strength + local_eyesight + local_intuition))) # creates a number for est. death

    local_charstr = "" # Clear
    local_charstr = f"{local_age}~{local_gender}~{local_attractivelvl}~{local_strength}~{local_eyesight}~{local_intuition}~{local_survivability}"
    return local_charstr

# Create all the test subjects.
testsubjects = []
for subjectcounter in range(0, subject_count):    
    testsubjects.append(testsubject_class(subjectcounter, char_generate()).returnstr())


# Create Simulation
# This is for Rim use. Use string splitting to determine factor, then use regeX to subsitute.
