import numpy as np
import pandas as pd

with open('/home/minato132/Documents/Data/ISE_369/House_Senate.txt') as file:
	data = pd.read_csv(file, sep = '|', header = None)

data = data.loc[data[0] < 'I']

def ICS(ar):
	if ar == 'Challenger':
		return 'a Challenger'
	else: 
		return 'an Incumbent'



#Q1________________________________________________________________

dataQ1 = data.loc[:, [1, 2 ,4, 5]]

dataQ1.sort_values(5, ascending = False, inplace = True)

print(f'(1) The individual that raised the most money is: {dataQ1.iat[0, 0]}, who raised about ${dataQ1.iat[0, 3] / 1000000:.2f}M. The person is a {dataQ1.iat[0, 2]} and {ICS(dataQ1.iat[0, 1])} \n')



#Q2________________________________________________________________

dataQ2 = data.loc[:, [1, 2, 4, 7]]

dataQ2.sort_values(7, ascending = False, inplace = True)

print(f'(2) The individual that spent the most money is: {dataQ2.iat[0, 0]}, who spent about ${dataQ2.iat[0, 3] / 1000000:.2f}M. The person is a {dataQ2.iat[0, 2]} and {ICS(dataQ2.iat[0, 1])} \n')



#Q3_________________________________________________________________

dataQ3 = data.loc[:, [1, 2, 4, 7]]

dataQ3 = dataQ3.loc[dataQ3[4] == 'DEM']

dataQ3_sum = dataQ3.loc[:, 7].mean()

print(f'(3) The Democrats spent an average of ${dataQ3_sum / 1000000:.2f}M \n')


#Q4_______________________________________________________________

dataQ4 = data.loc[:, [1, 2, 4, 7]]

dataQ4 = dataQ4.loc[data[4] == 'REP']

dataQ4_sum = dataQ4.loc[:, 7].mean()

print(f'(4) The Republicans spent an average of ${dataQ4_sum / 1000000:.2f}M \n')


#Q5________________________________________________________________

dataQ5 = data.loc[:, [1, 2, 4, 7]]

dataQ5 = dataQ5.loc[dataQ5[2] == 'I']

dataQ5_sum = dataQ5.loc[:, 7].mean()

print(f'(5) The Incumbent spent an average of ${dataQ5_sum / 1000000:.2f}M \n')


#Q6________________________________________________________________

dataQ6 = data.loc[:, [1, 2, 4, 7]]

dataQ6 = dataQ6.loc[data[2] == 'C']

dataQ6_sum = dataQ6.loc[:, 7].mean()

print(f'(6) The Challenger spent an average of ${dataQ6_sum / 1000000:.2f}M \n')

