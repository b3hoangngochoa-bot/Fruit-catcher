import cv2
import mediapipe as mp


class HandDetector:
    """
    Task 3 + 4 + 5 của Vision System:
      - Task 3: Detect bàn tay bằng MediaPipe (tối đa 2 tay)
      - Task 4: Lấy vị trí ngón trỏ (INDEX_FINGER_TIP, landmark index = 8)
      - Task 5: Đóng gói output thành hand_data chuẩn

    Output (hand_data):
        {
            "detected": bool,
            "fingertip": {
                "x": float,  # normalized [0.0, 1.0] — ngón trỏ tay đầu tiên
                "y": float,  # normalized [0.0, 1.0]
            },
            "hands": [                        # list landmarks của mỗi bàn tay
                [ {"x": float, "y": float, "z": float}, ... ],  # 21 landmarks/tay
            ],
            "frame": np.ndarray  # frame BGR gốc (để debug/render)
        }
    """

    # Landmark index của ngón trỏ (INDEX_FINGER_TIP = 8)
    FINGERTIP_INDEX = mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP

    def __init__(
        self,
        model_complexity: int = 0,
        min_detection_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
    ):
        self._mp_hands = mp.solutions.hands
        self._mp_drawing = mp.solutions.drawing_utils
        self._mp_drawing_styles = mp.solutions.drawing_styles

        self._hands = self._mp_hands.Hands(
            model_complexity=model_complexity,
            max_num_hands=2,  # Detect tối đa 2 tay để nhận diện gesture
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def detect(self, frame_bgr) -> dict:
        """
        Task 2 → 3 → 4 → 5:
        Nhận frame BGR từ Camera, xử lý và trả về hand_data chuẩn.

        Args:
            frame_bgr: numpy array BGR từ Camera.get_frame()

        Returns:
            hand_data dict:
            {
                "detected": True/False,
                "fingertip": { "x": float, "y": float },  # None nếu không detect
                "frame": frame_bgr
            }
        """
        # --- Task 2: Frame Preprocessing ---
        # Tắt writeable để tối ưu hiệu suất (pass by reference)
        frame_bgr.flags.writeable = False
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

        # --- Task 3: Hand Detection ---
        results = self._hands.process(frame_rgb)

        # Bật lại writeable sau khi xử lý
        frame_bgr.flags.writeable = True

        # Không phát hiện được bàn tay
        if not results.multi_hand_landmarks:
            return {
                "detected": False,
                "fingertip": None,
                "hands": [],
                "frame": frame_bgr,
            }

        # --- Task 4: Fingertip Extraction (tay đầu tiên, landmark index = 8) ---
        first_hand = results.multi_hand_landmarks[0]
        tip = first_hand.landmark[self.FINGERTIP_INDEX]

        # Đóng gói landmarks thô của tất cả bàn tay (cho GestureDetector)
        hands_landmarks = [
            [
                {"x": lm.x, "y": lm.y, "z": lm.z}
                for lm in hand.landmark
            ]
            for hand in results.multi_hand_landmarks
        ]

        # --- Task 5: Output Packaging ---
        return {
            "detected": True,
            "fingertip": {
                "x": tip.x,  # normalized [0.0, 1.0]
                "y": tip.y,  # normalized [0.0, 1.0]
            },
            "hands": hands_landmarks,  # list landmarks của từng bàn tay
            "frame": frame_bgr,
        }

    def draw_landmarks(self, hand_data: dict):
        """
        Vẽ landmarks lên frame để debug/preview.
        Gọi sau detect(), trả về frame đã được annotate.

        Args:
            hand_data: dict trả về từ detect()

        Returns:
            frame BGR đã vẽ landmarks (hoặc frame gốc nếu không detect)
        """
        frame = hand_data["frame"]
        if not hand_data["detected"]:
            return frame

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self._hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for lm in results.multi_hand_landmarks:
                self._mp_drawing.draw_landmarks(
                    frame,
                    lm,
                    self._mp_hands.HAND_CONNECTIONS,
                    self._mp_drawing_styles.get_default_hand_landmarks_style(),
                    self._mp_drawing_styles.get_default_hand_connections_style(),
                )
        return frame

    def release(self):
        """Giải phóng tài nguyên MediaPipe."""
        self._hands.close()