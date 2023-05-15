from playwright.sync_api import Playwright, sync_playwright, expect
import time

def time2():
    time.sleep(2)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_SERV_UP/SignIn?ReturnUrl=%2FDT_BC21_SERV_UP%2F%3Fcompany%3DDeep%2520Catch%2520Trading%2520(Pty)%2520Ltd%26node%3D00002338-752d-0000-0c5f-2f00836bd2d2%26page%3D31%26dc%3D0")
    page.get_by_label("User name:").click()
    page.get_by_label("User name:").fill("Lothart")
    page.get_by_label("User name:").press("Tab")
    page.get_by_label("Password:").fill("Deepcatch@2023")
    page.get_by_label("Password:").press("Enter")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_SERV_UP/?company=Deep%20Catch%20Trading%20(Pty)%20Ltd&node=00002338-752d-0000-0c5f-2f00836bd2d2&page=31&dc=0&signInRedirected=1")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_SERV_UP/?company=Deep%20Catch%20Trading%20(Pty)%20Ltd&dc=0")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_SERV_UP/?company=Deep%20Catch%20Trading%20(Pty)%20Ltd&node=00002338-752d-0000-0c5f-2f00836bd2d2&page=31&dc=0")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_SERV_UP/?company=Deep%20Catch%20Trading%20(Pty)%20Ltd&node=00002338-752d-0000-0c5f-2f00836bd2d2&page=31&dc=0&bookmark=31%3bGwAAAAJ7%2fzIANABJAEMARQAwADAAMQAwADA%3d")
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox", name="Toggle FactBox").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Tall Tiles layout selected").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemradio", name="List").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Open menu for Base Unit of Measure").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Filter...").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Base Unit of Measure").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("gridcell", name="Code, sorted in Ascending order KG").click()
    time2()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="No., sorted in Ascending order AIDA002425").click()
    time2()
    

    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox", name="Toggle FactBox").click()
    time2()

    

    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="More options").click()
    time2()

    for i in range(283):
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Related").click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menu", name="Related").get_by_role("menuitem", name="Item").click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Units of Measure").click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Weight", exact=True).click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Weight", exact=True).fill("1")
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("grid", name="Item Units of Measure").locator("div").filter(has_text="Item Units of MeasurePress Ctrl+Enter to move to the next element after the tabl").click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Back").click()
        time2()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Go to the next document of the same type.").click()

        continue
        # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
