# 定义公共构造方法，封装初始化函数操作步骤
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = None  # 类变量，要在函数方法之前进行赋值的。当实例化Main(BasePage)时，会主动调用BasePage中的__init__，此时的drvier来判断是否有值。
    base_url = ""  # 类变量，要在函数方法之前进行赋值的。当实例化Main(BasePage)时，会主动调用BasePage中的__init__，此时url就是传进来的url。

    def __init__(self, driver: WebDriver = None):  # WebDriver默认值为None
        # 前提：复用浏览器调试开启：  如果driver为空，则调用复用浏览器并打开。
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            # 设置全局隐式等待
            self.driver.implicitly_wait(3)
        # 如果driver有值，则传入driver使用。比如： return Addmembers(self.driver)
        else:
            self.driver = driver
        # url不是都需要调用，在main中定义访问。  根据实际业务场景来设置即可。
        if self.base_url != "":
            self.driver.get(self.base_url)

    # 封装find方法,不再将drvier暴露
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 封装finds方法,不再将drvier暴露
    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    # # 设置显示等待
    def wait_for_click(self, locator, time=10):
        #element_to_be_clickable 元素是否可以被点击
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
