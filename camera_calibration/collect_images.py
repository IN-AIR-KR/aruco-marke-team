import cv2
import os

os.makedirs("images", exist_ok=True)

# GStreamer 파이프라인 설정
# Jetson에서 IMX219 카메라 모듈을 사용할 때 필요한 설정
gst = (
    "nvarguscamerasrc sensor-id=0 ! "
    "video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1 ! "
    "nvvidconv ! video/x-raw, format=BGRx ! "
    "videoconvert ! video/x-raw, format=BGR ! appsink"
)
cap = cv2.VideoCapture(gst, cv2.CAP_GSTREAMER)


# s: 저장, q: 종료
idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("capture", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(f"images/img_{idx:02d}.jpg", frame)
        print(f"Saved img_{idx:02d}.jpg")
        idx += 1

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
