import steps
from steps import main_page

def test_search_input():
    search_text = "hello"

    driver = steps.DriverSteps().create_driver_and_open_python_page()

    main_page(driver).search(search_text = search_text)




