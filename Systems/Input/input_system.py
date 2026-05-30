import Utils.constants as constants
from Core.event_type import EventType
from Systems.Input.gesture_detector import GestureDetector


class InputSystem:
    """
    Chuyển đổi dữ liệu tay (hand_data) thành điều khiển trong game.

    Pipeline:
        Task 1: Coordinate Mapping   →  norm → pixel
        Task 2: Smoothing Filter     →  làm mượt jitter
        Task 3: Cursor Generation    →  tạo dữ liệu cursor UI
        Task 4: Basket Generation    →  tạo dữ liệu basket (vùng bắt trái)
        Task 5: Gesture Detection    →  nhận diện cử chỉ 2 tay + emit event trực tiếp
        Task 6: Output Packaging     →  đóng gói input_data chuẩn

    Output (input_data):
        {
            "cursor": { "x": int, "y": int, "click": bool },
            "basket": { "x": int, "y": int, "radius": int }
        }
    """

    # Bán kính mặc định của vùng basket bắt trái cây
    BASKET_RADIUS = 50

    def __init__(self, mapper, smoother, event_bus, gesture_detector=None):
        self.mapper = mapper
        self.smoother = smoother
        self.event_bus = event_bus
        # GestureDetector: inject từ ngoài, hoặc tạo mặc định
        self.gesture_detector = gesture_detector or GestureDetector()

    def update(self, hand_data: dict | None, delta_time: float = 0.0) -> dict:
        """
        Xử lý hand_data và trả về input_data chuẩn.

        Args:
            hand_data: dict từ VisionSystem.get_hand_data()
                {
                    "detected": bool,
                    "fingertip": { "x": float, "y": float } | None,
                    "hands": [ [{x,y,z}, ...], ... ],
                    "frame": np.ndarray | None
                }
            delta_time: thời gian (giây) từ frame trước (dùng cho gesture debounce)

        Returns:
            input_data dict:
            {
                "cursor":  { "x": int, "y": int, "click": bool },
                "basket":  { "x": int, "y": int, "radius": int },
                "gesture": str | None
            }
            Khi không phát hiện tay: x/y là None.
        """
        # Không có dữ liệu hoặc không detect được tay
        if hand_data is None or not hand_data.get("detected", False):
            self.smoother.reset()
            # Vẫn chạy gesture detector để debounce tiếp tục đếm
            self.gesture_detector.update(hand_data, delta_time)
            return self._package(x=None, y=None, click=False)

        fingertip = hand_data["fingertip"]

        # --- Task 1: Coordinate Mapping ---
        screen_x, screen_y = self.mapper.map_to_screen(
            fingertip["x"],
            fingertip["y"],
        )

        # --- Task 2: Smoothing Filter ---
        smooth_x, smooth_y = self.smoother.smooth(screen_x, screen_y)
        x = int(smooth_x)
        y = int(smooth_y)

        # --- Task 5: Gesture Detection + Emit Event trực tiếp ---
        event_type = self.gesture_detector.update(hand_data, delta_time)
        if event_type is not None:
            # name phải khớp với bảng name_sfx trong AudioSystem
            name = "pause_game" if event_type == EventType.GAME_PAUSE else "resume_game"
            self.event_bus.emit(event_type, {"name": name})

        # --- Task 3 + 4 + 6: Generate cursor, basket, package output ---
        return self._package(x=x, y=y, click=False)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------
    def _package(self, x, y, click: bool) -> dict:
        """
        Task 3: Cursor Generation
        Task 4: Basket Generation
        Task 6: Output Packaging
        """
        return {
            # Task 3 — cursor theo ngón tay
            "cursor": {
                "x": x,
                "y": y,
                "click": click,  # TODO: detect gesture "pinch" → True
            },
            # Task 4 — basket vùng bắt trái (cùng vị trí cursor)
            "basket": {
                "x": x,
                "y": y,
                "radius": self.BASKET_RADIUS,
            },
        }
