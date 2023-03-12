import numpy as np
import pandas as pd

with open('/home/minato132/Documents/Data/ISE_369/House_Senate.txt') as file:
	data = pd.read_csv(file, sep = '|', header = None)

data = data.loc[:, [1, 2, 4, 5, 7, 18, 19]]

dataMD = data.loc[data[18] == 'MD']

dataMD = dataMD.loc[dataMD[19] == 3]

def ICS(ar):
	if ar == 'C':
		return 'a Challenger'
	else:
		return 'an Incumbent'



#Q8_____________________________________________________________________________________


dataQ8 = dataMD
dataQ8.sort_values(7, ascending = False, inplace = True)

print(f'(8) In MD District 3, the person that raised the most amount of money is {dataQ8.iat[0,0]}, with about ${dataQ8.iat[0, 4] / 1000:.2f}k.\n    The individual is a {dataQ8.iat[0, 2]} and is {ICS(dataQ8.iat[0, 1])} \n ')




#Q9_____________________________________________________________________________________

dataQ9 = dataMD
dataQ9.sort_values(5, ascending = False, inplace = True)

print(f'(9) In MD District 3, the person that spent the amount of money is {dataQ9.iat[0,0]}, with about ${dataQ9.iat[0, 3] / 1000:.2f}k \n    The individual is a {dataQ9.iat[0, 2]} and is {ICS(dataQ9.iat[0, 1])}\n')




#Q10___________________________________________________________________________________

dataQ10 = dataMD

dQ10_I = dataQ10.loc[data[2] == 'I']
dQ10_C = dataQ10.loc[data[2] == 'C']

def q10(ar1, ar2):
	if ar1 > ar2:
		return 'Incuments'
	elif ar1 < ar2:
		return 'Challenger'
	else:
		return 'same'

dI_sum = dQ10_I.loc[:, 7].sum()
dC_sum = dQ10_C.loc[:, 7].sum()

print(f'(10) Based on the data we find that {q10(dI_sum, dC_sum)} raised the most.\n')



#Q11________________________________________________________________________________

dataQ11 = dataMD

dQ11_I = dataQ11.loc[data[2] == 'I']
dQ11_C = dataQ11.loc[data[2] == 'C']

Q11_I = dQ11_I.loc[:, 5].sum()
Q11_C = dQ11_C.loc[:, 5].sum()

print(f'(11) Based on the data we find that {q10(Q11_I, Q11_C)} spent the most.\n')






