import employee
import customer



def Employee():
    print("this is the employee interface")
    rank = input("what is your rank: ")
    new_employee = employee.Employee(name, rank)

def Customer():
    customer_order = []
    location = ["london", "newcastle"]
    orderNumber = 0
    print("this is the customer interface")
    new_customer = customer.Customer(name)
    print(new_customer.name)

    pizza = input("what pizza would you like?")
    customer_order.append(pizza)

    pizza_type = input("what pizza type would you like?")
    customer_order.append(pizza_type)

    pizza_topping = input("what pizza topping would you like?")
    customer_order.append(pizza_topping)

    pizza_base = input("what size pizza base would you like?")
    customer_order.append(pizza_base)

    customer_location = input("which branch would you like to order from: ")

    while True:
        if customer_location in location:
            print("location exists")
            customer_order.append(customer_location)
            break

        else:
            print("location does not exist")
            print(location)

    print(customer_order)

    orderNumber = orderNumber + 1

    print(orderNumber)


name = input("what is your name: ")
user_type = input("are you a customer or employee: ")

if user_type == "customer" or "customer":
    Customer()






