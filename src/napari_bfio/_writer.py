"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/stable/plugins/guides.html?#writers

Replace code below according to your needs.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Sequence, Tuple, Union
from bfio import BioReader, BioWriter
import numpy as np

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def write_single_image(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single image layer"""
    if meta["rgb"]:
        BioWriter.logger.info("The BioWriter cannot write color images.")
        return None

    bw = BioWriter(path)
    bw.shape = data.shape
    bw.dtype = data.dtype

    data = np.transpose(data, tuple(reversed(range(data.ndim))))

    while data.ndim < 5:
        data = data[..., np.newaxis]

    bw[:] = data

    return [path]


def write_multiple(path: str, data: List[FullLayerData]) -> List[str]:
    """Writes multiple layers of different types."""

    # implement your writer logic here ...

    # return path to any file(s) that were successfully written
    return [path]
