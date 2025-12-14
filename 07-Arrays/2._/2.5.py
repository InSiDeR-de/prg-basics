# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total():
    result=''
    for x in cinema_seats:
        result += len(cinema_seats)
    return result

def seats_available():
    result=''
    for x in cinema_seats:
        result+=x.count("A")
    return result

def seats_booked():
    result=''
    for x in cinema_seats:
        result+=x.count("B")
    return result

def seat_status(row, place):
   i=1
   for rows in cinema_seats:
      if row==i:
        return rows[place-1]
      else:
         i+=1
        
      

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total())
print('Seats available:',seats_available())
print('Seats booked:', seats_booked())
print('Seat in row 1, place 1:', seat_status(1,1))
print('Seat in row 5, place 5:', seat_status(5,5))
print('Seat in row 3, place 5:', seat_status(3,5))