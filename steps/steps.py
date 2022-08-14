from steps.driver_steps import DriverSteps
from steps.main_page_steps import MainPageSteps
from steps.about_page_steps import AboutPageSteps

def main_page(driver) -> MainPageSteps:
    return MainPageSteps(driver=driver)


def driver_steps() -> DriverSteps:
    return DriverSteps()

def about_page(driver) -> AboutPageSteps:
    return AboutPageSteps(driver=driver)
