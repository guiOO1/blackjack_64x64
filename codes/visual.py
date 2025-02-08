import pygame
import math
import copy
import random

pygame.font.init()

class VisualElements():

    def __init__(self, screen):
        self.screen = screen
        self.screenHeight = self.screen.get_height()
        self.screenWidth = self.screen.get_width()

        self.backgroundOffsetX = -700
        self.playerSpriteOffsetX = 0
        self.tableSpriteOffsetX = 0
        self.currOldCardOffsetX = 0
        self.lampOffsetX = 0

        self.positionsSpecs = {
            'player1': 0,
            'player2': 0,
            'player3': 0,
            'player4': 0,
            'dealer': 0
        }

        self.mouseSprites = [pygame.image.load(f'sprites/dealer/dealer-hand-2.png'), pygame.image.load(f'sprites/dealer/dealer_hand_picking-two.png')]

        self.arrowSprite = pygame.image.load(f'sprites/arrow.png')

        self.finishRoundSprite = pygame.image.load(f'sprites/finish-round.png')

        self.playersSprites = {
            'player1': 
                {
                    'sprite': pygame.image.load(f'sprites/players/player-1-two.png'),
                    'pos': (80, 330)
                },
            'player2': 
                {
                    'sprite': pygame.image.load(f'sprites/players/player-2-two.png'),
                    'pos': (330, 240)
                },
            'player3': 
                {
                    'sprite': pygame.image.load(f'sprites/players/player-3-two.png'),
                    'pos': (770, 240)
                },
            'player4': 
                {
                    'sprite': pygame.image.load(f'sprites/players/player-4-two.png'),
                    'pos': (1000, 330)
                },
        }

        self.oldCards = {
            'cards': [],
            'pos': []
        }

        #redimensionar quando iniciar o jogo

        self.tableSprite = pygame.image.load(f'sprites/background/table-background.png')

        self.backgroundSprite = pygame.image.load(f'sprites/background/background.png')
        self.backgroundSpriteWidth = self.backgroundSprite.get_width()

        self.deckSprite = pygame.image.load(f'sprites/card-deck.png')
        self.cardBackSprite = pygame.image.load(f'sprites/card-back.png')

        self.lampSprite = pygame.image.load(f'sprites/background/lamp.png')
        self.lampSprite = pygame.transform.scale(self.lampSprite, (self.lampSprite.get_size()[0] * 2.7, self.lampSprite.get_size()[1] * 2.7))

        self.chipsSprite = pygame.image.load(f'sprites/background/chips.png')
        self.chipsSprite = pygame.transform.scale(self.chipsSprite, (self.chipsSprite.get_size()[0] * 1.5, self.chipsSprite.get_size()[1] * 1.5))

        self.bottleSprite = pygame.image.load(f'sprites/background/bottle.png')
        self.bottleSprite = pygame.transform.scale(self.bottleSprite, (self.bottleSprite.get_size()[0] * 1.5, self.bottleSprite.get_size()[1] * 1.5))

        self.dealerHeadSprite = pygame.image.load(f'sprites/dealer/dealer-head-1.png')

    def initiateDeckSprites(self, deck):
        self.cardSprites = {}

        for card in deck:
            cardRank = card.split('-')[0]
            cardSuit = card.split('-')[1]

            fileCardSprite = f'sprites/cards-{cardSuit.lower()}/{cardSuit[:-1].lower()}-card-{cardRank.lower()}.png'

            cardSprite = pygame.image.load(fileCardSprite)

            self.cardSprites[card] = cardSprite

    def showTutorialHUD(self, clickingState, isOnTutorial):
        if isOnTutorial == True:

            spriteSize = self.arrowSprite.get_size()

            match clickingState:
                case None:
                    transformedSprite = pygame.transform.flip(self.arrowSprite, flip_x=True, flip_y=True)

                    transformedSprite.set_alpha(random.choice([222,255]))

                    self.screen.blit(transformedSprite, (380 - self.playerSpriteOffsetX, 570))

                case 'deck':
                    transformedSprite1 = pygame.transform.flip(self.arrowSprite, flip_x=True, flip_y=False)

                    transformedSprite2 = pygame.transform.flip(self.arrowSprite, flip_x=False, flip_y=False)

                    ransformedSprite3 = pygame.transform.scale(transformedSprite1, (spriteSize[0] * 1.5, spriteSize[1] * 1.5))

                    transformedSprite3 = pygame.transform.flip(self.arrowSprite, flip_x=False, flip_y=True)

                    self.screen.blit(transformedSprite1, (220 - self.playerSpriteOffsetX, 500))
                    self.screen.blit(transformedSprite2, (440 - self.playerSpriteOffsetX, 460))
                    self.screen.blit(transformedSprite3, (800 - self.playerSpriteOffsetX, 200))
                    self.screen.blit(transformedSprite2, (1050 - self.playerSpriteOffsetX, 520))
                    self.screen.blit(transformedSprite3, (700 - self.playerSpriteOffsetX, 460))

        else:
            pass
        
    def showFlipSpriteCard(self, card, pos):
        spriteCardSize = card.get_size()
    
        if pos[1] == 460 or pos[1] == 500:
            transformedSprite = pygame.transform.scale(card, (spriteCardSize[0] * 2.5, spriteCardSize[1] * 2.5))
        
        elif pos[1] == 400:
            transformedSprite = pygame.transform.scale(card, (spriteCardSize[0] * 2, spriteCardSize[1] * 2))

        elif pos[1] == 550:    
            transformedSprite = pygame.transform.scale(card, (spriteCardSize[0] * 3, spriteCardSize[1] * 3))

        return transformedSprite, pos

    def showBackSpriteCard(self):
        self.updateOldCardsLocation()

        card = self.cardBackSprite

        spriteCardSize = card.get_size()

        for pos in self.oldCards['pos']:
            if pos[1] == 460 or pos[1] == 500:
                transformedSprite = pygame.transform.scale(card, (spriteCardSize[0] * 0.6, spriteCardSize[1] * 0.6))

                self.screen.blit(transformedSprite, (pos[0] - self.currOldCardOffsetX, pos[1]))
            
            elif pos[1] == 400:
                transformedSprite = pygame.transform.scale(card, (spriteCardSize[0] * 0.5, spriteCardSize[1] * 0.5))

                self.screen.blit(transformedSprite, (pos[0] - self.currOldCardOffsetX, pos[1]))

    def showDealerCards(self):
        self.updateOldCardsLocation()

        for card, pos in zip(self.oldCards['cards'], self.oldCards['pos']):
            if pos[1] == 550:
                self.screen.blit(card, (pos[0] - self.currOldCardOffsetX, pos[1]))

    def showMouseSprite(self, holdingCard):
        self.updateMouseLocation()

        mousePerspective = max((self.mousePosY/self.screenWidth) * 7, 1.3)

        angle = 0

        if holdingCard == False:
            currMouseSprite = self.mouseSprites[0]

        elif holdingCard == True:
            currMouseSprite = self.mouseSprites[1]

        spriteMouseSize = currMouseSprite.get_size()
        currMousePos = pygame.mouse.get_pos()

        transformedMouseSprite = pygame.transform.scale(currMouseSprite, (spriteMouseSize[0] * mousePerspective , spriteMouseSize[1] * mousePerspective))

        if currMousePos[1] < 600:
            angle = math.atan2(currMousePos[0] - self.screenWidth/2, currMousePos[1] - 0)
            angle = (180 / math.pi) * angle

        if currMousePos[0] < self.screenWidth/2:
            transformedMouseSprite = pygame.transform.flip(transformedMouseSprite, True, False)
        elif currMousePos[0] < self.screenWidth/2:
            transformedMouseSprite = pygame.transform.rotate(transformedMouseSprite,-90)


        rotatedMouseSprite = pygame.transform.rotate(transformedMouseSprite, -angle)

        rotatedRect = rotatedMouseSprite.get_rect(center=currMousePos)

        self.screen.blit(rotatedMouseSprite, rotatedRect)

    def showPlayersSprites(self):
        self.updatePlayerLocation()

        for playerSpriteSpecs in self.playersSprites.values():
            spritePlayer = playerSpriteSpecs['sprite']
            spritePlayerSize = spritePlayer.get_size()

            spritePlayerPos = playerSpriteSpecs['pos']

            transformedPlayerSprite = pygame.transform.scale(spritePlayer, (spritePlayerSize[0] * 3.5, spritePlayerSize[1] * 3.5))

            adjustedSpritePos = (spritePlayerPos[0] - self.playerSpriteOffsetX, spritePlayerPos[1])

            self.screen.blit(transformedPlayerSprite, adjustedSpritePos)

    def showBackgroundSprites(self):
        self.updateBackgroundItemsLocation()

        tableSpritesSize = self.tableSprite.get_size()

        transformedTableSprite = pygame.transform.scale(self.tableSprite, (tableSpritesSize[0] * 4, tableSpritesSize[1] * 4))

        if self.backgroundOffsetX < 0:
            self.backgroundOffsetX += self.backgroundSpriteWidth

        elif self.backgroundOffsetX >= self.backgroundSpriteWidth:
            self.backgroundOffsetX -= self.backgroundSpriteWidth

        self.screen.blit(self.backgroundSprite, (self.backgroundOffsetX, 0))
        self.screen.blit(self.backgroundSprite, (self.backgroundOffsetX - self.backgroundSpriteWidth, 0))

        self.screen.blit(transformedTableSprite, (100 - (self.tableSpriteOffsetX), 210))

        self.screen.blit(self.chipsSprite, (550 - (self.tableSpriteOffsetX),450))

        self.screen.blit(self.bottleSprite, (490 - (self.tableSpriteOffsetX),500))

    def showLampSprite(self):
        self.screen.blit(self.lampSprite, (450 - (self.lampOffsetX),0))
        
    def showDealer(self):
        self.updateMouseLocation()

        spritePos = (270, 570)

        dealerHeadSpriteSize = self.dealerHeadSprite.get_size()

        transformedDealerHeadSprite = pygame.transform.scale(self.dealerHeadSprite, (dealerHeadSpriteSize[0] * 3, dealerHeadSpriteSize[1] * 3))

        self.screen.blit(transformedDealerHeadSprite, (680 - self.playerSpriteOffsetX, 530))

    def showOldCards(self):
        self.updateOldCardsLocation()

        for card, pos in zip(self.oldCards['cards'], self.oldCards['pos']):
            self.screen.blit(card, (pos[0] - self.currOldCardOffsetX, pos[1]))

    def showDeckCard(self):
        deckCardSpritesSize = self.deckSprite.get_size()

        transformedDeckCardSprite = pygame.transform.scale(self.deckSprite, (deckCardSpritesSize[0] * 0.8, deckCardSpritesSize[1] * 0.8))

        self.screen.blit(transformedDeckCardSprite, (300 - self.playerSpriteOffsetX, 570))

    def showText(self, text, pos, fontSize):
        textFont = pygame.font.SysFont('impact', fontSize)

        textRendered = textFont.render(f'{str(text)}', False, pygame.Color('black'))

        self.screen.blit(textRendered, pos)

    def showFinishRoundButton(self):
        self.screen.blit(self.finishRoundSprite, (1000, 530))

    def updateMouseLocation(self):
        self.mousePosX, self.mousePosY = pygame.mouse.get_pos()

    def updateCameraLocation(self):
        self.updateMouseLocation()

        if self.mousePosX < 100:
            self.backgroundOffsetX += 10

        elif self.mousePosX > (self.screenWidth - 100):
            self.backgroundOffsetX -= 10

        return self.backgroundOffsetX

    def updatePlayerLocation(self):
        self.updateMouseLocation()

        if self.mousePosX < 100:
            self.playerSpriteOffsetX -= 6

        elif self.mousePosX > (self.screenWidth - 100):
            self.playerSpriteOffsetX += 6

        if self.playerSpriteOffsetX >= 1760:
            self.playerSpriteOffsetX = -1280

        elif self.playerSpriteOffsetX <= -1760:
            self.playerSpriteOffsetX = 1280

        #print(f'playerOffsetX: {self.playerSpriteOffsetX}')

        #print(f'backgroundOffsetX: {self.backgroundOffsetX}')

        return self.playerSpriteOffsetX

    def updateBackgroundItemsLocation(self):
        self.updateMouseLocation()

        if self.mousePosX < 100:
            self.tableSpriteOffsetX = self.playerSpriteOffsetX
            self.lampOffsetX = self.playerSpriteOffsetX * 1.2

        elif self.mousePosX > (self.screenWidth - 100):
            self.tableSpriteOffsetX = self.playerSpriteOffsetX
            self.lampOffsetX = self.playerSpriteOffsetX * 1.2

    def updateOldCardsLocation(self):
        self.updateMouseLocation()

        if self.mousePosX < 100:
            self.currOldCardOffsetX = self.playerSpriteOffsetX*1

        elif self.mousePosX > (self.screenWidth - 100):
            self.currOldCardOffsetX = self.playerSpriteOffsetX*1

    def saveOldCards(self, cardSprite, pos):
        if pos == (200, 500):  
            cardPos = self.positionsSpecs['player1']

            pos = (pos[0] + cardPos, pos[1])
            self.positionsSpecs['player1'] -= 18

        elif pos == (400,400):  
            cardPos = self.positionsSpecs['player2']

            pos = (pos[0] + cardPos, pos[1])
            self.positionsSpecs['player2'] += 20

        elif pos == (800,400):  
            cardPos = self.positionsSpecs['player3']

            pos = (pos[0] + cardPos, pos[1])
            self.positionsSpecs['player3'] -= 20

        elif pos == (1010,500):  
            cardPos = self.positionsSpecs['player4']

            pos = (pos[0] + cardPos, pos[1])
            self.positionsSpecs['player4'] -= 18

        elif pos == (700, 550):  
            cardPos = self.positionsSpecs['dealer']

            pos = (pos[0] + cardPos, pos[1])
            self.positionsSpecs['dealer'] += 20

        self.oldCards['cards'].append(cardSprite)
        self.oldCards['pos'].append(pos)

    def getCardSprite(self, card):
        cardSprite = self.cardSprites[card]

        return cardSprite

    def resetAllCards(self):
        self.oldCards = {
            'cards': [],
            'pos': []
        }

        self.positionsSpecs = {
            'player1': 0,
            'player2': 0,
            'player3': 0,
            'player4': 0,
            'dealer': 0
        }