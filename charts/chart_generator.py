import matplotlib.pyplot as plt

def bar_chart(x, y):
    plt.bar(x, y)
    plt.title("Bar Chart")

def line_chart(x, y):
    plt.plot(x, y)
    plt.title("Line Chart")

def pie_chart(labels, values):
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Pie Chart")

def scatter_chart(x, y):
    plt.scatter(x, y)
    plt.title("Scatter Plot")
