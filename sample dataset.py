import pandas as pd
import numpy as np
data = {
    "student" : ["alice","bobs","charlie","diana","frank","henry","jack","tinku","reethika","deepika"],
    "Math" : [92,78,91,90,88,85,83,98,99,96],
    "Science" : [78,95,99,96,94,88,82,84,92,91],
    "English" : [78,98,97,98,94,93,92,95,96,99],
       }
df = pd.DataFrame(data)
print(df.head())
