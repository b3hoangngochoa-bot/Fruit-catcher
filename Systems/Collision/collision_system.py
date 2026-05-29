from Core.event_type import EventType


class CollisionSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def check(self, objects):
        """
        Detect collision giữa basket và các object
        """

        basket = None
        others = []

        # tách basket ra
        for obj in objects:
            if not obj.active:
                continue

            if obj.tag == "BASKET":
                basket = obj
            else:
                others.append(obj)

        if basket is None:
            return

        # check collision
        for obj in others:
            if not obj.active:
                continue

            if self._is_colliding(basket, obj):
                self._handle_collision(obj)

    # ----------------------------
    # COLLISION CHECK
    # ----------------------------
    def _is_colliding(self, basket, obj):
        """
        Simple AABB collision
        """
        left_basket = basket.x - basket.width // 2
        right_basket = basket.x + basket.width // 2
        top_basket = basket.y - basket.height // 2
        bottom_basket = basket.y + basket.height // 2

        left_obj = obj.x
        right_obj = obj.x + obj.width
        top_obj = obj.y
        bottom_obj = obj.y + obj.height
        return (
            left_obj < right_basket
            and right_obj > left_basket
            and top_obj < bottom_basket
            and bottom_obj > top_basket
        )

    # ----------------------------
    # EMIT EVENT
    # ----------------------------
    def _handle_collision(self, obj):
        if obj.tag == "FRUIT":
            self.event_bus.emit(
                EventType.FRUIT_HIT, {"fruit": obj, "name": "fruit_hit"}
            )

        elif obj.tag == "BOMB":
            self.event_bus.emit(EventType.BOMB_HIT, {"bomb": obj, "name": "bomb_hit"})
