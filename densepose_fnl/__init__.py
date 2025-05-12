"""
DensePose Fast and Light - A lightweight implementation of DensePose

This package contains the implementation of the paper "Making DensePose fast and light"
"""

__version__ = "0.1.0"

# Import main components to make them available at the package level
from densepose_fnl.fpn import BiFPN
from densepose_fnl.backbone import build_timm_backbone, build_timm_bifpn_backbone
from densepose_fnl.roi_heads import MyDensePoseROIHeads