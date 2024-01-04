#Instance Attributes
'''
class Item:
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to received arguments
        # 'f' is used to identify the arguments as arguments, not as a general string

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 1000, -5)

item2 = Item("Laptop", 5000, -3)


print("Total price for item1 is: ", item1.calculate_total_price())
print("Total price for item2 is: ", item2.calculate_total_price())
'''
#Class Attributes
'''
class Item:
    pay_rate = 0.8 #Pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to received arguments
        # 'f' is used to identify the arguments as arguments, not as a general string

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        #If we have used Item.pay_rate then pay rate at 'class level' will be checked first
        #but for self.pay_rate, 'instance level' will be checked first


item1 = Item("Phone", 1000, 5)

item2 = Item("Laptop", 5000, 3)

item1.apply_discount()
print(item1.price)

#Suppose I want to change the discount rate for a particular item to say 0.3, then
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

#print(Item.__dict__) #Show all the attributes to Class level           #This can be used
#print(item1.__dict__) #Show all the attributes to Instance level       #for debugging.
'''

class Item:
    pay_rate = 0.8  # Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.__name} {self.quantity} times.
        Regards Parth Gautam
        """
    def __send(self):
        pass
    def __send_email(self):
        self.coonect()
        self.prepare_body()
        self.send()

    def __calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        #If we have used Item.pay_rate then pay rate at 'class level' will be checked first
        #but for self.pay_rate, 'instance level' will be checked first

    def __repr__(self):
        return f"('{self.__class__.__name__}', '{self.__price}', {self.quantity})"
    #responsible to represent the object

item1 = Item("Phone", 1000, 5)
item2 = Item("Laptop", 5000, 3)
item3 = Item("Cable", 400, 7)
item4 = Item("Pendrive", 800, 4)
item5 = Item("Charger", 950, 6)

#Inheritance
'''
class Phone(Item):      #Phone is called a child class
    all = []
    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)
'''
class Phone(Item):      #Phone is called a child class
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones






