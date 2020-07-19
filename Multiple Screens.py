import pygame, sys

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (210,105,30)

def terminate():
    pygame.quit()
    sys.exit()


def intro_screen(screen, clock):
    done = False

    # Set up text
    title_font = pygame.font.SysFont('Calibri', 25, True, False)
    title_text = title_font.render("Intro Screen", True, BLACK)
    instruction_font = pygame.font.SysFont('Calibri', 10, True, False)
    instruction_text = instruction_font.render("Press any key to quit", True, RED)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(GREEN)
        # --- Drawing code should go here
        screen.blit(title_text, [250, 250])
        screen.blit(instruction_text, [250, 400])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

def exit_screen(screen, clock):
    done = False

    # Set up text
    title_font = pygame.font.SysFont('Calibri', 25, True, False)
    title_text = title_font.render("Game Over", True, RED)
    instruction_font = pygame.font.SysFont('Calibri', 10, True, False)
    instruction_text = instruction_font.render("Press any key to quit", True, RED)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                terminate()

        screen.fill(BLACK)
        # --- Drawing code should go here
        screen.blit(title_text, [250, 250])
        screen.blit(instruction_text, [250, 400])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

target = pygame.Rect(325, 225, 50, 100)



intro_screen(screen, clock)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_location = pygame.mouse.get_pos()
            if target.collidepoint(mouse_location):
                exit_screen(screen, clock)

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.rect(screen, BROWN, target)
    pygame.draw.circle(screen, BLACK, [342, 270], 7)    # Door Knob

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
