class Hotel:

    def __init__(self, name, rating, regular_weekday_price, regular_weekend_price, reward_weekday_price,
                 reward_weekend_price):
        self.name = name
        self.rating = rating
        self.regular_weekday_price = regular_weekday_price
        self.regular_weekend_price = regular_weekend_price
        self.reward_weekday_price = reward_weekday_price
        self.reward_weekend_price = reward_weekend_price

    def hotel_rating(self):
        return self.rating

    def regular_total_weekday_price(self, no_of_days):
        return self.regular_weekday_price * no_of_days

    def regular_total_weekend_price(self, no_of_days):
        return self.regular_weekend_price * no_of_days

    def reward_customer_weekday_price(self, no_of_days):
        return self.reward_weekday_price * no_of_days

    def reward_customer_weekend_price(self, no_of_days):
        return self.reward_weekend_price * no_of_days