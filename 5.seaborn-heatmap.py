import pandas as pd
import  matplotlib.pyplot as plt

data = {
    "student" : ["alice","bob","charlie","diana","frank"],
    "Math" : [87,89,98,79,98],
    "Science" : [98,97,96,95,94],
    "English" : [87,86,85,84,83],
    "Hours_Studied":[5,4,3,2,1]
       }
df = pd.DataFrame(data)
print(df.head())
import seaborn as sns
numeric_df= df[["Math","Science","English","Hours_Studied"]]
corr = numeric_df.corr()
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",linewidth=0.5, vmin=-1,vmax=1)
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=150)
plt.show()
