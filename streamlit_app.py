import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Aplikasi Text Summary
Aplikasi untuk merangkum artikel.
"""

txtInput = st.text_area("Masukkan Text disini...")
bt = st.button("Ringkas Artikel")
txtOutput = st.text_area("Output")


