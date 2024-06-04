#1- Қолданушыдан атын, жасын және алған білімі туралы мәліметтерді
#   сұрап, жүргізуші куәлігін ала алатынын біліңіз. Жүргізуші куәлігін алу шарты:
#    жасы ең кіші 18 және білімі колледж немесе университет болу керек
# aty = input('atynyz: ')
# jasy = int(input('jasynyz: '))
# bilimi = input('biliminiz: ')

# if(jasy >= 18):
#     if (bilimi == 'kolledj' or bilimi == 'universitet'):
#         print(f'{aty} siz jurgizuwi kualigin ala alasiz')
#     else:
#         print(f' {aty} biliminiz jetkiliksiz')
# else:
#     print(f'{aty} jasynyz jetkiliksiz')    
#2- Бір студенттің 2 жазбаша, 1 ауызша алған бағаларын сұрап, орташа бағаны есептеп
#   Төмендегі кесте бойынша бағасын экранға шығарыңыз:
#   0-24   =>0
#   25-44  =>1
#   45-54  =>2
#   55-69  =>3
#   70-84  =>4
#   85-100 =>5

# jazbawa1 = float(input('jazbawa baga 1: '))
# jazbawa2 = float(input('jazbawa baga 2: '))
# auizwa = float(input('auizwa: '))
# ortawa = (jazbawa1 + jazbawa2 + auizwa)/3
# if ortawa>=0 and ortawa<25:
#     print('0')
# elif ortawa>=25 and ortawa<45:
#     print('1')    
# elif ortawa>=45 and ortawa<55:
#     print('2')    
# elif ortawa>=55 and ortawa<70:
#     print('3')
# elif ortawa>=70 and ortawa<85:
#     print('4')   
# elif ortawa>=85 and ortawa<=100:
#     print('5')
# else:
#     print('kate baga endirdiniz')                         
#3- Сақтандыру полисіне жазылған автокөліктің сақтандырылған уақытын алып
#   3 жылдық сервистің қай жылында екенін анықтаңыз:
#   1 ші жыл - сервис 
#   2 ші жыл - сервис
#   3 ші жыл - сервис
#*Есепті алынған күн ай жыл мәліметтерін күн арқылы есептеңіз
#*datetime модулін қолдануыңыз керек
# Мысалы: (26-05-2024) - (15-04-2018) => күн
# import datetime

# kun = input('saktandiru datasin endir: (2024-5-26) ')
# kun = kun.split('-')

# data = datetime.datetime.now()
# bugun = datetime.datetime(int(kun[0]),int(kun[1]),int(kun[2]))
# kunder = data - bugun
# days = kunder.days

# if days<=365:
#     print(f'{days} kun 1 wi servis jili')
# elif days>365 and days<=365*2:
#     print(f'{days} kun 2 wi servis jili')
# elif days>365*2 and days <= 365*3:
#     print(f'{days} kun 3 wi servis jili')
# else:
#     print('duris kun endiriniz')            

