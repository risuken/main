import streamlit as st
from PIL import Image
import numpy as np

data = st.file_uploader("ファイルアップロード", type='csv')
