import cv2
import numpy as np


def create_a4_checkerboard():
    # A4 용지 해상도 설정 (300 DPI 기준: 2480 x 3508 픽셀)
    dpi = 300
    width_mm, height_mm = 210, 297
    width_px = int((width_mm / 25.4) * dpi)
    height_px = int((height_mm / 25.4) * dpi)

    # 30mm를 픽셀로 변환
    sq_size_mm = 30
    sq_size_px = int((sq_size_mm / 25.4) * dpi)

    # 흰색 배경 생성
    board = np.ones((height_px, width_px), dtype=np.uint8) * 255

    # 격자 개수 계산 (가로 6칸, 세로 9칸 정도가 여백 있게 들어감)
    rows = 9
    cols = 6

    # 중앙 정렬을 위한 시작 오프셋
    start_x = (width_px - (cols * sq_size_px)) // 2
    start_y = (height_px - (rows * sq_size_px)) // 2

    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:  # 체커 패턴 (0,0이 검은색)
                y = start_y + i * sq_size_px
                x = start_x + j * sq_size_px
                board[y:y + sq_size_px, x:x + sq_size_px] = 0

    return board


# 보드 생성 및 저장
img = create_a4_checkerboard()
cv2.imwrite('checkerboard_A4.png', img)
print("A4 사이즈(300DPI) 체커보드가 'checkerboard_A4.png'로 저장되었습니다.")
# 인쇄할 때 반드시 "실제 크기(Actual size)" 또는 **"배율 100%"**로 설정해야 함
