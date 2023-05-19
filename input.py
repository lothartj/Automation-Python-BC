import os
from playwright.sync_api import Page, sync_playwright
import time

def test_file_upload(page: Page) -> None:
    page.goto('https://online2pdf.com/')
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, 'images', 'Red_Car', 'Red Car_8.png')
    
    with page.expect_file_chooser() as fc_info:
        page.locator('text=Select files').click()
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)

    page.wait_for_timeout(3000)

# Create a Playwright instance and launch a browser
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Call the test function
    test_file_upload(page)
    time.sleep(3000000)
    # Close the browser
    context.close()
    browser.close()
