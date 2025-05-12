# ace-tools-lite

A lightweight Python package that provides a drop-in replacement for `ace_tools.display_dataframe_to_user` 
and related utilities — making it easier to follow ChatGPT guidance involving `ace_tools` 
without changing your code or prompts.

## ✨ Purpose

If you've ever been advised by ChatGPT to use:

```
from ace_tools import display_dataframe_to_user
```

…but ran into an error because `ace_tools` doesn't exist in your environment — this package is for you.

**`ace-tools-lite`** is a minimal implementation of the most commonly referenced `ace_tools` functions used in AI-assisted workflows. It aims to make advice from ChatGPT and similar models easier to use **out of the box**, with no prompt rewrites or function renaming required.

## ✅ Features

- `display_dataframe_to_user(name, dataframe)`  
  Renders DataFrames natively in Jupyter or in the terminal, just like `display()` or `print()` — no unnecessary styling.

- `display_chart_to_user(title=None)`  
  Shows the current matplotlib figure with an optional title.

- `display_matplotlib_image_to_user(fig=None)`  
  Displays a matplotlib `Figure` object, falling back gracefully in non-notebook environments.

- `log_exception(error)`  
  Logs exceptions using standard Python logging.

- `log_matplotlib_img_fallback(reason)`  
  Logs when an image fallback is triggered (e.g., outside Jupyter).

## 🌱 Environment-Friendly (and Non-GMO)

By using `ace-tools-lite`, you reduce redundant model queries and avoid re-prompting ChatGPT just to reword answers. That saves **compute power, electricity, and carbon emissions** — making this package a small, but meaningful, step toward sustainable AI usage.

## 📦 Installation

```
pip install ace-tools-lite
```

## 🔍 Example

```
from ace_tools import display_dataframe_to_user
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

display_dataframe_to_user("Student Scores", df)
```

This will render cleanly in both Jupyter and terminal environments.

## 🛠 Why This Exists

Many developers using AI coding assistants like ChatGPT encounter `ace_tools.display_dataframe_to_user` in code suggestions. Since `ace_tools` is not a public package, this library was created to provide a seamless alternative — so you can continue using AI-generated code **without modifying your prompt or scripts**.


## 📄 License

MIT License © 2025 Alex Zankevich
