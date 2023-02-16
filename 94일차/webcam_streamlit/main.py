import streamlit as st
import numpy as np
import pandas as pd
import io
import os
from PIL import Image
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

def app():
    st.title("Webcam Test")
    webrtc_ctx = webrtc_streamer(key="example")#, video_transformer_factory=VideoTransformer)

app()

#실행   streamlit run main.py