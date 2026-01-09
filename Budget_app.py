class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[]
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        
        if self.check_funds(amount):
            
            self.ledger.append({'amount': -amount, 'description': description})     
            return True
        return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)
    def transfer(self, amount, other):
        
        if self.withdraw(amount, f"Transfer to {other.name}"):
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def __str__(self):
        output = self.name.center(30,"*")+"\n"
        for entry in self.ledger:
            description = entry["description"][:23]
            amount= entry["amount"]
            output+=f"{description:<23}{amount:>7.2f}\n"
        total=f"Total: {self.get_balance():.2f}"
        
        return output+total
    
    def check_funds(self, amount):
        balance=sum(entry["amount"] for entry in self.ledger)
        if amount>balance:
            return False
        return True
def create_spend_chart(categories):
    output="Percentage spent by category\n"
    category_names=[]
    
    #Rough Maths
    sum_category=[]
    for category in categories:
        category_names.append(category.name)
        category_sum=0
        for entry in category.ledger:
            if entry["amount"]>=0:
                pass
            else:
                category_sum+=abs(entry["amount"])
        sum_category.append(category_sum)
    total_sum=float(f"{sum(i for i in sum_category):.2f}")
    
    percentages=[]
    for i in sum_category:
        percentage=int(i/total_sum*100//10*10)
        percentages.append(percentage) 

    #Drawing
    x_axis="    "+"-"*(3*len(sum_category))+"-"+"\n"
    for i in range(100,-1,-10):
        output+=f"{i:3}"+"| "
        for percent in percentages:
            if percent<i:
                output+="   "
            else:
                output+="o  "
        output+='\n'
    output+=x_axis 
    max_length = max(len(name) for name in category_names)

    for i in range(max_length):
        output += "     "
        for name in category_names:
            if i < len(name):
                output += name[i] + "  "
            else:
                output += "   "
        output += "\n"
    
               
    return output.strip("\n")

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(50.00, "jeans")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")

print(food)
print()
print(create_spend_chart([food, clothing, auto]))




