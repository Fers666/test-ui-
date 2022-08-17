from src.steps.main_page_steps import MainPageSteps
from src.steps.about_page_steps import AboutPageSteps

class Steps:
    def __init__(self, driver):
        self.driver = driver

    @property
    def main_page(self) -> MainPageSteps:
        return MainPageSteps(driver = self.driver)

    @property
    def about_page(self) -> AboutPageSteps:
        return AboutPageSteps(driver=self.driver)
