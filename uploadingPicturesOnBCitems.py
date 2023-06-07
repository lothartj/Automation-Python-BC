from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pyperclip
import os
from win10toast import ToastNotifier

def time5():
    time.sleep(5)



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/SignIn?ReturnUrl=%2FDT_BC21_RET_UP%2F%3Fcompany%3DSeapride%2520(Pvt)%2520Ltd%26dc%3D0")
    page.get_by_label("User name:").click()
    page.get_by_label("User name:").fill("Lothart")
    page.get_by_label("User name:").press("Tab")
    page.get_by_label("Password:").fill("Deepcatch@2023")
    page.get_by_label("Password:").press("Enter")
    page.goto("https://bc.deepcatchgroup.com/DT_BC21_RET_UP/?company=Seapride%20(Pvt)%20Ltd&dc=0&signInRedirected=1")
    time5()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Items, View or edit detailed information for the products that you trade in. The item card can be of type Inventory or Service to specify if the item is a physical unit or a labor time unit. Here you also define if items in inventory or on incoming orders are automatically reserved for outbound documents and whether order tracking links are created between demand and supply to reflect planning actions.").click()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="No., sorted in Ascending order ALSUG02547").click()
    time5()
    # page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemcheckbox", name="Toggle FactBox").click()
    time5()

    for i in range(50):
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Description").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Description").press("Control+a")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox", name="Description").press("Control+c")
        description1 = pyperclip.paste()
        description2 = pyperclip.paste().replace(" ", "_")

        from pygoogle_image import image as pi
        Description = (description1)
        pi.download(Description, limit=10 )
        time.sleep(15)

        # Remove Background
        from rembg import remove
        from PIL import Image

        input_path = fr'C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images\\{description2}\\{description1}_7.jpeg'
        output_path = fr'C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images\\{description2}\\{description1}_11.jpeg'

        # Open input image
        input_image = Image.open(input_path)

        # Apply background removal
        output_image = remove(input_image)

        # Convert image to RGB mode
        output_image = output_image.convert("RGB")

        # Save output image
        output_image.save(output_path)

        
        #-----------------------


        # Resize image
        from PIL import Image

        image_path = fr'C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images\\{description2}\\{description1}_11.jpeg'
        desired_size = (771, 771)

        # Open image
        im = Image.open(image_path)

        # Create a new blank image with the desired size and white background
        new_image = Image.new('RGB', desired_size, (255, 255, 255))

        # Calculate the position to paste the original image to center it
        paste_position = ((desired_size[0] - im.width) // 2, (desired_size[1] - im.height) // 2)

        # Paste the original image onto the new image
        new_image.paste(im, paste_position)

        # Save the new image
        output_path = fr'C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images\\{description2}\\{description1}_12.jpeg'
        new_image.save(output_path)

        #---------------------
        
        time.sleep(5)

        #---------------------
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Picture").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Import").click()
        time5()

        # file_path = os.path.abspath(f"C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images\\{description2}\\{description1}_4.png")
        

        base_path = "C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\\Desktop\\playwright\\images"


        # Check if PNG file exists
        png_path = os.path.abspath(os.path.join(base_path, description2, f"{description1}_12.png"))
        if os.path.isfile(png_path):
            file_path = png_path
        else:
            # If PNG file doesn't exist, use JPEG file
            jpeg_path = os.path.abspath(os.path.join(base_path, description2, f"{description1}_12.jpeg"))
            if os.path.isfile(jpeg_path):
                file_path = jpeg_path
            else:
                print("No PNG or JPEG file found.")
                

# Use the file_path in your code for further processing

        


        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("textbox").set_input_files(file_path)
        time.sleep(5)
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Go to the next document of the same type.").click()
        time.sleep(10)
        #----------------------
        if os.path.isfile(png_path,jpeg_path):
            os.remove(png_path,jpeg_path)
            toaster = ToastNotifier()
            toaster.show_toast("File Deleted", "Existing file deleted.", duration=5)
        


with sync_playwright() as playwright:
    run(playwright)