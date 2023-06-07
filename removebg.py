from rembg import remove
from PIL import Image
input_path = r'C:\\Users\\lothart.IMPERIAL\\OneDrive - DP World\Desktop\\playwright\\images\\SUGARBIRD_XO_14year_Brandy\\SUGARBIRD XO 14year Brandy_10.jpeg'

output_path = 'output.png'
# Open input image
input_image = Image.open(input_path)
# Apply background removal
output_image = remove(input_image)
# Save output image
output_image.save(output_path)
