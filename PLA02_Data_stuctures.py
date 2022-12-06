#Список списков


people = [
    ["Andienko", "Yuri", 123456],
    ["Pupkin", "Vasya", 77777],
    ["Andreev", "Andrey", 30000000]
]
#print(people)

for person in people:
    #print(person)    посмотерть
    #print(f"{person[1]} {person[0]} has salary{person[2]}")   посмотерть
    print(f"{person[1]} {person[0]} has salary{person[2]}")




# Словари
print("\n Словари")
print("-------------------")
person1 =  {"lastName": "Andienko", "firstName":"Yuri","salary": 123456}
print(f"{person1['lastName']} {person1['firstName']} has salary{person1['salary']}")
print("-------------------")
print("-------------------")



# Список словарей
print("-------------------")
print("Список словарей")

people=[
    {"lastName": "Andienko", "firstName":"Yuri","salary": 123456},
    {"lastName": "Pupkin", "firstName":"Vasya","salary": 777777},
    {"lastName": "Andrey", "firstName":"Andreev","salary": 300000}
]
for p in people:
    # print(p)
    # print(f"{p['lastName']}{p['firstName']}has salary{p['salary']}")
    #print(f"{p['lastName']}\t{p['firstName']}t\has salary{p['salary']}")   \t табулятор

    print(f"{p['lastName']} {p['firstName']}has salary {p['salary']}")



print("-------------------")
print("-------------------")
print("Найти максимальныю зарплату")

# Найти максимальную зарплату
print("-------------------")
print("-------------------")
print("-------------------")


people=[
    {"lastName": "Andienko", "firstName":"Yuri","salary": 123456},
    {"lastName": "Pupkin", "firstName":"Vasya","salary": 77777},
    {"lastName": "Andrey", "firstName":"Andreev","salary": 300000}
]
for p in people:
   print(f"{p['lastName']} {p['firstName']}has salary {p['salary']}")


candidate = 0
for p in people:
    if p["salary"]>candidate:
        candidate = p["salary"]
print(candidate)



candidate = 0
for p in people:
    if p["salary"]>candidate:
        candidate = p["salary"]
print(candidate)





# Найти максимальную зарплату
print("Найти максимальную зарплату вариан 2")
print("-------------------")
print("-------------------")

#
#
# for max_sal in people:
#    if salary
#        print(max_sal)
#
#     # print(p)
#     # print(f"{p['lastName']}{p['firstName']}has salary{p['salary']}")
#     # print(f"{p['lastName']}\t{p['firstName']}t\has salary{p['salary']}")   \t табулятор
# #     p['salary']=int(p)
# #     if
# #     print(f"{p['lastName']} {p['firstName']}has salary {p['salary']}")
# #
# for x in amounts:
#     amount = int(x) #конверсия типов str то int
#     if amount>=10 and amount<100:
#         print(f"Нормальное число {amount}")