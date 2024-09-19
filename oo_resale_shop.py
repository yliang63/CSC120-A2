"""
Author: Yvonne Liang
Date: September 17th 2024
Description: Creationg of ResaleShop class
"""
from typing import Dict, Optional


class ResaleShop:

    def __init__(self):
        self.itemID = 0
        self.inventory: Dict[int, Dict] = {}


    def buy(self,computer: Dict):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
    
    def sell(self,item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self,item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
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