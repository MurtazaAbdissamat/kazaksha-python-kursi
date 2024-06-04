# studentter = {
#     '100': {
#         'aty': "Murtaza",
#         'tegi': "Abdissamat",
#         'tel': 87072250595
#     },
#     '200': {
#         'aty': "Mustafa",
#         'tegi': "Abdissamat",
#         'tel': 87072250596
#     },
#     '300': {
#         'aty': "Eralhan",
#         'tegi': "Abdissamat",
#         'tel': 87072250597
#     },
# }

# 1 - Қолданушыдан 3 Студенттің мәліметтерін алып оны бір Сөздікке сақтаңыз.

# 2 - Қолданушы Студенттің номерін тергенде сол студент жайлы ақпаратты 
#     сөздіктен алып экранға шығарыңыз.





# studentter.update(
#     {'400':{
#         'aty':'Abylai',
#         'tegi': 'Abdissamat',
#         'tel': 87072250598
#     }
# })

# studentter[stuNo] = {
#     'aty': name,
#     'tegi': surname,
#     'tel': phone
# }
# print(studentter)
studentter = {}

stuNo = input('Studenttik nomer: ')
name = input('Student aty: ')
surname = input("Student tegi: ")
phone = input('Student tel no: ')


studentter.update(
    {stuNo:{
        'aty':name,
        'tegi': surname,
        'tel': phone
    }
})

# stuNo = input('Studenttik nomer: ')
# name = input('Student aty: ')
# surname = input("Student tegi: ")
# phone = input('Student tel no: ')

# studentter.update(
#     {stuNo:{
#         'aty':name,
#         'tegi': surname,
#         'tel': phone
#     }
# })

# stuNo = input('Studenttik nomer: ')
# name = input('Student aty: ')
# surname = input("Student tegi: ")
# phone = input('Student tel no: ')

# studentter.update(
#     {stuNo:{
#         'aty':name,
#         'tegi': surname,
#         'tel': phone
#     }
# })

# print(studentter)

nomer = input("Student nomer endiriniz: ")

student = studentter[nomer]

print(f"Izdegen Student nomeri:{nomer}, aty: {student['aty']}, tegi: {student['tegi']}, nomeri: {student['tel']} ")

print(type(studentter))