# Natural Selection Simulation
In this simulation, I ran an experiment to test how test subjects would survive natural selection and which attributes would emerge as the prominant. 

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