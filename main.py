from tasks import plant_seed, remove_weed, harvest_crop
from servo_control import ServoController

controller = ServoController()

print("Choose mode: (1) Manual Test, (2) Task Mode")
mode = input()

if mode == '1':
    print("Run manual_test.py separately for manual testing")
elif mode == '2':
    print("Select task: (1) Plant Seed, (2) Remove Weed, (3) Harvest Crop")
    task = input()
    if task == '1':
        plant_seed()
    elif task == '2':
        remove_weed()
    elif task == '3':
        harvest_crop()
    else:
        print("Invalid task!")
else:
    print("Invalid mode!")
