import os, argparse
from os.path import join

parser = argparse.ArgumentParser(description="A simple tool to work with the image parser and provide useful information form the chat.txt file.")
parser.add_argument("directory", type=str, help="Path to exported chat folder")
parser.add_argument("start_date", type=int, help="Starting Date in format YYYYMMDD")
parser.add_argument("end_date", type=int, help="Ending Date in format YYYYMMDD")
args = parser.parse_args()

work_directory = args.directory
image_directory = join(work_directory, 'Images')
start_date = str(args.start_date)
end_date = str(args.end_date)

imageDir_set = ()
image_names = []
final_image_list = []

if os.path.isfile(join(work_directory, 'chat.txt')) == False:
    print("Changing Chat File Name...\n")
    item_list = os.listdir(work_directory)
    for item in item_list:
        if item[0:18] == "WhatsApp Chat with":
            os.rename(join(work_directory, item), join(work_directory, 'chat.txt'))
        else:
            continue

if os.path.isfile(join(work_directory, 'chat_temp.txt')) == False:
    print("Making chat_temp.txt...\n")
    with open(join(work_directory, 'chat.txt'), 'r+', encoding='utf-8') as chat:
        chat_temp = open(join(work_directory, 'chat_temp.txt'), 'w', encoding='utf-8')
        for line in chat:
            if 'IMG-' in line or 'Advance' in line:
                chat_temp.write(line)
        
        chat_temp.close()
    chat.close()

with open(join(work_directory, 'chat_temp.txt'), 'r+', encoding='utf-8') as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        if "advance" in line.lower():
            image_names.append(lines[index - 1])
file.close()

# print(image_names)
for image in image_names:
    # print(image, image[-36:-28], image[-36:-28] >= start_date, image[-36:-28] <= end_date)
    if image[-36:-28] >= start_date and image[-36:-28] <= end_date:
        final_image_list.append(image[-40:-17])
print(final_image_list)

imageDir_set = set(os.listdir(image_directory))
imageDir_set.remove("Removed_images")

for image in imageDir_set:
    if image not in final_image_list:
        os.rename(join(image_directory, image), join(image_directory, 'Removed_images', image))
    else:
        print(image)