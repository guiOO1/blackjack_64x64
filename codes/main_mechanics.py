import random
import copy
import time

from codes.audio import AudioPlayer

AUDIO_PLAYER = AudioPlayer()

class MainMechanism():

    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        self.actualPlayers = {    
            'player1':
                {
                'ableToPlay': True,
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (200, 500),
                'chanceToBuyCard': 100}
            ,
            'player2':
                {
                'ableToPlay': True,            
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (400, 400),
                'chanceToBuyCard': 100}
            ,    
            'player3':
                {
                'ableToPlay': True,    
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (800, 400),
                'chanceToBuyCard': 100}
            ,
            'player4':
                {
                'ableToPlay': True,        
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (1010,500),
                'chanceToBuyCard': 100}
            ,
            'dealer':
                {
                'ableToPlay': True,            
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (700, 550),
                'chanceToBuyCard': 100}
            ,   
            }

        self.someoneBlackjacked = False

    def buildDeck(self):
        deck = []

        for suit in self.suits:
            for rank in self.ranks:
                
                card = f'{rank}-{suit}'

                deck.append(card)

        return deck

    def randomizeDeck(self, deck):
        copiedDeck = copy.deepcopy(deck)

        random.shuffle(copiedDeck)

        return copiedDeck

    def giveCard(self, deck, player):
        card = random.choice(deck)

        if player in list(self.actualPlayers.keys()):
            self.actualPlayers[player]['currCards'].append(card)

            cardGifted = deck.pop(deck.index(card))

            return cardGifted
    
    def verifyCardsSum(self, playersToVerify):
        if type(playersToVerify) != list:
            playersToVerify = [playersToVerify]

        for player in playersToVerify:
            if len(self.actualPlayers[player]['currCards']) == 0:
                continue

            acesCount = 0
            cardsParsed = []

            cardsToSum = self.actualPlayers[player]['currCards']
        
            for card in cardsToSum:
                cardValue = card.split('-')[0]

                if (cardValue == 'Jack') or (cardValue == 'Queen') or (cardValue == 'King'):
                    cardValue = 10
                    cardsParsed.append(cardValue)

                elif cardValue =='Ace':
                    acesCount += 1

                else:
                    cardValue = int(cardValue)
                    cardsParsed.append(cardValue)

            for aces in range(acesCount):
                if (sum(cardsParsed) + 11) > 21:
                    cardsParsed.append(1)
                else:
                    cardsParsed.append(11)

            self.actualPlayers[player]['currCardsValues'] = sum(cardsParsed)

    def checkPlayerCanBuy(self, player):
        randomChance = random.randint(1, 100)

        playerChance = self.actualPlayers[player]['chanceToBuyCard']

        canBuy = (self.actualPlayers[player]['chanceToBuyCard'] >= randomChance)


        print(f'chance: {playerChance}%')
        print(f'random chance: {randomChance}')
        print(f'canBuy status: {canBuy}')

        if canBuy is False:
            self.actualPlayers[player]['chanceToBuyCard'] = 0
            self.actualPlayers[player]['ableToPlay'] = False
        else:
            pass
        
    def verifyWinner(self, availablePlayers):
        possibleWinner = {}

        for player in availablePlayers:
            playerCardsValues = availablePlayers[player]['currCardsValues']

            possibleWinner[player] = playerCardsValues   

        sortedPossibleWinner = sorted(possibleWinner.items(), key=lambda item: item[1], reverse=True)

        return playerWinner

    def checkRoundFinished(self):
        playersFinishedCount = 0
        
        for player in self.actualPlayers:
            if not self.actualPlayers[player]['ableToPlay']:
                playersFinishedCount += 1

        if playersFinishedCount >= len(self.actualPlayers)-1 and len(self.actualPlayers['dealer']['currCards']) > 2:  
            return True
        else:
            return False

    def updatePlayerChanceToBuyCard(self, player):
        if player in [p for p in self.actualPlayers.keys() if p != 'dealer']:
            initialChanceToBuy = self.actualPlayers[player]['chanceToBuyCard']

            playerCardsValues = self.actualPlayers[player]['currCardsValues']

            playerCardsInHand = self.actualPlayers[player]['currCards']

            if (len(playerCardsInHand) >= 2):

                if (playerCardsValues <= 14):
                    self.actualPlayers[player]['chanceToBuyCard'] = 100

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 15):
                    newRandomChanceToBuy = random.randint(1 + int(initialChanceToBuy*0.12), initialChanceToBuy - int(initialChanceToBuy*0.12))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 16):
                    newRandomChanceToBuy = random.randint(1 + int(initialChanceToBuy*0.1), initialChanceToBuy - int(initialChanceToBuy*0.15))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 17):
                    newRandomChanceToBuy = random.randint(1 + int(initialChanceToBuy*0.05), initialChanceToBuy - int(initialChanceToBuy*0.17))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 18):
                    newRandomChanceToBuy = random.randint(1 + int(initialChanceToBuy*0.02), initialChanceToBuy - int(initialChanceToBuy *0.2))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 19):
                    newRandomChanceToBuy = random.randint(1, initialChanceToBuy - int(initialChanceToBuy *0.5))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 20):
                    newRandomChanceToBuy = random.randint(1, initialChanceToBuy - int(initialChanceToBuy *0.95))

                    self.actualPlayers[player]['chanceToBuyCard'] = newRandomChanceToBuy

                    self.checkPlayerCanBuy(player)

                elif (playerCardsValues == 21):
                    self.actualPlayers[player]['chanceToBuyCard'] = 0
                    self.checkPlayerCanBuy(player)

                    self.someoneBlackjacked = True

                    print('21')

                    print(f'blackjacked: {self.someoneBlackjacked}')

                elif (playerCardsValues >= 21):
                    self.actualPlayers[player]['chanceToBuyCard'] = 0
                    self.checkPlayerCanBuy(player)

                    print('exploded')

        else:
            self.verifyCardsSum('dealer')

            if self.actualPlayers['dealer']['currCardsValues'] >= 21:
                self.actualPlayers['dealer']['ableToPlay'] = False

    def iniciateOrRestartTimer(self):
        self.startTimeSec = (time.localtime().tm_hour * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec

    def getCurrTime(self):
        timeSec = (time.localtime().tm_hour * 3600) + (time.localtime().tm_min * 60) + time.localtime().tm_sec

        timeSecDiff = timeSec - self.startTimeSec

        return timeSecDiff

    def checkTimeOver(self):
        isTimerOver = False

        currTime = self.getCurrTime()

        if currTime == 64:
            isTimerOver = True

        return isTimerOver

    def getActualPlayer(self):
        return self.actualPlayers

    def resetRound(self):
        self.actualPlayers = {    
            'player1':
                {
                'ableToPlay': True,
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (200, 500),
                'chanceToBuyCard': 100}
            ,
            'player2':
                {
                'ableToPlay': True,            
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (400, 400),
                'chanceToBuyCard': 100}
            ,    
            'player3':
                {
                'ableToPlay': True,    
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (800, 400),
                'chanceToBuyCard': 100}
            ,
            'player4':
                {
                'ableToPlay': True,        
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (1010,500),
                'chanceToBuyCard': 100}
            ,
            'dealer':
                {
                'ableToPlay': True,            
                'currCards': [],
                'currCardsValues': 0,
                'totalPoints': 10,
                'tablePlace': (700, 550),
                'chanceToBuyCard': 100}
            ,   
            }