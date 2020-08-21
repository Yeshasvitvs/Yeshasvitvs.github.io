"""
A python script to plot skills on a radar plot

Author: Yeshasvi Tirupachuri
Email: yeshasvitvs@gmail.com

"""

#######################################################################
## TODO: Make dependencies automatic installation
## TODO: Add arguments for options e.g. languages, technologies, theory
## TODO: Add argument for sending a CSV file
#######################################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi

# Create a color palette
color = plt.cm.get_cmap("Set3", 20)

def adjust_xticks(ax):
    for theta, xlabel in zip(ax.get_xticks(), ax.get_xticklabels()):
        theta = theta * ax.get_theta_direction() + ax.get_theta_offset()
        theta = np.pi / 2 - theta
        y, x = np.cos(theta), np.sin(theta)
        if x >= 0.1:
            xlabel.set_horizontalalignment('left')
        if x <= -0.1:
            xlabel.set_horizontalalignment('right')
        if y >= 0.5:
            xlabel.set_verticalalignment('bottom')
        if y <= -0.5:
            xlabel.set_verticalalignment('top')

def adjust_yticks(ax):
    for ytick, ylabel in zip(ax.get_yticks(), ax.get_yticklabels()):
        ylabel.set_position((10, 0))

def plot_radar(title, size, linewidth, titlesize):

    # Get language categories
    language_catergories = list(languages_df)[1:]
    nLanguages = len(language_catergories)

    # Divide plot for categories
    angles = [n / float(nLanguages) * 2 * pi for n in range(nLanguages)]
    angles += angles[:1]

    # Initialize figure
    dpi = 96
    plt.figure(figsize=(1500 / dpi, 1500 / dpi), dpi=dpi)

    # Initialise the radar plot
    ax = plt.subplot(111, polar=True, frameon=False)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], language_catergories, color="grey", size=size)
    adjust_xticks(ax)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5, 6], ["A1", "A2", "B1", "B2", "C1", "C2"], color="grey", alpha=0.9, size=size)
    plt.ylim(0, 6)
    adjust_yticks(ax)

    # Plot International Languages
    values = languages_df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]

    ax.plot(angles, values, color=color(0), alpha=0.85, linewidth=linewidth, linestyle='solid', label="International")
    ax.fill(angles, values, color=color(0), alpha=0.15)

    # Plot Indian Languages
    values = languages_df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color(8), alpha=0.85, linewidth=linewidth, linestyle='solid', label="Indian")
    ax.fill(angles, values, color=color(8), alpha=0.15)

    # Add title
    plt.title(title, loc='center', size=titlesize, y=-0.1, alpha=0.7)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=size)
    plt.show()

# General variables
linewidth = 2.5
fontsize  = 20
titlesize = 20

# Languages dataframe
# Language skill category
# [ A1 - 1, A2 - 2, B1 - 3, B2 - 4, C1- 5, C2 - 6]
languages_df = pd.DataFrame({
    'group': ['International', 'Indian'],
    'English': [6, 0],
    'Italian': [2, 0],
    'French': [1, 0],
    'Spanish': [1, 0],
    'Telugu': [0, 6],
    'Hindi': [0, 4],
    'Tamil': [0, 2]
})

# Create Languages plot
plot_radar("Language Skills", fontsize, linewidth, titlesize)