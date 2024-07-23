
from const import *
from bfs import BFS
from static_functions import *
import json
from a_star_hur_additive import A_Star_Additive
from a_star_pdbi import A_Star_PDBI
from a_star_buckets import A_Star_Buckets
from a_star_buckets_pdbi import A_Star_Buckets_PDBI


################### A* ############################
with open(f'hanoi_pdb_{num_disks-num_small_disk}.txt', "r") as file:
    fileData  = file.read()
    database = json.loads(fileData)

price_buckets = {} # key = price, value = (conig,allowed pegs)

for config in database: # buckets creating
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
    a_star_bucketing = A_Star_Buckets(a_star_buckets[bucket], str(num_towers-1)*num_disks)
    p = a_star_bucketing.solve()
    bucket_min_price[bucket] = p
    print(f"A* bucket {bucket} done...")


print(bucket_min_price)

with open(f'bucket_min_price_{num_disks-num_small_disk}.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(bucket_min_price))

################### creating strong hur ######################
pdbi_hur = {} 

with open(f'hanoi_pdb_{num_disks-num_small_disk}.txt', "r") as file:
    fileData  = file.read()
    database_big = json.loads(fileData)

with open(f'bucket_min_price_{num_disks-num_small_disk}.txt', "r") as file:
    fileData  = file.read()
    bucket_min_price = json.loads(fileData)

for config_big in database_big.keys():
    price_pdb = database_big[config_big][0]
    pdbi_hur_price = bucket_min_price[str(price_pdb)]
    full_configs = generate_complete_config(config_big,[p for p in range(num_towers)])
    for f_config in full_configs:
        pdbi_hur[f_config] = pdbi_hur_price

with open(f'pdbi_hur_{num_disks-num_small_disk},{num_small_disk}.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(pdbi_hur))

# ####################### checking admissablity ######################
# with open(f'pdbi_hur_{num_disks-num_small_disk},{num_small_disk}.txt', "r") as file:
#     fileData  = file.read()
#     pdbi_hur = json.loads(fileData)

# with open(f'hanoi_pdb_{num_disks}.txt', "r") as file:
#     fileData  = file.read()
#     hanoi_pdb = json.loads(fileData)

# for config in pdbi_hur.keys():
#     if pdbi_hur[config] > hanoi_pdb[config][0]:
#         print(f"Error with config: {config}")
#         print(f"pdbi_hur[config]: {pdbi_hur[config]}")
#         print(f"hanoi_pdb[config][0]: {hanoi_pdb[config][0]}")

# print("finnish")


############################# comperation ##############################

print(f"Num of small disk: {num_small_disk}")
a_star_additive = A_Star_Additive(str(0)*num_disks, str(num_towers-1)*num_disks)
print(f"a_star_additive price: {a_star_additive.solve()}")
print(f"a_star_additive nodes: {a_star_additive.N}")
a_star_pdbi = A_Star_PDBI(str(0)*num_disks, str(num_towers-1)*num_disks)
print(f"a_star_pdbi price: {a_star_pdbi.solve()}")
print(f"a_star_pdbi nodes: {a_star_pdbi.N}")
