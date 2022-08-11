import pandas as pd
quantile_df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=['a'])

print(f"50% quantile = {quantile_df['a'].quantile(.5)}")
print(f"median = {quantile_df['a'].median()}")
print(f"25%, 50%, and 75% quantiles are: \n{quantile_df['a'].quantile([.25,.5,.75])}")

