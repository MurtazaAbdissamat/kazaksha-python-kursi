# key : value

# Turkistan : 13
# Shymkent : 17
# Atyrau : 06

# kala = ['Turkistan','Shymkent','Atyrau']
# nomer = [13,17,6]

# print(nomer[kala.index('Turkistan')])

# nomerler = { 'Turkistan': 13,
#              'Shymkent': 17,
#              'Atyrau': 6}

# print(nomerler['Turkistan'])

# nomerler['Almaty'] = 2
# nomerler['Shymkent'] = 25

# print(nomerler)

users = {
    'make':{
        'jas':28,
        'rol':['admin','user'],
        'mail': 'make@gmail.com',
        'nomer': 135532115,
        'adres': "Turkistan"
    },


    'user':{
        'jas':27,
        'rol':['user'],
        'mail': 'user@gmail.com',
        'nomer': 135532115,
        'adres': "Turkistan"
    }
}

print(users['make']['jas'])
print(users['make']['mail'])
print(users['make']['nomer'])
print(users['make']['rol'][0])