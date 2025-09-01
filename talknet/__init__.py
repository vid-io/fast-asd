"""
TalkNet: Standalone implementation of active speaker detection model.

This module contains the optimized TalkNet model implementation with improved
performance and support for variable frame-rate videos.
"""

from .main import *
from .talkNet import *
from .demoTalkNet import *

__all__ = ["TalkNet", "demoTalkNet"]