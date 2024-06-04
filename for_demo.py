sandar = [1,3,5,7,9,12,19,21]

#1- сандар массивіндегі қай сандар 3 тің еселігі?

# for san in sandar:
#     if san%3==0:
#         print(san)
#2- сандар массивіндегі сандардың қосындысы қанша?
# sum = 0
# for san in sandar:
#     sum += san
# print(f'Summa = {sum}')

#3- сандар массивіндегі тақ сандардың квадратын жаздырыңыз

# for san in sandar:
#     if san%2==1:
#         print(san ** 2)

kalalar = ['Astana','Turkistan','Almaty','Shymkent','Kizilorda','Semey']

#4- Қалалар массивіндегілердің қайсысы ең көп 6 символдан тұрады?
# for kala in kalalar:
#     if len(kala)<=6:
#         print(kala)

zattar = [
    {'aty':'Samsung S6','bagasy':'50000'},
    {'aty':'Samsung S7','bagasy':'60000'},
    {'aty':'Samsung S8','bagasy':'70000'},
    {'aty':'Samsung S9','bagasy':'80000'},
    {'aty':'Samsung S10','bagasy':'90000'},
]

#5- Заттардың бағаларының қосындысы қанша?
# sum = 0
# for zat in zattar:
#     sum += int(zat['bagasy'])
# print(sum)
#6- Заттардың бағасы ең көп 70000 болған заттарды көрсетіңіз?
# for zat in zattar:
#     if int(zat['bagasy'])<=70000:
#         print(zat['aty'])