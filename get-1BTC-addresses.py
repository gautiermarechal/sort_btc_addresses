import csv
import json

data = []
with open('btc_balance_sorted.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    total_addresses = 28000000.0
    counter_100_Max = 0
    counter_10_100 = 0
    counter_1_10 = 0
    counter_0_1_1 = 0
    for row in csv_reader:
        if int(row[1]) >= 10000000000:
            print(int(row[1]))
            counter_100_Max += 1
        elif int(row[1]) < 10000000000 and int(row[1]) >= 1000000000:
            print(int(row[1]))
            counter_10_100 += 1
        elif int(row[1]) < 1000000000 and int(row[1]) >= 100000000:
            print(int(row[1]))
            counter_1_10 += 1
        elif int(row[1]) < 100000000 and int(row[1]) >= 10000000:
            print(int(row[1]))
            counter_0_1_1 += 1
        else:
            break

min_0_1_addresses = total_addresses - (counter_100_Max + counter_10_100 + counter_1_10 + counter_0_1_1)
proportion_100_Max = float(counter_100_Max/total_addresses) * 100
proportion_10_100 = float(counter_10_100/total_addresses) * 100
proportion_1_10 = float(counter_1_10/total_addresses) * 100
proportion_0_1_1 = float(counter_0_1_1/total_addresses) * 100
proportion_Min_0_1 = float(min_0_1_addresses/total_addresses) * 100

print('Total addresses: ' + str(total_addresses))
print('100Max addresses :' + str(counter_100_Max))
print('Proportion :' + str(proportion_100_Max))


data.append({'range': '100-Max BTC', 'no_addresses': counter_100_Max, 'Proportion': ("%.2f" % proportion_100_Max)})
data.append({'range': '10-100 BTC', 'no_addresses': counter_10_100, 'Proportion': ("%.2f" % proportion_10_100)})
data.append({'range': '1-10 BTC', 'no_addresses': counter_1_10, 'Proportion': ("%.2f" % proportion_1_10)})
data.append({'range': '0.1-1 BTC', 'no_addresses': counter_0_1_1, 'Proportion': ("%.2f" % proportion_0_1_1)})
data.append({'range': 'Min-0.1 BTC', 'no_addresses': min_0_1_addresses, 'Proportion': ("%.2f" % proportion_Min_0_1)})

        
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
