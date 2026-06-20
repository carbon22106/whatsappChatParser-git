import os, argparse
from os.path import join

parser = argparse.ArgumentParser(description="A simple tool to extract all images from a whatsapp chat export and rename it to numbers in order to make processing the images through another tool easier.")
parser.add_argument("directory", type=str, help="Path to the exported chat folder. ONLY enter the root of the extracted directory DO NOT go any deeper or the code wont work.")
parser.add_argument("keyword", type=str, default='', help="The word you put after every of the image you want. eg - advance, gas, food etc.")
parser.add_argument("-s", "--start", type=int, default=0, help="Starting Date in format YYYYMMDD")
parser.add_argument("-e", "--end", type=int, default=20500000, help="Ending Date in format YYYYMMDD")
parser.add_argument("-f", "--full-parse", action='store_true', help="A flag to tell the script to run a full parse - from moving the images to only leaving the image you want.")
args = parser.parse_args()

main_directory = args.directory
image_directory = join(args.directory, 'Images')
keyword_directory = join(args.directory, 'Images', args.keyword)
removed_image_directory = join(args.directory, 'Images', 'Removed_images')
keyword = args.keyword.lower()
start_date = str(args.start)
end_date = str(args.end)
full_parse = args.full_parse

date = []
imageDir_set = ()
image_names = []
final_image_list = []

def move_images():
    if not os.path.isdir(image_directory) and main_directory[-6:] != 'Images':
        os.mkdir(image_directory)
    item_list = os.listdir(main_directory)
    for item in item_list:
        if item[0:4] == "IMG-":
            os.rename(join(main_directory, item), join(image_directory, item))

def parse_chat():
    if os.path.isfile(join(main_directory, 'chat.txt')) == False:
        #print("Changing Chat File Name...\n")
        item_list = os.listdir(main_directory)
        for item in item_list:
            if item[0:18] == "WhatsApp Chat with":
                os.rename(join(main_directory, item), join(main_directory, 'chat.txt'))
                # print("Changing ", join(main_directory, item), " to ", join(main_directory, 'chat.txt'))
            else:
                # print("Warning : No Chat Text File Found.")
                continue
            
    # if os.path.isfile(join(main_directory, 'chat.temp')) == False:
    print("Making chat.temp...\n")
    with open(join(main_directory, 'chat.txt'), 'r+', encoding='utf-8') as chat:
        chat_temp = open(join(main_directory, 'chat.temp'), 'w', encoding='utf-8')
        for line in chat:
            if 'IMG-' in line or keyword in line.lower():
                chat_temp.write(line)

        chat_temp.close()
    chat.close()
    
    with open(join(main_directory, 'chat.temp'), 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if keyword in line.lower():
                image_names.append(lines[index - 1])
    file.close()
    # print(image_names)
    
    for image in image_names:
        # print(image, image[-36:-28], image[-36:-28] >= start_date, image[-36:-28] <= end_date)
        if image[-36:-28] >= start_date and image[-36:-28] <= end_date:
            final_image_list.append(image[-40:-17]) # for final image list we are checking the date range. We only put the 'in range' images in the final_image_list.
    # print(image_names)
    # print(final_image_list)

def remove_out_of_range():
    imageDir_set = set(os.listdir(image_directory))
    if os.path.isdir(removed_image_directory):
        imageDir_set.remove("Removed_images")
    if os.path.isdir(removed_image_directory) == False:
        os.makedirs(removed_image_directory)
        
    for image in imageDir_set:
        if image in final_image_list:
            # print("KEEP : ", image, final_image_list)
            continue
        else:
            # print("MOVE : ", image, final_image_list)
            os.rename(join(image_directory, image), join(removed_image_directory, image))

if full_parse:
    move_images()
    parse_chat()
    remove_out_of_range()