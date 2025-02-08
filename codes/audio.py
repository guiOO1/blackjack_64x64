import pygame

pygame.mixer.init()

class AudioPlayer():

    def __init__(self):
        self.musicChannel = pygame.mixer.Channel(0)
        self.musicChannel.set_volume(0.2)

        self.backgroundMusic = pygame.mixer.Sound('audios/music/background-music.mp3')
        self.backgroundMetalMusic = pygame.mixer.Sound('audios/music/background-metal.mp3')

        self.sfxChannel = pygame.mixer.Channel(1)
        self.sfxChannel.set_volume(0.2)
        
        self.AudioClick = pygame.mixer.Sound("audios/sfx/click.wav")

        self.voicesChannel = pygame.mixer.Channel(2)
        self.voicesChannel.set_volume(0.5)

        self.dealer_FoundCheater = pygame.mixer.Sound("audios/dealer/found-the-cheater.mp3")
        self.dealer_FunBegan = pygame.mixer.Sound("audios/dealer/fun-began.mp3")

        self.player1_IamWinner = pygame.mixer.Sound("audios/player1/iam-winner.mp3")
        self.player1_IamFine = pygame.mixer.Sound("audios/player1/iam-fine.mp3")
        self.player1_IwasWrong = pygame.mixer.Sound("audios/player1/iwas-wrong.mp3")
        self.player1_OneMoreCard = pygame.mixer.Sound("audios/player1/one-more-card.mp3")

        self.player2_Cheater = pygame.mixer.Sound("audios/player2/cheater-audio.mp3")
        self.player2_Ilost = pygame.mixer.Sound("audios/player2/i-lost.mp3")
        self.player2_OkOk = pygame.mixer.Sound("audios/player2/ok-ok.mp3")
        self.player2_QuePassa = pygame.mixer.Sound("audios/player2/que-passa.mp3")
        self.player2_RoundMine = pygame.mixer.Sound("audios/player2/round-mine.mp3")
        self.player2_StopBuy = pygame.mixer.Sound("audios/player2/stop-buy-1.mp3")

        self.player3_CardPlease = pygame.mixer.Sound("audios/player3/card-please.mp3")
        self.player3_HowLost = pygame.mixer.Sound("audios/player3/how-lost.mp3")
        self.player3_NoMoreCard = pygame.mixer.Sound("audios/player3/no-more-card.mp3")
        self.player3_NotKorean = pygame.mixer.Sound("audios/player3/not-korean.mp3")
        
        self.player4_CheaterTable = pygame.mixer.Sound("audios/player4/cheater-table.mp3")
        self.player4_EasyGame = pygame.mixer.Sound("audios/player4/easy-game.mp3")
        self.player4_GiveCard1 = pygame.mixer.Sound("audios/player4/give-card-1.mp3")
        self.player4_GiveCard2 = pygame.mixer.Sound("audios/player4/give-card-2.mp3")
        self.player4_IamWinner = pygame.mixer.Sound("audios/player4/iam-winner.mp3")
        self.player4_Iwin = pygame.mixer.Sound("audios/player4/i-win.mp3")
        self.player4_StopCard1 = pygame.mixer.Sound("audios/player4/stop-card-1.mp3")
        self.player4_StopCard2 = pygame.mixer.Sound("audios/player4/stop-card-2.mp3")

    def playAudio_BackgroundMusic(self):
        self.musicChannel.play(self.backgroundMusic, -1)

    def playAudio_Click(self):
        if self.sfxChannel.get_busy() == False:
            self.sfxChannel.play(self.AudioClick)

    def playAudio_DealerFoundCheater(self):
        self.voicesChannel.play(self.dealer_FoundCheater)

    def playAudio_DealerFunBegan(self):
        self.voicesChannel.play(self.dealer_FunBegan)

    def playAudio_Player1IamWinner(self):
        self.voicesChannel.play(self.player1_IamWinner)

    def playAudio_Player1IamFine(self):
        self.voicesChannel.play(self.player1_IamFine)
        
    def playAudio_Player1IwasWrong(self):
        self.voicesChannel.play(self.player1_IwasWrong)

    def playAudio_Player1OneMoreCard(self):
        self.voicesChannel.play(self.player1_OneMoreCard)

    def playAudio_Player2Cheater(self):
        self.voicesChannel.play(self.player2_Cheater)

    def playAudio_Player2Ilost(self):
        self.voicesChannel.play(self.player2_Ilost)

    def playAudio_Player2okok(self):
        self.voicesChannel.play(self.player2_OkOk)

    def playAudio_Player2QuePassa(self):
        self.voicesChannel.play(self.player2_QuePassa)

    def playAudio_Player2RoundMine(self):
        self.voicesChannel.play(self.player2_RoundMine)

    def playAudio_Player2StopBuy(self):
        self.voicesChannel.play(self.player2_StopBuy)

    def playAudio_Player3CardPlease(self):
        self.voicesChannel.play(self.player3_CardPlease)

    def playAudio_Player3HowLost(self):
        self.voicesChannel.play(self.player3_HowLost)

    def playAudio_Player3NoMoreCard(self):
        self.voicesChannel.play(self.player3_NoMoreCard)

    def playAudio_Player3NotKorean(self):
        self.voicesChannel.play(self.player3_NotKorean)

    def playAudio_Player4CheaterTable(self):
        self.voicesChannel.play(self.player4_CheaterTable)

    def playAudio_Player4EasyGame(self):
        self.voicesChannel.play(self.player4_EasyGame)

    def playAudio_Player4GiveCard1(self):
        self.voicesChannel.play(self.player4_GiveCard1)

    def playAudio_Player4GiveCard2(self):
        self.voicesChannel.play(self.player4_GiveCard2)

    def playAudio_Player4IamWinner(self):
        self.voicesChannel.play(self.player4_IamWinner)

    def playAudio_Player4Iwin(self):
        self.voicesChannel.play(self.player4_Iwin)

    def playAudio_Player4StopCard1(self):
        self.voicesChannel.play(self.player4_StopCard1)

    def playAudio_Player4StopCard2(self):
        self.voicesChannel.play(self.player4_StopCard2)