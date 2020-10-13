# ---
# jupyter:
#   jupytext:
#     formats: notebooks///ipynb,scripts///py:percent,markdown///md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Circles

# %% [markdown]
# Here's a normal markdown cell.

# %% [markdown]
# Try and see what `print()` does:

# %%
print('sdafdasf sdfsdafsd sdafsdafsd')

# %%
x = 44
y = 55
x + y

# %% language="html"
# <svg width="500" height="150">
#     <circle cx="50" cy="40" r="40" fill="PaleGreen"/>
#     <circle cx="100" cy="40" r="40" fill="SpringGreen"/>
#     <circle cx="150" cy="40" r="40" fill="MediumSeaGreen"/>
#     <circle cx="250" cy="80" r="40" fill="LightSkyBlue"/>
#     <circle cx="200" cy="80" r="40" fill="DodgerBlue"/>
# </svg>

# %% [markdown]
# normal md text
#
# ```python
# my_var = 45 + 32
# #comment within inline bit
# ```
# more normal markdown text
#
# > blockquote thindsknfsafsdf

# %% [markdown]
#
# !!! info
#     asdfasdfdasfsdafasdfasdf

# %%
2 + 2

# %% [markdown]
# inline code in md cell with python after dashes and then code block indented:
# ```python
#     import time as t
#     dd = 'the best'
# ```
#
# followed by a blockquote:
#
# > try this out
#
# followed by an indented blockquote:
#
#     > more of the same

# %%
import pandas as pd

# %%
df = pd.read_csv('lightings.csv')

# %%
df.head()

# %%
