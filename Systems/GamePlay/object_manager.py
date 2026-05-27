class ObjectManager:
    def __init__(self):
        """
        Manage all game entities (fruit, bomb, basket, cursor, etc.)
        """
        self.objects = []

    # ----------------------------
    # ADD / REMOVE
    # ----------------------------
    def add_object(self, obj):
        """
        Add new entity to the game
        """
        self.objects.append(obj)
        # print(f"Count after adding: {len(self.objects)}")

    def remove_object(self, obj):
        """
        Remove object manually (rarely used)
        """
        if obj in self.objects:
            self.objects.remove(obj)

    # ----------------------------
    # UPDATE
    # ----------------------------
    def update(self, delta_time, input_data=None, screen_height=None):
        """
        Update all active objects
        """
        for obj in self.objects:
            if obj.active:
                if obj.tag == "BASKET" and input_data is not None:
                    obj.update(input_data)  # Basket needs input data
                else:
                    obj.update(delta_time)
            
            if obj.is_out_of_screen(screen_height) and screen_height is not None:
                obj.destroy()  # Mark as inactive if it falls below the screen
        self.cleanup()  # Clean up inactive objects after update

    # ----------------------------
    # DRAW
    # ----------------------------
    def draw(self, screen):
        """
        Draw all active objects (render_system có thể override layer)
        """
        for obj in self.objects:
            if obj.active:
                obj.draw(screen)

    # ----------------------------
    # CLEANUP
    # ----------------------------
    def cleanup(self):
        """
        Remove inactive objects (despawn)
        """
        self.objects[:] = [obj for obj in self.objects if obj.active]

    # ----------------------------
    # GETTERS
    # ----------------------------
    def get_objects(self):
        """
        Return all objects (for collision system)
        """
        return self.objects

    def get_active_objects(self):
        """
        Return only active objects
        """
        return [obj for obj in self.objects if obj.active]

    # ----------------------------
    # OPTIONAL (RẤT HỮU ÍCH)
    # ----------------------------
    def clear(self):
        """
        Clear all objects (reset game)
        """
        self.objects.clear()

    def count(self):
        return len(self.objects)
