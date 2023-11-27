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


class TestCalls(TestCase):

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
      admin_password = 'password'
      admin_user = get_user_model().objects.create_user(admin_username, password=admin_password)
      admin_group.user_set.add(admin_user)

# Code for below from stack overflow:
# https://stackoverflow.com/questions/22457557/how-to-test-login-process
   def test_login_verified_user(self):
      """
      checks if verified user created in set up can log in. 
      Performs two assertions - checks user is verified and confirms
      if request has been successful.
      """
      user = get_object_or_404(User, **dict(username='test_user'))
      response = self.client.post('/accounts/login/', 
                                 { 'user': user, 
                                  'password':'password'
                                  }, follow=True)
      # check if user is authenticated.
      self.assertTrue(user.is_authenticated)
      # check if request has succeeded.
      self.assertEqual(response.status_code, 200)

   def test_emission_user(self):
      self.client.login(username="test_user", password='password')
      response = self.client.get('/add-emission', 
                                follow=True)
      # check if request has failed resulting in forbiddent HTTP code.
      self.assertEqual(response.status_code, 403)

   def test_emission_admin(self):
      self.client.login(username="admin_user", password='password')
      print(self.client)
      response = self.client.get('/add-emission', 
                                follow=True)
      # check if request has succeeded.
      self.assertEqual(response.status_code, 200)


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


