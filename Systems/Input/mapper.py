import Utils.constants as constants


class CoordinateMapper:
    """
    Chuyển đổi tọa độ chuẩn hoá của MediaPipe (0.0–1.0)
    sang tọa độ pixel màn hình game.

    Lưu ý: MediaPipe trả về tọa độ theo ảnh gốc (chưa flip),
    nên trục X cần đảo ngược (mirror) để khớp với selfie-view.
    """

    def __init__(
        self,
        screen_width: int = constants.SCREEN_WIDTH,
        screen_height: int = constants.SCREEN_HEIGHT,
        mirror: bool = True,
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.mirror = mirror

    def map_to_screen(self, norm_x: float, norm_y: float) -> tuple[int, int]:
        """
        Chuyển tọa độ chuẩn hoá từ hand_data["fingertip"] → pixel màn hình.

        Args:
            norm_x: fingertip["x"] — giá trị X [0.0, 1.0] từ MediaPipe
            norm_y: fingertip["y"] — giá trị Y [0.0, 1.0] từ MediaPipe

        Returns:
            (screen_x, screen_y) tính bằng pixel
        """
        if self.mirror:
            norm_x = 1.0 - norm_x  # Lật gương theo trục X

        screen_x = int(norm_x * self.screen_width)
        screen_y = int(norm_y * self.screen_height)

        # Clamp trong phạm vi màn hình
        screen_x = max(0, min(screen_x, self.screen_width - 1))
        screen_y = max(0, min(screen_y, self.screen_height - 1))

        return screen_x, screen_y
