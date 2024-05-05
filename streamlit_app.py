import pandas as pd
import streamlit as st
import pandas as pd

df = pd.DataFrame({'col1': [1,2,3]})
x = 10
'x: ', x 
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine='python',
        na_values='-',
        header=None)
