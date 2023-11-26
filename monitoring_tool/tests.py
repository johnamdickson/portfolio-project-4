from django.test import TestCase
from .views import first_monday_current_month, first_monday_next_month
from datetime import datetime


# Create your tests here.

class FirstMonday(TestCase):

   first_monday_this_month = first_monday_current_month()
   first_monday_next_month = first_monday_next_month()

   def test_return_datetime(self):
      """
      Test that the functions return a datetime object.
      """
      self.assertEqual(type(self.first_monday_this_month), datetime)
      self.assertEqual(type(self.first_monday_next_month), datetime)

