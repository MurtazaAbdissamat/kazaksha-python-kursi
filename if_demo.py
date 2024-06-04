"""
Ендірілген санның 0-100 арасында екенін анықтаңыз
a = float(input("san = "))

if(a > 0) and (a<=100):
    print('san 0-100 araliginda')
else:
    print('san 0-100 arasinda emes')  

"""
"""
Ендірілген санның оң және жұп сан екенін анықтаңыз
a = float(input("san = "))

if(a > 0):
    if (a % 2 == 0):
        print("on jane jup san")
    else:
        print('on jane tak san')
else:
    print('teris san') 

"""
"""
Логин Парольді тексеріп кіруді тексеріңіз
login = 'email@makedev.com'
password = 'abc123'

endirgenMail = input("email: ")
endirgenPassword = input("password: ")
if(endirgenMail == login):
    if (endirgenPassword == password):
        print('saitka kiru orindaldi')
    else:
        print('parol kate! kaita engiziniz')    
else:
    print('login kate! kaita engiziniz')  
"""
 
"""
Ендірілген 3 санның ең үлкенін табыңыз
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if(c>b):
    if (c>a):
        print('c ulken')
elif(a>b):
    if(a>c):
        print('a ulken')
elif(b>a):
    if (b>c):
        print('b ulken')
"""
"""
Қолданушыдан 2 блок бағасын, 1 емтихан бағасын алып орташа бағасын есептеңіз
Егер орташа баға 50 және одан үлкен болса өтті, кіші болса қалды деп жаздырыңыз
А) Орташа баға 50 болса да, емтихан бағасы ең төменгі бағасы 50 болу керек
Б) Емтиханнан 70 алса орташа бағаның керегі болмасын, бірден өтті деп шығару керек
blok1 = float(input('blok 1 = '))
blok2 = float(input('blok 2 = '))
emtihan = float(input('emtihan = '))

ortawa = (((blok1 + blok2) / 2) * 0.6) + (emtihan * 0.4)
if(ortawa >= 50):
    if (emtihan>=50):
        print(f'{ortawa} ottiniz')
    else:
        print(f'emtihannan otpediniz bagasy {emtihan}')    
else:
    print(f"otpediniz ortawa baganyz {ortawa}")
"""
"""
Қолданушының аты, салмағы, бойының мәндерін алып салмақ индексін есептеңіз
Формула (салмақ / бойының ұзындығының квадраты)
Төмендегі кесте бойынша қай топқа жататынын анықтаңыз
0-18.4     Арық
18.5-24.9  Орташа
25.0-29.9  Артық салмақ
30.0-34.9  Семіздік (Обез)
name = input("atynyz: ")
boy = float(input('boiynyz:'))
salmak = float(input('salmaginiz: '))

formula = (salmak)/(boy ** 2)

if(formula>=0) and (formula<=18.4):
    print('Арық')
elif(formula>18.4) and (formula<=24.9):
    print('Орташа')
elif(formula>24.9) and (formula<=29.9):
    print('Артық салмақ')
elif(formula>29.9) and (formula<=34.9):
    print('Семіздік (Обез)')   
"""
     