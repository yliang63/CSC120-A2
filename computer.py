"""
Author: Yvonne Liang
Date: September 17th 2024
Description: Creation of a computer class
"""
class Computer:

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
    def __init__(self,description: str,
    processor_type: str,
    hard_drive_capacity: int,
    memory: int,
    operating_system: str,
    year_made: int,
    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    def update_os(self, new_os):
       self.operating_system = new_os

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


    # What methods will you need?
if __name__ == "__main__":
    main()
    