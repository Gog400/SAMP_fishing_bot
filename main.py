import cv2
import time
import numpy as np
import datetime
from PIL import ImageGrab

template2 = cv2.imread('screenshots/Red_square_marker.jpg', cv2.IMREAD_COLOR)
# print(template[10][10]) #[row/ordinal/[B, G, R]]
templateColor = template2[10][10]
template = cv2.imread('screenshots/Red_square_marker_2.jpg', cv2.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]

def process_img(original_img):

    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    ## Нахождение предмета
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.7)
    # loc_n = list(zip(*loc[::-1]))
    #
    # print(loc_n, '\n')
    # f = 0
    # for pt in loc_n:
    #     cv2.rectangle(original_img, pt, (pt[0] + w+10, pt[1] + h+10), (204, 40, 142), 1)
    #     print(f, ': ', original_img[loc_n[f][1], loc_n[f][0]])
    #     f+=1

    for pt in zip(*loc[::-1]):
        x = int(pt[0]+w/2)
        y = int(pt[1]+h/2)
        print(original_img[y][x])
        cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)

    # try:
    #     # print(original_img[loc_n[2][1], loc_n[2][0]][2])
    #     # if original_img[loc_n[0][1], loc_n[0][0]][2] == templateColor[2]:
    #     #     print("YEP COCK")
    #     #     loc_n_s.append(loc_n[0])
    #     # for pt in loc_n_s:
    #         # print(original_img[pt[1], pt[0]][2])
    #
    #
    #     x = int(loc_n[0][1]+w/2)
    #     y = int(loc_n[0][0]+h/2)
    #     # cv2.putText(original_img,'X: %d | Y: %d' % (x, y) , (x+w+5, y+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (58, 222, 130), 2)
    #     cv2.rectangle(original_img, loc_n[0], (loc_n_s[0] + w+10, loc_n_s[1] + h+10), (204, 40, 142), 1)
    #     # cv2.rectangle(original_img, (x-1, y-1), (x+1, y+1), (255, 230, 255), 2) #(255, 0, 100)
    #
    # except:
    #     pass


    # for multiple templating
    # for pt in zip(*loc[::-1]):
    #     x = int(pt[0]+w/2)
    #     y = int(pt[1]+h/2)
    #     print(original_img[y][x])
    #     cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)

# for i in list(range(3))[::-1]:
#     print(i+1)
#     time.sleep(1)

last_time = time.time()
while True:

    screen = np.array(ImageGrab.grab(bbox=(960, 0, 1920, 1080))) # Right half of monitor
    # screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080))) # Full monitor


    process_img(screen)

    # print('FPS: {}'.format(1 / (time.time()-last_time) ))
    cv2.putText(screen, 'FPS: {}'.format(int(1 / (time.time()-last_time))), (0, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    last_time = time.time()

    cv2.imshow('Original screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    # cv2.imshow('template', template)
    # cv2.imshow('Proccdaseed screen', screen2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
