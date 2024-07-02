import matplotlib.pyplot as plt
def generateBarCharts(labels, values):
    fig, ax= plt.subplots()
    ax.bar(labels,values)
    plt.show()