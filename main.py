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



def OrderingSystem():
    ## customer_order will be storing the objects of the pizza order
    customer_order = []
    location = ["london", "newcastle", "bath", "liverpool", "kent"]
    orderNumber = 0
    pizza_name = input("what pizza would you like?")

    pizza_type = input("what pizza type would you like?")

    new_pizza = pizza.Pizza(pizza_name, pizza_type)

    customer_order.append(new_pizza)

    pizza_topping = input("what pizza topping would you like?")
    new_topping = topping.Topping(pizza_topping)
    customer_order.append(new_topping)

    pizza_base = input("what size pizza base would you like?")
    customer_order.append(pizza_base)
    # new base object initialised
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
            customer_location = input("which branch would you like to order from: ")

    orderNumber = orderNumber + 1

    customer_order.append(orderNumber)

    print("Order Summary")
    print(customer_order)
    placed = "order placed"
    not_placed = "order not placed"

    place_order = input("would you like to place your order: ")

    if place_order == "yes":
        print(bool(placed))
        main()
    elif place_order == "no":
        print(bool(not_placed))
        customer_order.clear()
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





