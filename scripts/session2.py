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

# %% [markdown] slideshow={"slide_type": "slide"}
# # SESSION 1
# ## Introduction to Pandas

# %% [markdown] slideshow={"slide_type": "slide"}
# [replit](https://repl.it)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### DataFrames
#
# #### loading data

# %% slideshow={"slide_type": "slide"}
weights = [12, 16, 20, 24, 28, 32]
sets = [1, 2, 3, 4, 5, 6]

import pandas as pd


# %%
df = pd.DataFrame([weights, sets])

# %%
df

# %% [markdown] slideshow={"slide_type": "notes"}
# Test out the notes ideas here
#
# - try this
# and more
#
# - sfdsdsd
#

# %% slideshow={"slide_type": "slide"}
df.head(1)

# %% [markdown]
# Here we see `.head()`

# %%
