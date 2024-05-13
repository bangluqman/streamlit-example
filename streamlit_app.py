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

summary_sentences = "Teks hasil rangkuman"
txtOutput = st.text_area(summary_sentences)


