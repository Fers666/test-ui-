from pages.main_page import MainPage
from steps.base_steps import BaseSteps


class MainPageSteps(BaseSteps):

    @property
    def main_page (self)-> MainPage:
        return MainPage(self.driver)

    def search(self,search_text):
        assert self.main_page.search_input.is_displayed(),"seacrh field not displayed"
        self.main_page.search_input.clear()
        self.main_page.search_input.send_keys(search_text)
        assert self.main_page.search_input.get_property("value") == search_text, "Описание ошибки"
        self.main_page.start_search.click()

    def check_search_result(self):
        pass

    def open_donate_steps(self ):
        assert  self.main_page.donate_button.text == "Donate", "Donate button text is not Donate"
        self.main_page.donate_button.click()

    #Этот метод должен лежать в отдельном степе и отдельном пейдже
    def check_donate_page_is_open(self):
        pass

    def open_about_page(self):
        assert self.main_page.about_botton.text == "About", "About button text is not About"
        self.main_page.about_botton.click()

    def check_about_page_is_open(self):
        pass

    def open_downloads_page(self):
        assert self.main_page.downloads_button.text == "Downloads", "Downloads button text is not Downloads"
        self.main_page.downloads_button.click()

    def check_downloads_page_is_open(self):
        pass

    def open_community_page(self):
        assert  self.main_page.community_button.text == "Community", "Community button text is not Community"
        self.main_page.community_button.click()

    def check_community_page(self):
        pass

