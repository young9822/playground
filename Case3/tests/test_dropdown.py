"""
test_dropdown.py
Dropdown: Exercise dropdown list

[Scenario]
Click dropdown list and select option 1
Again, click dropdown list and select option 2

[Young's comment]


"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_drag_drop_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'Dropdown' page
    pageName = 'Dropdown'
    page.get_by_role('link', name=pageName).click()
    expect(page.get_by_role('heading')).to_have_text(pageName+' List')

    dropdownLocator = page.locator('select#dropdown')

    # click dropdown list and select option 1
    dropdownLocator.select_option(value='1')
    assert page.locator("option[value='1']").get_attribute('selected') == 'selected'

    # click dropdown list and select option 2
    dropdownLocator.select_option(value='2')
    assert page.locator("option[value='2']").get_attribute('selected') == 'selected'
