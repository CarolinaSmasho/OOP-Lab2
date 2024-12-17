import json
import re

def update_records(dictionary_record, id, property, value):
    new_record = dictionary_record

    id = id.replace(" ", "")
    property = property.strip()
    value = value.strip()


    if property in new_record[id] and property == "tracks":
        new_record[id][property].append(value)
    else:
        if property == "tracks":
        # value = str(value).split("\"")
            value = re.split('\" |, ', value)
        new_record[id][property] = value
    

    if value == "\'\'":
        new_record[id].pop(property)

  

    # print(dictionary_record)
    # print(id)
    # print(property)
    # print(value)
    return(new_record)



    return 0

#"{'2548': {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi'}} | 2548 | tracks | Wanted Dead or Alive"
# "{'2548': {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi', 'tracks': ['Wanted Dead or Alive']}}"

# value = "{'2548': {'albumTitle': 'Slippery When Wet'}} | 1 | artist | Bon Jovi"
value= input()
value =[str(e) for e in value.split("|")]
value[0] = eval(value[0].replace("'", "\""))
output = update_records(dictionary_record=value[0], id=value[1], property=value[2], value=value[3])
print(output)