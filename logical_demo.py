#1 Ендірілген санның 0-100 арасында екенін анықтаңыз
# a = float(input("san = "))

# result = (a > 0) and (a<=100)

# print(f'san 0-100 araliginda ma: {result}')

#2 Ендірілген санның оң және жұп сан екенін анықтаңыз

# a = float(input("san = "))

# result = (a > 0) and (a % 2 == 0)

# print(f"san on jane jup san ba: {result}")

#3 Логин Парольді тексеріп кіруді тексеріңіз
# login = 'email@makedev.com'
# password = 'abc123'

# endirgenMail = input("email: ")
# endirgenPassword = input("password: ")
# result = (endirgenMail == login) and (endirgenPassword == password)

# print(f'login parol durus pa: {result}')

#4 Ендірілген 3 санның ең үлкенін табыңыз
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# ulken1 = (a>b)and(a>c)
# print(f'a en ulken san {ulken1}')
# ulken2 = (b>a)and(b>c)
# print(f'b en ulken san {ulken2}')
# ulken3 = (c>b)and(c>a)
# print(f'a en ulken san {ulken3}')

#5 Қолданушыдан 2 блок бағасын, 1 емтихан бағасын алып орташа бағасын есептеңіз
# Егер орташа баға 50 және одан үлкен болса өтті, кіші болса қалды деп жаздырыңыз
# А) Орташа баға 50 болса да, емтихан бағасы ең төменгі бағасы 50 болу керек
# Б) Емтиханнан 70 алса орташа бағаның керегі болмасын, бірден өтті деп шығару керек

# blok1 = float(input('blok 1 = '))
# blok2 = float(input('blok 2 = '))
# emtihan = float(input('emtihan = '))

# ortawa = (((blok1 + blok2) / 2) * 0.6) + (emtihan * 0.4)
# #result = (ortawa >= 50) and (emtihan>=50)
# result = (emtihan>=70)or(ortawa>=50)
# print(f"ortawa baga = {ortawa} jane otu jagdaiy: {result}")

#6 Қолданушының аты, салмағы, бойының мәндерін алып салмақ индексін есептеңіз
# Формула (салмақ / бойының ұзындығының квадраты)
# Төмендегі кесте бойынша қай топқа жататынын анықтаңыз
# 0-18.4     Арық
# 18.5-24.9  Орташа
# 25.0-29.9  Артық салмақ
# 30.0-34.9  Семіздік (Обез)

# name = input("atynyz: ")
# boy = float(input('boiynyz:'))
# salmak = float(input('salmaginiz: '))

# formula = (salmak)/(boy ** 2)

# arik = (formula>=0) and (formula<=18.4)
# ortawa = (formula>18.4) and (formula<=24.9)
# salmakty = (formula>24.9) and (formula<=29.9)
# obez = (formula>29.9) and (formula<=34.9)


# print(f'{name} salmak indeksiniz: {formula} aryk {arik}')
# print(f'{name} salmak indeksiniz: {formula} ortawa {ortawa}')
# print(f'{name} salmak indeksiniz: {formula} salmakty {salmakty}')
# print(f'{name} salmak indeksiniz: {formula} obez {obez}')
