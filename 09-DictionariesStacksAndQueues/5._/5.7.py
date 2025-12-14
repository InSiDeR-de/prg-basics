hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":590.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
krk=''
s=''
ak=0
sk=0
i=0
c=''
for key in hotels_in_Krakow:
    krk+=f'{key['name']}, '
    ak+=key['price']
    i+=1
ak/=i
i=0
for key1 in hotels_in_Sopot:
    s+=f'{key1['name']}, '
    sk+=key1['price']
    i+=1
sk/=i
if ak>sk:
    c='Sopot'
elif sk>ak:
    c='Krakow'
else:
    c='Te same ceny'


print('Hotels in Krakow:', krk)
print('Average hotel price in Krakow:', ak)
print('Hotels in Sopot:', s)
print('Average hotel price in Sopot:', sk)
print('Cheaper hotels in:',c)
