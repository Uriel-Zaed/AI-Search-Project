
from const import *
from bfs import BFS
from static_functions import *
import json
from a_star_hur_additive import A_Star_Additive
from a_star_pdbi import A_Star_PDBI

# ######################## BFS ###########################
# goal_state = [num_towers-1 for d in range(num_disks_bfs)]

# bfs = BFS(goal_state)
# print("BFS...")
# database = bfs.solve()
# print("BFS done")

# with open(f'hanoi_pdb_{num_disks_bfs}.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(database))

##################### A* ############################
# with open(f'hanoi_database {num_small_disk}.txt', "r") as file:
#     fileData  = file.read()
#     database = json.loads(fileData)

# price_buckets = {} # key = price, value = (conig,allowed pegs)

# for config in database:
#     if database[config][0] not in price_buckets.keys():
#         price_buckets[database[config][0]] = [(config, database[config][1])]
#     else:
#         price_buckets[database[config][0]].append((config, database[config][1]))

# print(price_buckets)


# a_star_buckets = {}

# for bucket in price_buckets.keys():
#     a_star_buckets[bucket] = []
#     for config_tuple in price_buckets[bucket]:
#         a_star_buckets[bucket].extend(generate_complete_config(config_tuple[0],config_tuple[1]))

# print(a_star_buckets)

# bucket_min_price = {}

# for bucket in a_star_buckets.keys():
#     print(f"A* bucket {bucket} starting...")
#     a_star = A_Star(a_star_buckets[bucket], str(num_towers-1)*num_disks, database)
#     p = a_star.solve()
#     bucket_min_price[bucket] = p
#     print(f"A* bucket {bucket} done...")


# print(bucket_min_price)

# with open(f'bucket_min_price {num_disks_bfs}.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(bucket_min_price))

##################### creating strong hur ######################
# strong_hur = {} # hur for 8 disk

# with open(f'hanoi_database 8.txt', "r") as file:
#     fileData  = file.read()
#     database8 = json.loads(fileData)

# with open(f'hanoi_database 4.txt', "r") as file:
#     fileData  = file.read()
#     database4 = json.loads(fileData)

# # with open(f'bucket_min_price 8.txt', "r") as file:
# #     fileData  = file.read()
# bucket_min_price8 = {0: 0, 1: 7, 2: 9, 3: 11, 4: 13, 5: 15, 6: 17, 7: 19, 8: 20, 9: 24}

# for config in database8.keys():
#     price_pdb4 = database4[config[num_small_disk:]][0]
#     strong_hur[config] = bucket_min_price8[price_pdb4]

# with open(f'strong_hur 8.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(strong_hur))

######################## checking admissablity ######################
# with open(f'strong_hur 8.txt', "r") as file:
#     fileData  = file.read()
#     strong_hur8 = json.loads(fileData)

# with open(f'hanoi_database 8.txt', "r") as file:
#     fileData  = file.read()
#     database8 = json.loads(fileData)

# for config in strong_hur8.keys():
#     if strong_hur8[config] > database8[config][0]:
#         print(f"Error with config: {config}")

# print("finnish")

# ###################### compper between hur ###################
# a_star_double4 = A_Star_Double4([str(0)*num_disks], str(num_towers-1)*num_disks)
# print(f"a_star_double4 price: {a_star_double4.solve()}")
# print(f"a_star_double4 nodes: {a_star_double4.N}")
# a_star_strong = A_Star_Strong([str(0)*num_disks], str(num_towers-1)*num_disks)
# print(f"a_star_strong price: {a_star_strong.solve()}")
# print(f"a_star_strong nodes: {a_star_strong.N}")


########################## test for better strong hur ##########
# with open(f'hanoi_database {num_small_disk}.txt', "r") as file:
#     fileData  = file.read()
#     database = json.loads(fileData)

# price_buckets = {} # key = price, value = (conig,allowed pegs)

# for config in database.keys():
#     if database[config][0] not in price_buckets.keys():
#         price_buckets[database[config][0]] = [(config, database[config][1])]
#     else:
#         price_buckets[database[config][0]].append((config, database[config][1]))

# print(price_buckets)


# a_star_buckets = {}

# for bucket in price_buckets.keys():
#     a_star_buckets[bucket] = []
#     for config_tuple in price_buckets[bucket]:
#         a_star_buckets[bucket].extend(generate_complete_config(config_tuple[0],config_tuple[1]))

# print(a_star_buckets)

# bucket_min_price = {}

# for bucket in a_star_buckets.keys():
#     print(f"A* bucket {bucket} starting...")
#     a_star = A_Star_Better_Hur(a_star_buckets[bucket], str(num_towers-1)*num_disks, database)
#     p = a_star.solve()
#     bucket_min_price[bucket] = p
#     print(f"A* bucket {bucket} done...")


# print(bucket_min_price)

# with open(f'bucket_min_price_better_hur {num_disks_bfs}.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(bucket_min_price))

# better_hur = {} # hur for 8 disk

# with open(f'hanoi_database 8.txt', "r") as file:
#     fileData  = file.read()
#     database8 = json.loads(fileData)

# with open(f'hanoi_database 4.txt', "r") as file:
#     fileData  = file.read()
#     database4 = json.loads(fileData)

# with open(f'bucket_min_price_better_hur {num_disks_bfs}.txt', "r") as file:
#     fileData  = file.read()
#     bucket_min_price_better_hur = json.loads(fileData)

# for config in database8.keys():
#     price_pdb4 = database4[config[num_small_disk:]][0] 
#     better_hur[config] = bucket_min_price_better_hur[str(price_pdb4)] + database4[config[:num_small_disk]][0] 

# with open(f'better_hur 8.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(better_hur))

# with open(f'better_hur 8.txt', "r") as file:
#     fileData  = file.read()
#     better_hur8 = json.loads(fileData)

# with open(f'hanoi_database 8.txt', "r") as file:
#     fileData  = file.read()
#     database8 = json.loads(fileData)

# for config in better_hur8.keys():
#     if better_hur8[config] > database8[config][0]:
#         print(f"Error with config: {config}")

# print("finnish")