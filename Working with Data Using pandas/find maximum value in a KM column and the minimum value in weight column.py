## Dataset-Toyotan.csv
import pandas as pd
df = pd.read_csv('/content/Toyotan.csv')
print('Maximum : ',df['KM'].max(),'\nMinimum: ',df['Weight'].min())
