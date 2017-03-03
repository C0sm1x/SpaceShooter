import pygame, random, os

pygame.init()

#Initializing sound!
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

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

# Loading the spaceship images
spaceShip = pygame.image.load(os.path.join("Sprites", "Spaceship.png"))
enemyShip = pygame.image.load(os.path.join("Sprites", "Red Spaceship.png"))

# Loading sound
fireSound = pygame.mixer.Sound(os.path.join("sfx", "fire.ogg"))

def player(playerX, playerY):
    #Drawing the player's ship to the screen
    gameDisplay.blit(spaceShip, (playerX, playerY))
    
def bullet(bulletX, bulletY, bulletWidth, bulletHeight):
    pygame.draw.rect(gameDisplay, white, (bulletX, bulletY, bulletWidth, bulletHeight))

def enemy(enemyX, enemyY,):
    gameDisplay.blit(enemyShip, (enemyX, enemyY))

def gameloop():
    running = True

    # The "sprites" are both 54+56
    spriteWidth = 54
    spriteHeight = 56

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
    enemyX = rightBoundery + 100
    enemyY = random.randint(topBoundery, bottomBoundery)

    # The variables for the bullet 
    bulletX = playerX 
    bulletY = playerY + spriteHeight / 2
    bulletWidth = 10
    bulletHeight = 4
    bulletXVelocity = 0
    playerFired = False
    
    #variables for the sound, and delay of when the sound can be played again
    delay = 300
    soundCanPLay = False
    
    while running:
        # Setting screen color to black
        gameDisplay.fill(black)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerXVelocity = 5
                elif event.key == pygame.K_LEFT:
                    playerXVelocity = -5
                if event.key == pygame.K_UP:
                    playerYVelocity = -5
                elif event.key == pygame.K_DOWN:
                    playerYVelocity = 5
                if event.key == pygame.K_SPACE:
                    playerFired = True
                    soundCanPlay = True
                    while delay > 0:
                        soundCanPLay = True
                        fireSound.play()
                        delay = delay - 1
                        if delay < 0:
                            soundCanPlay = False

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
        if playerFired == False:
            bulletX = playerX
            bulletY = playerY + spriteHeight / 2
            soundCanPlay = True
            # Setting sound back to 300 so that sound can play again
            delay = 300

        if playerFired == True:
            # What to do if the bullet's x cordinate isn't equal to the right boundery
            if bulletX != rightBoundery:
                bullet(bulletX, bulletY, bulletWidth, bulletHeight)
                bulletXVelocity = 10 

            # What to d if the x cordinate of the bullet is greater than the right boundery
            if bulletX >= rightBoundery:
                # Sets the playerFired boolean back to false
                bulletXVelocity = 0
                playerFired = False

            
        # Player movement        
        playerX += playerXVelocity
        playerY += playerYVelocity
        enemyX -= 4
        #Buller movement
        bulletX += bulletXVelocity

        # Calling the player function which was defined above to draw the player
        player(playerX, playerY)
        enemy(enemyX, enemyY)
        # What happens if the enemy ship reaches the end of the screen, or gets hit by a bullet
        if enemyX < leftBoundery or bulletY > enemyY and bulletY < enemyY + spriteHeight and bulletX > enemyX and bulletX < enemyX + spriteWidth and playerFired == True:
            playerFired = False
            enemyX = rightBoundery + 100
            enemyY = random.randint(topBoundery, bottomBoundery)
            enemy(enemyX, enemyY)
 
        # Updating the display
        pygame.display.update()
        # FPS clock.tick(60) 
        clock.tick(60)

# Running the gameloop function
gameloop()

#exiting pygame and Python
pygame.mixer.quit()
pygame.quit()
quit()
