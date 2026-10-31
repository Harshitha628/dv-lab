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
subjects = ["Math", "Science", "English"]
averages =[df["Math"].mean(),df["Science"].mean(),df["English"].mean()]
plt.figure(figsize=(7, 5))
bars = plt.bar(subjects, averages, color=["#3498db","#2ecc71","#e74c34"], edgecolor="black")
for bar, avg in zip(bars, averages) :
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 3,f"{avg:.1f}", ha="center", va="top", color="white", fontweight="bold")
    plt.title("Average scores by subject")
    plt.ylabel("Average marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig("bar_chart.png",dpi=150)
    plt.show()
