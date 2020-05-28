import cv2
import time
import numpy as np
import datetime
from PIL import ImageGrab

template = cv2.imread('screenshots/Red_square_marker.jpg', cv2.IMREAD_COLOR)
w, h = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY).shape[::-1]
templateColor = [0, 0, 170]

def templating(original_img):
    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(grey_img, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.7)
    loc_n = list(zip(*loc[::-1]))
    print(loc_n)
    for pt in loc_n:
        # print(original_img[loc_n[0][1], loc_n[0][0]])
        print(original_img[pt[1], pt[0]])
        if original_img[pt[1], pt[0]][2] == templateColor[2]:

            # if original_img[loc_n[0][1], loc_n[0][0]][2] == templateColor[2]:
            #     print("YEP COCK")
            cv2.rectangle(original_img, (pt[1], pt[0]), (pt[1] + w, pt[0] + h), (204, 40, 142), 2)


last_time = time.time()
while True:

    screen = np.array(ImageGrab.grab(bbox=(960, 0, 1920, 1080))) # Right half of monitor


    cv2.putText(screen, 'FPS: {}'.format(int(1 / (time.time()-last_time))), (0, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    last_time = time.time()

    templating(screen)

    # cv2.imshow('Original screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imshow('template', template)
    cv2.imshow('output', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
