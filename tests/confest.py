import pytest
from appium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_cap)
    yield driver
    driver.quit()