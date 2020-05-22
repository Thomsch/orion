"""
Plotting public API.
Authors of third-party plotting backends should implement a module with a
public ``plot(data, kind, **kwargs)``. The parameter `data` will contain
the data structure and can be a `ExperimentClient`. For example,
for ``ec.plot()`` the parameter `data` will contain the ExperimentClient `ec`.

The parameter `kind` will be one of:
- learning
"""

from orion.plotting._core import (PlotAccessor, learning)

__all__ = ["PlotAccessor", "learning"]