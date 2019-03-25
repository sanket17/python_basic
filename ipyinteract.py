# create a slider

from ipywidgets import interact, interactive, fixed
import iypwidgets as widgets

def func(x):
    return x

interact(func, x=10)