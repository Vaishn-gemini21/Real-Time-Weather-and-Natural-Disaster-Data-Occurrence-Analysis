import matplotlib.pyplot as plt

class ChartVisualizer:

    def plot_line(self, x, y, title="", xlabel="", ylabel=""):
        plt.figure(figsize=(8,5))
        plt.plot(x,y,marker = 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

    def plot_bar(self, labels, values, title="", xlabel="", ylabel=""):
        plt.figure(figsize=(8,5))
        plt.bar(labels,values)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis="y")
        plt.show()

    def plot_pie(self, labels, values, title=""):
        plt.figure(figsize=(7,7))
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title(title)
        plt.show()

    def plot_multiple_days(self, temps, dates, title="Temperature Trend"):
        plt.figure(figsize=(8,5))
        plt.plot(dates, temps,  marker ="o", linestyle="--")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.show()
        


