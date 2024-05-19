# pyPlot_Groups
Python scrypt to bar plot 2 groups and break each bar to 3 parts.

## Example Plot

![Example Plot](https://raw.githubusercontent.com/Thodorhs/pyPlot_Groups/main/plot.png)

## Overview

This script is designed to read data from a file, parse it, and generate a bar plot. Each group in the dataset will have two bars: one for `local` and one for `nvmeOF`. Each bar is visually broken down by `MINOR_GC`, `MAJOR_GC`, and `OTHER` parts. The script automatically converts times from seconds to minutes for readability.

## Script Configuration

- `figsize`: Size of the figure.
- `fontsize`: Font size used in the plot.
- `linewidth`: Width of the lines.
- `edgewidth`: Width of the bar edges.
- `edgecolor`: Color of the bar edges.
- `bar_width`: Width of the bars.
- `workload_name_pos`: Position adjustment for workload names.
- `bbox_to_anchor`: Position of the legend.
- `bar_names_loc`: Position of the bar labels (`local`, `nvmeOF`).
- `colors`: Black and white color palette for the parts of the bars.

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

1. **Prepare your `data.txt` file** following the format described above.

2. **Run the script**: ```python3 plot_data.py ```

3. The plot will be saved as `plot.png` in the same directory.


