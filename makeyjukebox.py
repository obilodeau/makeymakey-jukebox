#!/usr/bin/env python3

import time

import dbus
from dbus.mainloop.glib import DBusGMainLoop
import pympris

class Jukebox(object):

    def __init__(self):

        # internal constants
        self.jitter = 1

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
            time.sleep(self.jitter)

if __name__ == "__main__":

    jk = Jukebox()
    jk.Run()
