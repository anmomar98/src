import os
import ee
import geemap
import ipywidgets as widgets

Map = geemap.Map()
Map.add_basemap('HYBRID')
Map

style = {'description_width': 'initial'}
title = widgets.Text(
    description='Title:', value='Landsat Timelapse', width=200, style=style
)

bands = widgets.Dropdown(
    description='Select RGB Combo:',
    options=[
        'Red/Green/Blue',
        'NIR/Red/Green',
        'SWIR2/SWIR1/NIR',
        'NIR/SWIR1/Red',
        'SWIR2/NIR/Red',
        'SWIR2/SWIR1/Red',
        'SWIR1/NIR/Blue',
        'NIR/SWIR1/Blue',
        'SWIR2/NIR/Green',
        'SWIR1/NIR/Red',
    ],
    value='NIR/Red/Green',
    style=style,
)

hbox1 = widgets.HBox([title, bands])
hbox1