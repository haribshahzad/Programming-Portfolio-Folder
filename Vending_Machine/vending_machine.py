print ("Welcome to the Vending Machine")

# Available items in the vending machine
products= {
'1':{'name':'Skittles', 'price':3.50, 'stock':10},
'2':{'name':'Lays', 'price':1.50, 'stock':10},
'3':{'name':'Red_Bull', 'price':7.50, 'stock':10}
}


# Defining functions to display items 
def display_products():
    print("\nAvailable Items:")
    for product_id, product_info in products.items():
        print(f"{product_id}: {product_info['name']} - ${product_info['price']} (Stock: {product_info['stock']})")

# Function to process vending 
def vending_products(product_id, money_inserted):
    if product_id in products:
        product = products[product_id]
        if product['stock'] > 0:
            if money_inserted >= product['price']:
                product['stock'] -= 1
                change = money_inserted - product['price']
                print(f"Dispensing {product['name']}. Your change is £{change:.2f}. Enjoy!")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print(f"Sorry, {product['name']} is out of stock.")
    else:
        print("Invalid selection. Please choose a valid item.")


# Main loop of the vending machine
while True:
    display_products()
    choice = input("\nEnter the item number you wish to purchase (or 'q' to quit): ")
    if choice.lower() == 'q':
        print("Thank you for using the Vending Machine. Goodbye.")
        break
    try:
        money = float(input("Insert money: £"))
        vending_products(choice, money)
    except ValueError:
        print("Invalid input. Please enter a valid amount of money.")


