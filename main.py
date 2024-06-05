import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Blob")

# Space Invader properties
invader_size = 50
invader_x = screen_width // 2
invader_y = screen_height // 2
invader_speed_x = 3
invader_speed_y = 3
arm_offset = 0
arm_direction = 1

# Function to draw the Space Invader
def draw_space_invader(x, y, arm_offset):
    # Body
    pygame.draw.rect(screen, green, (x, y, invader_size, invader_size // 2))
    pygame.draw.rect(screen, green, (x + invader_size // 4, y - invader_size // 4, invader_size // 2, invader_size // 4))
    pygame.draw.rect(screen, green, (x + invader_size // 4, y + invader_size // 2, invader_size // 2, invader_size // 4))
    
    # Arms
    pygame.draw.rect(screen, blue, (x, y + invader_size +1// 4 + arm_offset, invader_size // 4, invader_size // 4))
    pygame.draw.rect(screen, blue, (x+20, y + invader_size +1// 4 + arm_offset, invader_size // 4, invader_size // 4))
    pygame.draw.rect(screen, blue, (x + invader_size - invader_size // 4, y+40 + invader_size // 4 + arm_offset, invader_size // 4, invader_size // 4))
    #pygame.draw.rect(screen, blue, (x + invader_size +1 // 4 + arm_offset, y, invader_size // 4, invader_size // 4))
    #pygame.draw.rect(screen, blue, (x + invader_size +1 // 4 + arm_offset, y + invader_size // 2, invader_size // 4, invader_size // 4))

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the invader
    invader_x += invader_speed_x
    invader_y += invader_speed_y

    # Bounce the invader off the edges
    if invader_x <= 0 or invader_x + invader_size >= screen_width:
        invader_speed_x = -invader_speed_x
    if invader_y <= 0 or invader_y + invader_size >= screen_height:
        invader_speed_y = -invader_speed_y

    # Animate arms
    arm_offset += arm_direction
    if arm_offset > 5 or arm_offset < -5:
        arm_direction = -arm_direction

    # Fill the screen with black
    screen.fill(black)

    # Draw the Space Invader
    draw_space_invader(invader_x, invader_y, arm_offset)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)