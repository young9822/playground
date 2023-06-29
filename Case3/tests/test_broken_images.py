"""
test_broken_images.py
Broken Images: has 2 broken images in the page

[Scenario]
Check if all image element are attached

[Young's comment]


"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_broken_images_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'Broken Images' page
    pageName = 'Broken Images'
    page.get_by_role('link', name=pageName).click()
    expect(page.get_by_role('heading')).to_have_text(pageName)
    
    # check if all image element are attached
    for i in range(3):
        # can't use get_by_role() as the role of images is changed from image to presentation        
        expect(page.locator("img").nth(i)).to_be_attached()