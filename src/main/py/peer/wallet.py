"""
Module to manage peer wallet functionality.

Wallet class allows us to ...
"""


class Wallet:
    """
    Class to manage Peer wallet functionality
    """

    def __init__(self):
        """
        Initializes an instance of the Wallet class
        """

        self.balance = 0

    def add_to_balance(self, amount: int):
        """
        Adds balance to the wallet.

        Params:
        - amount (int): The amount to add to the wallet.
        """

        self.balance += amount

    def remove_from_balance(self, amount: int):
        """
        Removes balance from the wallet.

        Params:
        - amount (int): The amount to remove from the wallet.
        """

        self.balance -= amount

    def current_balance(self):
        """
        Gets the current balance of the wallet.
        """

        return self.balance
