"""
test_dynamic_content.py
Dynamic Content: demonstrates the ever-evolving nature of content by loading new text and images on each page refresh.

[Scenario]
Get the inner HTML of third imgae

[Young's comment]
In complex cases, still easier to use CSS selector 

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_dynamic_content_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'Dynamic Content' page
    pageName = 'Dynamic Content'
    page.get_by_role('link', name=pageName).click()
    expect(page.get_by_role('heading')).to_have_text(pageName)

    # get the inner html of third image
    for i in range(5):
        print(page.locator("#content > div:nth-child(7) > div.large-2.columns > img").get_attribute('src'))
        page.reload()