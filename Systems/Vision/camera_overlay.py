import numpy as np
import pygame
import cv2
from Systems.Render.render_layer import RenderLayer
from Utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class CameraOverlay:
    def __init__(
        self,
        width=240,
        height=180,
    ):
        self.frame = None

        self.width = width
        self.height = height

        self.x = SCREEN_WIDTH - width - 10
        self.y = SCREEN_HEIGHT - height - 10

    def update(self, frame):
        self.frame = frame

    def get_render_data(self):

        if self.frame is None:
            return []

        frame_rgb = cv2.cvtColor(
            self.frame,
            cv2.COLOR_BGR2RGB,
        )

        frame_surface = pygame.surfarray.make_surface(np.rot90(frame_rgb))

        # resize nhỏ lại
        frame_surface = pygame.transform.scale(
            frame_surface,
            (self.width, self.height),
        )

        return {
            "layer": RenderLayer.OVERLAY,
            "image": frame_surface,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }
