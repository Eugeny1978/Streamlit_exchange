import streamlit as st
import pandas as pd

# # Удалить меню от Streamlit
# .st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;} # top menu
# .st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} # foot
st.markdown("""
<style>
.st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;}
.st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} 
</style>
""", unsafe_allow_html=True)


st.title('Интерфейс Ботов')
st.header('Заголовок. Чтобы ЗАПУСТИТЬ Сервер Введи команду в терминале:')
st.subheader('streamlit run <name_file>.py')
st.subheader('Подзаголовок. Чтобы остановить Сервер Нажми в терминале: Cntr + C ')
st.text('Блок обычного Текста.')
st.markdown('**Полужирный Стиль** *Курсив Стиль* Обычный Стиль')
st.markdown('### Подзаголовок 3уровня. Более подробно о стилях markdown см на странице:')
st.markdown('[Официальная Страница документации markdown](https://www.markdownguide.org/basic-syntax/)')
st.markdown(">block pip install streamlit" )
st.markdown("---" ) # разделительная линия

st.markdown('[Документация katex (Для создания Математических  Формул (latex)](https://katex.org/docs/supported.html)')
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}') # формула матрицы
st.markdown("---" ) # разделительная линия
json_str = {'key1': "value1", 'key2': 'value2'}
st.json(json_str)
st.markdown("---" ) # разделительная линия
block_code = '''
print("Hello, it's str of code")
def func1():
    pass'''
st.code(block_code, language='python')
st.markdown("---" ) # разделительная линия
st.write('#### H4')
st.markdown("---" ) # разделительная линия
st.markdown('[Спец Символы Степени и нижние Индексы](https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts)')
st.metric(label='Wind Speed', value='12ms\u207B\u00B9', delta='-1.4ms\u207B\u00B9')
st.markdown("---" ) # разделительная линия
table = pd.DataFrame({'Price': [1200, 1190, 1180, 1170, 1160, 1150],
                      'Ammount': [12, 16, 27, 178, 12, 500]})
st.table(table)
st.dataframe(table)

st.markdown("---" ) # разделительная линия
st.markdown('#### Медиа ####')
st.image('media/my_image.png', caption='Это снимок моего рабочего стола') # width=500
st.caption('Секретная Запись часть 1')
st.audio('media/my_audio_1.mp3')
st.caption('Секретная Запись часть 2')
st.audio('media/my_audio_2.mp3')
st.video('media/my_video.mp4')

st.markdown("---" ) # разделительная линия

# Функция обратного вызова
def change():
    print('Изменено')
    print(st.session_state.key_checkbox)

state_checkbox = st.checkbox('my_checkbox', on_change=change, key='key_checkbox') # value=True
if state_checkbox:
    st.write('Вы нажали ЧекБокс в положение ВКЛ')
else:
    st.write('ЧекБокс в положении ВЫКЛ')





st.markdown("---" ) # разделительная линия
st.caption('Это подпись. Автор Luchnik78')

