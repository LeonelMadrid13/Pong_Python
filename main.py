import random
import pygame as pg

pg.mixer.init()

# Constants
WIDTH = 800
HEIGHT = 600
BALL_SPEED_X = 5
PALET_SOUND = pg.mixer.Sound("./golpe_paleta.mp3")
PALET_SOUND.set_volume(0.5)
WALL_SOUND = pg.mixer.Sound("./golpe_pared.mp3")
POINT_SOUND = pg.mixer.Sound("./punto.mp3")
POINT_SOUND.set_volume(0.3)

# Color Palette
WHITE = (255, 255, 255)
BG = (150, 200, 170)
BLUE = (70, 130, 180)
RED = (200, 70, 90)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)

# Player Coords and dimensions
PALET_WIDTH = 30
PALET_HEIGHT = 100

p1_x = 50
p1_y = HEIGHT // 2 - 60
p2_x = WIDTH - 50 - PALET_WIDTH
p2_y = HEIGHT // 2 - 60

# Ball Coords and dimensions
ball_x = WIDTH // 2 - 15
ball_y = HEIGHT // 2 - 15
ball_speed_y = random.randint(1, 5)
BALL_WIDTH = 10
BALL_HEIGTH = 10

# Player points
p1_points = 0
p2_points = 0

# Create Elements
p1 = pg.Rect(p1_x, p1_y, PALET_WIDTH, PALET_HEIGHT)
p2 = pg.Rect(p2_x, p2_y, PALET_WIDTH, PALET_HEIGHT)
ball = pg.Rect(ball_x, ball_y, BALL_WIDTH, BALL_HEIGTH)

# Create Main Menu
def main_menu(screen):
    screen.fill(BG)

    # Fonts
    font = pg.font.Font(None, 74)
    small_font = pg.font.Font(None, 50)

    # Button properties
    start_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 60)
    quit_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 60)

    # Get mouse position
    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()

    # Draw buttons and check hover
    if start_button.collidepoint(mouse_pos):
        pg.draw.rect(screen, BUTTON_HOVER_COLOR, start_button)
        if mouse_click[0]:  # Left mouse button clicked
            return "start"
    else:
        pg.draw.rect(screen, BUTTON_COLOR, start_button)

    if quit_button.collidepoint(mouse_pos):
        pg.draw.rect(screen, BUTTON_HOVER_COLOR, quit_button)
        if mouse_click[0]:  # Left mouse button clicked
            return "quit"
    else:
        pg.draw.rect(screen, BUTTON_COLOR, quit_button)

    # Draw text
    title_text = font.render("Pong", True, WHITE)
    start_text = small_font.render("Start", True, WHITE)
    quit_text = small_font.render("Quit", True, WHITE)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 60))

    pg.display.flip()

    return None  # No button clicked

# Winner Screen
def winner_screen(screen, winner):
    screen.fill(BG)

    # Fonts
    font = pg.font.Font(None, 74)
    small_font = pg.font.Font(None, 50)

    # Button properties
    play_again_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 60)
    quit_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60)

    # Get mouse position
    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()

    # Draw buttons and check hover
    if play_again_button.collidepoint(mouse_pos):
        pg.draw.rect(screen, BUTTON_HOVER_COLOR, play_again_button)
        if mouse_click[0]:  # Left mouse button clicked
            return "play_again"
    else:
        pg.draw.rect(screen, BUTTON_COLOR, play_again_button)

    if quit_button.collidepoint(mouse_pos):
        pg.draw.rect(screen, BUTTON_HOVER_COLOR, quit_button)
        if mouse_click[0]:  # Left mouse button clicked
            return "quit"
    else:
        pg.draw.rect(screen, BUTTON_COLOR, quit_button)

    # Display winner text
    winner_text = font.render(f"{winner} Wins!", True, WHITE)
    play_again_text = small_font.render("Play Again", True, WHITE)
    quit_text = small_font.render("Quit", True, WHITE)

    screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 4))
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 10))
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 110))

    pg.display.flip()

    return None  # No button clicked

def draw_screen(screen):
    screen.fill(BG)
    
    font = pg.font.Font(None, 74)
    text = font.render(str(p1_points), True, BLUE)
    screen.blit(text, (WIDTH // 4, 50))
    text = font.render(str(p2_points), True, RED)
    screen.blit(text, (WIDTH // 4 * 3, 50))
    
    pg.draw.rect(screen, BLUE, p1)
    pg.draw.rect(screen, RED, p2)
    pg.draw.ellipse(screen, WHITE, ball)
    pg.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Pong")
    pg.display.set_icon(pg.image.load("./pong.png"))

    global ball_speed_y
    global p1_points
    global p2_points

    clock = pg.time.Clock()
    running = True

    # Ball movement direction
    direction_x = random.choice([-1, 1])
    direction_y = random.choice([-1, 1])

    # Main loop
    while running:
        # Main menu loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    return

            menu_choice = main_menu(screen)
            if menu_choice == "start":
                break  # Exit menu to start game
            elif menu_choice == "quit":
                running = False
                return

        # Game loop
        while running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            draw_screen(screen)
            
            ball.x += BALL_SPEED_X * direction_x
            ball.y += ball_speed_y * direction_y
            
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                pg.mixer.Sound.play(WALL_SOUND)
                direction_y *= -1
                
            if ball.colliderect(p1) or ball.colliderect(p2):
                direction_x *= -1
                ball_speed_y = random.randint(1, 5)
            
            #detect if ball touches the top or bottom of the player
            # at the moment of the collision if it does, the ball will enter the player and will bounce inside
            if ball.colliderect(p1) and (ball.left <= p1.right and ball.right >= p1.right):
                pg.mixer.Sound.play(PALET_SOUND)
                direction_x = 1
            if ball.colliderect(p2) and (ball.right >= p2.left and ball.left <= p2.left):
                pg.mixer.Sound.play(PALET_SOUND)
                direction_x = -1
                
            # Check for a winner
            if p1_points == 5 or p2_points == 5:
                winner = "Player 1" if p1_points == 5 else "Player 2"
                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            running = False
                            return

                    winner_choice = winner_screen(screen, winner)
                    if winner_choice == "play_again":
                        running = True  # Restart game
                        p1_points = 0
                        p2_points = 0
                        break
                    elif winner_choice == "quit":
                        running = False
                        return

            
            if ball.left <= 0:
                pg.mixer.Sound.play(POINT_SOUND)
                p2_points += 1
            if ball.right >= WIDTH:
                pg.mixer.Sound.play(POINT_SOUND)
                p1_points += 1
            
            if ball.left <= 0 or ball.right >= WIDTH:
                ball.x = ball_x
                ball.y = ball_y
                ball_speed_y = random.randint(1, 5)
                if random.randint(0, 100) < 50:
                    direction_x = 1
                    direction_y = 1
                else:
                    direction_x = -1
                    direction_y = -1
            
            # move the players
            keys = pg.key.get_pressed()
            if keys[pg.K_w] and p1.y > 0:
                p1.y -= 5
            if keys[pg.K_s] and p1.y < HEIGHT - PALET_HEIGHT:
                p1.y += 5
            if keys[pg.K_UP] and p2.y > 0:
                p2.y -= 5
            if keys[pg.K_DOWN] and p2.y < HEIGHT - PALET_HEIGHT:
                p2.y += 5
            
            pg.display.flip()
            clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
