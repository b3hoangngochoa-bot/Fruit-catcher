import Utils.constants as constants


class InputSystem:
    """
    Chuyển đổi dữ liệu tay (hand_data) thành điều khiển trong game.

    Pipeline:
        Task 1: Coordinate Mapping   →  norm → pixel
        Task 2: Smoothing Filter     →  làm mượt jitter
        Task 3: Cursor Generation    →  tạo dữ liệu cursor UI
        Task 4: Basket Generation    →  tạo dữ liệu basket (vùng bắt trái)
        Task 5: Output Packaging     →  đóng gói input_data chuẩn

    Output (input_data):
        {
            "cursor": { "x": int, "y": int, "click": bool },
            "basket": { "x": int, "y": int, "radius": int }
        }
    """

    # Bán kính mặc định của vùng basket bắt trái cây
    BASKET_RADIUS = 50

    def __init__(self, mapper, smoother):
        self.mapper = mapper
        self.smoother = smoother

    def update(self, hand_data: dict | None) -> dict:
        """
        Xử lý hand_data và trả về input_data chuẩn.

        Args:
            hand_data: dict từ VisionSystem.get_hand_data()
                {
                    "detected": bool,
                    "fingertip": { "x": float, "y": float } | None,
                    "frame": np.ndarray | None
                }

        Returns:
            input_data dict:
            {
                "cursor": { "x": int, "y": int, "click": bool },
                "basket": { "x": int, "y": int, "radius": int }
            }
            Khi không phát hiện tay: x/y là None.
        """
        # Không có dữ liệu hoặc không detect được tay
        if hand_data is None or not hand_data.get("detected", False):
            self.smoother.reset()
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

        # --- Task 3 + 4 + 5: Generate cursor, basket, package output ---
        return self._package(x=x, y=y, click=False)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------
    def _package(self, x, y, click: bool) -> dict:
        """
        Task 3: Cursor Generation
        Task 4: Basket Generation
        Task 5: Output Packaging
        """
        return {
            # Task 3 — cursor theo ngón tay
            "cursor": {
                "x": x,
                "y": y,
                "click": click,   # TODO: detect gesture "pinch" → True
            },
            # Task 4 — basket vùng bắt trái (cùng vị trí cursor)
            "basket": {
                "x": x,
                "y": y,
                "radius": self.BASKET_RADIUS,
            },
        }