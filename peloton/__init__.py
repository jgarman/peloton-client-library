#! /usr/bin/env python3.6
# -*- coding: latin-1 -*-

from .peloton import NotLoaded
from .peloton import PelotonException
from .peloton import PelotonAPI
from .peloton import PelotonUser
from .peloton import PelotonWorkout
from .peloton import PelotonRide
from .peloton import PelotonMetric
from .peloton import PelotonInstructor
from .peloton import PelotonWorkoutSegment
from .peloton import PelotonWorkoutFactory

from .peloton import follow_user, get_followers, get_following, approve_user, change_user

_ALL_ = [
    "NotLoaded",
    "PelotonException",
    "PelotonAPI",

    "PelotonUser",
    "PelotonWorkout",
    "PelotonRide",
    "PelotonMetric",
    "PelotonInstructor",
    "PelotonWorkoutSegment",

    "PelotonWorkoutFactory",

    "follow_user",
    "get_followers",
    "get_following",
    "approve_user",
    "change_user"
]