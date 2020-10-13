---
jupyter:
  jupytext:
    formats: notebooks///ipynb,scripts///py:percent,markdown///md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

## Circles


Here's a normal markdown cell.


Try and see what `print()` does:

```python
print('sdafdasf sdfsdafsd sdafsdafsd')
```

```python
x = 44
y = 55
x + y
```

```html
<svg width="500" height="150">
    <circle cx="50" cy="40" r="40" fill="PaleGreen"/>
    <circle cx="100" cy="40" r="40" fill="SpringGreen"/>
    <circle cx="150" cy="40" r="40" fill="MediumSeaGreen"/>
    <circle cx="250" cy="80" r="40" fill="LightSkyBlue"/>
    <circle cx="200" cy="80" r="40" fill="DodgerBlue"/>
</svg>
```

<!-- #region -->
normal md text

```python
my_var = 45 + 32
#comment within inline bit
```
more normal markdown text

> blockquote thindsknfsafsdf
<!-- #endregion -->


!!! info
    asdfasdfdasfsdafasdfasdf

```python
2 + 2
```

<!-- #region -->
inline code in md cell with python after dashes and then code block indented:
```python
    import time as t
    dd = 'the best'
```

followed by a blockquote:

> try this out

followed by an indented blockquote:

    > more of the same
<!-- #endregion -->

```python
import pandas as pd
```

```python
df = pd.read_csv('lightings.csv')
```

```python
df.head()
```

```python

```
