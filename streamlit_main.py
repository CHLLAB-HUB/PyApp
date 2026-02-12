import streamlit as st
import os, time

print(f'✅ {os.path.basename(__file__)} 실행됨 {time.strftime("%Y-%m-%d %H:%M:%S")}')

import random

st.title(':sparkles: lotto 생성기 :sparkles:')

def generate_lotto():
    lotto = [i + 1 for i in range(45)]
    random.shuffle(lotto)
    return lotto[:6]

button = st.button('로또 번호 생성기')

if button:
    for i in range(5):
        st.subheader(f'{i + 1}번째 로또 번호: :green[{generate_lotto()}]')