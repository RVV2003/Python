# Прочитать текст из текстового файла
# "D:\Документы\Рабочий стол\LL-104\venv\Scripts\python.exe" "D:\Документы\Рабочий стол\LL-104\pla01_files.py"
# 123
# 12
# 1
# 7
# 55
# 685
# 59
# ..
f = open("Data/amounts.txt", "r")
text = f.read()
print(text)
f.close()

# Пример записи в файл
# Hello, World!
# Good bye, World!

f1=open("Data/result.txt", "w")
f1.write("Hello, World!\n")
f1.write("Good bye, World!")
f1.close()
#----------

f1=open("Data/result.txt", "w")
f1.write("Hello, World!\n" "Good bye, World!")
#f1.write("Good bye, World!")
f1.close()




#Далее текст требуется разобрать для обработки
#['123', '12', '1', '7', '55', '685', '59', '46', '35', '44']
amounts = text.split("\n") #перевод на новую строку \n
print(amounts)


#Далее текст требуется разобрать для обработки
#amounts = text.split("\n") #перевод на новую строку \n
# чисоло 123
# чисоло 12
# чисоло 1
# чисоло 7
# чисоло 55


print(amounts)
for x in amounts:
    print(f"число {x}")

#----------++++++++++++-------------

amounts = text.split("\n") #перевод на новую строку \n
print(amounts)



#Обрабатываем разобранные данные - находим нормальные числа <>
for x in amounts:
    amount = int(x) #конверсия типов str то int
    if amount>=10 and amount<100:
        print(f"Нормальное число {amount}")




#Обрабатываем разобранные данные - находим нормальные числа <> и записываем их в файд
for x in amounts:
    amount = int(x) #конверсия типов str то int
    if amount>=10 and amount<100:
        print(f"Нормальное число {amount}")
        f.write(str(amount)+ ";")
f.close()
