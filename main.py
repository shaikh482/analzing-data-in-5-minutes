import pandas as pd
from pandas_profiling import ProfileReport 
df = pd.read_csv('movies.csv')
print(df)
#generating a report
profile = ProfileReport(df)
profile.to_file(output_file="movies.csv")
