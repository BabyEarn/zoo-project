import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)  

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100) 
    
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150) 
    
    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100) 

    def test_edge_case_lower_bound(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)  

    def test_edge_case_upper_teen(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)  
    
    def test_edge_case_senior(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 100)  

    def test_invalid_age_zero(self):
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(0)  

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-5)  

    def test_edge_case_unhandled_age(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 150)  
if __name__ == '__main__':
    unittest.main()
