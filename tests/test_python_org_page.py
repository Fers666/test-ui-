# noinspection PyUnresolvedReferences
from src.fixtures import steps

import pytest



@pytest.Mark.parametrize("search_text", "hello" , "buy" , "good")
def test_search_input(steps,search_text):
    steps.main_page.search(search_text= search_text)
    steps.main_page.check_search_result()

def test_donation_button(steps):
    steps.main_page.open_donate_page()

def test_about_button(steps):
    steps.main_page.open_about_page()







