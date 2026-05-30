from Core.event_type import EventType

class GestureDetector:
    """
    Nhận diện cử chỉ tay từ landmarks thô (output của HandDetector).

    Cử chỉ hỗ trợ:
        - "BOTH_HANDS_OPEN": Cả 2 bàn tay đều mở (5 ngón duỗi thẳng)
          → Lần đầu detect: emit GAME_PAUSE
          → Lần tiếp theo (sau debounce): emit GAME_RESUME

    MediaPipe Hand Landmarks (21 điểm):
        0  = WRIST
        1  = THUMB_CMC,  2  = THUMB_MCP,  3  = THUMB_IP,   4  = THUMB_TIP
        5  = INDEX_MCP,  6  = INDEX_PIP,  7  = INDEX_DIP,  8  = INDEX_TIP
        9  = MIDDLE_MCP, 10 = MIDDLE_PIP, 11 = MIDDLE_DIP, 12 = MIDDLE_TIP
        13 = RING_MCP,   14 = RING_PIP,   15 = RING_DIP,   16 = RING_TIP
        17 = PINKY_MCP,  18 = PINKY_PIP,  19 = PINKY_DIP,  20 = PINKY_TIP

    Quy tắc nhận diện ngón duỗi:
        - 4 ngón (trỏ → út): tip.y < pip.y  (y tăng xuống dưới trong ảnh)
        - Ngón cái: |tip.x - wrist.x| > |mcp.x - wrist.x|
    """

    # Landmark indices
    WRIST     = 0
    THUMB_MCP = 2
    THUMB_IP  = 3
    THUMB_TIP = 4
    # (mcp, pip, tip) cho 4 ngón còn lại
    FINGERS = [
        (5,  6,  8),   # Index:  MCP, PIP, TIP
        (9,  10, 12),  # Middle: MCP, PIP, TIP
        (13, 14, 16),  # Ring:   MCP, PIP, TIP
        (17, 18, 20),  # Pinky:  MCP, PIP, TIP
    ]

    def __init__(self, debounce_seconds: float = 2.0):
        """
        Args:
            debounce_seconds: Thời gian (giây) chờ sau khi gesture được trigger
                              trước khi cho phép trigger lại.
        """
        self._debounce = debounce_seconds
        self._cooldown = 0.0      # Đếm ngược thời gian debounce
        self._is_paused = False   # Trạng thái toggle: False = đang chơi, True = đang pause

    def update(self, hand_data: dict, delta_time: float) -> str | None:
        """
        Kiểm tra cử chỉ từ hand_data và trả về EventType cần emit.

        Toggle nội bộ:
            - Lần đầu detect → trả về EventType.GAME_PAUSE
            - Lần tiếp theo (sau debounce) → trả về EventType.GAME_RESUME

        Args:
            hand_data: dict từ HandDetector.detect() — phải có trường "hands"
            delta_time: thời gian (giây) từ frame trước

        Returns:
            EventType.GAME_PAUSE, EventType.GAME_RESUME, hoặc None.
        """
        # Đếm ngược debounce
        if self._cooldown > 0:
            self._cooldown -= delta_time
            return None

        hands = hand_data.get("hands", []) if hand_data else []

        # Cần đúng 2 bàn tay
        if len(hands) < 2:
            return None

        # Kiểm tra cả 2 tay có mở không
        if self._is_open_palm(hands[0]) and self._is_open_palm(hands[1]):
            self._cooldown = self._debounce  # Bật debounce

            # Toggle PAUSE ↔ RESUME
            if not self._is_paused:
                self._is_paused = True
                return EventType.GAME_PAUSE
            else:
                self._is_paused = False
                return EventType.GAME_RESUME

        return None

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------
    def _is_open_palm(self, landmarks: list[dict]) -> bool:
        """
        Kiểm tra 1 bàn tay có đang mở (tất cả ngón duỗi thẳng) không.

        Args:
            landmarks: list 21 dict {"x", "y", "z"} từ MediaPipe

        Returns:
            True nếu tất cả 5 ngón đều duỗi.
        """
        if len(landmarks) < 21:
            return False

        # Kiểm tra 4 ngón (trỏ, giữa, áp út, út)
        for mcp_i, pip_i, tip_i in self.FINGERS:
            tip = landmarks[tip_i]
            pip = landmarks[pip_i]
            # Ngón duỗi: tip ở TRÊN pip (y nhỏ hơn vì y tăng xuống)
            if tip["y"] >= pip["y"]:
                return False

        # Kiểm tra ngón cái: tip xa wrist hơn mcp
        wrist    = landmarks[self.WRIST]
        mcp      = landmarks[self.THUMB_MCP]
        thumb_tip = landmarks[self.THUMB_TIP]

        dist_tip = abs(thumb_tip["x"] - wrist["x"])
        dist_mcp = abs(mcp["x"] - wrist["x"])

        if dist_tip <= dist_mcp:
            return False

        return True
