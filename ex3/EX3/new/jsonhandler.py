import json

def write():
    with open('C:/Users/evign/OneDrive/Documents/GitHub/vignesh_learnrepo/ex3/EX3/new/EX5.json','r') as file:
        ex5=json.load(file)

    for x in ex5:
        if x['type'] == "donut" and x['name'] == 'Old Fashioned':
            x['batters']['batter'].append({'id': '1003', 'type': 'Coffee'})

    with open('C:/Users/evign/OneDrive/Documents/GitHub/vignesh_learnrepo/ex3/EX3/new/EX5+.json','w') as file:
        json.dump(ex5,file,indent=4)

def show_the_write():
    write()
    with open('C:/Users/evign/OneDrive/Documents/GitHub/vignesh_learnrepo/ex3/EX3/new/EX5+.json','r') as file:
        data=json.load(file)
    file.close()
    return data