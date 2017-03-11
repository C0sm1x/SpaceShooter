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
grey = (100, 100, 100)

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

def titleScreen():
    titleScreenFont = pygame.font.SysFont("None", 50)
    pressEnter = titleScreenFont.render("Press Enter", True, (white))
    gameDisplay.blit(pressEnter, (200, 100))

def gameOverScreen():
    gameOverScreenFont = pygame.font.SysFont("None", 50)
    gameOverPressEnterFont = pygame.font.SysFont("None", 30)
    gameOver = gameOverScreenFont.render("Game Over", True, (white))
    gameDisplay.blit(gameOver, (200, 100))
    gameOverPressEnter = gameOverPressEnterFont.render("Press Enter to continue", True, (grey))
    gameDisplay.blit(gameOverPressEnter, (190, 220))

def keepingScore(score):
    font = pygame.font.SysFont("none", 50)
    score_Font_Render = font.render(str(score), True, white)
    gameDisplay.blit(score_Font_Render, (300, 20))

def gameloop():
    running = True
    onTitleScreen = True
    onGameOverScreen = False
    # The "sprites" are both 54+56
    spriteWidth = 54
    spriteHeight = 56

    # Boundery variables
    topBoundery = 2 + 50
    rightBoundery = 585
    bottomBoundery = 425 - 50
    leftBoundery = 2

    # The variables for the player 
    playerX = 200
    playerY = 200
    playerXVelocity = 0
    playerYVelocity = 0
 
    # Enemy variables
    enemyX = rightBoundery + 100
    enemyY = random.randint(topBoundery + 50, bottomBoundery - 50)

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

    # Keeping score
    score = 0
    
    while onTitleScreen:
        pygame.display.update()
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                quit()               

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    onTitleScreen = False
        titleScreen() 

    while running:
        
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
                        fireSound.set_volume(0.2)
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
        
        # corner collisions
        if playerX <= leftBoundery and playerY >= bottomBoundery:
            playerX = leftBoundery
            playerY = bottomBoundery
        elif playerX >= rightBoundery and playerY >= bottomBoundery:
            playerX = rightBoundery
            playerY = bottomBoundery
        elif playerY <= topBoundery and playerX <= leftBoundery:
            playerY = topBoundery
            playerX = leftBoundery
        elif playerY <= topBoundery and playerX >= rightBoundery:
            playerX = rightBoundery
            playerY = topBoundery

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

            # What to do if the x cordinate of the bullet is greater than the right boundery
            if bulletX >= rightBoundery + 100:
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
        
        # Calling the score function
        keepingScore(score)

        # What happens if the enemy ship reaches the end of the screen, or gets hit by a bullet 
        if enemyX < leftBoundery - 100 : 
            enemyX = rightBoundery + 100
            enemyY = random.randint(topBoundery, bottomBoundery)

        if bulletY > enemyY and bulletY < enemyY + spriteHeight and bulletX > enemyX and bulletX < enemyX + spriteWidth and playerFired == True:
            playerFired = False
            enemyX = rightBoundery + 100
            enemyY = random.randint(topBoundery, bottomBoundery)
            enemy(enemyX, enemyY) 
            score += 50


        if enemyY > playerY and enemyY <= playerY + spriteHeight and enemyX > playerX and enemyX < playerX + spriteWidth or enemyY < playerY and enemyY >= playerY - spriteHeight and enemyX > playerX and enemyX < playerX + spriteWidth: 
            onGameOverScreen = True
            # Displaying the game over screen
            while onGameOverScreen:
                pygame.display.update()
                gameDisplay.fill(black)
                gameOverScreen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.mixer.quit()
                        pygame.quit()
                        quit()               

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            onGameOverScreen = False               
                            gameloop()


        # Updating the display
        pygame.display.update()

        # Setting screen color to black
        gameDisplay.fill(black)

        # FPS clock.tick(60) 
        clock.tick(60)

# Running the gameloop function
gameloop()

#exiting pygame and Python
pygame.mixer.quit()
pygame.quit()
quit()
