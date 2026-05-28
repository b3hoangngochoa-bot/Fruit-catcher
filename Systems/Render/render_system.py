from PIL.DdsImagePlugin import item
import pygame


class RenderSystem:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, state, input_data):
        # draw everything based on state
        pass

    def draw(self):
        pass

    def draw_cursor(self, cursor):
        pass

    def draw_basket(self, basket):
        pass

    # def draw_gameplay(self, gameplay_system):
    #     # clear screen
    #     self.screen.fill((0, 0, 0))
    #     # 1. draw game objects
    #     gameplay_system.draw(self.screen)

    def draw_ui(self, ui_data, state):
        pass

    def draw(self, render_queue):
        self.screen.fill((0, 0, 0))

        # sort layer
        render_queue = [item for item in render_queue if item]
        render_queue.sort(key=lambda x: x["layer"])

        for item in render_queue:
            self._draw_item(item)

    def _draw_item(self, item):
        # ưu tiên image
        if item.get("image"):
            self.screen.blit(item["image"], (item["x"], item["y"]))
            return
        else:
            shape = item.get("shape")

            if shape == "circle":
                pygame.draw.circle(
                    self.screen,
                    item["color"],
                    (int(item["x"]), int(item["y"])),
                    item["radius"],
                )

            elif shape == "rect":
                pygame.draw.rect(
                    self.screen,
                    item["color"],
                    pygame.Rect(
                        item["x"] - item["width"] // 2,
                        item["y"] - item["height"] // 2,
                        item["width"],
                        item["height"],
                    ),
                )

        # UI text
        if item.get("text_surface"):
            self.screen.blit(item["text_surface"], item["text_rect"])
