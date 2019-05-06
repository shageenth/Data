import matplotlib.pyplot as plt
import csv
cond = True
Generation_count = {}
Gen_numbers = {}
Country_count = {}

with open('master.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        Generation = line[11]
        Country = line[0]
        if Generation in Generation_count:
            Generation_count[Generation] += int(line[5])
        else:
            Generation_count[Generation] = int(line[5])
        if Country in Country_count:
            Country_count[Country] += int(line[5])
        else:
            Country_count[Country] = int(line[5])

x = []
y = []
z = []
w = []
for key in Generation_count:
    y.append(Generation_count[key])
    x.append(key)
for key in Country_count:
    w.append(Country_count[key])
    z.append(key)
plt.bar(x,y)

plt.show()


