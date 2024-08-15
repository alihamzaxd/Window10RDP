import pyautogui as pag
import time
import requests
import os

# Define the coordinates and use the `actions` list
actions = [
    (266, 287, 4),  # unattended access
    (266, 287, 1),  # unattended access
    (681, 564, 4),  # next
    (260, 507, 4),  # i accept agreement
    (673, 567, 4),  # next
    (672, 565, 4),  # next
    (675, 566, 4),  # next
    (677, 570, 4),  # install (wait 15sec)
    (261, 306, 4),  # type pass
    (671, 567, 4),  # next (wait 15sec)
    (437, 303, 4),  # tic launch iperius
    (667, 567, 4),  # finish
    (667, 567, 1),  # finish
    (447, 286, 4),  # ss id & upload (launch iperius)
]

# Wait for a few seconds to give time to focus on the target application
time.sleep(10)
password = "TheDisa1a"
access_token = '0205418ed7afc732fb798302849561a71c82b7a4'
title = 'Iperius Remote ID | The Disala'
show = 'Iperius Remote ID'
description = 'Iperius Remote Pass : TheDisa1a'
img_filename = 'IperiusRemoteID.png'


# Upload To IMGUR 
def upload_image_to_imgur(img_filename, access_token, title, description):
    url = 'https://api.imgur.com/3/image'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    with open(img_filename, 'rb') as f:
        files = {'image': f}
        data = {'title': title, 'description': description}
        response = requests.post(url, headers=headers, files=files, data=data)
        
    if response.status_code == 200:
        imgur_link = response.json()['data']['link']
        # Open the show.bat file in append mode and write the image information
        with open('show.bat', 'a') as bat_file:
            bat_file.write(f'\necho {show} : {imgur_link}')
        return imgur_link
    else:
        print("Image upload failed.")
        return None


for x, y, duration in actions:
    if (x, y, duration) == (677, 570, 4):
        pag.click(x, y, duration=duration)
        time.sleep(10)
    elif (x, y, duration) == (261, 306, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (671, 567, 4):
        pag.click(x, y, duration=duration)
        time.sleep(10)
    elif (x, y, duration) == (667, 567, 4):
        pag.click(x, y, duration=duration)
        time.sleep(10)
    elif (x, y, duration) == (447, 286, 4):
        os.system('"C:\\Program Files\\IperiusRemote\\IperiusRemote.exe"')
        time.sleep(5)
        pag.screenshot().save(img_filename)
        imgur_link = upload_image_to_imgur(img_filename, access_token, title, description)
        if imgur_link:
            print("Image uploaded successfully.")
    else:
        pag.click(x, y, duration=duration)

print('Done !')


