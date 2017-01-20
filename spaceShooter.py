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
    # The variables for the player 
    playerX = 200
    playerY = 200
    playerXVelocity = 0
    playerYVelocity = 0
    # The variables for the bullet 
    bulletX = playerX
    bulletY = playerY
    bulletWidth = 10
    bulletHeight = 2
    bulletXVelocity = 0
    
    # Boundery variables
    topBoundery = 2
    rightBoundery = 585
    bottomBoundery = 425
    leftBoundery = 2

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
                    while bulletX < rightBoundery:
                        bullet(bulletX, bulletY, bulletWidth, bulletHeight)
                    fire = False
                    bulletXVelocity = 4
                    print bulletXVelocity

        # Edge of sceen collision for the player
        if playerX <= leftBoundery:
            playerX = leftBoundery
        elif playerX >= rightBoundery:
            playerX = rightBoundery
        elif playerY <= topBoundery:
            playerY = topBoundery
        elif playerY >= bottomBoundery:
            playerY = bottomBoundery

        # Player movement        
        playerX += playerXVelocity
        playerY += playerYVelocity

        #Buller movement
        bulletX += bulletXVelocity
        
        # Calling the player function which was defined above to draw the player
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
