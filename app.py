import streamlit as st
import pandas as pd
import plotly


st.image('https://www.agrisafe.org/wp-content/uploads/2021/07/breast-cancer-wyntk.jpg')
st.title('Breast Cancer Prediction')
df = pd.read_csv('./data/breast-cancer-final.csv', index_col=[0])

st.subheader('Original dataset')
st.dataframe(df)

# cat_attr = ['menopause', 'node-caps', 'breast', 'breast-quad', 'irradiat']
# bin_attr = ['age', 'tumor-size', 'inv-nodes']

attr_desc = {
    'age': 'Age of the patient',
    'menopause': 'Type of menopause',
    'tumor-size': 'The size of the tumor',
}

st.plotly_chart(figure_or_data=plotly.graph_objs.Figure, use_container_width=False,sharing='streamlit', **kwargs)


st.subheader('Prediction section')

with st.form('Input information: '):
    for attribute in df.columns.tolist()[1:]:
        st.selectbox(f'Select {attribute}', df[attribute].unique().tolist())
    
    predict_button = st.form_submit_button('Predict')
    
st.subheader('Results here!')