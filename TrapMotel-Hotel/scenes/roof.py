#ROOF LEVEL (sscenes/roof.py)

import math
import random
import pygame
#from core.scene immport Scene
#from entities.player import Player
#from entities.interactable import Interactable
#from systems.raycaster import render_world
#from settings import (W,H, WHITE, GRAY, YELLOW, RROOF_TIME, CLUES_NEEDED, WRONG_COMBO_PENALTY)
#from ui.text import draw_text, draw_wrapped

#posters
LORE = (#[PLACEHOLDER]poster1: dangers of second-hand boofing
    )
    
RANDOM = (#[PLACEHOLDER]random stuff
    )

#one of these is the correct door to open, these appear on the poster
DOOR_METHODS = [
    "[PLACEHOLDER] door method A",
    "[PLACEHOLDER] door method B",
    "[PLACEHOLDER] door method C",
    "[PLACEHOLDER] door method D"
]

#pigeon lady crackhead riddles
RIDDLES = [
    (#"Pigeon lady riddle 1")
        #riddle 1 answer,
    (#"Riddle 2")
        #riddle 2 answer
]

#correct poster
DOOR_POSTER_TEXT = #"[PLACEHOLDER] MAINTENANCE NOTICE: {method}"
DOOR_POSTER_LABEL = #"Poster: {method}"

#short messages shwon during gameplay
MSG_DOOR_LOCKED = "Locked. You need at least {n} clues to try a combo!"
MSG_WRONG_COMBO = "Door won't budge, TRY AGAIN Tiny -{s} seconds"
MSG_PIGEON_REPLY = "The pigeon lady tilts her head and coos"
MSG_TIME_UP = "Time is NIEN!" #wakes up on the roof
MSG_SUCCESS = "Open SASHIMI!"

#roof structure
MAP = []

#POV visuals ( swap for images whem art is ready)
#TODO: add an "image" entry per thing, for example: "poster": {..., "image": "assets/images/poster.png"}
LOOK = {
    "poster": {"color": (255, 210, 80), "w": 0.5, "h": 0.5, "z": 0.3},
    "pigeon": {"color": (150, 90, 200), "w": 0.4, "h": 0.8, "z": 0.0},
    "door": {"color": (130, 80, 40), "w": 0.8, "h": 1.0, "z": 0.0},
}

#the correct answers
SOLUTION = {"poster_correct", "riddle_correct"}

#game logic

def parse_map(rows):
    #"""Read the MAP and return a dict of where everything is.
    #Positions are (x, y) in tile units, centered in the tile."""
    width = len(rows[0])
    for y, row in enumerate(rows):
        if len(row) != width:
            raise ValueError(f"MAP row {y} has length {len(row)}, expected {width}. "
                             "Every row must be the same length.")


    found = {}
    for y, row in enumerate(rows) :
        for x, ch in enumerate(row):
            if ch in "SBD1234":
                foud.setdefualt(ch, []).append(x + 0.5, y + 0.5))

    for ch in "SBD1234":
        count = len(found.get(ch, []))
        if count != 1: 
            raise ValueError(f"MAP must contain one '{ch}' (found {count}).")
    return {ch: spots[0] for ch, spots in found.items()}

