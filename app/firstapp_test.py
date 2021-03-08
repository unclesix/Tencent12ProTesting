from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.1.2'
desired_caps['deviceName']='127.0.0.1:21503'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()