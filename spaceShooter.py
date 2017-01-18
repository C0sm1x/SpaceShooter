import pygame, random

pygame.init()
#Screen size varables
screenWidth = 640
screenHeight = 480

# Creating the screen
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))

# Seting the Window's caption
pygame.display.set_caption("Space Shooter")

# Defining RGB values for color
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

spaceShip = pygame.image.load("Sprites/Spaceship.png")

def player(playerX, playerY):
    #Drawing the player's ship to the screen
    gameDisplay.blit(spaceShip, (playerX, playerY))
    
def bullet(bulletX, bulletY, bulletWidth, bulletHeight):
    pygame.draw.rect(gameDisplay, white, (bulletX, bulletY, bulletWidth, bulletHeight))

def gameloop():
    running = True
    
    playerX = 200
    playerY = 200
    playerXVelocity = 0
    playerYVelocity = 0
    
    bulletX = playerX
    bulletY = playerY
    bulletWidth = 10
    bulletHeight = 2
    

    while running:
        # Setting screen color to black
        gameDisplay.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerXVelocity = 4
                elif event.key == pygame.K_LEFT:
                    playerXVelocity = -4
                if event.key == pygame.K_UP:
                    playerYVelocity = -4
                elif event.key == pygame.K_DOWN:
                    playerYVelocity = 4

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerXVelocity = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerYVelocity = 0
                
                if event.key == pygame.K_SPACE:
                    fire = True
                else:
                    fire = False

                if fire == True:
                    bullet(bulletX, bulletY, bulletWidth, bulletHeight)
                    bulletX += 4

        # Edge of sceen collision for the player
        if playerX <= 2:
            playerX = 2
        elif playerX >= 585:
            playerX = 585
        elif playerY <= 2:
            playerY = 2
        elif playerY >= 425:
            playerY = 425

                
        playerX += playerXVelocity
        playerY += playerYVelocity
          
        player(playerX, playerY)
         # Updating the display
        pygame.display.update()
         # FPS clock.tick(60) 
        clock.tick(60)

# Running the gameloop function
gameloop()

#exiting pygame and Python
pygame.quit()
quit()
