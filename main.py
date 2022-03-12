import cv2

# region Read image from default webcam using OpenCV convert to grayscale and then apply a colormap before displaying.
video_capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
Equalize = False
while True:
    return_code, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    rows = gray.shape[0]
    if Equalize:
        gray = cv2.equalizeHist(gray)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,param1=100, param2=50,minRadius=5, maxRadius=30)
    if circles is not None:
        for c in circles[0, :]:
            center = (int(c[0]), int(c[1]))
            cv2.circle(frame, center, 1, (0, 255, 0), 3)
            radius = int(c[2])
            cv2.circle(frame, center, radius, (255, 0, 255), 3)
            n_circles = circles.shape[1]
        if n_circles==2:
            PCB_Center = (circles[0, 0] + circles [0, 1])/2
            PCB_Center = tuple(map(int, PCB_Center[:-1]))
            cv2.circle(frame, PCB_Center, 5, (0, 255, 0), 10)
            cv2.imshow(‘Circles’, frame)
        if cv2.waitKey(1) & 0xFF == ord(‘q’):
            break
# endregion

# region Release the camera resources.
video_capture.release()
cv2.destroyAllWindows()
# endregion
