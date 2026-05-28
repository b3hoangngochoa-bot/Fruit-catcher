class VisionSystem:
    """
    Hệ thống thị giác — điều phối toàn bộ pipeline:

    Task 1: Camera Initialization  →  Camera.start()
    Task 2: Frame Preprocessing    ┐
    Task 3: Hand Detection         ├  HandDetector.detect(frame)
    Task 4: Fingertip Extraction   │
    Task 5: Output Packaging       ┘

    Output mỗi frame (hand_data):
        {
            "detected": bool,
            "fingertip": { "x": float, "y": float } | None,
            "frame": np.ndarray
        }
    """

    def __init__(self, camera, hand_detector):
        self.camera = camera
        self.hand_detector = hand_detector
        self._hand_data = None

    # ------------------------------------------------------------------
    # Task 1: Camera Initialization
    # ------------------------------------------------------------------
    def start(self):
        """Khởi tạo webcam — đảm bảo đọc được frame liên tục."""
        self.camera.start()

    # ------------------------------------------------------------------
    # Task 2 → 5: Chạy mỗi frame trong game loop
    # ------------------------------------------------------------------
    def update(self):
        """
        Chụp frame từ camera, chạy qua HandDetector, lưu hand_data.
        Được gọi mỗi vòng lặp game (trong main loop).
        """
        frame = self.camera.get_frame()

        if frame is None:
            # Camera chưa sẵn sàng hoặc frame lỗi
            self._hand_data = {
                "detected": False,
                "fingertip": None,
                "frame": None,
            }
            return

        # Detect + extract + package (Task 2 → 5)
        self._hand_data = self.hand_detector.detect(frame)

    def get_hand_data(self) -> dict:
        """
        Trả về hand_data từ lần update() gần nhất.

        Returns:
            {
                "detected": bool,
                "fingertip": { "x": float, "y": float } | None,
                "frame": np.ndarray | None
            }
        """
        return self._hand_data

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------
    def release(self):
        """Giải phóng tài nguyên camera và MediaPipe."""
        self.camera.release()
        self.hand_detector.release()