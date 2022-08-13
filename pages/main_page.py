from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def donate_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//a[@class='donate-button']")

    @property
    def search_input(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@id='id-search-field']")

    @property
    def start_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")
    @property
    def about_botton(self):
        return self.driver.find_element(By.XPATH,"//li[@id='about']")

    @property
    def downloads_button(self):
        return self.driver.find_element(By.XPATH,"//li[@id='downloads']")

    @property
    def community_button(self):
        return self.driver.find_element(By.XPATH,"//li[@id='community']")