import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.steps import Steps


@pytest.fixture
def steps() -> Steps:

    driver = webdriver.chrome(
        service = Service(ChromeDriverManager(
            path= "C:\Programs\Test-UI"
        ).install()),
        #options = None,

    )

    driver.get("https://python.org")

    steps_obj = Steps(driver)

    yield steps_obj

    driver.quit()


