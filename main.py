# Import Packages
import random
import os
import json

# These settings you can modify to change how this simulation runs.
subject_count = 10

# Create Test-Subject
class testsubject_class():
    def __init__(self, id, age, charstr):
        self.id = id
        self.age = age
        self.charstr = charstr
    def returnstr(self):
        return (f"no{(self.id + 1)}/{self.age}/{self.charstr}")

# Create all the test subjects.
testsubjects = []
for subjectcounter in range(0, subject_count):
    testsubjects.append(testsubject_class(subjectcounter, 0, "charstr").returnstr())

print(testsubjects)
