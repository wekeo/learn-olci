"""Module responsible for building the Jupyter notebook widgets for model interaction."""
from ipywidgets import widgets
import os

def build_widgets(conditions):

    chl_slider = widgets.FloatSlider(
        value=conditions["chl_default"],
        min=0.001,
        max=1000,
        step=0.1,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.3f',
        description="Chl a [mg.m$^{-3}$] (0.001 - 1000)",
        )
    chl_slider_hbox = widgets.HBox([widgets.Label('Chl a [mg.m$^{-3}$] (0.001 - 1000):\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', style={'description_width': 'initial'}), chl_slider])

    nap_slider = widgets.FloatSlider(
        value=conditions["nap_default"],
        min=0.001,
        max=1000,
        step=0.1,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.3f',
        )
    nap_slider_hbox = widgets.HBox([widgets.Label('NAP [g.m$^{-3}$] (0.001 - 1000):\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', style={'description_width': 'initial'}), nap_slider])

    cdom_slider = widgets.FloatSlider(
        value=conditions["cdom_default"],
        min=0.001,
        max=1000,
        step=0.1,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.3f',
        )
    cdom_slider_hbox = widgets.HBox([widgets.Label('CDOM443 [m$^{-1}$] (0.001 - 1000):\xa0\xa0\xa0\xa0\xa0', style={'description_width': 'initial'}), cdom_slider])

    rrs_buttons = widgets.RadioButtons(

        options=[f'{os.path.basename(ii)}' for ii in conditions["sample_files"]],
        disabled=False
    )
    rrs_buttons_hbox = widgets.HBox([widgets.Label('Available Rrs samples:', style={'description_width': 'initial'}), rrs_buttons])

    opts_buttons = widgets.RadioButtons(
        options=["variable f'/Q"],
        disabled=False
    )    
    opts_buttons_hbox = widgets.HBox([widgets.Label('Model options:', style={'description_width': 'initial'}), opts_buttons])

    controls = widgets.VBox([
        chl_slider, 
        nap_slider,
        cdom_slider,
        rrs_buttons,
        opts_buttons
    ])

    return controls