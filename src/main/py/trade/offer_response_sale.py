#!/usr/bin/env python3
"""
Module to manage sale response functionality.

OfferResponseSale class allows us to respond to a sale Announcement
"""


class OfferResponseSale:
    """
    Class to manage sale and sale responses
    """

    def __init__(
        self,
        sale_id: str,
        artwork_price: int,
        originator_public_key: str = "",
    ):
        """
        Initializes an instance of the OfferResponse class.
        - sale_id (str): The sale id to respond to.
        """
        self.sale_id = sale_id
        self.artwork_price = artwork_price
        self.originator_public_key = originator_public_key

    def get_sales_id(self):
        """
        Returns the sale id to respond to.
        """

        return self.sale_id

    def get_originator_public_key(self):
        """
        Returns the public key of the originator of the sale response.
        """

        return self.originator_public_key

    def get_artwork_price(self):
        """
        Returns the price of the announced artwork.
        """

        return self.artwork_price
