class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)
