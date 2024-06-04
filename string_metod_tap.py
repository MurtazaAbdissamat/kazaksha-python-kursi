website = 'https://m.abdissamat.com'
kurs = 'Kazakwa python kursi 0 den bastap jogari dengei (40 sagat)'

# 1 - ' Hello World ' simvoldar tiziminin basindagi jane sonindagi bos simvoldardi owiriniz.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()

# 2 -  'website' iwindegi m.abdissamat tan baska simvoldardi owiriniz.
result = website.lstrip('htps:/')
result = website.rstrip('moc.')
# 3 - 'kurs' ainymalysy iwindegi barlik simvoldardi kiwi arippen jazdiriniz.
result = kurs.lower()
result = kurs.capitalize()
result = kurs.title()
#result = kurs.lower()

# 4 - 'website' kanwa 'a' simvoli bar? (count(a))
result = website.count('com')
# 5 - 'website' iwinde '.com' sozi bar ma?
result = website.find('comm')

#result = website.index('comm') try exeption
# 6 - 'website' 'https' pen bastalip '.com' men aiaktaladi ma?
result = website.startswith('https')
result = website.endswith('.com')
# 7 - 'kurs' iwindegi barlik simvol arip pa alde san ba?
result = 'dasfsdfdsf'.isalpha()
result = 'dasfsdfdsf'.isdigit()
# 8 - 'Murtaza Abdissamat' sozin 50 simvoldik katarga ornalastirip onina jane solina '*' kosip jaziniz.
result = 'Murtaza Abdissamat'.center(50,'*')
result = 'Murtaza Abdissamat'.ljust(50,'*')
result = 'Murtaza Abdissamat'.rjust(50,'*')
# 9 - 'kurs' simvoldar iwindegi bos orindardin ornina '-' simvolina auistirip jaziniz.
result = kurs.replace(' ', '-')
result = kurs.replace(' ', '-',3)
# 10 - 'Salem Alem' simvoldar massivinen 'Alem' sozin 'Dostar!' etip ozgertiniz.
result = 'Salem Alem'.replace('Alem', 'Dostar!')
# 11 - 'kurs' simvoldar massivin bos orindar boinwa bolip alip jazdiriniz.
result = kurs.split(' ')

print(result)
print(result[5])