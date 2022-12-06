# Конкатенация строк
s1 = "Vladimir"
s2 = "Rud"
s3 = s1 +" " + s2
print(s3)
s4 = s2 + ", " + s1
print(s4)


# Именование переменных
first_name = "Vladimir"
last_name = "Rud"
full_name = first_name + " " + last_name
print(full_name)
first_letter = first_name[0]                         # это срез
name_with_initial = first_letter+ "." + last_name
print(name_with_initial)


# Разборка строки
full_name = "Vladimir Rud"
first_name = full_name [0:8]
last_name = full_name [9:]
name2=last_name + ", " + first_name
print(first_name)
print(last_name)
print(name2)

print()
print("-------------")


full_name = "Vladimir0000000000 Rud"
space_index = full_name.index(" ")
print("Вывод пробела")
print(space_index)
first_name = full_name [0:space_index]
last_name = full_name [space_index + 1:]
name2=last_name + ", " + first_name
print(name2)


print("----+++-----")

otchestvo = "Victorovich"
name3=last_name + ", " + first_name + " " + otchestvo
print(name3)


print("+++++++++++----+++-----")

# f - строка
otchestvo = "Victorovich"
#name3=last_name + ", " + first_name + " " + otchestvo
name3 = f"{last_name}, {first_name} {otchestvo}"
print(name3)



#  Закоментировать блок Ctrl + "/ "




first_name_1 = first_name[0]                         # это срез
last_name_1 = last_name[0]                              # это срез
name4 = first_name_1+ ". "+ last_name_1 + "." + otchestvo

print("Инициалы + Отчество")
print(name4)



print("Инициалы + Отчество   вариант 2 ")
name5 =f"{first_name[0]}.{otchestvo [0]}.{last_name}"
print(name5)




# Ветвление  (условный "Если" оператор)
amount = 1
if amount <10:
    print("Малова-то будет")
    print("Овёс нынче дорог")
if amount >=10 and amount<100 :
    print("Нормально")
    print("Спасибо")
if amount >=100:
    print("Премного благодарен")
    print("Приходите ещё")

#print("Анализ окончен!!!")

# Циклы и множественные данные (списки, массивы)

amounts = [1,123,55,77,888,5551,55,55]
amounts.append(8)   # Добавляем в массив
print(amounts[1])   # Вывести 2 элемент списка
print(amounts)      # Вывести весь список


print("-------------")


for x in amounts:   # Вывести весь список
    print(x)




for x in amounts:   #Анализируем сумму 8.....
    print(f"Анализируем сумму {x}.....")




# Анализируем сумму 1.....
# Малова-то будет
# Овёс нынче дорог



for x in amounts:   #А.
    print(f"Анализируем сумму {x}.....")
    if x < 10:
        print("Малова-то будет")
        print("Овёс нынче дорог")

    if x >= 10 and x < 100:
        print("Нормально")
        print("Спасибо")

    if x >= 100:
        print("Премного благодарен")
        print("Приходите ещё")


print("Анализ завершён")


# Пользовательский ввод
# База данных
# Web API
amounts = [1,123,55,77,888,5551,55,55]
amounts.append(8)   # Добавляем в массив
print(amounts[1])   # Вывести 2 элемент списка
print(amounts)      # Вывести весь список


print("-------------")




























