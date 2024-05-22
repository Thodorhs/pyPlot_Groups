import matplotlib.pyplot as plt
import numpy as np
import config

# Function to parse the data from the file
def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            if key == 'y_l':
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
    groups.remove('y_label')
    groups.remove('x_label')

    n_groups = len(groups)
    index = np.arange(n_groups) * (1 + config.group_spacing_factor)  # Adjust the index array for spacing
    fig, ax = plt.subplots(figsize=config.quartfigsize)
    part_names = ['MINOR_GC', 'MAJOR_GC', 'OTHER']

    for group_index, group in enumerate(groups):
        
        local_bottom = 0
        nvmeOF_bottom = 0

        for i, part_name in enumerate(part_names):
            local_value = data[group]['local'][part_name]
            nvmeOF_value = data[group]['nvmeOF'][part_name]

            plt.bar(index[group_index], local_value, config.bar_width, bottom=local_bottom, color=config.colors[i], edgecolor=config.edgecolor, linewidth=config.linewidth_2)
            plt.bar(index[group_index] + config.bar_width, nvmeOF_value, config.bar_width, bottom=nvmeOF_bottom, color=config.colors[i], edgecolor=config.edgecolor, linewidth=config.linewidth_2)

            local_bottom += local_value
            nvmeOF_bottom += nvmeOF_value

        # Add labels below each bar
        plt.text(index[group_index], config.bar_names_loc, 'L', ha='center', fontsize=config.fontsize-3)
        plt.text(index[group_index] + config.bar_width, config.bar_names_loc, 'R', ha='center', fontsize=config.fontsize-3)
    
    plt.xlabel(data['x_label'], fontsize=config.fontsize)
    plt.ylabel(data['y_label'] + " (min)", fontsize=config.fontsize)
    #plt.title(data['title'], fontsize=config.fontsize)
    plt.xticks(index + config.bar_width / 2 , groups, fontsize=config.fontsize, rotation=0)
    plt.yticks(fontsize=config.fontsize)

    # Adjust the position of the workload names (group names)
    ax.set_xticks(index + config.bar_width / 2)
    ax.set_xticklabels(groups, fontsize=config.fontsize,rotation=40)
    for tick in ax.get_xticklabels():
        tick.set_y(config.workload_name_pos)  # Lower the position of the workload names


    # Add legend
    #legend_elements = [plt.Rectangle((0, 0), 1, 1, color=config.colors[i], edgecolor='w') for i, part_name in enumerate(part_names)]
    #ax.legend(legend_elements, part_names, fontsize=config.fontsize, loc='upper center', bbox_to_anchor=config.bbox_to_anchor, ncol=len(part_names), handleheight=1, handlelength=1, labelspacing=-50)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)  # Adjust bottom margin to add space for x-axis labels
    plt.savefig('plot.eps',bbox_inches='tight', dpi=config.dpi,format='eps')

def main(filename):
    data = parse_data(filename)
    plot_data(data)

if __name__ == "__main__":
    main('data.txt')
