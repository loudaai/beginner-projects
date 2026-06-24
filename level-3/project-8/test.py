import cv2

cap = cv2.VideoCapture(0)

print(cap.isOpened())

while True:
    ret, frame = cap.read()

    print(ret)

    if ret:
        cv2.imshow("Test", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
