from django.test import TestCase, Client, SimpleTestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User, Group, Permission
from .views import first_monday_current_month, first_monday_next_month
import datetime
from freezegun import freeze_time
# freezegun info here: https://github.com/spulec/freezegun
import cloudinary
import logging
from django.contrib.auth import get_user_model
import cloudinary_config_test as cct
from .models import Emission


class TestEmissionCalls(TestCase):

   @classmethod
   def setUpTestData(cls):
      cloudinary.config(
         cloud_name = cct.cloud_name,
         api_key = cct.api_key,
         api_secret = cct.api_secret,
         secure = True
         )
      client = Client()
      # set up base user group - emission_user
      user_group = Group(name="emission_user")
      user_group.save()
      username = 'test_user'
      password = 'password'
      base_user = get_user_model().objects.create_user(username, password=password)

      # set up admin user group - emission_admin
      admin_group = Group(name="emission_admin")
      admin_group.save()
      # solution to adding multiple permissions to group at once from Stack Overflow:
      # https://stackoverflow.com/questions/71225949/django-how-to-add-multiple-permissions-on-group
      permissions_names = ['view_emission', 'change_emission', 'add_emission']
      permissions = Permission.objects.filter(content_type__app_label='monitoring_tool', codename__in=permissions_names)
      for permission in permissions.all():
         admin_group.permissions.add(permission)
      admin_username = 'admin_user'
      admin_user = get_user_model().objects.create_user(admin_username, password=password)
      admin_group.user_set.add(admin_user)

      # create a superuser
      superuser_username = 'super_user'
      superuser = User.objects.create_superuser(superuser_username, password=password)

      # create an emission object in test database.
      emission = Emission.objects.create(
         title = 'test_emission',
         location = 'here',
         username = admin_user,
         emission_image = 'static/images/favicon.png',
         description = 'This is a test',
         latitude = 0,
         longitude = 0,
         created_on = datetime.datetime.now(),
         next_check_due = datetime.datetime.now(),
         current_check_due = datetime.datetime.now(),
         status = 0,
         type = 1,
      )


# Code for below from stack overflow:
# https://stackoverflow.com/questions/22457557/how-to-test-login-process
   def test_login_verified_user(self):
      """
      Checks if verified user created in set up can log in. 
      Performs two assertions - checks user is verified and confirms
      if request has been successful.
      """
      user = get_object_or_404(User, **dict(username='test_user'))
      response = self.client.post('/accounts/login/', 
                                 { 'user': user, 
                                  'password':'password'
                                  }, follow=True)
      
      # How to access vars in class allowing me to access the _testMethodName property.
      #  https://stackoverflow.com/questions/5969806/print-all-properties-of-a-python-class
      print(
         self._testMethodName.upper(), 
         "\nUser verification returned: ",
         user.is_authenticated, '\n',
         f"Status code on attempted login by {user}: ",
         response.status_code, '\n'
         )
       # check if user is authenticated.
      self.assertTrue(user.is_authenticated)
      # check if request has succeeded.
      self.assertEqual(response.status_code, 200)

   def test_non_verified_user(self):
      """
      Test non-verified user trying to access any page other than home, 
      in this case emissions. Assert redirect should confirm an initial
      302 error with a target status code of 200 once redirected to login
      page.
      """
      # code for this test derived from this answer on Stack Overflow:
      # https://stackoverflow.com/questions/47020253/django-testing-how-to-assert-redirect
      response = self.client.get('/emissions/', 
                                follow=True)
      # assert that get request outside of home page returns a 302 status code and redirects 
      # user to log in page.
      print(
         self._testMethodName.upper(), 
         "\nInitial Response code: ",
         response.redirect_chain[0][1],'\n',
         f"Status code on redirect to login page: ",
         response.status_code, '\n'
         )
      self.assertRedirects(
         response, 
         '/accounts/login/?next=/emissions/',
         status_code=302, 
         target_status_code=200,
         fetch_redirect_response=True)

   def test_adding_emission_no_perms(self):
      """
      Test base user trying to add an emission. Assert equal should confirm
      a 403 error indicating this operation IS NOT allowed for this particular
      user.
      """
      self.client.login(username="test_user", password='password')
      response = self.client.get('/add-emission', 
                                follow=True)
      # check if request has failed resulting in forbidden HTTP code.
      print(
         self._testMethodName.upper(), 
         '\nStatus code on attempting to add an emission by base_user:',
         response.status_code, '\n',
         "The following exception was raised: ",
         response.context['exception'], '\n'
         )
      self.assertEqual(response.status_code, 403)
      self.assertEqual(
         response.context['exception'], 
         'You do not have the necessary permissions to add an emission. Please contact your system administrator.'
         )

   def test_adding_emission_with_perms(self):
      """
      Test admin_user with emission_admin rights trying to add an emission. Assert equal should confirm
      a 200 status code indicating this operation IS allowed for this particular
      user.
      """
      self.client.login(username="admin_user", password='password')
      response = self.client.get('/add-emission', 
                                follow=True)
      # check if request has succeeded.
      print(
         self._testMethodName.upper(), 
         '\nStatus code on attempting to add an emission by admin_user:',
         response.status_code, '\n'
         )
      # print('Status code on attempted login by admin_user:', response.status_code)
      self.assertEqual(response.status_code, 200)

   def test_emission_deletion_no_perms(self):
      """
      Test admin_user trying to delete an emission. Assert equal should confirm
      a 403 status code indicating this operation IS NOT allowed for this particular
      user.
      """
      emission = Emission.objects.get(title='test_emission')
      slug = emission.slug
      self.client.login(username="admin_user", password='password')
      response = self.client.get(f'/delete-emission/{slug}', 
                                follow=True)
      print(
         self._testMethodName.upper(), 
         '\nStatus code on attempting to delete an emission by admin_user:',
         response.status_code, '\n',
         f"The following exception was raised: ",
         response.context['exception'], '\n'
         )
      self.assertEqual(response.status_code, 403)
      self.assertEqual(
         response.context['exception'], 
         'You do not have the necessary permissions to delete an emission. Please contact your system administrator.'
         )

   def test_emission_deletion_with_perms(self):
      """
      Test superuser trying to delete an emission. Assert equal should confirm
      a 200 status code indicating this operation IS allowed for this particular
      user.
      """
      emission = Emission.objects.get(title='test_emission')
      slug = emission.slug
      self.client.login(username="super_user", password='password')
      response = self.client.get(f'/delete-emission/{slug}', 
                                follow=True)
      print(
         self._testMethodName.upper(), 
         "\nInitial Response code: ",
         response.redirect_chain[0][1],'\n',
         f"Status code on redirect to emissions page: ",
         response.status_code, '\n'
         )
     
      self.assertRedirects(
         response, 
         '/emissions/',
         status_code=301, 
         target_status_code=200,
         fetch_redirect_response=True)

         
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
      print(
         self._testMethodName.upper(), 
         "\nFirst monday of April 1978 was: ",
         first_monday_april_78, '\n'
         )  
      self.assertEqual (first_monday_april_78, datetime.datetime(2012, 4, 2))


   @freeze_time("2012-04-30")
   def test_first_monday_next_month(self):
      """
      Use freeze gun to set datetime to 30/04/1978. This enables 
      assertEqual to check against known first Monday of the following
      month which was 07/05/1978.
      """
      first_monday_may_78 = first_monday_next_month()
      print(
         self._testMethodName.upper(), 
         "\nFirst monday of May 1978 was: ",
         first_monday_may_78, '\n'
         )  
      self.assertEqual (first_monday_may_78, datetime.datetime(2012, 5, 7))


