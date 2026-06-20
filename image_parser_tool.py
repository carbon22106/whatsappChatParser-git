import os, argparse
from os.path import join

parser = argparse.ArgumentParser(description="A simple tool to extract all images from a whatsapp chat export and rename it to numbers in order to make processing the images through another tool easier.")
parser.add_argument("directory", type=str, help="Path to exported chat folder")
parser.add_argument("start_date", type=int, help="Starting Date in format YYYYMMDD")
parser.add_argument("end_date", type=int, help="Ending Date in format YYYYMMDD")
args = parser.parse_args()
main_directory = args.directory
start_date = str(args.start_date)
end_date = str(args.end_date)

file = open(join(args.directory, 'renames_map.txt'), 'w')
image_list = 0
date = []

def move_images(work_directory):
    global main_directory
    if not os.path.isdir(join(work_directory, 'Images')) and work_directory[-6:] != 'Images':
        os.mkdir(join(work_directory, 'Images'))
    item_list = os.listdir(work_directory)
    for item in item_list:
        if item[-4:] == '.jpg' or item[-4:] == '.png':
            os.rename(join(work_directory, item), join(work_directory, 'Images', item))
            
    main_directory = join(args.directory, 'Images')

def remove_out_of_range(work_directory):
    global image_list
    image_list = os.listdir(work_directory)
    if os.path.isdir(join(work_directory, 'Removed_images')) == False:
        os.mkdir(join(work_directory, 'Removed_images'))
    # print(image_list)
    for image in image_list:
        if image[0:4] == 'IMG-':
            if image[-4:] == '.jpg' or image[-4:] == '.png':
                current_img = image
                date.append(current_img[4:-11])
                if current_img[4:-11] >= start_date and current_img[4:-11] <= end_date:
                    #print("KEEP : ", image)
                    continue
                else:
                    #print("MOVE : ", image)
                    os.rename(join(work_directory, image), join(work_directory, 'Removed_images', image))
            else:
                continue
        else:
            continue
        
    image_list = os.listdir(main_directory)
    return date

def rename_images(work_directory):
    index = 0
    
    for image in image_list:
        if image != 'Removed_images' and join(work_directory, image) != join(work_directory, str(index)+".jpg"):
            os.rename(join(work_directory, image), join(work_directory, str(index)+".jpg"))
            renames = (image + "|" + str(index)+".jpg\n")
            file.write(renames)
            index += 1
        else:
            continue
    file.close()

move_images(main_directory)
remove_out_of_range(main_directory)
# rename_images(main_directory)