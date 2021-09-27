import csv
from collections import defaultdict
import omega_index
#reading gt dataset
filename4="gt_converted.intra"
 #keys will be community id and value is a list of nodes ids
dict_node_gt={}
dict_node_gt=defaultdict(list)
with open(filename4, newline = '') as games:                                                                                          
    game_reader = csv.reader(games, delimiter='\t')
    for game in game_reader:
        dict_node_gt[game[1]].append(game[0])
#convert default dict to dict
dict_node_gt=dict(dict_node_gt)
print(dict_node_gt)

#reading ce-or dataset
filename5="ff_ceORwf_Re_ceORwf_RT-info.vcomm"
 #keys will be community id and value is a list of nodes ids
dict_node_data={}
dict_node_data=defaultdict(list)
with open(filename5, newline = '') as games:                                                                                          
    game_reader = csv.reader(games, delimiter=',')
    for game in game_reader:
        dict_node_data[game[1]].append(game[0])
#convert default dict to dict
dict_node_data=dict(dict_node_data)
print(dict_node_data)

omega = omega_index.Omega(dict_node_gt, dict_node_data)
print(omega.omega_score)
