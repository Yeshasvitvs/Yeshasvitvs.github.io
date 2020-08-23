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

def plot_radar(df, title, size, linewidth, titlesize,  ytickslen, yticks, colors=''):

    # Get language categories
    catergories = list(df)[1:]
    N = len(catergories)

    # Get labels
    labels = df['group'].tolist()

    # Divide plot for categories
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialize figure
    dpi = 96
    plt.figure(figsize=(1700 / dpi, 1700 / dpi), dpi=dpi)

    # Initialise the radar plot
    ax = plt.subplot(111, polar=True, frameon=False)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], catergories, color="grey", size=size[0])
    adjust_xticks(ax)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([*range(1, ytickslen+1, 1)], yticks, color="grey", alpha=0.9, size=size[1])
    plt.ylim(0, ytickslen)
    adjust_yticks(ax)

    for i in range(len(df)):

        values = df.loc[i].drop('group').values.flatten().tolist()
        values += values[:1]

        ax.plot(angles, values, color=colors[i], alpha=0.75, linewidth=linewidth, linestyle='solid', label=labels[i])
        ax.fill(angles, values, color=colors[i], alpha=0.2)

    if len(df) > 1:
        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=size[0])

    # Add title
    plt.title(title, loc='center', size=titlesize, y=-0.1, alpha=0.7)


    plt.show()

# General variables
linewidth = 2.5
fontsize  = [20, 20]
titlesize = 20

# Languages dataframe
# [ A1 - 1, A2 - 2, B1 - 3, B2 - 4, C1- 5, C2 - 6]
languages_df = pd.DataFrame({
    'group':   ['International', 'Indian'],
    'English': [6, 0],
    'Italian': [2, 0],
    'French':  [1, 0],
    'Spanish': [1, 0],
    'Telugu':  [0, 6],
    'Hindi':   [0, 4],
    'Tamil':   [0, 2]
})

ytickslen = 6
yticks    = ["A1", "A2", "B1", "B2", "C1", "C2"]

# Create Languages plot
plot_radar(languages_df, "Language Skills", fontsize, linewidth, titlesize, ytickslen, yticks, colors=[color(0), color(8)])

# Technologies dataframe
# Reference: https://hr.nih.gov/working-nih/competencies/competencies-proficiency-scale
# [ Fundamental Awareness - 1,
#  Novice - 2,
#  Intermediate - 3,
#  Advanced - 4,
#  Expert- 5]
technologies_df = pd.DataFrame({
    'group':      ['Programming', 'OS/Middleware', 'Tools'],
    'C++':        [3, 0, 0],
    'Matlab':     [3, 0, 0],
    'Python':     [2, 0, 0],
    'HTML':       [1, 0, 0],
    'ROS':        [0, 4, 0],
    'YARP':       [0, 4, 0],
    'Ubuntu':     [0, 3, 0],
    'Git/Github': [0, 0, 4],
    'Gazebo':     [0, 0, 4],
    'QtCreator':  [0, 0, 3],
    'Simulink':   [0, 0, 3],
    'Latex':      [0, 0, 3],
    'PyCharm':    [0, 0, 2],
    'Lightroom':  [0, 0, 4],
})

ytickslen = 5
yticks    = ["Fundamental", "Novice", "Intermediate", "Advanced", "Expert"]
fontsize  = [20, 12]

# Create Technologies plot
plot_radar(technologies_df, "Technical Skills", fontsize, linewidth, titlesize, ytickslen, yticks, colors=[color(5), color(10), color(15)])

# Theory dataframe
# Reference: https://hr.nih.gov/working-nih/competencies/competencies-proficiency-scale
# [ Fundamental Awareness - 1,
#  Novice - 2,
#  Intermediate - 3,
#  Advanced - 4,
#  Expert- 5]
theory_df = pd.DataFrame({
    'group':                       ['Theory'],
    'Robotics':                    [4],
    'Software Engineering':        [3],
    # 'Data Structures & Algorithms':[2],
    # 'Object Oriented Programming': [3],
    'Control Theory':              [3],
    'Machine Learning':            [2],
    'Optimization':                [2],
})

ytickslen = 5
yticks = ["Fundamental", "Novice", "Intermediate", "Advanced", "Expert"]

# Create Technologies plot
plot_radar(theory_df, "Theoretical Skills", fontsize, linewidth, titlesize, ytickslen, yticks, colors=[color(17)])