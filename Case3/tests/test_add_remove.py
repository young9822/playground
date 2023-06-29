"""
test_add_remove.py
Add/Remove Elements

[Scenario]
Click 'Add Element' button 3 times
Click all 'Delete' buttons one by one
Check if there is no 'Delete'

[Young's comment]
Nothing special

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_add_remove_by_playwright(BasePage):
    page :Page = BasePage

    # go to Add/Remove Elements page
    pageName = 'Add/Remove Elements'
    page.get_by_role('link', name=pageName).click()
    expect(page.get_by_role('heading')).to_have_text(pageName)

    # click 'Add Element' button 5 times
    for i in range(5):
        page.get_by_role('button', name='Add Element').click()

    # click all 'Delete' buttons one by one
    for i in range(5):
        page.get_by_role('button', name='Delete').first.click()

    # check if there is no 'Delete'
    expect(page.get_by_role('button', name='Delete')).not_to_be_attached()