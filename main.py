import pygame
import os
import random

from codes.main_mechanics import MainMechanism
from codes.visual import VisualElements
from codes.hitboxes import MainHitboxes
from codes.audio import AudioPlayer

pygame.init()

pygame.mouse.set_visible(False)

pygame.display.set_caption('64 seconds to kill the cheater')

SCREEN_W = 1280
SCREEN_H = 720
ON_TUTORIAL = True

pygame.mouse.set_pos(SCREEN_W/2, SCREEN_H/2)

SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
CLOCK = pygame.time.Clock()
RUNNING = True

MAIN_MECHANISM = MainMechanism()
VISUAL_ELEMENTS = VisualElements(SCREEN)
MAIN_HITBOXES = MainHitboxes(SCREEN)
AUDIO_PLAYER = AudioPlayer()

DECK = MAIN_MECHANISM.buildDeck()

VISUAL_ELEMENTS.initiateDeckSprites(DECK)

def playRound(player):
    RANDOMIZED_DECK = MAIN_MECHANISM.randomizeDeck(DECK)

    actualPlayers = MAIN_MECHANISM.getActualPlayer()
    
    print(actualPlayers[player])

    cardGifted = MAIN_MECHANISM.giveCard(RANDOMIZED_DECK, player)

    if cardGifted is not None:
        cardSprite = VISUAL_ELEMENTS.getCardSprite(cardGifted)

        transformedSprite, pos = VISUAL_ELEMENTS.showFlipSpriteCard(cardSprite, actualPlayers[player]['tablePlace'])

        VISUAL_ELEMENTS.saveOldCards(transformedSprite, pos)

    playersNames = list(actualPlayers.keys())

    MAIN_MECHANISM.verifyCardsSum(playersNames)

    MAIN_MECHANISM.updatePlayerChanceToBuyCard(player)

    playAudioVoices(player)

    return False

def playAudioVoices(player):
    actualPlayers = MAIN_MECHANISM.getActualPlayer()

    if player in actualPlayers.keys():
        playerAbleToPlay = actualPlayers[player]["ableToPlay"]

    else:
        playerAbleToPlay = None

    if playerAbleToPlay == True:
        match player:
            case "player1":
                AUDIO_PLAYER.playAudio_Player1OneMoreCard()

            case "player2":
                AUDIO_PLAYER.playAudio_Player2okok()

            case "player3":
                AUDIO_PLAYER.playAudio_Player3CardPlease()

            case "player4":
                randomVoice = random.choice([AUDIO_PLAYER.playAudio_Player4GiveCard1, AUDIO_PLAYER.playAudio_Player4GiveCard2])

                randomVoice()

    elif playerAbleToPlay == False:
        match player:
            case "player1":
                AUDIO_PLAYER.playAudio_Player1IamFine()

            case "player2":
                AUDIO_PLAYER.playAudio_Player2StopBuy()

            case "player3":
                AUDIO_PLAYER.playAudio_Player3NoMoreCard()

            case "player4":
                randomVoice = random.choice([AUDIO_PLAYER.playAudio_Player4StopCard1, AUDIO_PLAYER.playAudio_Player4StopCard2])

                randomVoice()
    
def finishRound():
    VISUAL_ELEMENTS.showOldCards()

    MAIN_MECHANISM.resetRound()
    MAIN_MECHANISM.getActualPlayer()

    pygame.time.delay(1500)

    VISUAL_ELEMENTS.resetAllCards()

    ON_TUTORIAL = True

def hitboxAlgorithm():
    updatedPlayers = MAIN_MECHANISM.getActualPlayer()

    playersNames = list(updatedPlayers.keys())

    if pygame.mouse.get_pressed()[0]:
        AUDIO_PLAYER.playAudio_Click()

    canPlay = False
    playersPossibles = []

    for player in updatedPlayers: 
        if updatedPlayers[player]['ableToPlay'] == True:
            playersPossibles.append(player)

    whereIsMouseHitbox = MAIN_HITBOXES.getCollidingHitboxes()

    lastClickeds = MAIN_HITBOXES.returnLastClickeds()

    objectSelected = lastClickeds[-1]

    if (lastClickeds[-2] == 'deck' and objectSelected in playersPossibles):
        MAIN_HITBOXES.restartLastClickeds()

        playerSelected = objectSelected
        canPlay = True

        return playerSelected, canPlay

    elif (lastClickeds[-2] == 'deck' and objectSelected not in playersPossibles):
        MAIN_HITBOXES.restartLastClickeds()

        playerSelected = objectSelected

        playAudioVoices(objectSelected)

    hitboxOffsetX = VISUAL_ELEMENTS.updatePlayerLocation()

    MAIN_HITBOXES.updateHitboxes(hitboxOffsetX)

    return objectSelected, canPlay

    
def getHoldingCardState():
    lastClickeds = MAIN_HITBOXES.returnLastClickeds()

    if lastClickeds[-1] == 'deck':
        return True
    else:
        return False 

AUDIO_PLAYER.playAudio_BackgroundMusic()

MAIN_MECHANISM.iniciateOrRestartTimer()

while RUNNING:
    for event in pygame.event.get():
        pygame.event.set_grab(True)
        if event.type == pygame.QUIT:
            RUNNING = False

    SCREEN.fill("white")

    VISUAL_ELEMENTS.showBackgroundSprites()
    VISUAL_ELEMENTS.showText(f'{MAIN_MECHANISM.getCurrTime()} seconds past', (1040, 20), 30)

    VISUAL_ELEMENTS.showDeckCard()
    VISUAL_ELEMENTS.showPlayersSprites()

    VISUAL_ELEMENTS.showLampSprite()
    VISUAL_ELEMENTS.showDealer()
    VISUAL_ELEMENTS.showDealerCards()

    VISUAL_ELEMENTS.updateCameraLocation()

    objectSelected, canPlay = hitboxAlgorithm()

    VISUAL_ELEMENTS.showTutorialHUD(objectSelected, ON_TUTORIAL)

    finishedRound = MAIN_MECHANISM.checkRoundFinished()

    if canPlay is True:
        ON_TUTORIAL = playRound(objectSelected)
        VISUAL_ELEMENTS.showBackSpriteCard()

    elif objectSelected == "buttonFinishRound" and finishedRound is True:
        finishRound()
        MAIN_HITBOXES.restartLastClickeds()

    elif finishedRound is True:
        VISUAL_ELEMENTS.showBackSpriteCard()
        VISUAL_ELEMENTS.showFinishRoundButton()

    elif finishedRound is False:
        VISUAL_ELEMENTS.showBackSpriteCard()


    holdingState = getHoldingCardState()
    VISUAL_ELEMENTS.showMouseSprite(holdingState)

    #MAIN_HITBOXES.showHitboxes()
    
    pygame.display.flip()
    CLOCK.tick(60)

    print(CLOCK.get_fps())


pygame.quit()