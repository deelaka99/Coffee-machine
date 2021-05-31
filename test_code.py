import unittest
from cMachineClass import Person
from cMachineClass import Customer
from cMachineClass import Operator
from cMachineClass import Coffee


class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("You're going to test Person class")

    @classmethod
    def tearDownClass(cls):
        print("End of the test of  Person class")

    def setUp(self):
        print("Test is started")
        self.p1 = Person()
        self.p2 = Person()

    def tearDown(self):
        print("End test\n")

    def test_handle(self):
        # testing for p1
        self.assertEqual(self.p1.handle(), 'Someone is handling the coffee machine')
        self.assertNotEqual(self.p1.handle(), 'Deelaka is handling the coffee machine')
        # testing for p2
        self.assertEqual(self.p2.handle(), 'Someone is handling the coffee machine')
        self.assertNotEqual(self.p2.handle(), 'Deelaka is handling the coffee machine')

        self.p1.name = "Deelaka" # chanege name to "Deelaka"
        self.p2.name = "Deelaka"  # chanege name to "Deelaka"
        # testing for p1
        self.assertEqual(self.p1.handle(), 'Deelaka is handling the coffee machine')
        self.assertNotEqual(self.p1.handle(), 'Someone is handling the coffee machine')
        # testing for p2
        self.assertEqual(self.p2.handle(), 'Deelaka is handling the coffee machine')
        self.assertNotEqual(self.p2.handle(), 'Someone is handling the coffee machine')


class TestCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("You're going to test Customer class")

    @classmethod
    def tearDownClass(cls):
        print("End of the test of  Customer class")

    def setUp(self):
        print("Test is started")
        self.cus1 = Customer()
        self.cus2 = Customer()

    def tearDown(self):
        print("End test\n")

    def test_ordering(self):
        # testing for cus1
        self.assertEqual(self.cus1.ordering(), '***Someone is going to order***\n')
        self.assertNotEqual(self.cus1.ordering(), '***Deelaka is going to order***\n')
        self.assertEqual(self.cus1.handle(), 'Someone is handling the coffee machine')
        self.assertNotEqual(self.cus1.handle(), 'Deelaka is handling the coffee machine')
        # testing for cus2
        self.assertEqual(self.cus2.ordering(), '***Someone is going to order***\n')
        self.assertNotEqual(self.cus2.ordering(), '***Deelaka is going to order***\n')
        self.assertEqual(self.cus2.handle(), 'Someone is handling the coffee machine')
        self.assertNotEqual(self.cus2.handle(), 'Deelaka is handling the coffee machine')

        self.cus1.name = "Deelaka"  # change name to "Deelaka"
        self.cus2.name = "Deelaka"  # change name to "Deelaka"
        # testing for cus1
        self.assertEqual(self.cus1.ordering(), '***Deelaka is going to order***\n')
        self.assertNotEqual(self.cus1.ordering(), '***Someone is going to order***\n')
        self.assertEqual(self.cus1.handle(), 'Deelaka is handling the coffee machine')
        self.assertNotEqual(self.cus1.handle(), 'Someone is handling the coffee machine')

        # testing for cus2
        self.assertEqual(self.cus2.ordering(), '***Deelaka is going to order***\n')
        self.assertNotEqual(self.cus2.ordering(), '***Someone is going to order***\n')
        self.assertEqual(self.cus2.handle(), 'Deelaka is handling the coffee machine')
        self.assertNotEqual(self.cus2.handle(), 'Someone is handling the coffee machine')


class TestOperator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("You're going to test Operator class")

    @classmethod
    def tearDownClass(cls):
        print("End of the test of  Operator class")

    def setUp(self):
        print("Test is started")
        self.o1 = Operator()
        self.o2 = Operator()

    def tearDown(self):
        print("End test\n")

    """Enter 'someone' when test this"""
    def test_handle_inputSomeone(self):
        # testing for o1
        self.assertEqual(self.o1.handle(), '***\\;-) Someone is handling the coffee machine/***\n')
        self.assertNotEqual(self.o1.handle(), '***\\;-) Deelaka is handling the coffee machine/***\n')

        # testing for o2
        self.assertEqual(self.o2.handle(), '***\\;-) Someone is handling the coffee machine/***\n')
        self.assertNotEqual(self.o2.handle(), '***\\;-) Deelaka is handling the coffee machine/***\n')


class TestCoffee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("You're going to test Coffee class")

    @classmethod
    def tearDownClass(cls):
        print("End of the test of  Coffee class")

    def setUp(self):
        print("Test is started")
        self.c1 = Coffee("Black", 125, "Africa", 10)

    def tearDown(self):
        print("End test\n")

    def test_availability_check(self):
        # testing for c1
        self.assertEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: 10.0Kg +++\nYou can brew/order 200 of Black coffee cups!\n")
        self.assertNotEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: 9.5Kg +++\nYou can brew/order 200 of Black coffee cups!\n")
        self.assertNotEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: 0Kg +++\nYou can brew/order 200 of Black coffee cups!\n")
        self.assertNotEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: -1Kg +++\nYou can brew/order 200 of Black coffee cups!\n")
        self.assertNotEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: -99999999999999999Kg +++\nYou can brew/order 200 of Black coffee cups!\n")
        self.assertNotEqual(self.c1.availability_check(), "***Be cool!***\n+++Present value of raw materials: 9.5Kg +++\nYou can brew/order 55555555555555000 of Black coffee cups!\n")

    """Enter 1 and 5 when test this"""
    def test_input_raw_materials(self):
        # testing for c1
        self.assertEqual(self.c1.input_raw_materials(), "Your entered 5.0Kg of Black raw material! \n Full amount of the Black raw material is 15.0Kg.\nTo activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Raw materials were successfully added!***\n")
        self.assertNotEqual(self.c1.input_raw_materials(), "Your entered 0.0Kg of Black raw material! \n Full amount of the Black raw material is 10.0Kg.\nTo activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Raw materials were successfully added!***\n")

    """Enter 1 and 5 when test this"""
    def test_brew(self):
        Coffee.pay_statues = "Good"
        Coffee.amount = 8
        # testing for c1
        self.assertEqual(self.c1.brew(), ":-) Your 8 Black coffees are being brewed\n")
        self.assertNotEqual(self.c1.brew(), ":-) Your 2 Black coffees are being brewed\n")
        self.assertNotEqual(self.c1.brew(), ":-) Your 0 Black coffees are being brewed\n")
        self.assertNotEqual(self.c1.brew(), ":-) Your -1 Black coffees are being brewed\n")
        self.assertNotEqual(self.c1.brew(), ":-) Yours 2 Black coffees are being brewed\n")

        Coffee.amount = 1
        # testing for c1
        self.assertEqual(self.c1.brew(), ";-) Your  coffee is being brewed\n")
        self.assertNotEqual(self.c1.brew(), ";-) Your  coffee are being brewed\n")
        self.assertNotEqual(self.c1.brew(), ";-) Your  coffees is being brewed\n")

        Coffee.pay_statues = "Bad"
        # testing for c1
        self.assertEqual(self.c1.brew(), ";-) Can't brew now\n Please try again!\n")
        self.assertNotEqual(self.c1.brew(), ";-) Can't brew now\n Please try again!")
        self.assertNotEqual(self.c1.brew(), ";-) Can't brew now Please try again!\n")
        self.assertNotEqual(self.c1.brew(), ";-) Can't brews now\n Please try again!\n")

    def test_update(self):
        # testing for c1
        self.assertEqual(self.c1.update(), "To activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Coffee type was successfully modified!***\n")
        self.assertNotEqual(self.c1.update(), "To activate this Coffee typ, you must restart the machine!\n|||Thank you!|||\n***Coffee type was successfully modified!***\n")

    def test_print_receipt(self):
        # testing for c1
        self.assertEqual(self.c1.print_receipt(10), "\nTake your receipt!")
        self.assertNotEqual(self.c1.print_receipt(10), "Take you receipt!")


if __name__ == "__main__":
    unittest.main()
