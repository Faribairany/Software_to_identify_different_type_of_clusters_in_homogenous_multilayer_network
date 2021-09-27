import csv
from collections import defaultdict
#reading the top 20 node with high degree
#reading the input file 
#keys will be community id and value is a list of nodes ids
dict_node={}
dict_node=defaultdict(list)
#filename= "test.vcomm"   
filename="Light_ceORwf_Weather_ceORwf_RoadSurface-louvain.vcomm"
with open(filename, newline = '') as games: 
    next(games)                                                                                         
    game_reader = csv.reader(games, delimiter=',')
    for game in game_reader:
        dict_node[game[1]].append(game[0])


#dict that stores the number of nodes in each community
print("Total no of communities")
Total_no_of_com=len(dict_node)
print(Total_no_of_com)
#convert default dict to dict
dict_node=dict(dict_node)
#print(dict_node)      

#keys are comm ids and value is number of nodes in each comm
dict_com_size={}
for keys in dict_node:
    dict_com_size[keys]=len(dict_node[keys])


#size of largest community
first_max_value=sorted(dict_com_size.values())[-1]

print("Size of largest com")
print(first_max_value)

#size of second largest community
sec_max_value=sorted(dict_com_size.values())[-2]
print("Size of sec largest com")
print(sec_max_value)

#ratio of size of sec largest com to size of first largest com
ratio=sec_max_value/first_max_value

print("ratio of size of sec largest com by size of first largest com")
print(ratio)
#no of singleton community, find all com with size 1
# Using loop
# Selective key values in dictionary
k=1
No_of_singleton_community = 0
for key in dict_com_size:
    if dict_com_size[key] == k:
        No_of_singleton_community = No_of_singleton_community + 1


print("No_of_singleton_community")
print(No_of_singleton_community)

print("No of non-singleton community")
No_of_non_singleton_community=Total_no_of_com-No_of_singleton_community
print(No_of_non_singleton_community)

#percentage of singleton community
print(No_of_singleton_community/Total_no_of_com)

#print size of the largest community
#dict that stores the number of nodes in each community
#print("No of node in each community")
#print(dict_com_size)