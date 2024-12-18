"""
Author: Yvonne Liang
Date: September 17th 2024
Description: A class representing a resale shop for managing computer inventory using the Computer class.
"""

from typing import List
from computer import Computer

class ResaleShop:
    """
    Represents a resale shop that manages a computer inventory using instances of the Computer class.

    Attributes:
        itemID (int): A unique identifier for each item in the inventory.
        inventory (List[Computer]): A list containing the inventory items, where each element is an instance of the Computer class.

    Methods:
        __init__: Initializes a new instance of the ResaleShop class.
        buy: Adds a new Computer instance to the inventory.
        sell: Removes a Computer instance from the inventory.
        print_inventory: Prints the current inventory.
        refurbish: Refurbishes a Computer instance in the inventory, updating its price and OS.
    """

    def __init__(self):
        """
        Initializes a new instance of the ResaleShop class.
        """
        self.itemID = 0
        self.inventory: List[Computer] = []

    def buy(self, computer: Computer):
        """
        Adds a new Computer instance to the inventory.

        Args:
            computer (Computer): An instance of the Computer class to be added.

        Returns:
            int: The item ID assigned to the new computer.
        """
        self.itemID += 1
        computer.id = self.itemID
        self.inventory.append(computer)
        return self.itemID

    def sell(self, item_id: int):
        """
        Removes a Computer instance from the inventory.

        Args:
            item_id (int): The item ID of the computer to be removed.
        """
        for i, computer in enumerate(self.inventory):
            if computer.id == item_id:
                del self.inventory[i]
                print("Item", item_id, "sold!")
                return
        print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Prints the current inventory.
        """
        if self.inventory:
            for computer in self.inventory:
                print(f'Item ID: {computer.id} : {computer.__dict__}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: str = None):
        """
        Refurbishes a Computer instance in the inventory, updating its price and OS.

        Args:
            item_id (int): The item ID of the computer to be refurbished.
            new_os (str): The new operating system to be installed, if any.
        """
        for computer in self.inventory:
            if computer.id == item_id:
                if computer.year_made < 2000:
                    computer.price = 0
                elif computer.year_made < 2012:
                    computer.price = 250
                elif computer.year_made < 2018:
                    computer.price = 550
                else:
                    computer.price = 1000

                if new_os:
                    computer.update_os(new_os)
                return
        print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    myshop = ResaleShop()
    print(len(myshop.inventory))
    c = {"name": "Crazy Computer", "year_made": 2005, "price": 500, "operating_system": "Windows XP"}
    myshop.buy(c)
    print(len(myshop.inventory))
 

if __name__ == "__main__":
    main()