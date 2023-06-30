"""
test_file_upload.py
File Upload: exercise file upload case using FileChooser object

[Scenario]
choose testpic.jpg and click upload button
check if it's uploaded

[Young's comment]


"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_file_upload_by_playwright(BasePage):
    page :Page = BasePage

    # go to 'File Upload' page
    pageName = 'File Upload'
    page.get_by_role('link', name=pageName, exact=True).click()
    expect(page.get_by_role('heading')).to_have_text(pageName+"er")

    # choose a file to upload
    file_name = "testpic.jpg"
    upload_from = "./file"

    with page.expect_file_chooser() as fc_info:
        page.locator("#file-upload").click()

    file_chooser = fc_info.value
    file_chooser.set_files(f"{upload_from}/{file_name}")

    # click upload button
    page.get_by_role('button', name='Upload').click()

    # check if it's uploaded
    expect(page.locator("#uploaded-files")).to_have_text(file_name)



