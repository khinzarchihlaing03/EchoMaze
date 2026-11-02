print("EchoMaze is starting!")

import pygame

# Start Pygame
pygame.init()

# Game settings
TILE_SIZE = 50

LEVEL = [
    "############",
    "#P.........#",
    "#.###......#",
    "#...#......#",
    "#...#..##..#",
    "#..........#",
    "#.........G#",
    "############"
]

ROWS = len(LEVEL)
COLS = len(LEVEL[0])

WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE + 70

# Colors
BACKGROUND = (25, 30, 50)
FLOOR_COLOR = (52, 65, 85)
WALL_COLOR = (115, 130, 160)
PLAYER_COLOR = (100, 210, 255)
GOAL_COLOR = (100, 230, 150)
WHITE = (255, 255, 255)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EchoMaze")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# Find walls, player and exit
walls = set()
player_x = 1
player_y = 1
goal_x = 10
goal_y = 6

for row in range(ROWS):
    for col in range(COLS):
        tile = LEVEL[row][col]

        if tile == "#":
            walls.add((col, row))

        elif tile == "P":
            player_x = col
            player_y = row

        elif tile == "G":
            goal_x = col
            goal_y = row


# Move the player
def move_player(dx, dy):
    global player_x, player_y

    new_x = player_x + dx
    new_y = player_y + dy

    if (new_x, new_y) not in walls:
        if 0 <= new_x < COLS and 0 <= new_y < ROWS:
            player_x = new_x
            player_y = new_y


# Draw the maze
def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            rect = pygame.Rect(
                x, y, TILE_SIZE, TILE_SIZE
            )

            if (col, row) in walls:
                color = WALL_COLOR
            else:
                color = FLOOR_COLOR

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(
                screen, BACKGROUND, rect, 1
            )


# Draw the player and exit
def draw_objects():
    # Exit
    goal_rect = pygame.Rect(
        goal_x * TILE_SIZE + 10,
        goal_y * TILE_SIZE + 10,
        30, 30
    )
    pygame.draw.rect(
        screen, GOAL_COLOR, goal_rect
    )

    # Player
    center_x = player_x * TILE_SIZE + 25
    center_y = player_y * TILE_SIZE + 25

    pygame.draw.circle(
        screen,
        PLAYER_COLOR,
        (center_x, center_y),
        17
    )


# Main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key in (pygame.K_UP, pygame.K_w):
                move_player(0, -1)

            elif event.key in (pygame.K_DOWN, pygame.K_s):
                move_player(0, 1)

            elif event.key in (pygame.K_LEFT, pygame.K_a):
                move_player(-1, 0)

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                move_player(1, 0)

    # Draw everything
    screen.fill(BACKGROUND)

    draw_maze()
    draw_objects()

    # Check if the player reached the exit
    if player_x == goal_x and player_y == goal_y:
        message = "LEVEL COMPLETE!"
    else:
        message = "Move: WASD / Arrows | ESC: Quit"

    text = font.render(
        message, True, WHITE
    )

    screen.blit(
        text, (20, ROWS * TILE_SIZE + 20)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
