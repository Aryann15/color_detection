import cv2 as cv
from PIL import Image

from utils import get_limits

yellow = [0,255,255]
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv= cv.cvtColor(frame , cv.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)


    mask = cv.inRange(hsv,lower_limit,upper_limit )
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    cv.imshow('frame',mask  )

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()