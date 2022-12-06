f = open("Data/people.txt", "r")
text = f.read()
zpt_index = text.index(",")
first_name=text[:zpt_index]
print(first_name)



#
first_name_1let = f"{text[0]}"
print(first_name_1let)
for x in text:
    print(text)
#      if "А" in first_name[0]:
#          print(text)
f.close()
#         #print("Овёс нынче дорог")
#     #
#     # if x >= 10 and x < 100:
#     #     print("Нормально")
#     #     print("Спасибо")
#     #
#     # if x >= 100:
#     #     print("Премного благодарен")
#     #     print("Приходите ещё")
#
#
# # print("Анализ завершён")
#
#
#
#
#
#
# #print(text)



print("\n  \n РЕШЕНИЕ")


f = open("Data/people.txt", "r")
text = f.read()
people = text.split("\n") #перевод на новую строку \n
print(people)

for person in people:
    if person[0]=="А":
        print(person)
f.close()





print("\n  \n РЕШЕНИЕ №2")


f = open("Data/people.txt", "r")
text = f.read()
people = text.split("\n") #перевод на новую строку \n
print(people)

for person in people:
    if person.startswith("A"):
        print(person)
f.close()





print("\n  \n РЕШЕНИЕ №3")


f = open("Data/people.txt", "r", encoding="utf-8")
text = f.read()
f.close()

people = text.split("\n") #перевод на новую строку \n
print(people)

for person in people:
    if person.startswith("A"): # буква "А" русская!!!!!!
        print(person)







print("\n  \n РЕШЕНИЕ №4")


f = open("Data/people.txt", "r", encoding="utf-8")
text = f.read()
f.close()

people = text.split("\n") #перевод на новую строку \n
#print(people)

# Вывести в формате Юрий Андриенко
for person in people:
    splitted = person.split(", ")
    first_name=splitted[1]
    last_name=splitted[0]
    #print(splitted)
    if person.startswith("A"): # буква "А" русская!!!!!!
        print(f"{first_name} {last_name}")