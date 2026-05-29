from Core.event_type import EventType


class CollisionSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        print(id(self.event_bus))

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
    def _is_colliding(self, a, b):
        """
        Simple AABB collision
        """
        return (
            a.x < b.x + b.width
            and a.x + a.width > b.x
            and a.y < b.y + b.height
            and a.y + a.height > b.y
        )

    # ----------------------------
    # EMIT EVENT
    # ----------------------------
    def _handle_collision(self, obj):
        if obj.tag == "FRUIT":
            self.event_bus.emit(EventType.FRUIT_HIT, {"fruit": obj, "name": "fruit_hit"})

        elif obj.tag == "BOMB":
            self.event_bus.emit(EventType.BOMB_HIT, {"bomb": obj, "name": "bomb_hit"})
