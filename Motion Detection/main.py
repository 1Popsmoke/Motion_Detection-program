import cv2
cap = cv2.VideoCapture(0)
bg_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = bg_sub.apply(frame)
    cv2.imshow('original', frame)
    cv2.imshow('foreground', fgmask)

    K = cv2.waitKey(1) & 0xff
    if K ==27:
        break

cap.release() 
cv2.destroyAllWindows()   