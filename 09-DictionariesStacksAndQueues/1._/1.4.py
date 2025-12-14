person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print('1.-----')
print(person['name'])
print('2.-----')
print(person['hobby'])
print('3.-----')
for key,value in person.items():
   print(f"{key} : {value}")
print('4.-----')
person["surname"]='Nowak'
print(person['surname'])
print('5.-----')
person['married']=False
print(person["married"])
print('6.-----')
person['gender']='male'
print(person['gender'])
print('7.-----')
person['hobby'].append('bicycle')
print(person['hobby'])
print('8.-----')
person['phone']['work']='313131444'
print(person['phone'])
print('9.-----')
for key,value in person.items():
   print(f"{key} : {value}")