# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate([data, new_record])
#Code starts here



# --------------
#Code starts here
age = census[:,0]

max_age = max(age)
min_age = min(age)
age_mean = sum(age)/len(age)
age_std = np.std(age)



# --------------
#Code starts here
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

# Lenght of Race
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

# Minimum no. of citizens
_temparr = [len_0,len_1,len_2,len_3,len_4]

# Minority race
minority_race = _temparr.index(min(_temparr))



# --------------
#Code starts here
senior_citizens = census[census[:, 0] > 60]

#Total working hours of all senior citizens
working_hours_sum = sum(senior_citizens[:,6])

#senior citizen's count
senior_citizens_len = len(senior_citizens)

#average working hours per citizen
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

#Average pay high
avg_pay_high= np.mean(high[:,7])
print (avg_pay_high)

#Average pay low
avg_pay_low= np.mean(low[:,7])
print (avg_pay_low)



