from .base import FunctionalTest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from unittest import skip

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        

