import json

# Open the JSON file in read mode
with open('reservations.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Support both formats: either top-level list or {"reservations": [...]}
if isinstance(data, dict) and 'reservations' in data:
    reservations_list = data['reservations']
else:
    reservations_list = data

# Counters / accumulators
num_rooms = 0
paid_count = 0
unpaid_count = 0
total_paid = 0.0
total_unpaid = 0.0

for reservation in reservations_list:
    num_rooms += 1
    # use .get with defaults to avoid KeyError
    price = reservation.get('price_per_night', 0)
    nights = reservation.get('nights', 0)
    paid = reservation.get('paid', False)

    value = price * nights
    if paid:
        paid_count += 1
        total_paid += value
    else:
        unpaid_count += 1
        total_unpaid += value

print('number of rooms:', num_rooms)
print('number of paid reservations:', paid_count)
print('number of unpaid reservations:', unpaid_count)
print('total value of paid reservations:', round(total_paid, 2))
print('total value of unpaid reservations:', round(total_unpaid, 2))