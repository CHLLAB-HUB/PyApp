import streamlit as st
import os, time

print(f'✅ {os.path.basename(__file__)} 실행됨 {time.strftime("%Y-%m-%d %H:%M:%S")}')

st.title('다양한 widget들')

model = st.selectbox('모델선택', ('GPT-4', 'GPT-3.5', 'Claude-3'))
st.markdown(f'model: :green[{model}]')

name = st.text_input('이름을 입력하세요')
st.markdown(f'이름: :red[{name}]')

age = st.slider(label='나이', min_value=0, max_value=20)
st.markdown(f'나이: :blue[{age}]')

if age >= 4:
    st.write('성묘')
else:
    st.write('아묘')
    st.text_input('고양이 이름은?')

button = st.button('버튼을 눌러보세요')
if button:
    st.write(':yellow[버튼]이 눌렸어요 :sparkles:')

st.markdown('---')

num1 = st.number_input('숫자1', min_value=10, max_value=100, step=1)
num2 = st.number_input('숫자2', min_value=10, max_value=100, step=1)

btn_calc = st.button('더하기')
if btn_calc:
    st.markdown(f"""
                {num1} + {num2} = :green[{num1 + num2}]\n
                {num1} - {num2} = :red[{num1 - num2}]
                """)