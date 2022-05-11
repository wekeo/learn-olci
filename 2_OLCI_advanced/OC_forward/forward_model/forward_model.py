"""Module responsible for the core logic of the forward model."""

from forward_model.read_params import read_iop_params
from forward_model.read_params import read_iops
from forward_model.read_samples import read_rrs_samples
from forward_model.jupyter_widgets import build_widgets
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np

'''
class ForwardModel:

    # initialise with all LUTs and parameters
    def __init__(self):

        self.conditions = {}
        self.conditions["params"] = read_iop_params()
        self.conditions["wavelengths"], self.conditions["abs_coeff_water"], self.conditions["abs_increment"], self.conditions["scattering_coefficient"] = read_iops()
        self.conditions["sample_files"], self.conditions["samples"] = read_rrs_samples(self.conditions["params"])
        self.conditions["chl_default"] = 0.01
        self.conditions["nap_default"] = 0.01
        self.conditions["cdom_default"] = 0.01

    def run_model(self):

        # set plots
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim([0, 4])
        ax.set_ylim([-3.25, 3.25])
        ax.set_yticks(range(-3,4))
        ax.set_yticklabels([10**exp for exp in range(-3,4)])
        ax.set_ylabel('Concentration')
        ax.set_xticks([1,2,3])
        ax.set_xticklabels(["CHL ", "NAP ", "CDOM "])
        ax.grid(True)

        # create widgets
        self.widgets = build_widgets(self.conditions)

        @widgets.interact(
            chl = self.widgets[0],
            nap = self.widgets[1],
            cdom = self.widgets[2])
        def update(chl, nap, cdom):
            [pt.remove() for pt in ax.lines]
            ax.plot([1, 2, 3],[np.log10(chl), np.log10(nap), np.log10(cdom)], "o", linewidth=0, color='k', markersize=10)
'''

def make_box_layout():
     return widgets.Layout(
        border='solid 1px black',
        margin='0px 10px 10px 0px',
        padding='5px 5px 5px 5px'
     )

class ForwardModel(widgets.HBox):
     
    def __init__(self):
        super().__init__()
        output = widgets.Output()
 
        self.x = np.linspace(0, 2 * np.pi, 100)
        initial_color = '#FF00DD'
 
        with output:
            self.fig, self.ax = plt.subplots(constrained_layout=True, figsize=(5, 3.5))
        self.line, = self.ax.plot(self.x, np.sin(self.x), initial_color)
         
        self.fig.canvas.toolbar_position = 'bottom'
        self.ax.grid(True)
 
        # define widgets
        int_slider = widgets.IntSlider(
            value=1, 
            min=0, 
            max=10, 
            step=1, 
            description='freq'
        )
        color_picker = widgets.ColorPicker(
            value=initial_color, 
            description='pick a color'
        )
        text_xlabel = widgets.Text(
            value='', 
            description='xlabel', 
            continuous_update=False
        )
        text_ylabel = widgets.Text(
            value='', 
            description='ylabel', 
            continuous_update=False
        )
 
        controls = widgets.VBox([
            int_slider, 
            color_picker, 
            text_xlabel, 
            text_ylabel
        ])
        controls.layout = make_box_layout()
         
        out_box = widgets.Box([output])
        output.layout = make_box_layout()
 
        # observe stuff
        int_slider.observe(self.update, 'value')
        color_picker.observe(self.line_color, 'value')
        text_xlabel.observe(self.update_xlabel, 'value')
        text_ylabel.observe(self.update_ylabel, 'value')
         
        text_xlabel.value = 'x'
        text_ylabel.value = 'y'
         
 
        # add to children
        self.children = [controls, output]
     
    def update(self, change):
        """Draw line in plot"""
        self.line.set_ydata(np.sin(change.new * self.x))
        self.fig.canvas.draw()
 
    def line_color(self, change):
        self.line.set_color(change.new)
 
    def update_xlabel(self, change):
        self.ax.set_xlabel(change.new)
 
    def update_ylabel(self, change):
        self.ax.set_ylabel(change.new)
         
         
ForwardModel()