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
plt.figure(figsize=(8,5))

plt.scatter(
    df["Hours_Studied"],
    df["Math"],
    c=df["Math"],
    cmap="viridis",
    s=100,
    edgecolors="black"
)

for i, name in enumerate(df["Student"]):
    plt.annotate(
        name,
        (df["Hours_Studied"][i], df["Math"][i]),
        textcoords="offset points",
        xytext=(5,5),
        fontsize=8
    )

plt.colorbar(label="Math Score")
plt.title("Hours Studied vs Math Score")
plt.xlabel("Hours Studied per Day")
plt.ylabel("Math Score")

plt.tight_layout()
plt.savefig("scatter.png", dpi=150)
plt.show()
