from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class AboutPage(BasePage):

    @property
    def about_page(self)-> WebElement:
        return self.driver.find_element(By.XPATH,"//body[@class='python about']")

