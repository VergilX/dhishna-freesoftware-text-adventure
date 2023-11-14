"""
Program for manipulation of music
"""

import pygame
import time

MUSIC_DIRECTORY = "music/"

class MusicPlayer:
    def __init__(self):
        self.currently_playing = 0
        pygame.init()
        pygame.mixer.init()

    def __del__(self):
        pygame.quit()

    def play(self, filepath):
        """ Loads the music sound file """

        pygame.mixer.Channel(self.currently_playing).play(pygame.mixer.Sound(MUSIC_DIRECTORY+filepath))
        self.currently_playing += 1

    def pause(self, channel_no=None):
        """ Pause playing music """

        if channel_no is not None:
            pygame.mixer.Channel(channel_no).pause()
        else:
            pygame.mixer.Channel(self.currently_playing).pause()

    def unpause(self, channel_no=None):

        if channel_no is not None:
            pygame.mixer.Channel(channel_no).unpause()
        else:
            pygame.mixer.Channel(self.currently_playing).unpause()

    def stop(self, channel_no=None):

        if channel_no is not None:
            pygame.mixer.Channel(channel_no).stop()
        else:
            pygame.mixer.Channel(self.currently_playing).stop()
