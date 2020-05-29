import cv2
import time
import numpy as np
import datetime
from PIL import ImageGrab

template = cv2.imread('screenshots/Red_square_marker.jpg', cv2.IMREAD_COLOR)
w, h = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY).shape[::-1]
templateColor = template[int(w/2), int(h/2)] #picking central pixel color from template

def templating(original_img):
    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(grey_img, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.75)
    loc_n = list(zip(*loc[::-1]))

    for pt in loc_n:
        # cv2.rectangle(original_img, (pt[0]+int(w/2), pt[1]+int(h/2)), (pt[0]+int(w/2) + 1, pt[1]+int(h/2) + 1), (204, 40, 142), 2) #centre of the template
        if set(original_img[pt[1]+int(w/2), pt[0]+int(h/2)]) == set(templateColor):
            cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)
            cv2.putText(original_img,'X: %d | Y: %d' % (pt[0], pt[1]) , (pt[0]+w+5, pt[1]+int(h/2)+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (58, 222, 130), 1)
            #                                                                                   ^^^ centralising the text by Y


last_time = time.time()
while True:

    screen = np.array(ImageGrab.grab(bbox=(960, 0, 1920, 1080))) # Right half of monitor


    cv2.putText(screen, 'FPS: {}'.format(int(1 / (time.time()-last_time))), (0, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    last_time = time.time()

    templating(screen)

    cv2.imshow('template', template)
    cv2.imshow('output', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
