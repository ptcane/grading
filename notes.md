Open the command shell by pressing Cmd+Shift+S on MacOS or Ctrl+Shift+S on other computers. Note that this is different from the Python output pane that's open by default. The command shell will open up below the Python one, as shown below.




jupyter nbconvert slides/notebook.ipynb --to slides --SlidesExporter.reveal_theme=white --output slides.html

mkdocs serve -a 0.0.0.0:8080


jupytext --sync notebooks/*.ipynb