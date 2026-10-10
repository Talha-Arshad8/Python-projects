
print("------------Wlecome To Special Resturant------------")
user_name = input('Enter Your name Sir: ')
menu = {"Beef Biryani":350,
        "Chicken Biryani":300, 
        "Pizza Small":400,
        "Pizza Large":700,
        "Pasta":250,
        "Chips":200,
        "Chicken Roll":280,
        "Shwarma": 360}
print(" 1)Beef Biryani-->350\n 2)Chicken Biryani-->300\n 3)Pizza Small-->400\n 4)Pizza Large-->700\n 5)Pasta-->250\n 6)Chips-->200\n 7)Chicken Roll-->280\n 8)Shwarma-->360\n")
user_order = input(f"Hi {user_name} Enter Your order? ")

order_item = []
  
if user_order in menu:
    print(f"{user_order} Add Successfully!!----")
    order_item.append(user_order)
    while True:
        order = input("Do you want more item?(Yes/No) ")
        if order.lower() == 'no':
            break
        elif order.lower() == 'yes':
            new_order = input(f"Hi {user_name} Enter Your order? ")
            order_item.append(new_order)
            if new_order in menu:
                print(f"{new_order} Add Successfuly!!----")
    print("==========Total Bill==========")
    total = 0
    for item in order_item:
        print(f"{item:<15}  Rs{menu[item]}")
        total += menu[item]
    print("---------------------")
    print(f"Total Bill      Rs.{total}")

    print(f"Thanks for visiting {user_name}.")
else:
    print("Sorry Sir Not Available") 
 