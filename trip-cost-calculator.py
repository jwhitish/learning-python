#define cost of hotel
def hotel_cost(nights):
  return 140 * nights

#define cost of plane ride to specified cities
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

#define rental car cost with discount for extended rental
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    return cost - 50
  elif days >= 3:
    return cost - 20
  else:
    return cost

#sum total cost
def trip_cost(city, days, spending_money):
  return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

#print total trip cost to specified city
print trip_cost("Los Angeles", 5, 600)
