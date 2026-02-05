import cv2
import os

# 저장 폴더 생성
save_path = 'calib_images'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# CSI 카메라 사용 시 아래 GStreamer 파이프라인 활성화
# def gstreamer_pipeline():
#     return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGR ! appsink"
# cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

cap = cv2.VideoCapture(0)  # USB 카메라는 0번
count = 0

print("명령어: 'S' - 이미지 저장, 'Q' - 종료")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Mode", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        img_name = os.path.join(save_path, f"img_{count:02d}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"저장 완료: {img_name}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
