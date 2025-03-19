city_flight=input('The city they will be flying to (Paris, Spain, New York, Hong Kong, Tokyo)->' )
num_nights=input('The number of nights staying at a hotel ->')
rental_days=input('The number of days of hiring a car ->')

def plane_cost(city_flight):
    if city_flight=='Paris':
        flight_cost=100        
    elif city_flight=='Spain':
        flight_cost=200        
    elif city_flight=='New York':
        flight_cost=300        
    elif city_flight=='Hong Kong':
        flight_cost=400       
    elif city_flight=='Tokyo':
        flight_cost=500   
    return flight_cost
        
def hotel_cost(num_nights,price_per_night=200):
    hotel_cost=int(num_nights) * price_per_night
    return hotel_cost

def rental_cost(rental_days,cost_per_day=10):
    car_rental_cost=int(rental_days) * cost_per_day
    return car_rental_cost

def holiday_cost(city_flight,num_nights,rental_days): 
    total_holiday_cost=int(plane_cost(city_flight))+int(hotel_cost(num_nights))+int(rental_cost(rental_days))
    return total_holiday_cost

print('*Thank you for using travel cost calculator. The cost details as follow:')
print('The cost for the flight is',plane_cost(city_flight))   
print('The cost for the hotel stay is',hotel_cost(num_nights))  
print('The cost for the car rental is',rental_cost(rental_days)) 
print('The total holiday cost for the trip is',holiday_cost(city_flight,num_nights,rental_days))