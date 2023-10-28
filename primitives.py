import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.stretch'] = 'condensed'
plt.rcParams['figure.figsize'] = [10.0, 8.0]
plt.rcParams['figure.dpi'] = 150
size = {'line_height': 0.045, 'font_size': 10, 'va': 'bottom', 'ha': 'left', 'line_height_shift': 0.03, 'char_width': 0.01}


def table(ax, x, y, name, columns):
    global size
    columns = [name] + columns
    width = size['char_width'] * max([len(col) for col in columns])
    height = size['line_height_shift'] + size['line_height'] * len(columns)
    ax.add_patch(Rectangle((x, y), width, height, edgecolor='grey', fill=False, lw=1))
    ax.add_patch(Rectangle((x + 1, y + height - size['line_height'] * 1.2 - 1.0), width - 2.0, size['line_height'] * 1.2 - 2.0, edgecolor='grey', fill='blue', lw=1))
    for ind, textline in enumerate(columns):
        ax.text(x + size['line_height']/6, y + height - size['line_height'] * (ind + 1), textline, ha=size['ha'], va=size['va'], size=size['font_size'])
    return ax


fig, ax = plt.subplots()
ax = table(ax, 0.1, 0.1, 'AppsFlyer.main', ['Prikol', 'Prikol', 'Prikol', 'Prikol', 'dlcmdlvmflkvmfvfvf', ])
ax.axis("off")
plt.show()


