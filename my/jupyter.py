import ipywidgets as widgets
from IPython.display import display


class Leafer:
    """Class to leaf through a list of objects

    Usage:
    >>> l = Leafer(some_list); l()
    >>> [some_list[i] for i in l.marked_idxs]  # contains the items "marked"
    """

    def __init__(self, data: list):
        self.current_idx = 0
        self.marked_idxs = set()
        self.data = data
        self.idx_display = widgets.IntText(value=self.current_idx)
        self.prev_b = widgets.Button(description='Prev')
        self.next_b = widgets.Button(description='Next')
        self.mark_b = widgets.Button(description='Mark')
        self.output = widgets.Output()

        self.prev_b.on_click(lambda b: self.change(-1))
        self.next_b.on_click(lambda b: self.change(1))
        self.mark_b.on_click(lambda b: self.marked_idxs.add(self.current_idx))

        self.change(0)

    def change(self, n):
        if not 0 <= self.current_idx + n < len(self.data):
            return
        self.current_idx += n
        self.idx_display.value = self.current_idx
        with self.output:
            self.output.clear_output()
            print(self.data[self.current_idx])

    def __call__(self):
        display(widgets.HBox([self.idx_display,
                              widgets.Box([self.prev_b, self.next_b, self.mark_b])]),
                self.output)

