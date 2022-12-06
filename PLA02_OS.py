# Модули
print("-----------------")

import os
#модуль для работы со времением

import datetime





print(os.name)

print("-----------------")
#изменяе кодировку chcp
# os.system("СHCP 65001")

# Запуск калькулятора
# cmd = "calc"
# os.system(cmd)
# print("-----------------")
# Запуск команды dir
# cmd1 = "dir"
# os.system(cmd1)

print("Ping------------------")
#ping
# hosts=["127.0.0.1","ya.ru","192.190.1.1", "bad.bad", "192.168.11.1"]
# for host in hosts
# host = "127.0.0.1"
# cmd3 = f"ping {hosts}"
# os.system(cmd3)

hosts = ["127.0.0.1", "ya.ru", "192.190.1.1", "bad.bad", "192.168.11.1"]
# for host in hosts:
#     cmd3 = f"ping {host}"
#     os.system(cmd3)
# print("Снифер-----------------")

# Диапазон              снифер
# base = "192.168.11.1"
# for i in range(1,10):
#     host=f"{base}{i}"
#     cmd4=f"ping {host}"
#     os.system(cmd4)
#
# print("-Не только пинг----------------")
# for host in hosts:
#     cmd5 = f"ping {host}"
#     result = os.popen(cmd5).read().encode("windows-1251").decode("866")   # изменение кодировки
#     print("---------------")
#     if result.find("TTL")>0:               # варианты          result.count     result.index
#         print(f"{host} is good")
#     else:
#         print(f"{host} is BAD")
#         # print(result)

#
#
#
# print("-Не только пинг----------------")
# for host in hosts:
#     cmd5 = f"ping {host}"
#     result = os.popen(cmd5).read().encode("windows-1251").decode("866")   # изменение кодировки
#     print("---------------")
#     if result.find("TTL")>0:               # варианты          result.count     result.index
#         # print(f"{host} is good")          # пропустить действия pass
#         pass
#     else:
#         print(f"{host} is BAD")
#         # print(result)
#
#



#
# print("--------------write to LOG----------------")
# for host in hosts:
#     cmd5 = f"ping {host}"
#     result = os.popen(cmd5).read().encode("windows-1251").decode("866")   # изменение кодировки
#     print("---------------")
#     if result.find("TTL")>0:               # варианты          result.count     result.index
#         # print(f"{host} is good")          # пропустить действия pass
#         pass
#     else:
#         now = datetime.datetime.now()   #текущее время
#         print(f"{now}\t{host}\t is BAD")
#         f=open("Data/log.txt", "a", encoding="utf-8")
#         f.write(f"{now}\t{host} is BAD\n")
#         f.close()
#
#         # print(result)
#

# насройки для Linux ttl + cmd = f"ping {host} -c1"
#  result.upper().find("TTL")>0:     в верхний регистр


#
# в начале еще можно
# if os.path.isfile('data/log.txt'): os.remove('data/log.txt')





#
# # чтение из файла
# f=open("Data/hosts.txt")
# hosts=f.read().split("\n")
# f.close()


# # чтение из файла вариант №2
with open("Data/hosts.txt") as f:
    hosts=f.read().split("\n")

print("--------------write to LOG1----------------")
for host in hosts:
    cmd5 = f"ping {host}"
    result = os.popen(cmd5).read().encode("windows-1251").decode("866")   # изменение кодировки
    print("---------------")
    if result.find("TTL")>0:               # варианты          result.count     result.index
        # print(f"{host} is good")          # пропустить действия pass
        pass
    else:
        now = datetime.datetime.now()   #текущее время
        print(f"{now}\t{host}\t is BAD")
        with open("Data/log.txt", "a", encoding="utf-8") as f:   #close не нужно
            f.write(f"{now}\t{host} is BAD\n")














# про пинги
# для винды cmd = f"ping {base}{i} -n 1"