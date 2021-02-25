# Pandas

## Introduction

### Load CSV files 

```python
import pandas as pd

# load csv file into a dataframe
df = pd.read_csv("mc16a_BSM4tops_even.csv")

# setup to show all columns
pd.set_option('display.max_columns', None)

# print out the dataframe
print(df)

# to print out specific columns 
print(df[["column1","column2","column3"]])
```

