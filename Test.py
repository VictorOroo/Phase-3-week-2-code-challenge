from Customer import Customer
from Restaurant import Restaurant
from Review import Review


customer1 = Customer("Victor", "Oroo")
customer2 = Customer("Chris", "Omondi")

restaurant1 = Restaurant("chakula tamu")
restaurant2 = Restaurant("snack things")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

print("Customers:")
for customer in Customer.all():
    print(customer.full_name())

print("\nRestaurants:")
for restaurant in Restaurant.all():
    print(restaurant.name)

print("\nCustomer 1's Restaurants:")
for restaurant in customer1.restaurants():
    print(restaurant.name)

print("\nAverage Rating for Restaurant 1:", restaurant1.average_star_rating())

print("\nNumber of Reviews by Customer 1:", customer1.num_reviews())

print("\nFinding Customer by Name 'Victor Oroo':", Customer.find_by_name("Victor Oroo").full_name())

print("\nFinding Customers by Given Name 'Victor':")
for customer in Customer.find_all_by_given_name("Victor"):
    print(customer.full_name())
