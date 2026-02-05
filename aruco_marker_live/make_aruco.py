import os
import cv2

# ------------------ configuration (edit these) ------------------
# Predefined dictionary name (e.g. DICT_4X4_50, DICT_5X5_100, DICT_6X6_250)
DICT_NAME = "DICT_4X4_50"

IDS = [0, 1, 2, 3]

# Marker size in pixels (square)
MARKER_SIZE = 400

# Output directory
OUT_DIR = "output/markers"
# ----------------------------------------------------------------


DICT_MAP = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
}


def draw_and_save(dictionary, marker_id: int, size: int, out_dir: str) -> str:
    img = cv2.aruco.generateImageMarker(dictionary, marker_id, size)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"marker_{marker_id}.png")
    cv2.imwrite(out_path, img)
    return out_path


def main():
    dictionary = cv2.aruco.getPredefinedDictionary(DICT_MAP[DICT_NAME])

    for marker_id in IDS:
        try:
            path = draw_and_save(dictionary, int(marker_id), int(MARKER_SIZE), OUT_DIR)
            print(f"Saved marker {marker_id} -> {path}")
        except Exception as e:
            print(f"Failed to create marker {marker_id}: {e}")


if __name__ == "__main__":
    main()
