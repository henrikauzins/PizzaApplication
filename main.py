#importing external py classes
import employee
import customer
import base
import topping
import branch
import pizza


#Employee function
def Employee():
    print("this is the employee interface")
    name = input("what is your name: ")
    rank = input("what is your rank: ")
    new_employee = employee.Employee(name, rank)
    print(new_employee)

def Customer():
    placed = "order placed"
    not_placed = "order not placed"

    print("this is the customer interface")
    name = input("what is your name: ")
    # creating a new Customer object
    new_customer = customer.Customer(name)
    print("Customer Name: ", new_customer.name)

    #calls the ordering system function
    OrderingSystem()

def CheckToppings():
    print("availible Toppings")

def CheckPizzaTypes():
    print("availible pizza types")


def OrderingSystem():
    ## customer_order will be storing the objects of the pizza order

    #stores order details
    customer_order = []
    #stores prices of order elements
    total_price = []

    location = ["london", "newcastle", "bath", "liverpool", "kent"]
    orderNumber = 0

    while True:
        pizza_name = input("what pizza would you like?")
        pizza_choices = {"margherita": 10.00, "pepperoni": 11.00, "hawaiian": 10.00, "meat feast": 12.00, "bbq chicken": 13.00}

        if pizza_name in pizza_choices:
            print(pizza_name, "exists")
        # prints cost of selected topping
            print("this will cost you £", pizza_choices[pizza_name])
            total_price.append(pizza_choices[pizza_name])
            print(total_price)
            break



        # if inputted base does not exist
        elif pizza_name not in pizza_choices:
            print(pizza_name, "is not on offer")

    while True:
        pizza_type = input("what pizza type would you like?")
        pizza_types = {"deep dish": 4.00, "sicilian": 5.00, "greek": 6.00, "calzone": 7.00, "neapolitan": 8.00, "new york style": 9.00}



        if pizza_type in pizza_types:
                print(pizza_type, "exists")
            # prints cost of selected pizza type
                print("this will cost you £", pizza_types[pizza_type])
                total_price.append(pizza_types[pizza_type])
                print(total_price)
                break



        elif pizza_type not in pizza_types:
                print(pizza_type, "is not on offer")

        new_pizza = pizza.Pizza(pizza_name, pizza_type)

        customer_order.append(new_pizza)

    while True:

        pizza_topping = input("what pizza topping would you like?")
        toppings = {"cheese": 0.86, "sausage": 0.90, "ham": 1.0}
        if pizza_topping in toppings:
            print(pizza_topping, "exists")
            #prints cost of selected topping
            print("this will cost you £",toppings[pizza_topping])
            total_price.append(toppings[pizza_topping])
            print(total_price)
            new_topping = topping.Topping(pizza_topping)
            customer_order.append(new_topping)
            break

# if inputted topping does not exist
        elif pizza_topping not in toppings:
                print(pizza_topping, "is not on offer")



    while True:
        print("base choices are small, medium or large")
        pizza_base = input("what size pizza base would you like?")

        base_selection = {"small": 5, "medium": 6, "large": 7}

        if pizza_base in base_selection:
            print(pizza_base, "exists")
            # prints cost of selected topping
            print("this will cost you £", base_selection[pizza_base])
            total_price.append(base_selection[pizza_base])
            print(total_price)

            # new base object initialised
            new_base = base.Base(pizza_base)
            customer_order.append(new_base)
            break

        # if inputted base does not exist
        elif pizza_base not in base_selection:
            print(pizza_base, "is not on offer")




    customer_location = input("which branch would you like to order from: ")

    while customer_location not in location:
        if customer_location in location:
            print("location exists")
            new_branch = branch.Branch(customer_location)
            customer_order.append(new_branch)
            break

        else:
            print("location does not exist")
            print(location)
            customer_location = input("which branch would you like to order from: ")

    orderNumber = orderNumber + 1

    customer_order.append(orderNumber)

    print("Order Summary")
    print(customer_order)
    #add dictionary for total prices of items on the customers order
    placed = "order placed"
    not_placed = "order not placed"

    print("the total cost of your order is: £", sum(total_price))

    place_order = input("would you like to place your order: ")

    if place_order == "yes":
        print(bool(placed))
        customer_order.clear()
        total_price.clear()
        main()
    elif place_order == "no":
        print(bool(not_placed))
        customer_order.clear()
        total_price.clear()
        main()


## main function
def main():

    while True:

        user_type = input("are you a customer or employee: ")


        if user_type == "customer":
            Customer()
        elif user_type == "employee":
            Employee()

## runs main() function

main()





