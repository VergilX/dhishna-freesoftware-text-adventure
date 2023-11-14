"""
Program for manipulation of music
"""

import pygame
import time

MUSIC_DIRECTORY = "music/"

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def __del__(self):
        pygame.quit()

    def load(self, filepath):
        """ Loads the music sound file """

        pygame.mixer.music.load(MUSIC_DIRECTORY+filepath)

    def play(self):
        """ Plays loaded music """

        pygame.mixer.music.play()

    def pause(self):
        """ Pause playing music """

        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
