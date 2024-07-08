
from const import *
from bfs import BFS
from static_functions import *
from a_star import A_Star
import json


######################## BFS ###########################
# goal_state = [num_towers-1 for d in range(num_disks_bfs)]

# bfs = BFS(goal_state)
# print("BFS...")
# database = bfs.solve()
# print("BFS done")

# with open(f'hanoi_database {num_disks_bfs}.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(database))

##################### A* ############################
with open(f'hanoi_database {num_small_disk}.txt', "r") as file:
    fileData  = file.read()
    database = json.loads(fileData)

price_buckets = {} # key = price, value = (conig,allowed pegs)

for config in database.keys():
    if database[config][0] not in price_buckets.keys():
        price_buckets[database[config][0]] = [(config, database[config][1])]
    else:
        price_buckets[database[config][0]].append((config, database[config][1]))

print(price_buckets)


a_star_buckets = {}

for bucket in price_buckets.keys():
    a_star_buckets[bucket] = []
    for config_tuple in price_buckets[bucket]:
        a_star_buckets[bucket].extend(generate_complete_config(config_tuple[0],config_tuple[1]))

print(a_star_buckets)

bucket_min_price = {}

for bucket in a_star_buckets.keys():
    print(f"A* bucket {bucket} starting...")
    a_star = A_Star(a_star_buckets[bucket], str(num_towers-1)*num_disks, database)
    p = a_star.solve()
    bucket_min_price[bucket] = p
    print(f"A* bucket {bucket} done...")


print(bucket_min_price)

with open(f'bucket_min_price {num_disks_bfs}.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(database))
