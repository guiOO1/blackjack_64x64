import pygame

class MainHitboxes():

    def __init__(self, screen):
        self.screen = screen

        self.deckCardHitbox = pygame.Rect(320, 620, 150, 90)

        #self.player1CardsHitbox = pygame.Rect(10, 230, 75, 75)
        #self.player2CardsHitbox = pygame.Rect(110, 10, 75, 75)
        #self.player3CardsHitbox = pygame.Rect(360, 10, 75, 75)
        #self.player4CardsHitbox = pygame.Rect(550, 250, 75, 75)
        #self.dealerCardsHitbox = pygame.Rect(390, 500, 75, 75)

        self.player1Hitbox = pygame.Rect(80, 330, 200, 200)
        self.player2Hitbox = pygame.Rect(330, 240, 200, 200)
        self.player3Hitbox = pygame.Rect(770, 240, 200, 200)
        self.player4Hitbox = pygame.Rect(550, 330, 200, 200)
        self.dealerHitbox = pygame.Rect(1000, 330, 200, 200)

        self.buttonFinishRoundHitbox = pygame.Rect(1050, 530, 200, 150)

        self.whereIsHitbox = None

        self.lastClickeds = [None, None]

    def getCollidingHitboxes(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        mouseRect = pygame.Rect(mouseX,mouseY, 3, 3)

        self.whereIsHitbox = None

        if self.deckCardHitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'deck'

        #elif self.player1CardsHitbox.colliderect(mouseRect) == True:
        #    self.whereIsHitbox = 'player1Cards'
#
        #elif self.player2CardsHitbox.colliderect(mouseRect) == True:
        #    self.whereIsHitbox = 'player2Cards'
        #
        #elif self.player3CardsHitbox.colliderect(mouseRect) == True:
        #    self.whereIsHitbox = 'player3Cards'
#
        #elif self.player4CardsHitbox.colliderect(mouseRect) == True:
        #    self.whereIsHitbox = 'player4Cards'
#
        #elif self.dealerCardsHitbox.colliderect(mouseRect) == True:
        #    self.whereIsHitbox = 'dealerCards'
#
        elif self.player1Hitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'player1'

        elif self.player2Hitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'player2'
        
        elif self.player3Hitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'player3'

        elif self.player4Hitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'player4'

        elif self.dealerHitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'dealer'

        elif self.buttonFinishRoundHitbox.colliderect(mouseRect) == True:
            self.whereIsHitbox = 'buttonFinishRound'

        return self.whereIsHitbox

    def updateHitboxes(self, offsetX):
        self.player1CardsHitbox = pygame.Rect(10 - offsetX, 230, 75, 75)
        self.player2CardsHitbox = pygame.Rect(110 - offsetX, 10, 75, 75)
        self.player3CardsHitbox = pygame.Rect(360 - offsetX, 10, 75, 75)
        self.player4CardsHitbox = pygame.Rect(550 - offsetX, 250, 75, 75)
        self.dealerCardsHitbox = pygame.Rect(390 - offsetX, 500, 75, 75)

        self.player1Hitbox = pygame.Rect(80 - offsetX, 330, 200, 200)
        self.player2Hitbox = pygame.Rect(330 - offsetX, 240, 200, 200)
        self.player3Hitbox = pygame.Rect(770 - offsetX, 240, 200, 200)
        self.player4Hitbox = pygame.Rect(1000 - offsetX, 330, 200, 200)
        self.dealerHitbox = pygame.Rect(680 - offsetX, 520, 200, 200)

        self.deckCardHitbox = pygame.Rect(320 - offsetX, 600, 150, 90)

    def returnLastClickeds(self):
        isClicking = pygame.mouse.get_pressed()[0]

        if (self.whereIsHitbox != None) and isClicking and (self.lastClickeds[-1] != self.whereIsHitbox):
            self.lastClickeds.append(self.whereIsHitbox)

        return self.lastClickeds

    def restartLastClickeds(self):
        self.lastClickeds = [None, None]

    def showHitboxes(self):
        pygame.draw.rect(self.screen, 'black', self.deckCardHitbox, 2)

        #pygame.draw.rect(self.screen, 'black', self.player1CardsHitbox, 2)
        #pygame.draw.rect(self.screen, 'black', self.player2CardsHitbox, 2)
        #pygame.draw.rect(self.screen, 'black', self.player3CardsHitbox, 2)
        #pygame.draw.rect(self.screen, 'black', self.player4CardsHitbox, 2)
        #pygame.draw.rect(self.screen, 'black', self.dealerCardsHitbox, 2)

        pygame.draw.rect(self.screen, 'black', self.player1Hitbox, 2)
        pygame.draw.rect(self.screen, 'black', self.player2Hitbox, 2)
        pygame.draw.rect(self.screen, 'black', self.player3Hitbox, 2)
        pygame.draw.rect(self.screen, 'black', self.player4Hitbox, 2)
        pygame.draw.rect(self.screen, 'black', self.dealerHitbox, 2)

        pygame.draw.rect(self.screen, 'black', self.dealerHitbox, 2)

        pygame.draw.rect(self.screen, 'black', self.buttonFinishRoundHitbox, 2)
        