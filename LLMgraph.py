# import the necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dictionary to store the data
data = {
    'Model': ['xAI Grok', 'GPT-4o-mini', 'O1-mini', 'Claude 3 Haiku', 'Claude 3.5 Sonnet V1'],
    'V1 Math': [90, 100, 100, 80, 100],
    'V1 Reasoning': [80, 60, 80, 45, 80],
    'V1 Total': [85, 80, 90, 62.5, 90],
    'V2 Math': [100, 100, 100, 80, 100],
    'V2 Reasoning': [80, 50, 80, 45, 70],
    'V2 Total': [90, 75, 90, 62.5, 85],
    'V3 Math': [100, 100, 100, 80, 100],
    'V3 Reasoning': [80, 70, 70, 60, 90],
    'V3 Total': [90, 85, 85, 70, 95]
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# colors for qualitative set 2
qualitative_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# colors for each model
model_colors = {
    'xAI Grok': qualitative_colors[0],
    'GPT-4o-mini': qualitative_colors[1],
    'O1-mini': qualitative_colors[2],
    'Claude 3 Haiku': qualitative_colors[3],
    'Claude 3.5 Sonnet V1': qualitative_colors[4]
}

# create a figure and a set of subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# draw the bar chart for each version
for idx, version in enumerate(['V1', 'V2', 'V3']):
    ax = axes[idx]
    width = 0.2  # bar width
    x = range(len(['Math', 'Reasoning', 'Total']))  # Xlocations for the groups

    # set the gap between the groups
    gap = 0.5

    # draw the bars for each model
    for i, model in enumerate(df['Model']):
        # get the scores for the model
        math_score = df.loc[i, f'{version} Math']
        logical_score = df.loc[i, f'{version} Reasoning']
        total_score = df.loc[i, f'{version} Total']

        # draw the bars
        ax.bar(x[0] + width * i + gap * (x[0] // 1), math_score, width=width, 
               color=model_colors[model], label=model if x[0] == 0 else "")
        ax.bar(x[1] + width * i + gap * (x[1] // 1), logical_score, width=width, 
               color=model_colors[model])
        ax.bar(x[2] + width * i + gap * (x[2] // 1), total_score, width=width, 
               color=model_colors[model])

    # set the x-axis labels
    ax.set_xticks([p + width * 2 + gap * (p // 1) for p in x])
    ax.set_xticklabels(['Math', 'Reasoning', 'Total'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title(f'Performance Comparison of {version} with Models')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# adjust the layout
plt.tight_layout()

# save the plot
plt.savefig('model_performance_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('/Users/jiaxinperse/Downloads/model_performance_comparison.png', dpi=300, bbox_inches='tight')


# display the plot
plt.show()
