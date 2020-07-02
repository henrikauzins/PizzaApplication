#importing py classes
import employee
import customer
import base
import topping
import branch
import pizza



def Employee():
    print("this is the employee interface")
    rank = input("what is your rank: ")
    new_employee = employee.Employee(name, rank)

def Customer():
    ## customer_order will be storing the objects of the pizza order
    customer_order = []
    location = ["london", "newcastle", "bath", "liverpool", "kent"]
    orderNumber = 0
    print("this is the customer interface")
    new_customer = customer.Customer(name)
    print(new_customer.name)

    pizza_name = input("what pizza would you like?")


    pizza_type = input("what pizza type would you like?")


    new_pizza = pizza.Pizza(pizza_name, pizza_type)

    customer_order.append(new_pizza)


    pizza_topping = input("what pizza topping would you like?")
    new_topping = topping.Topping(pizza_topping)
    customer_order.append(new_topping)

    pizza_base = input("what size pizza base would you like?")
    customer_order.append(pizza_base)
    #new base object initialised
    new_base = base.Base(pizza_base)
    new_base.GetBase(pizza_base)

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
            break





    orderNumber = orderNumber + 1

    customer_order.append(orderNumber)

    print("Order Summary")
    print(customer_order)

name = input("what is your name: ")
user_type = input("are you a customer or employee: ")

if user_type == "customer" or "customer":
    Customer()






