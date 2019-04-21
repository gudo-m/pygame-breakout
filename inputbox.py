# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import sys


def get_key(game=None):
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        elif event.type == pygame.QUIT:
            game.game_over = True
            pygame.quit()
            sys.exit()
        else:
            pass


def display_box(screen, message, error=None):
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font(None, 20)
    fontobject2 = pygame.font.Font(None, 26)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject2.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))

    screen.blit(fontobject2.render('Press <ENTER> to continue', 1, (255, 255, 255)),
                ((screen.get_width() / 2) - 150, (screen.get_height() / 2) + 50))


    screen.blit(fontobject2.render('Write complexity of game', 1, (255, 255, 255)),
                ((screen.get_width() / 2) - 100, (int(screen.get_height() / 4))))
    screen.blit(fontobject2.render('(0 - noob, 10 - pro)', 1, (255, 255, 255)),
                ((screen.get_width() / 2) - 100, (int(screen.get_height() / 4) + 20)))

    if error:
        screen.blit(fontobject2.render(error, 1, (255, 0, 0)),
                    ((screen.get_width() / 2) - 120, 50))

    pygame.display.flip()


def ask(screen, error=None, game=None):
    "ask(screen, question) -> answer"
    question = 'Complexity'
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + ''.join(current_string), error=error)
    while 1:
        inkey = get_key(game=game)
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey in (pygame.K_RETURN, 271, K_RETURN):
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            if chr(inkey).isdigit():
                current_string.append(chr(inkey))
        display_box(screen, question + ": " + ''.join(current_string))
    return ''.join(current_string)


def main():
    screen = pygame.display.set_mode((320, 240))
    print(ask(screen, "Name") + " was entered")


if __name__ == '__main__': main()
