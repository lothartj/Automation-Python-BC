from pygoogle_image import image as pi
Description = input('Image Description ')
pi.download(Description, limit=10 )

from pygoogle_image import image as pi

Description = input('Image Description ')
pi.download(Description, limit=10)

# Get file path of 5th downloaded image
if len(pi.image_paths) >= 5:
    fifth_image_path = pi.image_paths[4]
    print(fifth_image_path)
else:
    print("There are less than 5 images downloaded.")