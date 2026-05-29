import pygame


class RenderSystem:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, render_queue):
        # sort layer
        render_queue = [item for item in render_queue if item]
        render_queue.sort(key=lambda x: x["layer"])

        for item in render_queue:
            self._draw_item(item)

    def _draw_item(self, item):

        # 🎯 background full screen
        if item.get("full_screen"):
            if item.get("image"):
                self.screen.blit(item["image"], (0, 0))
            else:
                self.screen.fill(item["color"])
            return

        # ưu tiên image
        if item.get("image"):
            if item.get("basket"):
                self.screen.blit(
                    item["image"],
                    (
                        item["x"] - item["width"] // 2,
                        item["y"] - item["height"] // 2 - 50,
                    ),
                )
            elif item.get("button"):
                self.screen.blit(
                    item["image"],
                    (
                        item["x"] - item["width"] // 2 - 50,
                        item["y"] - item["height"] // 2,
                    ),
                )
            else:
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
