from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.common.by import By

from tests.testAndroid import driver
#начала описывать элементы страницы

class AuthorizationLocators:
    ENTER_BUTTON = (by=AppiumBy.ID, value='com.atel.yard:id/button')
    LOGIN_FIELD = (By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.EditText')
    PASSWORD_FIELD = (By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.EditText')
    SUBMIT_BUTTON = (By.CLASS_NAME, value='android.widget.Button')
    CONTINUE_BUTTON = (By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.Button').click()
