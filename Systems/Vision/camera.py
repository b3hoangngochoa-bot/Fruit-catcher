import cv2


class Camera:
    """
    Chịu trách nhiệm mở webcam và cung cấp từng frame ảnh.
    """

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.cap = None

    def start(self):
        """Mở kết nối tới webcam."""
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError(f"Không thể mở camera với index {self.camera_index}")

    def get_frame(self):
        """
        Đọc một frame từ webcam.
        Trả về frame (numpy array BGR) hoặc None nếu thất bại.
        """
        if self.cap is None or not self.cap.isOpened():
            return None

        success, frame = self.cap.read()
        if not success:
            return None

        return frame

    def release(self):
        """Đóng kết nối webcam."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None