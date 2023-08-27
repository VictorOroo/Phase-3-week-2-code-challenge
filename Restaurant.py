class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        customers = []
        for review in self.reviews:
            customers.append(review.customer)
        return list(set(customers))

    @classmethod
    def all(cls):
        return cls.all_restaurants
