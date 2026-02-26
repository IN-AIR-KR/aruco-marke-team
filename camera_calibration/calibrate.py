import cv2
import numpy as np
import glob

# 설정: 체커보드 내부 교차점 개수 (가로, 세로)
CHECKERBOARD = (5, 8)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 29, 0.001)

objpoints = []
imgpoints = []

# 3D 실제 세계 좌표 준비
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# 저장된 이미지 목록 가져오기
images = glob.glob('images/*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 체커보드 코너 찾기
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objpoints.append(objp)
        # 코너 정밀화
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # 찾은 코너 그리기 (확인용)
        cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
        cv2.imshow('Checking Corners', img)
        cv2.imwrite(f'output/{fname.split("/")[-1]}', img)
        cv2.waitKey(100)

cv2.destroyAllWindows()

# 캘리브레이션 수행
if len(objpoints) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    print("\n=== Calibration Result ===")
    print(f"Reprojection Error: {ret}")
    print("\nCamera Matrix (mtx):")
    print(mtx)
    print("\nDistortion Coefficients (dist):")
    print(dist)

    # 파일로 저장 (나중에 불러와서 사용)
    np.savez("calibration_result.npz", mtx=mtx, dist=dist)
    print("\n결과가 'calibration_result.npz'로 저장되었습니다.")
else:
    print("인식된 이미지가 없습니다.")
