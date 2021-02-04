import pygame
import random
import sys

pygame.init()

Block_razmer = 20
ramochka = (255, 99, 71)
Ne_ramochka = (255, 255, 255)
ramockha = (255, 99, 71)
Cvet_rat = (80, 80, 80)
SHAPOCHKA = (0, 80, 0)
Cvet_zmey = (0, 105, 0)
Kolvo_blocks = 20
SHAPOCHKA_OTSTUPY = 70
OTSTUP = 1
RAZMER = (Block_razmer * Kolvo_blocks + 2 * Block_razmer + OTSTUP * Kolvo_blocks,
          Block_razmer * Kolvo_blocks + 2 * Block_razmer + OTSTUP * Kolvo_blocks + SHAPOCHKA_OTSTUPY)
screen = pygame.display.set_mode(RAZMER)
pygame.display.set_caption('Змеёныш, а может шыш?!')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('couritr', 36)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < Kolvo_blocks and 0 <= self.y < Kolvo_blocks

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def get_random_empty_block():
    x = random.randint(0, Kolvo_blocks - 1)
    y = random.randint(0, Kolvo_blocks - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, Kolvo_blocks - 1)
        empty_block.y = random.randint(0, Kolvo_blocks - 1)
    return empty_block


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [Block_razmer + column * Block_razmer + OTSTUP * (column + 1),
                                     SHAPOCHKA_OTSTUPY + Block_razmer + row * Block_razmer + OTSTUP * (row + 1),
                                     Block_razmer, Block_razmer])


snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
rat = get_random_empty_block()
d_row = 0
d_col = 1
Ochki = 0
speeeeeid = 1
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Не выдержал и пошел спать,'
                  ' Мотя выздоравливай!)')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1
    screen.fill(ramochka)
    pygame.draw.rect(screen, SHAPOCHKA, [0, 0, RAZMER[0], SHAPOCHKA_OTSTUPY])

    text_total = courier.render(f"Total: {Ochki}", 0, Ne_ramochka)
    screen.blit(text_total, (Block_razmer, Block_razmer))
    text_speed = courier.render(f"speed: {speeeeeid}", 0, Ne_ramochka)
    screen.blit(text_speed, (Block_razmer + 235, Block_razmer))

    for row in range(Kolvo_blocks):
        for column in range(Kolvo_blocks):
            if (row + column) % 2 == 0:
                color = ramockha
            else:
                color = Ne_ramochka

            draw_block(color, row, column)

    golovushka = snake_blocks[-1]
    if not golovushka.is_inside():
        print('ШУтка ымора: произошел crash bandicoot')
        pygame.quit()
        sys.exit()

    draw_block(Cvet_rat, rat.x, rat.y)
    for block in snake_blocks:
        draw_block(Cvet_zmey, block.x, block.y)

    if rat == golovushka:
        Ochki += 1
        speeeeeid += Ochki // 5 + 1.5
        snake_blocks.append(rat)
        rat = get_random_empty_block()

    new_head = SnakeBlock(golovushka.x + d_row, golovushka.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(3 + speeeeeid)
