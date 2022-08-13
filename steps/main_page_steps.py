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