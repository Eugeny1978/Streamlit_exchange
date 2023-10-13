import seaborn
import streamlit as st
import pandas  as pd
import numpy as np
from matplotlib import pyplot as plt
# import LovelyPlots.utils as lp
import seaborn as sns

sns.set_style("darkgrid")

# plt.style.reload_library()
# plt.style.use('ipynb')
# lp.set_font('my_font.tiff')
# lp.set_retina()

# # Удалить меню от Streamlit
# .st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;} # top menu
# .st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} # foot
st.markdown("""
<style>
.st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} 
</style>
""", unsafe_allow_html=True)


table = pd.DataFrame({'Price': [1200, 1190, 1180, 1170, 1160, 1150],
                      'Ammount': [12, 124, 27, 178, 32, 500]})

x = np.linspace(0, 10, 100)

st.sidebar.write('Боковое Menu')
graph_types = ['Line', 'Bar', 'H-Bar']
graph_page = st.sidebar.radio('Выберите Вид Графика:', options=graph_types)
if graph_page == 'Line':
    st.markdown("<h4 style='text-align: left'>Line Graph</h4>", unsafe_allow_html=True)
    figure = plt.figure()
    sns.lineplot(x=x, y=np.sin(x))
    sns.lineplot(x=x, y=np.cos(x), linestyle='--').set_title('Синус и Косинус')
    st.write(figure)
elif graph_page == 'Bar':
    st.markdown("<h4 style='text-align: left'>Bar Graph</h4>", unsafe_allow_html=True)
    st.dataframe(table)
    figure = plt.figure()
    sns.barplot(data=table, x='Price', y='Ammount', hue='Ammount', legend=False).set_title('Стакан Цен')
    st.write(figure)
elif graph_page == 'H-Bar':
    st.markdown("<h4 style='text-align: left'>H-Bar Graph</h4>", unsafe_allow_html=True)
    figure = plt.figure()
    sns.barplot(data=table, x='Ammount', y='Price', orient='h').set_title('Стакан Цен')
    st.write(figure)