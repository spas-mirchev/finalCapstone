# Inventory

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Credits](#credits)

#### Description

This is a terminal app, which represents a shoe warehouse to assist store managers.

It has the following functionalities:
1. Restock the product with the lowest quantity.
2. Print the shoe with the highest quantity as being "For Sale"
3. Calculate the total value of each stock item. 
   
    The total value is calculated by multiplying the cost by the quantity for each item entered into the system.
4. Search a product by code.
5. See all inventory

### Installation

1. Install a recent version of Python

2. Install the python-tabulate library

    ```sh
   pip install tabulate
   ```


### Usage

1. Create a `inventory.txt` file in the same directory as the main file `inventory.py` with your inventory list. For each inventory item, specify:
   1. `Country`
   2. `Code`
   3. `Product`
   4. `Cost`
   5. `Quantity` 
   
   separated by commas (`,`).

   Example:

   ```
   Country,Code,Product,Cost,Quantity
   South Africa,SKU44386,Air Max 90,2300,20
   China,SKU90000,Jordan 1,3200,50
   Vietnam,SKU63221,Blazer,1700,19
   ...
   ```

2. Run the program

    ```sh
    python inventory.py
    ```

3. Choose one of the available options:
   1. view all - prints all inventory in a tabular format
   2. add new - allows the user to add a new shoe
   3. restock - prints the shoe item with the lowest stock quantity and increases it by the specified number.
   4. search - look up an item by SKU
   5. report - prints out a table with the Total Value for each item
   6. for sale - prints the item with the highest stock


[Demo](https://user-images.githubusercontent.com/33859135/218468315-dbc9b5dc-b088-41fe-8124-a940be6f7379.webm)

### Credits

The project was a task by [HyperionDev](https://hyperiondev.com/)