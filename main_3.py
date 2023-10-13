import streamlit as st


# # Удалить меню от Streamlit
# .st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;} # top menu
# .st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} # foot
st.markdown("""
<style>
.st-emotion-cache-iiif1v.ef3psqc3 {visibility: hidden;}
.st-emotion-cache-h5rgaw.ea3mdgi1 {visibility: hidden;} 
</style>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center'> Регистрация / Авторизация </h4>", unsafe_allow_html=True)
# v.1 Создание Формы
form = st.form('Form 1')
form.text_input('Name / Имя', max_chars=100)
form.form_submit_button('Submit / Отправить')

# v.2 Создание Формы
with st.form('Form 2'):
    st.text_input('Name / Имя', max_chars=100)
    st.form_submit_button('Submit / Отправить')

with st.form('Form 3', clear_on_submit=True):
    column_R, column_L = st.columns(2)
    user_name = column_R.text_input('Name / Имя:', max_chars=100)
    user_last_name = column_L.text_input('Last Name / Фамилия:', max_chars=100)
    st.text_input('Email Adress:')
    st.text_input('Password:')
    st.text_input('Confirm Password:')
    year, month, day = st.columns(3)
    year.text_input('Year', max_chars=4)
    month.text_input('Month', max_chars=2)
    day.text_input('Day', max_chars=2)
    submit_state = st.form_submit_button('Submit / Отправить')
    if submit_state:
        if not user_name or not user_last_name:
            st.warning('Заполните Поля "Имя" и "Фамилия"')
        else:
            st.success('Отправка Данных прошло Успешно')

