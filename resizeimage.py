from PIL import Image

image_path = r'C:\Users\lothart.IMPERIAL\OneDrive - DP World\Desktop\playwright\images\SUGARBIRD_XO_14year_Brandy\SUGARBIRD XO 14year Brandy_8.jpeg'
desired_size = (771, 771)

# Open image
im = Image.open(image_path)

# Create a new blank image with the desired size and white background
new_image = Image.new('RGB', desired_size, (255, 255, 255))

# Calculate the position to paste the original image to center it
paste_position = ((desired_size[0] - im.width) // 2, (desired_size[1] - im.height) // 2)

# Paste the original image onto the new image
new_image.paste(im, paste_position)

# Display the new image
new_image.show()
