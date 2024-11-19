# -*- coding: utf-8 -*-
"""
Application
===========
"""

import streamlit as st
import tempfile
from datetime import datetime

import colour

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2020-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__application_name__ = 'Colour - Streamlit'

__major_version__ = '0'
__minor_version__ = '1'
__change_version__ = '0'
__version__ = '.'.join(
    (__major_version__,
     __minor_version__,
     __change_version__))  # yapf: disable

__all__ = ['single_sd_colour_rendition_report']


def single_sd_colour_rendition_report():
    """
    Generates the *ANSI/IES TM-30-18 Colour Rendition Report*.
    """

    uploaded_file = st.sidebar.file_uploader(str())
    method = st.sidebar.selectbox('Method', ('Full', 'Intermediate', 'Simple'))
    date = st.sidebar.text_input(
        'Date', value=datetime.now().strftime("%b %d, %Y %H:%M:%S"))
    manufacturer = st.sidebar.text_input('Manufacturer', value='')
    model = st.sidebar.text_input('Model', value='')

    if uploaded_file is None:
        st.title('IES TM-30-18 Colour Rendition Report')

        st.markdown('This *Streamlit* app generates an '
                    '**ANSI/IES TM-30-18 Colour Rendition Report** using '
                    '[Colour](https://colour-science.org).')

        st.markdown(
            'Please use the sidebar to load the *CSV* file containing the '
            'light source spectral distribution.')

        return

    csv_path = tempfile.mkstemp()[1]
    with open(csv_path, 'w') as csv_file:
        csv_file.write(uploaded_file.getvalue().decode('utf-8'))

    sds = colour.read_sds_from_csv_file(csv_path)
    sd = sds[list(sds.keys())[0]]
    if sd.shape.interval not in [1, 5, 10, 20]:
        sd = sd.align(
            colour.SpectralShape(start=sd.shape.start,
                                 end=sd.shape.end,
                                 interval=1))

    figure, _axes = colour.plotting.plot_single_sd_colour_rendition_report(
        sd,
        method,
        date=date,
        manufacturer=manufacturer,
        model=model,
        transparent_background=False)

    st.pyplot(figure)


single_sd_colour_rendition_report()
