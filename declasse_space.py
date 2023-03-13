# "mains" demo adapted from https://github.com/lordmauve/pgzero/tree/master/examples/basic to pygame

import pygame
import random
import math


def main():

    accel = 1.0  # Warp factor per second
    drag = 0.3  # 0.71  # Fraction of speed per second
    trail_length = 2
    min_warp_factor = 0.1
    warp_factor = 0.1
    mains = []

    def __init__(position, velocity):
        pos = position
        vel = velocity
        brightness = 100
        speed = velocity.length()

    @property
    def end_pos(self):
        """Get the point where the main trail ends."""
        x, y = pos.x, pos.y
        vx, vy = vel.x, vel.y
        return pygame.math.Vector2(
            x - vx * main.warp_factor * main.trail_length / 60,
            y - vy * main.warp_factor * main.trail_length / 60,
        )

    def update(seconds):
        pos += vel * seconds
        # Grow brighter
        brightness = min(brightness + main.warp_factor * 200 * seconds, speed, 255)

    def draw(screen):
        b = brightness
        pygame.draw.line(screen, (b, b, b), (pos.x, pos.y), (end_pos.x, end_pos.y))

    width = 0
    height = 0
    max_mains = 0


def viewer():

    screenwidth = 800
    screenheight = 600
    max_mains = 300
    viewer.width = screenwidth
    viewer.height = screenheight
    viewer.max_mains = max_mains

    def setup():

        pygame.init()
        screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        screenrect = screen.get_rect()
        background = pygame.Surface(screen.get_size()).convert()
        background.fill((0, 0, 0))  # fill background black
        clock = pygame.time.Clock()
        fps = 60
        playtime = 0.0  # how many seconds the game was played

    def run():
        running = True
        while running:
            # ------maint of event handler ----
            for event in pygame.event.get():
                seconds = clock.tick(fps) / 1000
                playtime += seconds

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            # --- end of event handler -----

            # create new mains until we have reached max_mains
            while len(main.mains) < Viewer.max_mains:
                # Pick a direction and speed
                angle = random.uniform(0, 360)
                speed = 255 * random.uniform(0.3, 1.0) ** 2
                v = pygame.math.Vector2(speed, 0)
                v.rotate_ip(angle)

                # Turn the direction into position and velocity vectors
                # dx = math.cos(angle)
                # dy = math.sin(angle)
                dx = v.x / v.length()
                dy = v.y / v.length()
                d = random.uniform(25 + main.trail_length, 100)
                pos = pygame.math.Vector2(
                    screenrect.centerx + dx * d, screenrect.centery + dy * d
                )
                # vel = speed * dx, speed * dy
                main.mains.append(main(pos, v))

            # print(len(main.mains))
            screen.blit(background, (0, 0))
            # update warp
            main.warp_factor = (
                main.min_warp_factor
                + (main.warp_factor - main.min_warp_factor) * main.drag ** seconds
            )
            for s in main.mains:
                s.update(seconds)
            # check if a main is outside the screenrect -> delete
            # print(main.mains)
            # print(main.mains[0].__dict__)
            main.mains = [s for s in main.mains if screenrect.collidepoint(s.end_pos)]
            for s in main.mains:
                s.draw(screen)

            text = "fps: {:.2f} mains: {}  Press ESC to quit".format(
                clock.get_fps(), len(main.mains)
            )
            pygame.display.set_caption(text)
            pygame.display.flip()
        # --- end of pygame main loop --
        pygame.quit()

    setup()
    run()


if __name__ == "__main__":
    viewer()
