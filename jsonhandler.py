import json
file_name = r'''C:\Users\evign\OneDrive\Documents\GitHub\vignesh_learnrepo\ex5.json'''
with open(file_name, 'r', encoding='utf-8') as file:
    ex5 = json.load(file)

    for i in ex5:
        if i['name'] == 'Old Fashioned' and i['type'] == 'donut':
            x = i['batters']['batter']

            for id in x:
                cur_id = id["id"]
                last_id = cur_id
            last_id=int(last_id) + 1
            z={ "id": last_id, "type": "Coffee" }
            x.append(z)
    print(ex5)
with open(file_name, 'w', encoding='utf-8') as out:
    json.dump(ex5,out,indent=4)