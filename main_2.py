import streamlit as st
import pandas as pd
from time import sleep
from datetime import time

# # Удалить меню от Streamlit
# .st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;} # top menu
# .st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} # foot
st.markdown("""
<style>
.st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;}
.st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} 
</style>
""", unsafe_allow_html=True)


st.title('Загрузка Файлов')
st.markdown('---')

def converter_time(time_value: str):
    m, s, ms = time_value.split(':')
    timer_sec = int(m)*60 + int(s) + int(ms)/1000
    return timer_sec


exp_image = ['jpeg', 'jpg', 'png', 'gif']
images = st.file_uploader('Пожалуйста, загрузите изображение...', type=exp_image, accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

# exp_video = ['mp4', 'avi']
# video = st.file_uploader('Пожалуйста, загрузите видео...', type=exp_video)
# if video is not None:
#     st.video(video)

slider = st.slider('Slider', min_value=0, max_value=1000, value= 300)
st.write(slider)
opt = [10, 20, 30, 40, 50]
st.select_slider('Select Slider', options=opt)

user_text = st.text_input('Input text', max_chars=80)
user_area_text = st.text_area('Input text', max_chars=500, height=120)
user_date = st.date_input('Input date')

button = st.button('Запусти Прогресс', )
print(button)
bar = st.progress(0, text='Прогресс: 0%')
if button:
    for t in range(11):
        procents = t*10
        bar.progress(procents, text=f'Прогресс: {procents}%')
        sleep(1)
        if t == 10:
            button = False

user_time = st.time_input('Set timer', value=time(0,0,0))
user_time_str = str(user_time)
if user_time_str == '00:00:00':
    st.write('Установите Таймер для Выполнения Прогресса')
else:
    secundes = converter_time(user_time_str)
    st.write(secundes)
    bar_timer = st.progress(0, text='Прогресс: 0%')
    per = secundes/100
    for t1 in range(101):
        bar_timer.progress(t1, text=f'Прогресс: {t1}%')
        sleep(per)



