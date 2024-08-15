import pyautogui as pag
import time
import requests
import os
from telegraph import Telegraph

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
telegraph_access_token = '735ad2af4aa8c6f52c6932404f2c6471122c1ef153d9577bd01cf7f3bf40'
title = 'Iperius Remote ID | The Disala'
img_filename = 'IperiusRemoteID.png'

# Initialize Telegraph
telegraph = Telegraph(access_token=telegraph_access_token)

# Upload to Telegraph
def upload_image_to_telegraph(img_filename, title):
    # Upload the image to Telegraph
    with open(img_filename, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post('https://telegra.ph/upload', files=files)
    
    if response.status_code == 200:
        image_url = response.json()[0]['src']
        # Create a new Telegraph page with the image
        response = telegraph.create_page(
            title=title,
            author_name='The_Disala',
            content=[
                {
                    'tag': 'img',
                    'attrs': {'src': image_url}
                }
            ]
        )
        telegraph_link = 'https://telegra.ph/' + response['path']
        # Open the show.bat file in append mode and write the image information
        with open('show.bat', 'a') as bat_file:
            bat_file.write(f'\necho {title} : {telegraph_link}')
        return telegraph_link
    else:
        print("Image upload to Telegraph failed.")
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
        telegraph_link = upload_image_to_telegraph(img_filename, title)
        if telegraph_link:
            print("Image uploaded successfully to Telegraph.")
    else:
        pag.click(x, y, duration=duration)

print('Done !')
