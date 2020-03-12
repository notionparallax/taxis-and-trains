import json
import os
import requests
import time

a_string = "A : Wow : So : Cool"
a = a_string[:a_string.index(":")]
print(a)

# d = {}
# list1 = []
# Triplets_List = [['a', 'b', 'c'], ['d', 'e', 'f']]
# for triplet in Triplets_List:
#     dir_url1 = "apple wow something here"
#     dir_url2 = "banana aww nothing here"
#     dir_url3 = "cherry adding more words"
#     list1 = [dir_url1, dir_url2, dir_url3]
#     # print(list1)
#     # dictionary = {triplet: list1}
#     # print(dictionary)
#     # dictionary = {triplet : dir_url1}
#     # dictionary.setdefault(triplet, []).append(dir_url2)
#     # print(dictionary)
# data = []
# for name in Triplets_List:
#     r = "The information"
#     json_data = r.json()
#     if not json_data.get("error_message"):
#         data.append(json_data)
#     else:
#         json_data["url"] = r
#         json_data["name"] = name
#         data.append({json_data})


# with open("jsontestfile", "w") as ts:
#     ts.write(json.dumps(data, indent=2))