from PIL import Image 
from IPython.display import display 
import random
import os
import glob
import csv

# Change these
COLLECTION_NAME = "Super Duper Example Collection"
COLLECTION_DESCRIPTION = "Super Duper Example NFT's"
TOTAL_IMAGES = 100 # Number of random unique images you want to generate

all_images = [] # This is used to store the images as they are generated

# Each image is made up a series of traits
# Make sure these traits match your component file names
# e.g., 'Pink' for Pink.png
# The weightings for each trait drive the rarity and add up to 100%
background = ["Pink", "Teal", "Lime", "Cream"]
background_weights = [30, 20, 10, 40] 

feature = ["House", "Tree", "Sun", "Moon"]
feature_weights = [15, 35, 35, 15] 

face = ["Round", "Square", "Triangle"]
face_weights = [30, 50, 20]

eyes = ["Blue", "Red", "Brown"]
eyes_weights = [30, 10, 60]

nose = ["Pointy", "Rounded", "Dots"]
nose_weights = [30 , 30 , 40]

mouth = ["Smile", "Grumpy", "Neutral", "Cute"]
mouth_weights = [30, 30, 20, 20]

## For a Simple project you should only need to change values above here

## Generate Traits
# A recursive function to generate unique image combinations
def create_new_image(ID):
    new_image = {}
    
    # For each trait category, select a random trait based on the weightings 
    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Feature"] = random.choices(feature, feature_weights)[0]
    new_image["Face"] = random.choices(face, face_weights)[0]
    new_image["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image["Nose"] = random.choices(nose, nose_weights)[0]
    new_image["Mouth"] = random.choices(mouth, mouth_weights)[0]
    
    if (new_image in all_images):
        return create_new_image(ID)
    else:
        # File metadata to suit MintGarden Bulk Generator
        # Feel free to change the values, do not change the keys.
        file_data = {
            "file": "%s.png" % (str(ID)),                        
            "name": "%s #%s" % (COLLECTION_NAME, str(ID)),         
            "description": "%s/%s %s" % (str(ID), str(TOTAL_IMAGES), COLLECTION_DESCRIPTION)  
        }
        file_data.update(new_image)
        return file_data



## Helper function for generating progress bars    
# Print iterations progress
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#', printEnd = "\r"):
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()



# Generate the unique combinations based on trait weightings
for i in progressBar(range(TOTAL_IMAGES), prefix = 'Combining Images:', suffix = 'Complete', length = 32):
    new_trait_image = create_new_image(i + 1)
    all_images.append(new_trait_image)
    
## Check the stats of the new images
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique? %s" % (all_images_unique(all_images)))

# Get Trait Counts
background_count = {}
for item in background:
    background_count[item] = 0
    
feature_count = {}
for item in feature:
    feature_count[item] = 0

face_count = {}
for item in face:
    face_count[item] = 0
    
eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
nose_count = {}
for item in nose:
    nose_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
    

for image in all_images:
    background_count[image["Background"]] += 1
    feature_count[image["Feature"]] += 1
    face_count[image["Face"]] += 1
    mouth_count[image["Mouth"]] += 1
    eyes_count[image["Eyes"]] += 1
    nose_count[image["Nose"]] += 1

print("\nTrait tally:")
print(background_count)
print(feature_count)
print(face_count)
print(eyes_count)
print(nose_count)
print(mouth_count, '\n')

#### Generate Images and Metadata 
# Note: Will delete existing files in Output Directory
# This is a feature, for quick re-generation
output_dir = f'./{COLLECTION_NAME}'
if (os.path.exists(output_dir)):
    try:
        files = glob.glob(output_dir)
        for f in files:
            if (f != output_dir):
                os.remove(f)
    except Exception as e:
        print("Failed to delete files in output directory. Reason: %s" % (e))
else:
    os.mkdir(output_dir)

# Create the metadata.csv file ready for the MintGarden Bulk minter
metadata_file = open("./%s/metadata.csv" % (COLLECTION_NAME), 'w', newline='')
writer = csv.writer(metadata_file, delimiter =';')

# Write the metadata headers
writer.writerow(all_images[0].keys())

# Create the .png files
for item in progressBar(all_images, prefix = 'Assembling Images & Metadata:', suffix = 'Complete', length = 20):
    im1 = Image.open(f'./components/{item["Background"]}.png').convert('RGBA')
    im2 = Image.open(f'./components/{item["Feature"]}.png').convert('RGBA')
    im3 = Image.open(f'./components/{item["Face"]}.png').convert('RGBA')
    im4 = Image.open(f'./components/{item["Eyes"]}.png').convert('RGBA')
    im5 = Image.open(f'./components/{item["Nose"]}.png').convert('RGBA')
    im6 = Image.open(f'./components/{item["Mouth"]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    rgb_im.save(output_dir + "/" + item["file"])

    # Write the metadata for this item to metadata.csv
    writer.writerow(item.values())

metadata_file.close()

print("Successfully Assembled.\n")