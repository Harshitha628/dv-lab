import pandas as pd
import numpy as np
data = {
    "student" : ["alice","bob","charlie","diana","frank"],
    "Math" : [87,89,98,79,98],
    "Science" : [98,97,96,95,94],
    "English" : [87,86,85,84,83],
       }
df = pd.DataFrame(data)
print(df.head())
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(df["student"], df["Math"],marker="o",label="Math",color="blue")
plt.plot(df["student"], df["Science"],marker="s",label="Science",color="green")
plt.plot(df["student"], df["English"],marker="^",label="English",color="red")
plt.title("student score trends",fontsize=14)
plt.xlabel("student")
plt.ylabel("marks")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png",dpi=150)
plt.show()
