"""
Author: Yvonne Liang
Date: September 17th 2024
Description: A class representing a resale shop for managing computer inventory.
"""

from typing import Dict, Optional

class ResaleShop:
    """
    Represents a resale shop that manages a computer inventory.

    Attributes:
        itemID (int): A unique identifier for each item in the inventory.
        inventory (Dict[int, Dict]): A dictionary containing the inventory items,
            where each key is an item ID and each value is another dictionary with
            the item's details.

    Methods:
        __init__: Initializes a new instance of the ResaleShop class.
        buy: Adds a new computer to the inventory.
        sell: Removes a computer from the inventory.
        print_inventory: Prints the current inventory.
        refurbish: Refurbishes a computer in the inventory, updating its price and OS.
    """

    def __init__(self):
        """
        Initializes a new instance of the ResaleShop class.
        """
        self.itemID = 0
        self.inventory: Dict[int, Dict] = {}

    def buy(self, computer: Dict):
        """
        Adds a new computer to the inventory.

        Args:
            computer (Dict): A dictionary containing the details of the computer to be added.

        Returns:
            int: The item ID assigned to the new computer.
        """
        self.itemID += 1  # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    def sell(self, item_id: int):
        """
        Removes a computer from the inventory.

        Args:
            item_id (int): The item ID of the computer to be removed.
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Prints the current inventory.
        """
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """
        Refurbishes a computer in the inventory, updating its price and OS.

        Args:
            item_id (int): The item ID of the computer to be refurbished.
            new_os (Optional[str]): The new operating system to be installed, if any.
        """
        if item_id in self.inventory:
            computer = self.inventory[item_id]  # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0  # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250  # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550  # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000  # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os  # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    myshop = ResaleShop()
    print(len(myshop.inventory))
    c = {"name": "Crazy Computer", "year_made": 2005, "price": 500, "operating_system": "Windows XP"}
    myshop.buy(c)
    print(len(myshop.inventory))
 

if __name__ == "__main__":
    main()