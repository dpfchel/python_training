# -*- coding: utf-8 -*-
import pytest
import json
from fixture.application import Application
import os.path

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    # __file__ = C:\Users\dpf\PycharmProjects\python_training\conftest.py
    # os.path.abspath(__file__) = C:\Users\dpf\PycharmProjects\python_training\conftest.py
    # os.path.dirname(os.path.abspath(__file__)) = C:\Users\dpf\PycharmProjects\python_training
    # os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption(--target)) = C:\Users\dpf\PycharmProjects\python_training\target.json
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file, encoding='cp1251') as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        fixture.session.login(username=target['username'], password=target['password'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True) # сработает автоматом, даже если ни в каком тесте не указана
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json') #'target.json'
