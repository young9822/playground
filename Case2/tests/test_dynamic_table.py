"""
test_dynamic_table.py
Dynamic Table: There is a table where columns and rows change their position upon page reload. Values in cells are random. The table is based on DIVs with ARIA attributes. See WAI-ARIA table design pattern for details.

[Scenario]
Get the CPU share of Chrome process from the table and compare it to the value of below yellow line

[Young's comment]
It's not easy to get the CPU share of Chrome in both cases.

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_dynamic_table_by_playwright(BasePage):
    page :Page = BasePage

    # go to AJAX Data page
    selection = 'Dynamic Table'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # get the CPU share of Chrome
    currentShare = page.get_by_role('row').filter(has_text='Chrome').get_by_role('cell').filter(has_text='%').inner_text()
    expectedMsg = f"Chrome CPU: {currentShare}"
    
    expect(page.locator('.bg-warning')).to_have_text(expectedMsg)

