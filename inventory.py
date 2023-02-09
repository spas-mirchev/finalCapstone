from tabulate import tabulate
# ========The beginning of the class==========


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return float(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


class Color:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDCOLOR = '\033[0m'
    UNDERLINE = '\033[4m'


# =============Shoe list===========
shoe_list = []


# ==========Functions outside the class==============


def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as f:
            # This function can return the headers and rows with shoes split as  lists
            headers = f.readline().strip('\n').split(',')
            data = f.readlines()
            data_as_array = [line.strip('\n').split(',') for line in data]
            for row_with_shoes in data_as_array:
                # We can use the unpack operator to initialize shoe objects
                shoe_list.append(Shoe(*row_with_shoes))
            return headers

    except OSError as e:
        print(f"{e}")


def capture_shoes():
    country = input("What's the country of the shoe?: ")
    code = input("What's the code of the shoe?: ")
    product = input("What's the product of the shoe?: ")
    cost = input("What's the cost of the shoe?: ")
    quantity = input("What's the quantity of the shoe?: ")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    print(
        f'\n{Color.WARNING}The {new_shoe.product} shoe has been added.{Color.ENDCOLOR}\n')
    # Finally, we update the text file using __str__ method to convert objects to strings
    with open("inventory.txt", "a") as f:
        f.write(f'{str(new_shoe)}\n')


def view_all():
    # We can convert the shoe object strings to lists and use them in the tabulate module
    # Headers are in the list /from read_shoes_data/
    shoe_strings = [str(item).split(',') for item in shoe_list]
    print(tabulate(shoe_strings, headers=headers, tablefmt='fancy_grid'))


def re_stock():
    # We can make a list with quantities of the shoes and find the index of the minimum value.
    quantity_list = [item.get_quantity() for item in shoe_list]
    min_value = min(quantity_list)
    index_min = quantity_list.index(min_value)
    print(
        f'\n{Color.WARNING}You have only {shoe_list[index_min].get_quantity()} pair of {shoe_list[index_min].product} shoes {Color.ENDCOLOR}\n')
    restock_quantity = int(
        input('How many pairs would you like to purchase?: '))

    new_quantity = restock_quantity + shoe_list[index_min].get_quantity()
    # We also need to update the quantity in the object so that the user can see the updated value in the while loop
    shoe_list[index_min].quantity = new_quantity
    print(
        f'\n{Color.WARNING}Now you have {shoe_list[index_min].get_quantity()} pair of {shoe_list[index_min].product} shoes {Color.ENDCOLOR}\n')

    # Finally, we update the text file using __str__ method to convert objects to strings
    shoe_strings = [f'{str(item)}\n' for item in shoe_list]
    with open('inventory.txt', 'w') as f:
        f.write(f"{','.join(headers)}\n")
        f.writelines(shoe_strings)


def search_shoe():
    # We can use a While loop to query until the user enters a correct code
    while True:
        quote = input("Please enter the code of the shoe: ")
        for item in shoe_list:
            if item.code != quote:
                continue
            print(f"\n{Color.WARNING} {item} {Color.ENDCOLOR}\n")
            return
        print("There is no item with this code")


def value_per_item():
    # We can make lists of price and total value and use them in the table module
    value_per_item = [
        [item.product, item.get_cost() * item.get_quantity()] for item in shoe_list]
    print(f'\n{Color.WARNING}{Color.UNDERLINE} Stock Report {Color.ENDCOLOR}')
    print(tabulate(
        value_per_item, headers=['Product', 'Total Value'], tablefmt='fancy_grid'))


def highest_qty():
    # We can make a list with quantities of the shoes and find the index of the maximum value.
    quantity_list = [item.get_quantity() for item in shoe_list]
    max_value = max(quantity_list)
    index_max = quantity_list.index(max_value)
    print(
        f'\n{Color.WARNING}{shoe_list[index_max].product} goes on Sale. There are {shoe_list[index_max].get_quantity()} pairs {Color.ENDCOLOR}\n')


user_choice = ''
headers = read_shoes_data()

# ==========Main Menu=============
while user_choice != "quit":
    user_choice = input(
        "What would you like to do - view all/add new/restock/search/report/for sale?: ")

    if user_choice == "view all":
        view_all()

    elif user_choice == "add new":
        capture_shoes()

    elif user_choice == "restock":
        re_stock()

    elif user_choice == "search":
        search_shoe()

    elif user_choice == "value":
        value_per_item()

    elif user_choice == "for sale":
        highest_qty()

    elif user_choice == "report":
        value_per_item()

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
