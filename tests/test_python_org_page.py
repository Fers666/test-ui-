import steps
from steps import main_page

def test_search_input():
    search_text = "hello"

    driver = steps.DriverSteps().create_driver_and_open_python_page()

    steps.main_page(driver).search(search_text = search_text)

def test_donation_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_donate_steps()

def test_about_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_about_page()
def test_downloads_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_downloads_page()

def test_community_button():
    driver = steps.DriverSteps().create_driver_and_open_python_page()
    steps.main_page(driver).open_community_page()




