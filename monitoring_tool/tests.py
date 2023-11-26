from django.test import TestCase
from .views import first_monday_current_month, first_monday_next_month
import datetime
from freezegun import freeze_time
# freezegun info here: https://github.com/spulec/freezegun

# Create your tests here.


class FirstMonday(TestCase):

   first_monday_of_this_month = first_monday_current_month()
   first_monday_of_next_month = first_monday_next_month()

   def test_return_datetime(self):
      """
      Test that the first Monday functions return a datetime object.
      """
      self.assertEqual(type(self.first_monday_of_this_month), datetime.datetime)
      self.assertEqual(type(self.first_monday_of_next_month), datetime.datetime)
  
   @freeze_time("2012-04-30")
   def test_first_monday_this_month(self):
      """
      Use freeze gun to set datetime to 30/04/1978. This enables 
      assertEqual to check against known first Monday of that particular
      month which was 02/04/1978.
      """
      first_monday_april_78 = first_monday_current_month()
      print("First monday of April 1978 was: ",first_monday_april_78)
      self.assertEqual (first_monday_april_78, datetime.datetime(2012, 4, 2))


   @freeze_time("2012-04-30")
   def test_first_monday(self):
      """
      Use freeze gun to set datetime to 30/04/1978. This enables 
      assertEqual to check against known first Monday of the following
      month which was 07/05/1978.
      """
      first_monday_may_78 = first_monday_next_month()
      print("First monday of May 1978 was: ",first_monday_may_78)
      self.assertEqual (first_monday_may_78, datetime.datetime(2012, 5, 7))


