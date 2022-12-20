v1.1.1
# Chia NFT Assembler for MintGarden Studio Bulk Minting 
This script can be used to assemble simple layered .png images using weighted components,
and create the metadata in the format required by [MintGarden.io](mintgarden.io)'s
MintGarden Studio bulk minter.

I've tried to make this as beginner friendly as possible.

#### Disclaimer:
* I am not affiliated with MintGarden.io
* This software is provided as is, i take no liability for any aspect of your project.


## Dependancies
- [Python 3](https://www.python.org/downloads/)
- [Pillow 9.x](https://pillow.readthedocs.io/en/stable/) `pip install Pillow`

## Running the Example
1. Clone the repository to your device, or [download the folder](https://github.com/andrewhstovell/Chia-NFT-Assembler-for-MintGarden-Bulk/archive/refs/heads/main.zip) and extract the contents.
2. Navigate to the directory in your CLI (or `right-click + open terminal here` in the folder on Windows)
3. Type/paste `python generator.py` and hit enter to run.
4. Should say "Successfully Completed" when done

![screenshot of steps 3 and 4](https://bafkreicxbxowibvripbzzfu5egp27kyfc2krscsynrbapowgcanec3hb5i.ipfs.nftstorage.link/)

5. Check the newly created ***./Super Duper Example Collection/*** folder and contents that have been created. Remember to look at the metadata file.

> ***In the name of all that is good, please don't try to turn these example images into NFT's.***

![Output of the Example Collection](https://bafybeibdujcp44qpw4s7shz66ekybpuqpjwi72bijpm2zzqvmjhwapoj2u.ipfs.nftstorage.link/)

## Usage
1. Create your own component PNG files and place them in the ***./components*** directory (delete the example files)

    *Your components can use any dimensions, as long as they are all the same.*

2. Edit the `generator.py` file, set your collection's name, description and the amount of images to generate
```
# Change these
COLLECTION_NAME = "Super Duper Example Collection"
COLLECTION_DESCRIPTION = "Super Duper Example NFT's"
TOTAL_IMAGES = 100 # Number of random unique images you want to generate
```
3. Replace the component names with the names of your component files. (minus the .png extension)
4. Adjust corresponding weights accordingly (lower = rarer)
```
# The weightings for each trait drive the rarity and add up to 100%
# Note traits in this list must be in order of Layer. 
# I.e., Background first, Foreground last.
traits = [
    Trait(
        "Background", 
        ["Pink", "Teal", "Lime", "Cream"], 
        [30, 20, 10, 40]), # 30% + 20% + 10% + 40% = 100%
    Trait(
        "Feature", 
        ["House", "Tree", "Sun", "Moon"], 
        [15, 35, 35, 15]),
    Trait(
        "Face", 
        ["Round", "Square", "Triangle"], 
        [30, 50, 20]),
    Trait(
        "Eyes", 
        ["Blue", "Red", "Brown"], 
        [30, 10, 60]),
    Trait(
        "Nose", 
        ["Pointy", "Rounded", "Dots"], 
        [30 , 30 , 40]),
    Trait(
        "Mouth", 
        ["Smile", "Grumpy", "Neutral", "Cute"], 
        [30, 30, 20, 20]),
]
```
* Run the program, and generate your Images and Metadata
* Run the program again until your batch of NFT's is just right!

## Testing
This is especially important if you have edited the code beyond what is presented in these instructions. 

To double-check that every NFT has unique trait assignments in the metadata, 
run `python duplicate_identifier.py`

You should get 0 duplicates identified.

### Problems or need help?
Feel free to create an issue ticket, i will try to address as soon as possible

----
> *Want to toss some Mojo's or an NFT at the Andy?* <br/>
`xch1pelfpwqtnn0waj6vkrvdn7v8cx7h93gjmknakhq58hhrnlhqmk9s8xv64r`