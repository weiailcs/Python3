import json
friend={'李尧':'20171002127'}
with open('frienddata.json','w') as file:
  json.dump(friend,file)

with open("frienddata.json") as file1:
    sb=json.load(file1)

for name in  friend.keys():
    print(name)


print(sb)
