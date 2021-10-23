import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
# print(sites[0])
# print(sites_new[0])

for index in range(0, len(sites_new)):
    sum = sum + sites_new[index]['size']

sum_gb = round(sum / 1024, 2)
print(f'Total size is {sum_gb} Gb')

avg = round(sum_gb / len(sites_new), 2)
print(f'Average size is {avg} Gb\n')

for index in range(0, len(sites_new)):
    change = 0
    if sites[index]['size'] != sites_new[index]['size']:
        change = sites_new[index]['size'] - sites[index]['size']
        change_percentage = change / sites_new[index]['size'] * 100

        print("{0} changed by {1:+.2f}%".format(sites[index]["domain"],
                                                change_percentage))

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] == 0:
        empty_sites = empty_sites + 1
print(f'\nNumber of empty sites is {empty_sites}\n')

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] > 0:
        if sites_new[index]['size'] < 1024:
            print(f'{sites[index]["domain"]} is {sites_new[index]["size"]} Mb')
        if sites_new[index]['size'] >= 1024:
            print(
                f'{sites[index]["domain"]} is {round(sites_new[index]["size"]/1024, 2)} Gb'
            )
