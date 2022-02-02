import rotatescreen 
import time
import keyboard
screen = rotatescreen.get_primary_display()
# for i in range(23):
#     time.sleep(1)
#     screen.rotate_to(0)
keyboard.add_hotkey('ctrl+alt+up', screen.set_landscape, suppress=True)
keyboard.add_hotkey('ctrl+alt+right', screen.set_portrait_flipped, suppress=True)
keyboard.add_hotkey('ctrl+alt+down', screen.set_landscape_flipped, suppress=True)
keyboard.add_hotkey('ctrl+alt+left', screen.set_portrait, suppress=True)

keyboard.wait()