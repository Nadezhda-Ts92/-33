import unittest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.reg_page import RegPage
from pages.new_pass_page import NewPassPage

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # или другой подходящий драйвер
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        auth_page = AuthPage(self.driver)
        auth_page.enter_reg_page()
        reg_page = RegPage(self.driver)
        reg_page.enter_firstname("John")
        reg_page.enter_lastname("Doe")
        reg_page.enter_email("john.doe@example.com")
        reg_page.enter_password("test123")
        reg_page.enter_pass_conf("test123")
        reg_page.btn_click()
        # Здесь вы можете добавить дополнительные проверки или действия после регистрации пользователя

if __name__ == "__main__":
    unittest.main()
