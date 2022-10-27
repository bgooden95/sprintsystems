class User:
    def __init__(self):
        self.first_name = "David"
        self.last_name = "Brooks"
        self.email = "gullygod876@aol.com"
        self.age = 41
        self.is_rewards_member = True
        self.gold_card_points = 0



    def display_info(self):
        print("==========")
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards member:", self.is_rewards_member)
        print("Gold card points:", self.gold_card_points)
    

    def enroll(self):
        if self.is_rewards_member == True:
            print("Thank you for choosing us!")
        else: 
            self.is_rewards_member = True
            print("Welcome!")
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points < amount:
            print("You need more points!")
        print("Current amount:", self.gold_card_points)


David = User()

David.spend_points(260)
David.display_info()
David.enroll()


    



        

        
