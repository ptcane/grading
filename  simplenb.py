# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb, /py:percent
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

# %% [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/ptcane/grading/blob/master/notebooks/simplenb.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %% id="JkRiEKN9ssXc"
x = 44

# %% id="rI1kaTgFssXf"
z = 23
a = 3
chief = "martin"

# %% id="qsEeoUiTssXh" outputId="9460f762-6ebf-43a4-9f6f-50fc89bd6465"
print(x + z + a)


# %% id="FgqQJJfVssXk"
import pandas as pd

# %% id="PCsNp2TFs8a8"
df = pd.DataFrame({"member":['dave', 'alan'], 'age': [23, 65]})

# %% id="TQRzViQ0t0t8" outputId="d890e50e-74c3-4d11-84c0-bb0bdddb7555" colab={"base_uri": "https://localhost:8080/", "height": 111}
df

# %% id="qPqCr2P3t6J2"
