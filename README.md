#test ui python 12 

pytest ./tests  - запуск тестов из папки последовательно 
pytest -n 3 ./tests - запуск тестов параллельно в 3-х потоках

from selenium.webdriver.common.action_chains import ActionChains


def hover(self):
    wd = webdriver_connection.connection
    element = wd.find_element_by_link_text(self.locator)
    hov = ActionChains(wd).move_to_element(element)
    hov.perform()