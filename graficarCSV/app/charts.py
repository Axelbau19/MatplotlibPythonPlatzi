import matplotlib.pyplot as plt
def generateBarCharts(labels, values):
    colorsBar = [plt.cm.get_cmap('tab10')(i / len(labels)) for i in range(len(labels))]
    fig, ax= plt.subplots()
    ax.bar(labels,values,color=colorsBar)
    plt.show()