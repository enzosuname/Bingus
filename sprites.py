# This class handles sprite sheets
# https://www.pygame.org/wiki/Spritesheet
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

from settings import *

import pygame

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        """rectangle is a tuple with (x, y, x+offset, y+offset)"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def load_grid_images(self, num_rows, num_cols, x_margin = 0, x_padding = 0,
            y_margin = 0, y_padding = 0, width = None, height = None, colorkey = None):
        """Load a grid of images.
        x_margin is the space between the top of the sheet and top of the first
        row. x_padding is space between rows. Assumes symmetrical padding on
        left and right.  Same reasoning for y. Calls self.images_at() to get a
        list of images.
        """

        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        # To calculate the size of each sprite, subtract the two margins,
        #   and the padding between each row, then divide by num_cols.
        # Same reasoning for y.

        if width and height:
            x_sprite_size = width
            y_sprite_size = height
        else:
            x_sprite_size = ( sheet_width - 2 * x_margin
                - (num_cols - 1) * x_padding ) / num_cols
            y_sprite_size = ( sheet_height - 2 * y_margin
                - (num_rows - 1) * y_padding ) / num_rows

        sprite_rects = []
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                # Position of sprite rect is margin + one sprite size
                #   and one padding size for each row. Same for y.
                x = x_margin + col_num * (x_sprite_size + x_padding)
                y = y_margin + row_num * (y_sprite_size + y_padding)
                sprite_rect = (x, y, x_sprite_size, y_sprite_size)
                sprite_rects.append(sprite_rect)

        return self.images_at(sprite_rects, colorkey)

class Walls:

    def __init__(self):

        pass

class Player(pygame.sprite.Sprite):

    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.run_rt_list = image_path
        self.image = self.run_rt_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = WIN_HEIGHT - 75

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.rect.x <= WIN_WIDTH:
                self.change_x = 4
        elif keys[pygame.K_LEFT]:
            if self.rect.x >= 0:
                self.change_x = -4
        else:
            self.change_x = 0

        # now = g.time.get_ticks()
        # if now - self.prev_update > self.framerate:
        #     self.prev_update = now
        #     self.frame += 1
        # if self.frame == 4:
        #     pass
        # else:
        #     self.image = image_path[self.frame]
        #     self.rect = self.image.get_rect()
        #     self.rect.center = self.kill_center