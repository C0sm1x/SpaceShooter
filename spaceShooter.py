import pygame, random, os

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

spaceShipDir = os.path.join("Sprites", "Spaceship.png")
spaceShip = pygame.image.load(spaceShipDir)
enemyShipDir = os.path.join("Sprites", "Red Spaceship.png")
enemyShip = pygame.image.load(enemyShipDir)

def player(playerX, playerY):
    #Drawing the player's ship to the screen
    gameDisplay.blit(spaceShip, (playerX, playerY))
    
def bullet(bulletX, bulletY, bulletWidth, bulletHeight):
    pygame.draw.rect(gameDisplay, white, (bulletX, bulletY, bulletWidth, bulletHeight))

def enemy(enemyX, enemyY,):
    gameDisplay.blit(enemyShip, (enemyX, enemyY))

def gameloop():
    running = True
    # Boundery variables
    topBoundery = 2
    rightBoundery = 585
    bottomBoundery = 425
    leftBoundery = 2

    # The variables for the player 
    playerX = 200
    playerY = 200
    playerXVelocity = 0
    playerYVelocity = 0
    # Enemy variables
    enemyX = rightBoundery + 80
    enemyY = random.randint(topBoundery, bottomBoundery)

    # The variables for the bullet 
    bulletX = playerX 
    bulletY = playerY
    bulletWidth = 10
    bulletHeight = 2
    bulletXVelocity = 0
    playerFired = False
    
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
                if event.key == pygame.K_SPACE:
                    playerFired = True
                                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerXVelocity = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerYVelocity = 0
                
        

        # Edge of sceen collision for the player
        if playerX <= leftBoundery:
            playerX = leftBoundery
        elif playerX >= rightBoundery:
            playerX = rightBoundery
        elif playerY <= topBoundery:
            playerY = topBoundery
        elif playerY >= bottomBoundery:
            playerY = bottomBoundery
        # What happens if playerFired is true
        if playerFired == True:
            # What to do if the bullet's x cordinate isn't equal to the right boundery
            if bulletX != rightBoundery:
                bullet(bulletX, bulletY, bulletWidth, bulletHeight)
                bulletXVelocity = 6 
            # What to d if the x cordinate of the bullet is greater than the right boundery
            if bulletX >= rightBoundery:
                # Sets the playerFired boolean back to false
                playerFired = False
                bulletX = playerX
                bulletY = playerY
                bulletXVelocity = 0
        # Player movement        
        playerX += playerXVelocity
        playerY += playerYVelocity

        #Buller movement
        bulletX += bulletXVelocity
        
        # Calling the player function which was defined above to draw the player
        player(playerX, playerY)
        enemy(enemyX, enemyY)

        if enemyX < leftBoundery or bulletY > enemyY and bulletY < enemyY + 100 and bulletX == enemyY:
            enemyX = rightBoundery + 80
            enemyY = random.randint(topBoundery, bottomBoundery)
            enemy(enemyX, enemyY)
 


        enemyX -= 2
         # Updating the display
        pygame.display.update()
         # FPS clock.tick(60) 
        clock.tick(60)

# Running the gameloop function
gameloop()

#exiting pygame and Python
pygame.quit()
quit()
