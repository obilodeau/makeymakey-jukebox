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

        # MPRIS dependencies
        self.dbus_loop = DBusGMainLoop()
        self.bus = dbus.SessionBus(mainloop=self.dbus_loop)

        # get a media player handle
        self.players_ids = list(pympris.available_players())
        self.mp = pympris.MediaPlayer(self.players_ids[0], self.bus)

    def _play(self):
        if self.mp.player.CanPlay and self.mp.player.CanPause:
                self.mp.player.PlayPause()

    def Run(self):
        self._play()
        while True:

            # grab key events (blocking)
            key = getch()
            if key == self.makey_key:
                # TODO: change for skip
                self._play()


if __name__ == "__main__":

    jk = Jukebox()
    jk.Run()
