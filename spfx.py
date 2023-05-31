from playwright.sync_api import Playwright, sync_playwright, expect
import time
def time5():
    time.sleep(5)

def time3():
    time.sleep(3)

username = input('Enter username: ')
password = input('Enter password: ')

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/")
    page.get_by_label("User name:").click()
    page.get_by_label("User name:").fill(username)
    page.get_by_label("User name:").press("Tab")
    page.get_by_label("Password:").fill(password)
    page.get_by_label("Password:").press("Enter")
    time5()
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/")
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Tall Tiles layout selected").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemradio", name="List").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Open menu for Base Unit of Measure").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Filter to this value").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="No., sorted in Ascending order AAR0080013").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Item, Show more").click()
    time5()

    for i in range(1170):
        time.sleep(2)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Product Weight").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Product Weight").fill("0")
        time3()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Saved").click()
        time3()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Go to the next document of the same type.").click()
         
        continue
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
