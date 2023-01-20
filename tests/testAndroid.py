from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

desired_cap = {
    "platformName": "Android",
    "appium:appPackage": "com.atel.yard",
    "appium:deviceName": "296ef605",
    "appium:appActivity": "com.intersvyaz.yard.root.RootActivity",
    "appium:appWaitDuration": "30000",
    "autoWebView": "true"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)
driver.find_element(by=AppiumBy.ID, value='com.atel.yard:id/button').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.EditText').send_keys('is59')
driver.find_element(By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.EditText').set_text('123456')
driver.find_element(By.CLASS_NAME, value='android.widget.Button').click()
sleep(3)
driver.find_element(By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.Button').click()
mainTitleText = driver.find_element(by=AppiumBy.ID, value='com.atel.yard:id/titleText').text
assert mainTitleText == "Домофон Ател"
print('done')

