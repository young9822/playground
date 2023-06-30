"""
test_file_download.py
File Download: exercise Download objest and its methods

[Scenario]
click testpic.jpg and check if it's downloaded

[Young's comment]


"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_file_download_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'File Download' page
    pageName = 'File Download'
    page.get_by_role('link', name=pageName, exact=True).click()
    expect(page.get_by_role('heading')).to_have_text(pageName+"er")

    # download testpic.jpg
    with page.expect_download() as download_info:
        page.get_by_role('link', name="testpic.jpg", exact=True).click()
    
    download = download_info.value

    print(f"{download}")
    print(f"{download.suggested_filename}: {download.path()}")

    # need to update the following path for yours
    # download.save_as("/YOUR/PATH/TO/DOWNLOAD/"+download.suggested_filename)
    
    download.delete()

