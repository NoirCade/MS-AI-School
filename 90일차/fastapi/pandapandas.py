import streamlit as st
import pandas as pd
import numpy as np
import search_stock
import webbrowser

from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import io
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ko', tz=540) # hl=host language, tz=time zone



#my_dataframe = pd.DataFrame([[1, 2], [4, 5], [7, 8]])
a = pytrends.trending_searches(pn='south_korea')

st.title('News Center')
st.header("today's korea trends")
print(a)
exit()
for i in range(10):
    #st.subheader(f"{i+1}위 : {a[0][i]}")
    #st.markdown(f"Check out this link:{i+1}위:{a[0][i]}(https://www.google.com/search?q=%{a[0][i]})")
    if st.button(f"{i+1}위 : {a[0][i]}"):
        webbrowser.open_new_tab(f"https://www.google.com/search?q={a[0][i]}")
    #pytrends.suggestions(a[0][i])
st.header("today's US trends")
b = pytrends.trending_searches(pn='united_states')
for i in range(10):
    #st.subheader(f"{i+1}위 : {a[0][i]}")
    #st.markdown(f"Check out this link:{i+1}위:{a[0][i]}(https://www.google.com/search?q=%{a[0][i]})")
    if st.button(f"{i+1}위 : {b[0][i]}"):
        webbrowser.open_new_tab(f"https://www.google.com/search?q={b[0][i]}")
    #pytrends.suggestions(a[0][i])
#st.dataframe(my_dataframe)
#st.table(data.iloc[0:10])
#st.json({'foo':'bar','fu':'ba'})
    # 데이터 로딩 함수는 여기에!