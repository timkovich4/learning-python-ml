import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

pivot_swapped = df.pivot_table(
    values="Survived", 
    index="Sex",      
    columns="Pclass",  
    aggfunc="mean"     
)
print(pivot_swapped)