from datetime import datetime

# Reads the bikes.txt file and converts each line into a list and appends them to another main list making a 2d list
def return_2d_list():
    file = open("data.txt")
    newList = []
    for line in file:
        line = line.replace("\n", "")
        line = line.split(",")
        newList.append(line)
    file.close()
    return newList

#Crates a global 2d list named bikes 
bikes = return_2d_list()

# Displays Welcome Messages
def welcome_message():
    print("-" * 33) 
    print("Welcome to Bike Management System")
    print("-" * 33)

# Displays Main Menu
def display_main_menu():
    print("1. Sell Bike")
    print("2. Order Bike")
    print("3. Exit")
    print("-" * 33)
    print()

#Sell menu functionality
def isellBike(): 
    customerName = input("Enter your name: ").title()
    customerNumber = input("Enter your phone number: ")
    customerAddress = input("Enter your address: ").title()
    continueLoop = "yes"
    saleDict = {}
    individualQuantity = 0

    while continueLoop == "yes":
        print("")
        print("-" * 98)
        print(" " * 42 + "Selling a Bike: ")
        print("-" * 98)
        
        # Lists the bikes in the file
        show_bikes()
        print()
        sell_bike_id = valid_bike_id("sell")
        sell_bike_list = []
        for sale in saleDict:
            sell_bike_list.append(sale)
        if sell_bike_id not in sell_bike_list:
            individualQuantity = 0
        else:
            for sale in saleDict:
                if sale == sell_bike_id:
                    individualQuantity = saleDict[sale]

        input_quantity = valid_stock(sell_bike_id)
        bikes[sell_bike_id - 1][3] = str(int(bikes[sell_bike_id - 1][3]) - input_quantity)
        individualQuantity += input_quantity
        saleDict[sell_bike_id] = individualQuantity

        print()
        continueLoop = input("Do you want to continue selling other bikes?\nYes/No? : ").lower()
        while continueLoop not in ["yes", "no"]:
            display_invalid_input("y/n")
            print()
            continueLoop = input("Do you want to continue selling other bikes?\nYes/No? : ").lower()
    
    total_price = 0
    file = open("./Sale Bills/" + customerName + "-" + "Sale" + "-" + get_random() + ".txt", "w")
    for sale in saleDict:
        # Creates a short sales bill in the terminal
        sell_price = int(bikes[sale - 1][4].replace("$", ""))
        individual_total_price = sell_price * saleDict[sale]
        
        print("-" * 98)
        print(f"| Sales Bill({customerName}): ")
        print("-" * 98 + "\n")
        print(f"| Name of the customer: {customerName}\t | Contact: {customerNumber}")
        print(f"| Address: {customerAddress}")
        print(f"| The bike of choice: {bikes[sale - 1][0]}")
        print(f"| Brand: {bikes[sale - 1][1]}")
        print(f"| Color: {bikes[sale - 1][2]}")
        print(f"| Quantity: {saleDict[sale]}")
        print(f"| Unit Price: {bikes[sale - 1][4]}")
        print(f"| Individual Total Price: ${individual_total_price}")
        print("-" * 98)

        # Creates a  sales bill in the file
        ''' --------- Printing Bill First Way --------- '''
        file.write(f"Sales Bill({customerName}):\n")
        file.write(f"Time of sale: {datetime.now()}\n\n")
        file.write("-" * 50 + "\n")
        file.write(f"| Name of the customer: {customerName}\t | Contact: {customerNumber}\n")
        file.write(f"| Address: {customerAddress}\n")
        file.write(f"| The bike of choice: {bikes[sale - 1][0]}\n")
        file.write(f"| Brand: {bikes[sale - 1][1]}\n")
        file.write(f"| Color: {bikes[sale - 1][2]}\n")
        file.write(f"| Quantity: {saleDict[sale]}\n")
        file.write(f"| Unit Price: {bikes[sale - 1][4]}\n")
        file.write(f"| Individual Total Price: ${individual_total_price}\n")
        file.write("-" * 50 + "\n\n\n")
        total_price += individual_total_price

    file.write(f"| Total Price: ${total_price}\n")
    file.close()

def orderBike():
    shipping_name = input("Enter the shipping company's name: ")
    shipping_number = input("Enter shipping company's contact number: ")
    shipping_address = input("Enter shipping company's address: ").title()
    continueLoop = "yes"
    orderDict = {}
    individualQuantity = 0

    while continueLoop == "yes":
        print("")
        print("-" * 98)
        print(" " * 41 + "Ordering a Bike: ")
        print("-" * 98)
            
        # Lists the bikes in the file
        show_bikes()
        print()
        order_bike_id = valid_bike_id("order")
        order_bike_list = []
        for order in orderDict:
            order_bike_list.append(order)
        if order_bike_id not in order_bike_list:
            individualQuantity = 0

        input_quantity = valid_order_quantity()
        bikes[order_bike_id - 1][3] = str(int(bikes[order_bike_id - 1][3]) + input_quantity)
        individualQuantity += input_quantity
        orderDict[order_bike_id] = individualQuantity

        print()
        continueLoop = input("Do you want to continue ordering more bikes?\nYes/No? : ").lower()
        while continueLoop not in ["yes", "no"]:
            display_invalid_input("y/n")
            print()
            continueLoop = input("Do you want to continue ordering more bikes?\nYes/No? : ").lower()

    
    total_price = 0
    file = open("./Order Bills/" + shipping_name + "-" + "Order" + "-" + get_random() + ".txt", "w")
    for order in orderDict:
        # Creates a short order bill in the terminal
        order_price = int(bikes[order - 1][4].replace("$", ""))
        individual_total_price = order_price * orderDict[order]

        print("-" * 98)
        print(f"| Order Bill({shipping_name}): ")
        print("-" * 98 + "\n")
        print(f"| Name of the shipping company: {shipping_name}\t | Contact: {shipping_number}")
        print(f"| Address: {shipping_address}")
        print(f"| The bike of choice: {bikes[order - 1][0]}")
        print(f"| Brand: {bikes[order - 1][1]}")
        print(f"| Color: {bikes[order - 1][2]}")
        print(f"| Unit Price: {bikes[order - 1][4]}")
        print(f"| Quantity: {orderDict[order]}")
        print(f"| Individual Total Price: ${individual_total_price}")
        print("-" * 98)

        # Creates a order bill in the file
        ''' --------- Printing Bill First Way --------- '''
        file.write(f"Order Bill({shipping_name}):\n")
        file.write(f"Time of sale: {datetime.now()}\n\n")
        file.write("-" * 50 + "\n")
        file.write(f"| Name of the shipping company: {shipping_name}\t | Contact: {shipping_number}\n")
        file.write(f"| Address: {shipping_address}\n")
        file.write(f"| The bike of choice: {bikes[order - 1][0]}\n")
        file.write(f"| Brand: {bikes[order - 1][1]}\n")
        file.write(f"| Color: {bikes[order - 1][2]}\n")
        file.write(f"| Quantity: {orderDict[order]}\n")
        file.write(f"| Unit Price: {bikes[order - 1][4]}\n")
        file.write(f"| Individual Total Price: ${individual_total_price}\n")
        file.write("-" * 50 + "\n\n\n")
        total_price += individual_total_price

    file.write(f"| Total Price: ${total_price}\n")
    file.close()




def exit():
    print()
    print("Thank you for connecting with us! Hope we see you again! ")
    print("_" * 56)
    print()

def display_invalid_menu_input():
    print(" ")
    print("INVALID INPUT!! Please enter the correct menu code from the options.")
    print(" ")
    print("-" * 34)
    print("1. Sell Bike")
    print("2. Order Bike")
    print("3. Exit")
    print("-" * 34)
    print()

def show_bikes():
    print("-" * 98)
    #          9                22                      19              17              13          11                                   
    print("| Bike Id |      Bike Name       |       Company     |      Color      |     Stock   |   Price   |") # total length 98
    print("―" * 98) #total character length of the entire table
    bike_id = 1
    for bike in bikes:
        # displays spaces according to (total characters between the ||) - 3(total spaces that will be added by a , in print and from that the length of the text is subtracted to give required spaces) 
        print("|",bike_id," "*(6 - len(str(bike_id))),"|",bike[0], " "*(19 - len(bike[0])),"|",bike[1], " "*(16 - len(bike[1])),"|", bike[2], " "*(14 - len(bike[2])),"|", bike[3], " "*(10 - len(bike[3])),"|", bike[4], " "*(8 - len(bike[4])),"|")
        bike_id += 1

    print("-" * 98)

def return_2d_list():
    file = open("data.txt")
    newList = []
    for line in file:
        # list_1d = []
        line = line.replace("\n", "")
        line = line.split(",")
        newList.append(line)
    file.close()
    return newList


def valid_bike_id(type):
    temp_type = type 
    try:
        if type == "sell": 
            bike_id = int(input("Enter id of the bike to sell: "))
        elif type == "order":
            bike_id = int(input("Enter id of the bike to order: "))
    except:
        display_invalid_input("conversion")
        show_bikes()
        print()
        return valid_bike_id(temp_type)
    while bike_id <= 0 or bike_id > len(bikes):
        display_invalid_input("logic")
        show_bikes()
        print()
        return valid_bike_id(temp_type)

    return bike_id


def valid_stock(bike_id):
    temp_bike_id = bike_id
    try:
        sell_input_quantity = int(input("Enter the number of the bikes you want to purchase: "))
    except:
        display_invalid_input("conversion")
        show_bikes()
        print()
        return valid_stock(temp_bike_id)
    else:
        listQuantity = (bikes[bike_id - 1][3])
        while sell_input_quantity <= 0 or sell_input_quantity > int(listQuantity):
            display_invalid_input("logic")
            show_bikes()
            print()
            return valid_stock(temp_bike_id)    
    return sell_input_quantity
        

def valid_order_quantity():
    try:
        order_input_quantity = int(input("Enter the quantity of bike you want to order: "))
    except:
        display_invalid_input("conversion")
        show_bikes()
        print()
        valid_order_quantity()

    while order_input_quantity <= 0:
            display_invalid_input("logic")
            show_bikes()
            print()
            return valid_order_quantity()
    return order_input_quantity



def get_random():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    second = str(datetime.now().microsecond)
    random = year+month+day+second
    return random

def display_invalid_input(type):
    if type == "logic":
        print("Invalid Input! Please provide a valid input!")
    elif type == "conversion":
        print("Invalid Input! Please provide a number!")
    elif type == "y/n":
        print("Invalid Input! Please enter yes/no!")



def update_file():
    file = open("data.txt", "w")
    file.truncate()
    for bike in bikes:
        file.write(f"{bike[0]},{bike[1]},{bike[2]},{bike[3]},{bike[4]}\n")
    file.close()

