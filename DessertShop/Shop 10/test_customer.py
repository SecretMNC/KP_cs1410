import unittest
from dessertshop import Customer, Order

class TestCustomer(unittest.TestCase):
    
    def test_customer_initialization(self):
        # Test if a Customer object is correctly initialized.
        customer = Customer("John Doe")
        self.assertEqual(customer.customer_name, "John Doe")
        self.assertIsInstance(customer.order_history, list)
        self.assertEqual(len(customer.order_history), 0)
        self.assertIsInstance(customer.customer_id, int)
        self.assertGreaterEqual(customer.customer_id, 10001)

    def test_customer_id_uniqueness(self):
        # Test if different Customer objects receive unique customer IDs.
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        self.assertNotEqual(customer1.customer_id, customer2.customer_id)

    def test_add2history(self):
        # Test if add2history method correctly adds an order to customer's history.
        customer = Customer("Jane Doe")
        order = Order()
        result = customer.add2history(order)
        
        self.assertEqual(len(customer.order_history), 1)
        self.assertEqual(customer.order_history[0], order)
        self.assertEqual(result, customer)

    def test_multiple_orders(self):
        # Test if multiple orders can be added to a customer's history correctly.
        customer = Customer("Multiple Order Tester")
        order1 = Order()
        order2 = Order()
        
        customer.add2history(order1)
        customer.add2history(order2)
        
        self.assertEqual(len(customer.order_history), 2)
        self.assertEqual(customer.order_history[0], order1)
        self.assertEqual(customer.order_history[1], order2)

    def test_customer_name_type(self):
        # Test if non-string customer names are converted to strings.
        customer = Customer(123)  # Passing a non-string
        self.assertIsInstance(customer.customer_name, str)
        self.assertEqual(customer.customer_name, "123")

    def test_customer_id_start_and_increment(self):
        # Test if customer IDs start from 10001 and increment correctly.
        customers = [Customer(f"Customer {i}") for i in range(5)]
        self.assertEqual(customers[0].customer_id, 10001)
        self.assertEqual(customers[-1].customer_id, 10005)
        for i in range(1, len(customers)):
            self.assertEqual(customers[i].customer_id, customers[i-1].customer_id + 1)
