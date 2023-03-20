# Natural Selection Simulation
In this simulation, I ran an experiment to test how test subjects would survive natural selection and which attributes would emerge as the prominant. The fully runable code will be in main.py, however, I will package it to EXE eventually.

This experiment uses main factors from this article:
[Kahn Academy Natural Selection (AP BIO)](https://www.khanacademy.org/science/ap-biology/natural-selection/artificial-selection/a/evolution-natural-selection-and-human-selection)

## Code Thought Processes

### v0.1
Preliminary steps are needed. Some of this code does not need comments, but I will explain all of my thought-process while coding here anyway as a better understanding of my own code in the future (as well as leave meaningful comments while coding)

```py
# Import Packages
import random
import os
import json
```

After such, I've created a section where you can modify certain manipulative variables which will change how long the simulation will last. Currently, it is only the subject count, which for test purposes 
```py
# Manipulative Variables
subject_count = 10
```
Afterwards, the class to be created will be where most of the init and creation of the character would go into. Our test subjects should more or less be setup in the same way. Perfectly, in Python, we have classes to do this for us.

```py
class testsubject_class():
    def __init__(self, id, age, charstr):
        self.id = id
        self.age = age
        self.charstr = charstr
```

We create this class with the id (which we use to identify the individual test_subject), the age of the test subject (which looking back should go into the charstr) and the character string (abb. charstr) which should hold all of the attributes of the test subject. I have no included the code to determine the test subject attributes yet, but will make sure to do so within 2-3 updates. 

Afterwards, we need to create test subjects, normally this would be a challenge, but since we may use strings for the entire class, we can create another class function to translate all subject information into a string with this function:
```py
    def returnstr(self):
        return (f"no{(self.id + 1)}/{self.age}/{self.charstr}")
```
We add 1 to the id to prevent id 0 which is hard to run calcuations with because any multiplicative element contributed to 0 will remain 0. The rest computes the string into this format:

```lua
no1/0/charstr -- this is in the format of id/age/charstr
```
Now, we can easily add these strings to an list:
```py
testsubjects = []
for subjectcounter in range(0, subject_count):
    testsubjects.append(testsubject_class(subjectcounter, 0, "charstr").returnstr())
```
We have a list now that looks something like this:
```python
'no1/0/charstr', 'no2/0/charstr', 'no3/0/charstr', 'no4/0/charstr', 'no5/0/charstr', 'no6/0/charstr', 'no7/0/charstr', 'no8/0/charstr', 'no9/0/charstr', 'no10/0/charstr'
```

This is something we can work with!

### v0.2
In this update, I would really like to get my charstr generator to work. I have brainstormed 7 factors that determine the test subjects survivability and reproductive chances. They are:

1. Age
2. Gender
3. Attractive Level
4. Strength
5. Eyesight
6. Intuition
7. Overall Survivability Chances

Those in 4-6 determine 7, which is a number ranging from 1-100. This number indicates the statistical probability of surviving (1%-100%). I will also plan for these factors to be constantly updating every time the age increases so the survival factor will decrease as the test subject gets older, so the equation to find the survivability should be very fluctuative to change. After some trial and error, I have come up with this equation:

```py
local_survivability = (100 - (local_age + (local_strength + local_eyesight + local_intuition)))
```
This line can be found on line 25 in this version (will be moved around in the future.)

We just need to factor in this with code now. This should be simple enough. We can create a function that generates a string with this factor and outputs that. Here it is:
```py
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
```

I have tried my best to comment out the functions of each one, but users can always refer here if they aren't sure of the meanings behind each survivability factor. 

Just a small thing before we continue, the age factor (because it is used in the calculation of survivability) needs to be replaced. I have removed it from the class.

Next, I just have to replace the temp string in line 34 with my new function. Nice!

```py
testsubjects.append(testsubject_class(subjectcounter, char_generate()).returnstr())

```

### v0.3