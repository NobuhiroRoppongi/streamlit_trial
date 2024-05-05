import pandas as pd
import streamlit as st
import pandas as pd
import streamlit as st

# Setting up page link 
st.set_page_config(page_title="Nobs Sample", page_icon='page_logo.png')
st.title("Nobs Sample analysis tool")

df = pd.DataFrame({'col1': [1,2,3]})
x = 10
'x: ', x 
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine='python',
        na_values='-',
        header=None)

st.markdown('### アクセスログ（先頭5件）')
st.write(df.head(5))
