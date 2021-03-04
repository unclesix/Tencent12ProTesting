from web.selenium_po.pageobject1 import Main

class Testpageobject:
    def test_one(self):
        main = Main()
        print(main.test_get_firstlink().test_gettext())
