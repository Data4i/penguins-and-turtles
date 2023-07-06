import json
import shutil
import os

train_image_folder = 'data/train/train'
test_image_folder = 'data/valid/valid'

train_labels_path = 'data/train_annotations'
test_labels_path = 'data/valid_annotations'

def get_labels(path: str):
    with open(path) as img_desc:
        labels = json.load(img_desc)

    label = list()
    for x in labels:
        label.append(x['category_id'])
    return label

train_labels = get_labels(path = train_labels_path)
test_labels = get_labels(path = test_labels_path)

os.makedirs('penguins', exist_ok = True)
os.makedirs('turtles', exist_ok = True)


def check_no(id):
    match len(f'{id}'):
        case 1: return f'00{id}'
        case 2: return f'0{id}'
        case 3: return f'{id}'

def sort_two_folders(
    source_path_folder: str,
    items_labels: list,
    ist_folder_name = 'penguins',
    second_folder_name = 'turtles',

    ):
    for i, picture in enumerate(items_labels):
        image_filename  = f'image_id_{check_no(i)}.jpg'
        destination_folder = ist_folder_name if picture == 1 else second_folder_name
        source_path = os.path.join(source_path_folder, image_filename)
        destination_path = os.path.join(destination_folder, image_filename)

        shutil.move(source_path, destination_path)
    
    print('Items Moved')

sort_two_folders(source_path_folder = train_image_folder, items_labels=train_labels)
sort_two_folders(source_path_folder = test_image_folder, items_labels = test_labels)