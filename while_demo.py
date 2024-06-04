sandar = [1,3,5,7,9,12,19,21]

#1- Сандар Массивін while циклімен экранға жаздырыңыз.

# i = 0
# while (i<len(sandar)):
#     print(sandar[i])
#     i+=1
#2- Бастапқы мәні мен соңғы мәнін қолданушыдан алып
#   сол сандар аралығындағы барлық тақ сандарды экранға жазыңыз.
# bas = int(input('bastapky: '))
# son = int(input('son: '))
# i = bas
# while (i<son):
#     if i%2==1:
#         print(i)
#     i+=1

#3- 1-100 аралығындағы сандарды кему ретімен жазыңыз.
# i = 100
# while i>0:
#     print(i)
#     i-=1

#4- Қолданушыдан алған 5 санды өсу ретімен жаздырыңыз.

# sandar = []
# i = 0
# while i<5:
#     san = int(input(f'{i+1} wi san endir: '))
#     sandar.append(san)
#     i+=1
# sandar.sort()    
# print(sandar)    
#5- Қолданушыдан алатын шексіз заттардың мәліметтерін 
#-  'zattar'- массивіне сақтаңыз.
#- * Заттар санын қолданушыдан сұраңыз
#- * Dictionary массиві ('aty','bagasy') болсын.
#- * Заттарды массивке сақтаған соң тізімді for
#- Циклі арқылы экранға жаздырыңыз

# zattar = []

# wt = int(input('kanwa zat endiresiz: '))

# i = 0
# while i < wt:
#     name = input(f'{i+1} wi Zattyn aty')
#     price = input(f'{i+1} wi zattyn bagasy')
#     zattar.append({
#         'aty': name,
#         'bagasy':price
#     })
#     i+=1

# for zat in zattar:
#     print(zat)