import cv2

def main():
    cam_id = 0
    cap = cv2.VideoCapture(cam_id)

    if not cap.isOpened():
        print(f"카메라({cam_id})를 열 수 없습니다.")
        return

    print("카메라 연결 성공! 'q'를 누르면 종료합니다.")

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        
        if not ret:
            print("프레임을 읽어올 수 없습니다.")
            break

        # 화면에 표시
        cv2.imshow("Jetson Orin Nano - USB Cam", frame)

        # 'q' 키를 누르면 루프 탈출
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()