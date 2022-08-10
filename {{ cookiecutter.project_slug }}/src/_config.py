#!/usr/bin/env python

"""A module to provide the boilerplate needed for all the analysis."""

import typing as tp

import numpy as np  # type: ignore[import]
import pandas as pd  # type: ignore[import]
import matplotlib  # type: ignore[import]
import matplotlib.pyplot as plt  # type: ignore[import]
import seaborn as sns  # type: ignore[import]

from src.types import Path, Array, DataFrame  # type: ignore[import]


class Config:
    """A class to hold constants used throughout the project. To be filled in at the start of each project."""

    # simple constants
    figkws: tp.Final[dict] = dict(
        dpi=300, bbox_inches="tight", pad_inches=0, transparent=False
    )

    # directories
    metadata_dir: tp.Final[Path] = Path("metadata")
    data_dir: tp.Final[Path] = Path("data")
    processed_dir: tp.Final[Path] = Path("processed")
    results_dir: tp.Final[Path] = Path("results")

    # major attributes to contrast when comparing sample groups
    attributes: tp.Final[list[str]] = []
    sample_attributes: DataFrame

    # definition of categorical or numeric
    categorical_attributes: list[str] = []
    numerical_attributes: list[str] = []

    # order of categorical attributes
    categorical_order: tp.Final[dict[str, list]] = dict(
        cat1=["val1", "val2"],
        cat2=["val1", "val2"],
    )

    # consistent color codes for categorical variables to be used throughout the project
    colors: tp.Final[dict[str, Array]] = dict(
        cat1=np.asarray(sns.color_palette())[[2, 0, 1, 3]],
        cat2=np.asarray(sns.color_palette())[[2, 0, 1, 5, 4, 3]],
    )
    # consistent colormaps for numeric variables to be used throughout the project
    cmaps: tp.Final[dict[str, str]] = dict(cont1="viridis")

    # input file paths
    metadata_file: tp.Final[Path] = metadata_dir / "samples.csv"
    clinical_file: tp.Final[Path] = metadata_dir / "clinical_annotation.csv"

    # output file paths
    ...
