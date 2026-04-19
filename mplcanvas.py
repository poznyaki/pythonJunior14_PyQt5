from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, data_dict=None, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        super().__init__(self.fig)

        if data_dict is None:
            data_dict = {}

        self.plot_pie(data_dict)

    def plot_pie(self, data):
        self.axes.clear()

        self.fig.patch.set_facecolor('#2a2b33')
        self.axes.set_facecolor('#2a2b33')

        if not data:
            self.axes.text(
                0.5, 0.5,
                "No data",
                color="white",
                ha="center",
                va="center"
            )
            self.draw()
            return

        labels = list(data.keys())
        values = list(data.values())

        colors = [
            "#6c8cff", "#5a78e0", "#4c66c0",
            "#8fd694", "#f4a261", "#e76f51"
        ]

        wedges, texts, autotexts = self.axes.pie(
            values,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors[:len(values)],
            textprops={'color': 'white'}
        )

        for autotext in autotexts:
            autotext.set_color('white')

        self.axes.set_title("Expense statistics", color="white")

        self.draw()

    def update_data(self, new_data):
        self.plot_pie(new_data)