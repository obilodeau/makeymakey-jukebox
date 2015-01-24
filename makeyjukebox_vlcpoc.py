#!/usr/bin/env python3

import sys
import time

import vlc

class Player(object):

    def __init__(self, filename):

        # player constants
        self.jitter = 0.2

        # VLC stuff
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.media = self.instance.media_new(filename)
        self.mediaplayer.set_media(self.media)

    def _play(self):
        if self.mediaplayer.play() == -1:
            raise Exception("play returned -1")

        # if we don't wait, it won't enter main loop since is_playing will
        # return false
        time.sleep(self.jitter)

    def _main_loop(self):
        while self.mediaplayer.is_playing():
            time.sleep(self.jitter)

        print("Finished")

    def Start(self):
        self._play()
        self._main_loop()

if __name__ == "__main__":
    if sys.argv[1:]:
        player = Player(sys.argv[1])
    else:
        raise Exception("No file to play given on command line")

    player.Start()
