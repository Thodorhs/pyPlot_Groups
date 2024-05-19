import matplotlib.pyplot as plt
import numpy as np

# Configuration settings
figsize = (17, 8.5)  # Adjust the figure size to be more balanced
fontsize = 12 # Adjusted the font size for better readability
linewidth = 3 # Adjusted the line width for better visibility
edgewidth = 1.2 # Adjusted the edge width for better visibility
edgecolor = 'k'
bar_width = 0.45  # Adjusted bar width for better spacing
workload_name_pos = -0.03  # Lower the position of the workload names
bbox_to_anchor=(0.5, -0.15) # Adjusted the position of the legend
bar_names_loc = -8.4  # Adjusted the position of the bar names
colors = ['#444444', '#888888', '#cccccc']  # Adjusted to three colors Black and white color palette

# Function to parse the data from the file
def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = {}
    for line in lines:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            if key == 'title':
                data['title'] = value
            elif key == 'y_l':
                data['y_label'] = value
            elif key == 'x_l':
                data['x_label'] = value
            elif key.startswith('group'):
                current_group = value
                data[current_group] = {'local': {}, 'nvmeOF': {}}
            elif key.startswith('part'):
                part_name = {
                    'part1': 'TOTAL_TIME',
                    'part2': 'MINOR_GC',
                    'part3': 'MAJOR_GC',
                    'part4': 'OTHER'
                }[key]
                local, nvmeOF = map(float, value.split(';'))
                data[current_group]['local'][part_name] = local / 60  # Convert to minutes
                data[current_group]['nvmeOF'][part_name] = nvmeOF / 60  # Convert to minutes
    return data

def plot_data(data):
    groups = list(data.keys())
    groups.remove('title')
    groups.remove('y_label')
    groups.remove('x_label')
    
    n_groups = len(groups)
    index = np.arange(n_groups)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    part_names = ['MINOR_GC', 'MAJOR_GC', 'OTHER']

    for group_index, group in enumerate(groups):
        
        local_bottom = 0
        nvmeOF_bottom = 0

        for i, part_name in enumerate(part_names):
            local_value = data[group]['local'][part_name]
            nvmeOF_value = data[group]['nvmeOF'][part_name]

            plt.bar(group_index, local_value, bar_width, bottom=local_bottom, color=colors[i], edgecolor=edgecolor, linewidth=edgewidth)
            plt.bar(group_index + bar_width, nvmeOF_value, bar_width, bottom=nvmeOF_bottom, color=colors[i], edgecolor=edgecolor, linewidth=edgewidth)

            local_bottom += local_value
            nvmeOF_bottom += nvmeOF_value

        # Add labels below each bar
        plt.text(group_index, bar_names_loc, 'local', ha='center', fontsize=fontsize)
        plt.text(group_index + bar_width, bar_names_loc, 'nvmeOF', ha='center', fontsize=fontsize)
    
    plt.xlabel(data['x_label'], fontsize=fontsize, fontweight='bold')  
    plt.ylabel(data['y_label'] + " (minutes)", fontsize=fontsize, fontweight='bold')  
    plt.title(data['title'], fontsize=fontsize, fontweight='bold')  
    plt.xticks(index + bar_width / 2, groups, fontsize=fontsize, rotation=0) 
    plt.yticks(fontsize=fontsize)
    
    # Adjust the position of the workload names (group names)
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(groups, fontsize=fontsize)
    for tick in ax.get_xticklabels():
        tick.set_y(workload_name_pos)  # Lower the position of the workload names

    # Add legend
    legend_elements = [plt.Rectangle((0, 0), 1, 1, color=colors[i], edgecolor='w') for i, part_name in enumerate(part_names)]
    ax.legend(legend_elements, part_names, fontsize=fontsize, loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=len(part_names))  # Lowered the legend

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)  # Adjust bottom margin to add space for x-axis labels
    plt.savefig('plot.png') 


def main(filename):
    data = parse_data(filename)
    plot_data(data)

if __name__ == "__main__":
    main('data.txt')
