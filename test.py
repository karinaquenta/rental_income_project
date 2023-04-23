import unittest

from Rentalincome import Rental_Roi

class TestRental_Roi(unittest.TestCase):

 def test_user_input(self):
   rental_roi = Rental_Roi()
   rental_roi.get_user_input()
   self.assertIsNotNone(rental_roi.user_input in ['1', '2'])

 def test_input_commas(self):
   rental_roi = Rental_Roi()
   rental_roi.get_user_input()  
   self.assertEqual(rental_roi.income, 0)
   self.assertEqual(rental_roi.expenses, 0)
   self.assertEqual(rental_roi.down_payment, 0)

 def test_monthly_calculation(self):
   rental_roi = Rental_Roi(income = 1000, expenses = 500, down_payment = 30000)
   rental_roi.calc_cash_flow_monthly()
   self.assertEqual(rental_roi.cash_flow_monthly, 500)

 def test_yearly_calculation(self):
   rental_roi = Rental_Roi(income = 1000, expenses = 500, down_payment = 30000)   
   rental_roi.calc_cash_flow_monthly()
   rental_roi.calc_cash_flow_yearly()
   self.assertEqual(rental_roi.cash_flow_yearly, 6000)

 def test_roi_calculation(self):
   rental_roi = Rental_Roi(income = 1000, expenses = 500, down_payment = 20000)
   rental_roi.calc_cash_flow_monthly()
   rental_roi.calc_cash_flow_yearly()
   rental_roi.calc_roi()
   self.assertEqual(rental_roi.roi, 30.0)















if __name__ == '__main__':
    unittest.main()    