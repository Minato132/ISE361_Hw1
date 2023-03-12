import numpy as np
import pandas as pd



with open('/home/minato132/Documents/Data/ISE_369/santos_disp.csv') as file:
	data = pd.read_csv(file)

pd.set_option('display.max_rows', None)

data = data.loc[:, ['disbursement_amount', 'recipient_state']]

data1 = data.loc[data['recipient_state'] == 'NY']

data1 = data1.loc[:, 'disbursement_amount'].sum()

print(f'The total amount that George Santos report spending in NY is: ${data1:.2f}')

data2 = data.loc[data['recipient_state'] != 'NY']


data2 = data2.loc[:, 'disbursement_amount'].sum()

print(data2)
#print(f'The total amount that George Santos report spending outside of NY is: ${data2:.2f}')


