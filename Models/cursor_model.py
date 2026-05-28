from Models.base_entity import BaseEntity
from Systems.Render.render_layer import RenderLayer
import pygame


class Cursor(BaseEntity):
    def __init__(self, width=10, height=10, image=None):
        super().__init__(width=width, height=height, image=image, tag="CURSOR")
        self.color = (255, 255, 255)  # Cursor color for debugging
        self.radius = width // 2  # Assuming cursor is circular for rendering
        self.render_layer = RenderLayer.OVERLAY
        # Ensure cursor is rendered above all other entities

    def update(self, input_data):
        if not self.active:
            return

        cursor = input_data.get("cursor", {})
        self.x = cursor.get("x") or self.x
        self.y = cursor.get("y") or self.y

    def get_render_data(self):
        if not self.active:
            return None

        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "radius": self.radius,
            "layer": self.render_layer,
            "shape": "circle",
            "image": self.image or None,
        }
