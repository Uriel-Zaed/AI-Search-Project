
import a_star_buckets_min_sol
from const import *
from bfs import BFS 
from static_functions import *
import json
from a_star_hur_additive import A_Star_Additive
from a_star_pdbi import A_Star_PDBI
from a_star_buckets_min_sol import A_Star_Buckets_Min_Sol

# # # ######################## BFS ###########################
# bfs_initial_state = "3"*num_disks_bfs

# bfs = BFS(bfs_initial_state)
# print("BFS...")
# database = bfs.solve()
# print("BFS done")

# with open(f'hanoi_pdb_{num_disks_bfs}_2_layer.txt', 'w') as convert_file: 
#      convert_file.write(json.dumps(database))

################# A* ############################
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
        a_star_buckets[bucket].extend(generate_complete_configless(config_tuple[0],config_tuple[1]))

print(a_star_buckets)

bucket_min_price = {}

for bucket in a_star_buckets.keys():
    print(f"A* bucket {bucket} starting...")
    a_star_bucketing = A_Star_Buckets_Min_Sol(a_star_buckets[bucket], str(num_towers-1)*num_disks)
    solved_node = a_star_bucketing.solve()
    a_star_bucketing_p = solved_node.g_n
    a_star_bucketing_nodes = a_star_bucketing.N

    min_state = get_initial_state(solved_node)

    a_star_bucketing_min = A_Star_Buckets_Min_Sol([min_state], str(num_towers-1)*num_disks)
    solved_node_min = a_star_bucketing_min.solve()
    a_star_bucketing_min_p = solved_node_min.g_n
    a_star_bucketing_min_nodes = a_star_bucketing_min.N


    bucket_min_price[bucket] = {"bucketing_price": a_star_bucketing_p, "bucketing_min_price":a_star_bucketing_min_p,
                                 "bucketing_nodes_N":a_star_bucketing_nodes, "num_initial_states": len(a_star_buckets[bucket]),
                                "bucketing_nodes_min_N":a_star_bucketing_min_nodes, "min_state": min_state}
    print(f"A* bucket {bucket} done...")


print(bucket_min_price)

with open(f'compare_bucket_min_price_{num_disks-num_small_disk}_{num_small_disk}_configless.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(bucket_min_price))
