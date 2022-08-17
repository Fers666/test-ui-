from src.pages.about_page import AboutPage
from src.steps.base_steps import BaseSteps

class AboutPageSteps(BaseSteps):

    @property
    def about_page(self)-> AboutPage:
        return AboutPage(self.driver)

    def check_about_page_is_open(self):
        assert self.about_page.about_page.is_displayed(),"about page is open"