#!/usr/bin/env python3

import time

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from getch import getch
import pympris

# TODO: Implement seeking, skip, Pause/Play toggle
#       http://pympris.readthedocs.org/en/latest/

class Jukebox(object):

    def __init__(self):

        # internal constants
        self.jitter = 1
        self.makey_key = 'w'
        self.quit_key = 'q'

        # MPRIS dependencies
        self.dbus_loop = DBusGMainLoop()
        self.bus = dbus.SessionBus(mainloop=self.dbus_loop)

        # get a media player handle
        self.players_ids = list(pympris.available_players())
        self.mp = pympris.MediaPlayer(self.players_ids[0], self.bus)

    def _play(self):
        if self.mp.player.CanPlay and self.mp.player.CanPause:
            self.mp.player.PlayPause()

    def _skip(self):
        if self.mp.player.CanGoNext:
            self.mp.player.Next()

    def Run(self):
        self._play()
        print("Connect skip button to key '{}' on the makeymakey board"\
                .format(self.makey_key))
        print("Press '{}' to quit".format(self.quit_key))
        while True:

            # grab key events (blocking)
            key = getch()

            if key == self.makey_key:
                self._skip()

            if key == self.quit_key:
                self._play()
                break


if __name__ == "__main__":

    jk = Jukebox()
    jk.Run()
