#dictionary seperti array
# costumer = {"name" : "pani" , "age" : "26" , "adrdess" : "Bandung"}

# name = costumer["name"]
# print(name)

# for key in costumer:
#     value = costumer [key]
#     print(f"{key} : {value}")
# print("=====================")
    
#menggunakan banyak data
costumers = [
    {"name" : "Yendra" , "age" : 16,"adress" : "Sumba"},
    {"name" : "Ravael" , "age" : 15,"adress" : "Manado"},
    {"name" : "Randy" , "age" : 100,"adress" : "Jayapura"}
]

for costumer in costumers:
    for key,value in costumer.items(): #items digunakan untuk menyederhanakan  "value = costumer [key]"
        print(f"{key} : {value}")
    print("========================")
    
for key in costumer:
    value = costumer [key]
    print(f"{key} : {value}")
print("=====================")