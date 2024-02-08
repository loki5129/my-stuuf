import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SIZE = 20
FPS = 10

# Set up colors
BLACK = (0, 0, 0)
red = (255, 0, 0)
WHITE = (255,255,255)
green= (0, 255, 0)

# Set up direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = green

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * SNAKE_SIZE)) % WIDTH), (cur[1] + (y * SNAKE_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

# Score class
class Score:
    def __init__(self):
        self.value = 0
        self.color = WHITE

    def increase(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def render(self, surface):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(self.value), True, self.color)
        surface.blit(score_text, (10, 10))

# Game over screen
def show_game_over_screen():
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    font = pygame.font.Font(None, 36)
    restart_text = font.render("Press R to restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting_for_restart = False

# Initialize game objects
snake = Snake()
food = Food()
score = Score()

# Set up the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Main game loop
while True:
    snake.handle_keys()
    snake.update()

    # Check for collisions with food
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()
        score.increase()

    # Check for collisions with the snake's body
    if len(snake.positions) > 2 and snake.get_head_position() in snake.positions[2:]:
        show_game_over_screen()
        snake.reset()
        food.randomize_position()
        score.reset()

    # Draw everything
    screen.fill(BLACK)
    snake.render(screen)
    food.render(screen)
    score.render(screen)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
