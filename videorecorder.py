import cv2
import numpy as np
import pyautogui


# Pillow is required

# import os, sys, subprocess
#
# def open_file(filename):
#     if sys.platform == "win32":
#         os.startfile(filename)
#     else:
#         opener = "open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, filename])

SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 12.0
out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))

record_seconds = 150

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot()
    # img = pyautogui.screenshot(region=(0, 0, 300, 400))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    # cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
out.release()
