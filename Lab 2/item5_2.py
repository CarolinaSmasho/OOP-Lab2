import json
import re

def update_records(dictionary_record, id, property, value):
    
   
   
    new_record = dictionary_record



    id = id.replace(" ", "")
    property = property.strip()
    value = value.strip()

    if int(id) <= 0:
        return "Invalid"

    if id not in new_record.keys():
        new_record[id] = {}


    if property in new_record[id] and property == "tracks":
        new_record[id][property].append(value)
    else:
        if property == "tracks":
        # value = str(value).split("\"")
            value = re.split('\" |, ', value)
        new_record[id][property] = value
    

   
    if value == "\'\'" and property == "artist":
        return "Invalid"
    elif value == "\'\'":
        new_record[id].pop(property)

    property_check=["albumTitle","artist","tracks"]
    if property not in property_check:
        return "Invalid"

    # print(dictionary_record)
    # print(id)
    # print(property)
    # print(value)
    return(new_record)



    return 0



# value = "{'2548': {'albumTitle': 'Slippery When Wet'}} | 2548 | artist | Bon Jovi"
value= input()
value =[str(e) for e in value.split("|")]

try:
    value[0] = eval(value[0].replace("'", "\""))

except:
  print("Invalid")
else:
    output = update_records(dictionary_record=value[0], id=value[1], property=value[2], value=value[3])
    print(output)