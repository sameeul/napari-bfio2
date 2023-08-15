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
import ome_types

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def write_single_image(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single image layer"""
    # need to check if we need to run in a seperate thread to stop GUI from freezing
    
    if ("metadata" in meta): # if this image is loaded via bfio BioReader
        ome_data = ome_types.model.OME(**meta["metadata"])
        with BioWriter(path, metadata=ome_data) as bw:
            while data.ndim < 5:
                data = data[..., np.newaxis]

            bw[:] = data

        return [path]
    else:
        if meta["rgb"]:
            BioWriter.logger.info("The BioWriter cannot write color images.")
            return None



def write_multiple(path: str, data: List[FullLayerData]) -> List[str]:
    """Writes multiple layers of different types."""

    # implement your writer logic here ...
    BioWriter.logger.info("Bfio: Multi-file writing not yet supported.")
    return None
    # return path to any file(s) that were successfully written
    # return [path]
