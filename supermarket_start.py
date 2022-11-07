"""
Start with this to implement the supermarket simulator.
"""
from datetime import datetime
from tiles_skeleton import SupermarketMap, Customer
import random

from faker import Faker
faker = Faker(use_weighting = False)



class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0

    def __repr__(self):
        return 'Supermarket class' # TODO

    def get_time(self):
        """current time in HH:MM format,
        """
        return datetime.now().strftime("%H:%M")

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            print(f'{customer},{self.get_time()},{customer.id}')
        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        for customer in self.customers:
            customer.next_state()
        return None

    def add_new_customers(self):
        """randomly creates new customers.
        """
        return Customer(self.last_id + 1, faker.first_name(), random.choices(['dairy', 'drinks', 'fruit', 'spices']), 200)

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        for customer in self.customers:
            if customer.state == ['checkout']:
                customer.is_active = False
                self.customers.remove(customer.id)

        return None
