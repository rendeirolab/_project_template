from pathlib import Path
import typing as tp
from functools import partial

import matplotlib.pyplot as plt
import scanpy as sc


# Make matplotlib use Arial font by default
# plt.rcParams["backend"] = "QtAgg"
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["text.usetex"] = False
plt.rcParams["figure.max_open_warning"] = 1000


# Make scanpy plotting functions return the figure
for func in ["embedding", "pca", "umap", "diffmap", "draw_graph"]:
    f = partial(getattr(sc.pl, func), show=False, return_fig=True)
    setattr(sc.pl, func, f)


class FigKws(tp.TypedDict):
    bbox_inches: str
    dpi: int


class config:
    metadata_dir = Path("metadata")
    data_dir = Path("data") / "gtex"
    results_dir = Path("results") / "gtex"
    figkws: FigKws = dict(bbox_inches="tight", dpi=300)
