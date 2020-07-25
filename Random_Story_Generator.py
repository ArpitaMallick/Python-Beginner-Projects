#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
print("Hello Reader")

readername = input("What is your name? ")
print("Hello "+ readername)

names = ["Arpita", "Shyam", "Trump", "Obama", "Modi", "Uno", "Ginger"]
places = ["Pune", "Delhi", "Chennai", "Pondicherry", "Disneyland", "Pakistan", "USA"]
roles = ["student", "teacher", "warrior", "witch", "farmer", "guitarist", "vocalist", "musician"]
quests = ["slay the dragon", "beat the deadline", "seek the holy grail"]

randomname = random.choice(names)
randomplace = random.choice(places)
randomrole = random.choice(roles)
randomquest = random.choice(quests)

story = "Once upon a time there was a " + randomrole + " called " + randomname + ", who lived in " + randomplace + ". There was only one mission on his/her mind and it was to " + randomquest + "."

print(story)


# In[ ]:




