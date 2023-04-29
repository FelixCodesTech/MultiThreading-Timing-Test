import pandas as pd

df = pd.DataFrame({"numbers":range(-1001, 1)})

df.to_csv("data2.csv")