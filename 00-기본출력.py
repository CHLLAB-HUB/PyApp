import streamlit as st

st.title('안녕하세요 Streamlit')

st.header('헤더를 입력해 주세요 :sunglasses:')

st.subheader('서브헤더를 입력해주세요')

st.text('일반텍스트')

st.caption('캡션을 넣어주세요')

sample_code = '''
def fuction():
    print('Hello, World)
'''

st.code(sample_code)

st.markdown('streamlit은 **마크다운 문법**을 지원합니다')

st.table([
    ['이름', '나이',],
    ['홍길동', '43'],
    ['뽀로로', '23'],
])

st.metric(label='삼성전자', value='151,200원', delta='-1,200원')

st.title('write()')
st.write('hello')
st.write(10, 20, 30)
st.write([1, 2, 3, 4])