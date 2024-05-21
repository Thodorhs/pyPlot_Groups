# pyPlot_Groups
Python scrypt to bar plot groups (each group with 2 bars one for local and one for nvmeOF) and break each bar to 3 parts.

## Example Plot

![Example Plot](https://raw.githubusercontent.com/Thodorhs/pyPlot_Groups/main/plot.png)

## Overview

This script is designed to read data from a file, parse it, and generate a bar plot. Each group in the dataset will have two bars: one for `local` and one for `nvmeOF`. Each bar is visually broken down by `MINOR_GC`, `MAJOR_GC`, and `OTHER` parts. The script automatically converts times from seconds to minutes for readability.

## Script Configuration

- `fullfigsize = (13, 2)`: Full figure size, setting the figure to be 13 inches wide and 2 inches tall.
- `halffigsize = (7, 3)`: Half figure size, setting the figure to be 7 inches wide and 3 inches tall.
- `thirdfigsize = (5, 3)`: One third figure size, setting the figure to be 5 inches wide and 3 inches tall.
- `quartfigsize = (3.25, 3)`: One fourth figure size, setting the figure to be 3.25 inches wide and 3 inches tall.
- `eightfigsize = (1.625, 1.6)`: One eighth figure size, setting the figure to be 1.625 inches wide and 1.6 inches tall.
- `fontsize = 12`: Font size used for text elements in the plot.
- `linewidth = 3`: Width of the main lines in the plot, set to 3 points wide.
- `linewidth_2 = 0.6`: Secondary line width for different lines in the plot, set to 0.6 points wide.
- `edgewidth = 1.2`: Width of the edges of bars or other shapes, set to 1.2 points wide.
- `edgecolor = 'k'`: Color of the edges of bars or other shapes, set to black (`'k'`).
- `markersize = 12`: Size of the markers in the plot, set to 12 points.
- `dpi=450`        : Quality of the plot (Dots Per Inches).
- `bar_width = 0.5`: Width of the bars in a bar plot, set to 0.5 units wide.
- `workload_name_pos = -0.05`: Position adjustment for workload names, moving them slightly downward by 0.05 units.
- `bbox_to_anchor = (0.12, -0.2)`: Position of the legend, placing it at the coordinates (0.12, -0.2) relative to the axes.
- `bar_names_loc = -22`: Position adjustment for bar labels such as `local` and `nvmeOF`, moving them to the position -22.
- `colors = ['#444444', '#888888', '#cccccc']`: Black and white color palette for the parts of the bars, using shades of gray.
- `group_spacing_factor = 0.5`: Factor to control the spacing between groups in a grouped bar plot, set to 0.5 units.


## Data File (`data.txt`)

The data file should contain information about the plot in a specific format. Below is a sample `data.txt` file and its explanation:

```
title=Performance Comparison
x_l=Workloads
y_l=Time
group1=Workload A
part1=600;800
part2=200;300
part3=100;150
part4=300;350
group2=Workload B
part1=500;700
part2=150;250
part3=100;100
part4=250;350
```

### Explanation

- `title`: Title of the plot.
- `x_l`: Label for the x-axis.
- `y_l`: Label for the y-axis.
- `groupN`: Name of the workload or group, where `N` is a number starting from 1.
- `part1`: `TOTAL_TIME` values in seconds for `local` and `nvmeOF`, separated by a semicolon.
- `part2`: `MINOR_GC` values in seconds for `local` and `nvmeOF`, separated by a semicolon.
- `part3`: `MAJOR_GC` values in seconds for `local` and `nvmeOF`, separated by a semicolon.
- `part4`: `OTHER` values in seconds for `local` and `nvmeOF`, separated by a semicolon.

The script will convert these values from seconds to minutes before plotting.

## Usage

1. **Prepare your `data.txt` file** following the format described above. (you can optionaly chose diferent configuration from the `config.py`).

2. **Run the script**: ```python3 plot_data.py ```

3. The plot will be saved as `plot.png` in the same directory.


