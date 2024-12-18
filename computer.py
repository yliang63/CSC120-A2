"""
Author: Yvonne Liang
Date: September 17th 2024
Description: A class representing a computer with its specifications and attributes.
"""

class Computer:
    """
    Represents a computer with its specifications and attributes.

    Attributes:
        description (str): A brief description of the computer.
        processor_type (str): The type of processor in the computer.
        hard_drive_capacity (int): The capacity of the hard drive in gigabytes.
        memory (int): The amount of RAM in gigabytes.
        operating_system (str): The operating system installed on the computer.
        year_made (int): The year the computer was manufactured.
        price (int): The price of the computer.

    Methods:
        __init__: Initializes a new instance of the Computer class.
        update_os: Updates the operating system of the computer.
        update_price: Updates the price of the computer.
    """

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        """
        Initializes a new instance of the Computer class.

        Args:
            description (str): A brief description of the computer.
            processor_type (str): The type of processor in the computer.
            hard_drive_capacity (int): The capacity of the hard drive in gigabytes.
            memory (int): The amount of RAM in gigabytes.
            operating_system (str): The operating system installed on the computer.
            year_made (int): The year the computer was manufactured.
            price (int): The price of the computer.
        """
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    def update_os(self, new_os):
        """
        Updates the operating system of the computer.

        Args:
            new_os (str): The new operating system to be installed.
        """
        self.operating_system = new_os

    def update_price(self, new_price):
        """
        Updates the price of the computer.

        Args:
            new_price (int): The new price of the computer.
        """
        self.price = new_price

def main():
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
        )
    print(computer.__dict__)
    os = input("Enter new_os:")
    computer.update_os(os)
    print(computer.__dict__)

if __name__ == "__main__":
    main()
    