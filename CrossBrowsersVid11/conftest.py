import json
from pytest import fixture
from selenium import webdriver

data_path = 'test_data.json'

def load_test_data(path):  #from test_data.json
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Safari])  #IMPORTANT when I add parameters to this fixture any test that calls this fixture is gonna run this test one time for every parameter in []
def broswer(request):   #we get request for free from pytest
    driver = request.param
    drvr = driver()
    yield drvr  #we yield because we want to shut it down when its done with each driver.  Each time its gonna use different browser drive
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data