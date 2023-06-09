import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Playwright, Page
import asyncio

# Enter The BC Item Cose
BC_Item_Code = str(input('Enter the Item Number (10 digits only): '))
while len(BC_Item_Code) != 10 or not BC_Item_Code:
    BC_Item_Code = input('Invalid input. Please enter exactly 10 digits: ')

# Enter The Item Description
Item_Description = input('Enter the Item Description (50 characters or less): ')
symbols = ['!','@', '#', '$', '%', '&', '*', '(',')','*','/','^' ]
while len(Item_Description) > 50 or any(symbol in Item_Description for symbol in symbols):
    Item_Description = input('Invalid input. Please enter 50 characters or less without using the following symbols: ! @ # $ % & * ( ) / ^ ')


# Enter UOM
while True:
    UOM = input('Enter the UOM (KG, EA, or CS): ')
    if UOM.upper() in ['KG', 'EA', 'CS']:
        break
    else:
        print('Invalid UOM. Please enter KG, EA, or CS.')

# Enter Barcode 
Barcode = input('Enter Barcode: ')
while not Barcode.isdigit():
    Barcode = input('Invalid input. Please enter only numbers: ')

# Enter Net Weight
Net_Weight = input('Enter Net Weight: ')
while not Net_Weight.isdigit():
    Net_Weight = input('Invalid input. Please enter only numbers: ')

# Enter Gross Weight
Gross_Weight = input('Enter Gross Weight: ')
while not Gross_Weight.isdigit():
    Gross_Weight = input('Invalid input. Please enter only numbers: ')

# Enter item Category 
valid_categories = ['BAKERY', 'BEVERAGES', 'DAIRY', 'DELI', 'FISH', 'FRUIT & VEG', 'GROCERIES', 'MEAT', 'NON DAIRY', 'NON FOOD', 'POULTRY', 'SEAFOOD']
Item_Category = input('Item Category [BAKERY, BEVERAGES, DAIRY, DELI, FISH, FRUIT & VEG, GROCERIES, MEAT, NON DAIRY, NON FOOD, POULTRY, SEAFOOD ')
while Item_Category.upper() not in valid_categories:
    Item_Category = input('Invalid input. Please enter a valid category: ')

# Enter General Prod Posting Group
General_Prod_Posting_Group = input('1010')

Height = input('Enter the Height ')

Width = input('Enter the Width ')

Length = input('Enter the Length ')

Location_Code = input('Enter the Location Code 1-ASTORE ')

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    username35 = input('Input your Username... ')
    password35 = input('Input your password... ')
    #Open Business Central
    def openBC():
        page.goto("https://bc.deepcatchgroup.com")
        page.get_by_label("User name:").click()
        page.get_by_label("User name:").fill(username35)
        page.get_by_label("User name:").press("Tab")
        page.get_by_label("Password:").fill(password35)
        page.get_by_label("Password:").press("Enter")
    openBC()

    def time1():
        time.sleep(4)
    time1()

    # Go to Main Page
    def goToMainPage():
        page.goto("https://bc.deepcatchgroup.com" )#Closed
        time1()
    goToMainPage()

    
    # Click Item Button
    def Click_Item_Button():
        itemB = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Items, View or edit detailed information for the products that you trade in. The item card can be of type Inventory or Service to specify if the item is a physical unit or a labor time unit. Here you also define if items in inventory or on incoming orders are automatically reserved for outbound documents and whether order tracking links are created between demand and supply to reflect planning actions.")
        itemB.click()
        time1()
    Click_Item_Button()

    # import asyncio

    # import asyncio

    # async def main():
    #     # your code to initialize the browser and page objects
    #     async def Click_Item_Button():
    #         itemB = await page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Items, View or edit detailed information for the products that you trade in. The item card can be of type Inventory or Service to specify if the item is a physical unit or a labor time unit. Here you also define if items in inventory or on incoming orders are automatically reserved for outbound documents and whether order tracking links are created between demand and supply to reflect planning actions.")
    #         await itemB.click()
    #     await Click_Item_Button()

    # asyncio.run(main())



    # Collapse The fact Box
    def collapse_fact_box():
        fact_box_button = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox[name=\"Toggle FactBox\"]")
        fact_box_button.click()
        time1()
    collapse_fact_box()

    # Press New Button to create a new item
    def newItem():
        newBtn = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="New")
        newBtn.click()
        time1()
    newItem()

    # Collapse Fact Box in new item creation frame
    def collapse_fact_box2():
        collapse_img_fct_bx = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox", name="Toggle FactBox")
        collapse_img_fct_bx.click()
        time1()
    collapse_fact_box2()

    # Fill in the Item No
    def ItemNo():
        Fill_itemNo = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="No.", exact=True)
        Fill_itemNo.fill(BC_Item_Code)
        time1()
    ItemNo()

    # Click the Description Column
    def click_description():
        clickD = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Description")
        clickD.click()
        time1()
    click_description()

    # fill in the Descripton
    def ItemDescription():
        fill_itemDesc = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Description")
        fill_itemDesc.fill(Item_Description)
        time1()
    ItemDescription()

    # Click The Show more icon to expand the Item field
    def showmore():
        show_more =  page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Item, Show more")
        show_more.click()
        time1()
    showmore()

    # Enter the UOM
    def BaseUOM():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Base Unit of Measure").click()
        Fill_UOM = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Base Unit of Measure")
        Fill_UOM.fill(UOM)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Base Unit of Measure").press("Enter")
        time1()
    BaseUOM()

    #Enter the Item Category Code
    def Item_Category_Code():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Item Category Code").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Item Category Code").fill(Item_Category)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Item Category Code").press("Enter")
        time1()
    Item_Category_Code()

    # Enter the Common Item No
    def Common_Item_No():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Common Item No.").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Common Item No.").fill(BC_Item_Code)
        time1()
    Common_Item_No()

    
    def fill_in_the_NetGross_Weight():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Inventory, Show more").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Net Weight").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Net Weight").fill(Net_Weight)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Net Weight").press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Gross Weight").fill(Gross_Weight)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Costs & Posting, This group contains one or more mandatory fields that are not filled in.").click()
        time1()
    fill_in_the_NetGross_Weight()


    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Costs & Posting, Show more").click()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Costing Method").select_option("3")
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Gen. Prod. Posting Group").click()

    # Enter the General Posting Group
    def General_Prod_Posting_Group1():
        gpg = page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Gen. Prod. Posting Group").fill(General_Prod_Posting_Group)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Gen. Prod. Posting Group").press("Enter")
    General_Prod_Posting_Group1()

    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for VAT Prod. Posting Group").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Code, sorted in Ascending order V1", exact=True).click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Inventory Posting Group").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Code, sorted in Ascending order 01-FIN").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Prices & Sales").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Prices & Sales, Show more").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Price/Profit Calculation").select_option("1")
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Profit %").click()
    time.sleep(3)
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Profit %").fill("50.00")
    time.sleep(3)

    time1()

    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="More options").click()
    time1()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Related").click()
    time1()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menu", name="Related").get_by_role("menuitem", name="Item").click()
    time1()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Item References").click()

    # Enter the Barcode
    def enter_Barcode():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Reference Type, sorted in Ascending order").select_option("3")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Reference No., sorted in Ascending order", exact=True).click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Reference No., sorted in Ascending order", exact=True).fill(Barcode)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("grid", name="Item Reference Entries").locator("div").filter(has_text="Item Reference EntriesPress Ctrl+Enter to move to the next element after the tab").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Unit of Measure, sorted in Ascending order").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Code, sorted in Ascending order KG").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Back").click()
    time1()
    enter_Barcode()

    #Enter the Height Width and Lenght
    def weight2():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Related").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menu", name="Related").get_by_role("menuitem", name="Item").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Units of Measure").click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Height", exact=True).click()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Height", exact=True).fill(Height)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Height", exact=True).press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Width", exact=True).fill(Width)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Width", exact=True).press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Length", exact=True).fill(Length)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Length", exact=True).press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Cubage", exact=True).press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Weight", exact=True).fill(Net_Weight)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Back").click()
    weight2()

    #Enter the Bin Location
    def binLocation():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Related").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Warehouse").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Bin Contents").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Location Code").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Location Code").fill("1-ASTORE")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Location Code").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Bin Code").fill("ASTORE")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("grid", name="Item Bin Contents").locator("div").filter(has_text="Item Bin ContentsPress Ctrl+Enter to move to the next element after the table.00").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").locator("#checkbox_b34oee").check()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").locator("#checkbox_b34pee").check()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Back").click()
    binLocation()

    #Add the Attributes
    def attributes1():
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Item").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Attributes").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").fill("01-GROUP")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill("FISH")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Enter")
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").fill("02-SUB GROUP")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill("FISH")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").fill("03-SUPPLIER")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill("DEEPCATCH")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").fill("04-BRAND")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill("DEEPCATCH")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Enter")
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("OKCancel").click()
        time.sleep(3)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="OK").click()

    attributes1()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)