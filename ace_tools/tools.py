# tools.py

import pandas as pd
import matplotlib.pyplot as plt
import logging

try:
    from IPython.display import display, HTML

    _in_notebook = True
except ImportError:
    _in_notebook = False


def display_dataframe_to_user(name: str, dataframe: pd.DataFrame):
    """Display a pandas DataFrame with a title."""
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame")

    if _in_notebook:
        display(HTML(f"<h3>{name}</h3>"))
        display(dataframe)
    else:
        print(f"\n{name}:\n")
        print(dataframe)


def display_chart_to_user(title: str = None):
    """Display the current matplotlib chart with optional title."""
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.show()


def display_matplotlib_image_to_user(fig=None):
    """Render a matplotlib figure."""
    if _in_notebook:
        if fig is None:
            fig = plt.gcf()
        display(fig)
    else:
        print("Matplotlib figure rendered (non-notebook mode).")


def log_exception(error: Exception):
    """Log an exception with traceback."""
    logging.exception("Exception caught:", exc_info=error)


def log_matplotlib_img_fallback(reason: str = "Unknown"):
    """Log a fallback when image rendering fails."""
    logging.warning(f"Matplotlib fallback triggered. Reason: {reason}")
