class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print (f'First Name: {self.first_name}')
        print (f'Last Name: {self.last_name}')
        print (f'Email: {self.email}')
        print (f'Age: {self.age}')
        print (f'Rewards Member: {self.is_rewards_member}')
        print (f'Gold Card Points: {self.gold_card_points}')
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        return self
    
    def earn_points(self):
        self.gold_card_points += 10
        return self

    def spend_points(self,amount):
        self.gold_card_points -= amount
        return self

Nora=User('Nora','McCarthy','nzmccarthy16@gmail.com',23)

latte = 100
chair_latte = 110

Nora.enroll().display_info().earn_points().display_info().spend_points(latte).display_info()