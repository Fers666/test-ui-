
import steps


def test_search_input():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).search(search_text="hello")
    steps.main_page(driver).check_search_result()

def test_donation_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_donate_page()

def test_about_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_about_page()

"""def test_about_menu():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_about_menu()
"""
def test_downloads_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_downloads_page()

def test_community_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_community_page()

def test_success_stories_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_success_stories_page()
def test_news_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_news_page()

def test_events_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_events_page()





