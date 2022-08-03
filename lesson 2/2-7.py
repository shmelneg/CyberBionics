lenght = 700
velocity = 90
time = lenght / velocity
print(time)

#more suitable format
hours = lenght // velocity
minutes = round((lenght % velocity) * 60 / velocity)
print("The time of the trip will be {0} hours and {1} minutes".format(hours, minutes))