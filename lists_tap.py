# 1 Bmw, Mercedes, Opel, Mazda атауларына ие бір тізім құрыңыз.
mawinalar = ["Bmw", "Mercedes", "Opel","Mazda"]
result = mawinalar
# 2 Тізімде қанша элемент бар?
result = len(mawinalar)
# 3 Тізімдегі алғашқы және соңғы элемет атауы не?
result = mawinalar[0]
result = mawinalar[3]
result = mawinalar[-1]
# 4 Mazda атауын Toyota атауына өзгертіңіз
mawinalar[-1] = 'Toyota'
result = mawinalar
# 5 Mercedes тізімнің элементі ма?
result = 'Mercedes' in mawinalar
# 6 Тізімнің 2 ші индексіндегі элемент атауы қандай?
result = mawinalar[2]
# 7 Тізімнің алғашқы 3 элементін бөліп алыңыз.
result = mawinalar[:3]    
# 8 Тізімнің соңғы 2 элемент атауларын Toyota және Renault атауларына өзгертіңіз.
mawinalar[-2:] = ['Toyota', 'Renault']
result = mawinalar
# 9 Тізімге Audi және Nissan элементтерін қосыңыз.
result = mawinalar + ['Audi','Nissan']
# 10 Тізімдегі соңғы элементті өшіріңіз.
del result[-1]
# 11 Тізім элементтерін терісінен жаздырыңыз
result = mawinalar[::-1]
# 12 Төмендегі мәліметтерді бір тізім ішіне сақтаңыз:
###  student1: Murtaza Abdissamat 1996, (80,90,95) 
###  student2: Mustafa Abdissamat 1998, (85,75,90)
###  student3: Eralhan Abdissamat 2000, (85,80,70)

studentA = ['Murtaza', 'Abdissamat',1996,[80,90,95]]
studentB = ['Mustafa', 'Abdissamat',1998,[85,75,90]]
studentC = ['Eralhan', 'Abdissamat',2000,[85,80,70]]
# 13 Тізім элементтерін экранға жаздырыңыз.
print(studentA[0])
print(studentB[1])
print(studentC[2])
print(studentA[3][0])
result = f"{studentA[0]} {studentA[1]} {2024 - studentA[2]} jasinda jane ortawa bagasi {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)