"""
test_client_side_delay.py
Client Side Dealy: Some elements may appear after client-side time consuming JavaScript calculations

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_client_side_delay_by_playwright(BasePage):
    page = BasePage

    # go to test input page
    selection = 'Client Side Delay'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    # click the button
    page.get_by_role('button', \
        name='Button Triggering Client Side Logic').click()
    # click the text to verify if it's disappeared
    # wonderful auto-waiting feature
    page.get_by_text('Data calculated on the client side.').click()
