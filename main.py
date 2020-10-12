bashCommand = "git pull origin master && jupytext --sync notebooks/*.ipynb && pytest && git add -A && git commit --allow-empty -m 'update' && git push origin master"
import os
os.system(bashCommand)
