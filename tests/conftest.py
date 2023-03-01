import pytest
import sys
import requests
sys.path.append(r'D:\PROGRAMOWANIE\PYTHON\CASE')
from PROJECTBLOG.main import API
from PROJECTBLOG.post import Post



@pytest.fixture()
def setup_API_get():
        response = requests.get(API)
        return response
    
@pytest.fixture()
def setup_API_text():
        text_page= '[{"id":1,"body":"Over the last 18 months, we’ve seen this transition in technology from proving that you can do things with AI to mapping it to actual scenarios and processes where it’s useful to the end user.","title":"News Microsoft","subtitle":"How brands are using Microsoft AI to be more productive and imaginative"},{"id":2,"body":"In partnership with CalHFA, Apple has provided mortgage and down payment assistance to thousands of low- and moderate-income first-time homebuyers, and launched an affordable housing investment program that has unlocked funding to support nearly 2,000 units across the state. They include 315 units at Avenue 34 in Los Angeles, almost 340 units at Redwood Gardens in Berkeley, and more than 230 units for families in Chico’s Cedar Village, including for those impacted by the 2018 Camp Fire.","title":"News Apple","subtitle":"Apple partnerships are helping build new homes and new starts in communities across California"}]'
        return text_page
    
@pytest.fixture()
def setup_API_json(setup_API_get):
        return setup_API_get.json()

@pytest.fixture()
def setup_wrong_API():
        response = requests.get(API + "k")
        return response

@pytest.fixture()
def setup_Post():
        user= Post("999", "WoW", "World of Warcraft", "The best game of from MMO category")
        return user
