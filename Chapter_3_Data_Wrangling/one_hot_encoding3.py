import pandas as pd
s = pd.Series(['dog', 'dog', 'cat', 'turtle', 'turtle', 'turtle'])
print(s)

results = pd.get_dummies(s, drop_first=True)
print(results)

