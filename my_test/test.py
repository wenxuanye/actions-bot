import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def draw_pic():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    # save the figure
    plt.savefig('sin.png')
draw_pic()