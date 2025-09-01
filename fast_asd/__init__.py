"""
fast-asd: Optimized, production-ready implementation of active speaker detection.

This package provides both a standalone TalkNet implementation and a full
active speaker detection system with face tracking.
"""

from .main import (
    push_video_segments_to_object_detection,
    get_active_speakers,
    push_video_segments_to_talknet,
    process_speaker_detection_futures,
    fast_asd,
)
from .utils import (
    get_video_dimensions,
    get_video_length,
    create_video_segments,
)
from .custom_types import VideoSegment, Frame, Box
from .scene_detection import get_scene_boundaries

__version__ = "0.1.0"
__all__ = [
    "push_video_segments_to_object_detection",
    "get_active_speakers", 
    "push_video_segments_to_talknet",
    "process_speaker_detection_futures",
    "fast_asd",
    "get_video_dimensions",
    "get_video_length", 
    "create_video_segments",
    "VideoSegment",
    "Frame",
    "Box",
    "get_scene_boundaries",
]