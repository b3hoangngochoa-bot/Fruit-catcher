class Smoother:
    """
    Làm mượt chuyển động tay bằng thuật toán trung bình trượt (moving average).
    Giúp loại bỏ nhiễu rung lắc nhỏ từ camera.
    """

    def __init__(self, buffer_size: int = 5):
        """
        Args:
            buffer_size: Số frame lưu lại để tính trung bình.
                         Giá trị nhỏ → nhanh nhạy hơn.
                         Giá trị lớn → mượt hơn nhưng trễ hơn.
        """
        self.buffer_size = buffer_size
        self._buffer_x: list[float] = []
        self._buffer_y: list[float] = []

    def smooth(self, x: float, y: float) -> tuple[float, float]:
        """
        Nhận tọa độ mới, thêm vào buffer, trả về giá trị trung bình.

        Args:
            x: Giá trị X hiện tại (pixel hoặc chuẩn hoá)
            y: Giá trị Y hiện tại (pixel hoặc chuẩn hoá)

        Returns:
            (smooth_x, smooth_y) đã làm mượt
        """
        self._buffer_x.append(x)
        self._buffer_y.append(y)

        if len(self._buffer_x) > self.buffer_size:
            self._buffer_x.pop(0)
            self._buffer_y.pop(0)

        smooth_x = sum(self._buffer_x) / len(self._buffer_x)
        smooth_y = sum(self._buffer_y) / len(self._buffer_y)

        return smooth_x, smooth_y

    def reset(self):
        """Xóa buffer (dùng khi mất tín hiệu tay)."""
        self._buffer_x.clear()
        self._buffer_y.clear()
