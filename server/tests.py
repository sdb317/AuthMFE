###########################################################
## File        : test.py
## Description : 

import sys
import os
import re
import time
import fnmatch
import csv
import fileinput

from urllib.parse import urljoin
import json

from django.conf import settings
from django.test import TestCase, Client, RequestFactory
from django.test.runner import DiscoverRunner
from rest_framework import status
from rest_framework.test import APIClient

import mock

# python manage.py test server.tests.MyTestCases.test<TestName>

class DiscoverRunnerNoDatabase(DiscoverRunner):
    """
    An override of Django's test runner that avoids creation of a test database (see TEST_RUNNER in settings.py)
    """

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        self.setup_test_environment()
        suite = self.build_suite(test_labels, extra_tests)
        result = self.run_suite(suite)
        self.teardown_test_environment()
        return self.suite_result(suite, result)

class MyTestCases(TestCase):

    @classmethod
    def setUpClass(cls):
        '''Call on class creation.'''
        print('Calling \'setUpClass\'')
        super(MyTestCases, cls).setUpClass()

    def setUp(self):
        '''Call before every test case.'''
        print('Calling \'setUp\'')

    def tearDown(self):
        '''Call after every test case.'''
        print('Calling \'tearDown\'')

    '''Test cases. Note that all test method names must begin with 'test'.'''

    def testAlwaysWorks(self): # test server.tests.MyTestCases.testAlwaysWorks
        try:
            assert True
        except Exception as e:
            assert False,'Exception: %s'%str(e)

    def testUserModel(self): # test server.tests.MyTestCases.testUserModel
        try:
            from django.contrib.auth.models import User
            users = User.objects # .filter()
            assert len(User.objects.filter()) > 0
        except Exception as e:
            assert False,'Exception: %s'%str(e)

    def testUserLogin(self): # test server.tests.MyTestCases.testUserLogin
        print('Calling \'testUserLogin\'')
        try:
            client = APIClient(enforce_csrf_checks=True)
            url = '/api/v1/users/'
            payload = {'username': 'test', 'password': 'moonboot'}
            response = client.post(url + 'login/', payload) # 'multipart' encoded
            assert response.status_code == 200 and response.data['success'] != None and response.data['success']['user']['authenticated']
            print(json.dumps(response.data))
        except Exception as e:
            assert False,'Exception: %s'%str(e)

    def testUserLogout(self): # test server.tests.MyTestCases.testUserLogout
        print('Calling \'testUserLogout\'')
        try:
            client = APIClient(enforce_csrf_checks=True)
            url = '/api/v1/users/'
            payload = {'username': 'test', 'password': 'moonboot'}
            response = client.post(url + 'login/', payload) # 'multipart' encoded
            response = client.post(url + 'logout/')
            assert response.status_code == 200 and response.data['success'] != None
            print(json.dumps(response.data))
        except Exception as e:
            assert False,'Exception: %s'%str(e)


if __name__=='__main__': # Only used if run outside of Django
    try:
        print("Starting tests")
        # unittest.main() # Run all tests
        suite=unittest.TestSuite() # ...or select tests to run using 'TestSuite'
        #suite.addTest(MyTestCases('<MethodName>')) # Add the test method name here
        unittest.TextTestRunner(verbosity=1).run(suite)
        print("Finished tests")
    except Exception as e:
        print('Exception: %s'%str(e))

