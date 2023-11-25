from django.test import TestCase
from monitoring_tool.views import EmissionList


# Create your tests here.


class EmissionList(TestCase):
    
     def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)