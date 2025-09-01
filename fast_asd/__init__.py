"""
fast-asd: Optimized, production-ready implementation of active speaker detection.

This package provides both a standalone TalkNet implementation and a full
active speaker detection system with face tracking.
"""

# Import TalkNet components (always available)
try:
    from .talknet import demoTalkNet
    from .talknet.talkNet import talkNet
except ImportError:
    pass

# Import main ASD components (requires sieve)
try:
    from .main import (
        push_video_segments_to_object_detection,
        get_active_speakers,
        push_video_segments_to_talknet,
        process_speaker_detection_futures,
        fast_asd,
    )
    _SIEVE_AVAILABLE = True
except ImportError:
    # Sieve not available, create stub functions
    _SIEVE_AVAILABLE = False
    
    def push_video_segments_to_object_detection(*args, **kwargs):
        raise ImportError("sieve-python is required for object detection functionality. Install with: pip install fast-asd[sieve]")
    
    def get_active_speakers(*args, **kwargs):
        raise ImportError("sieve-python is required for active speaker functionality. Install with: pip install fast-asd[sieve]")
    
    def push_video_segments_to_talknet(*args, **kwargs):
        raise ImportError("sieve-python is required for TalkNet functionality. Install with: pip install fast-asd[sieve]")
    
    def process_speaker_detection_futures(*args, **kwargs):
        raise ImportError("sieve-python is required for speaker detection futures. Install with: pip install fast-asd[sieve]")
    
    def fast_asd(*args, **kwargs):
        raise ImportError("sieve-python is required for full ASD functionality. Install with: pip install fast-asd[sieve]")

# Import utilities (should work without sieve)
try:
    from .utils import (
        get_video_dimensions,
        get_video_length,
        create_video_segments,
    )
    from .custom_types import VideoSegment, Frame, Box
except ImportError:
    pass

# Import scene detection (requires sieve)
try:
    from .scene_detection import get_scene_boundaries
    _SCENE_DETECTION_AVAILABLE = True
except ImportError:
    _SCENE_DETECTION_AVAILABLE = False

__version__ = "0.1.0"

# Dynamic __all__ based on available imports
__all__ = [
    "get_video_dimensions", "get_video_length", "create_video_segments", 
    "VideoSegment", "Frame", "Box",
    "push_video_segments_to_object_detection",
    "get_active_speakers", 
    "push_video_segments_to_talknet",
    "process_speaker_detection_futures",
    "fast_asd",
]

if _SCENE_DETECTION_AVAILABLE:
    __all__.append("get_scene_boundaries")