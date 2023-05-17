from playwright.sync_api import Playwright, sync_playwright, expect
import time

def time5():
    time.sleep(3)

items_code = [
    "FCBA000012",
    "FCBA000012",
    "FCBA000012",
    "FCBA000012",
    "FCBA006807",
    "FCBA006807",
    "FCBA006807",
    "FCFE000678",
    "FCFE000678",
    "FCFE000678",
    "FCFE006546",
    "FCFE006546",
    "FCGI000012",
    "FCGI000012",
    "FCGI000012",
    "FCMDM06523",
    "FCNE000010",
    "FCNE000010",
    "FCNE000010",
    "FCNE000011",
    "FCSK006355",
    "FCSK006355",
    "FRCHMD00",
    "FRCHMD00"
]

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bc.deepcatchgroup.com/")
    page.get_by_label("User name:").click()
    page.get_by_label("User name:").fill("")
    page.get_by_label("User name:").press("Tab")
    page.get_by_label("Password:").fill("")
    page.get_by_label("Password:").press("Enter")
    page.goto("https://bc.deepcatchgroup.com/")
    page.goto("https://bc.deepcatchgroup.com/")
    page.goto("https://bc.deepcatchgroup.com/")
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox", name="Toggle FactBox").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Tall Tiles layout selected").click()
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemradio", name="List").click()
    time5()

    for items in items_code:
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Search").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_placeholder("Search").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_placeholder("Search").fill(items)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Show the rest").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_title("View or edit the item's attributes, such as color, size, or other characteristics that help to describe the item.").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("columnheader", name="Description Open menu for Description").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("grid", name="Item Attribute Values").get_by_text("COPACOL").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill("COPACOL")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Enter")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("OKCancel").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="OK").click()
        time5()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
