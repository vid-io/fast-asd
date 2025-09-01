"""
TalkNet: Standalone implementation of active speaker detection model.

This module contains the optimized TalkNet model implementation with improved
performance and support for variable frame-rate videos.
"""

from . import demoTalkNet
from .talkNet import talkNet

__all__ = ['demoTalkNet', 'talkNet']