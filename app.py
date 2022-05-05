import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle


st.image('https://www.agrisafe.org/wp-content/uploads/2021/07/breast-cancer-wyntk.jpg')
st.title('Breast Cancer Prediction')
df = pd.read_csv('./data/breast-cancer-final.csv', index_col=[0])

st.subheader('Original dataset')
st.dataframe(df)

attr_desc = {
    'menopause': "the time that marks the end of a person's menstrual cycle.",
    'age': 'the age of the patient.',
    'tumor-size': 'the size of the tumor in the patient.',
    'inv-nodes': 'the number of axillary lymph nodes that contain metastatic breast cancer visible on histological examination.',
    'node-caps': 'node cap',
    'deg-malig': 'the histological grade of the tumor. Tumors that a grade 1 predominantly consist of cells that, while neoplastic, retain many of their usual characteristics. Grade 3 tumors predominately consist of cells that are highly abnormal.',
    'breast': 'the side of breast that the patient has had the most malignant tumor, may occur in either breast.',
    'breast-quad': 'the quadrant of the breast that the patient has had the most malignant tumor.',
    'irradiat': 'whether the patient has had radiation therapy to destroy cancer cells.'
}


st.subheader('Attributes description')
st.write(attr_desc)

st.subheader('Prediction section')

selected_answer = [st.selectbox(f'Select {column}', df[column].unique(
).tolist()) for column in df.columns.tolist()[1:]]


model = pickle.load(open('./svm_model', 'rb'))


encoder = LabelEncoder()
i = 0
encoded_answer = []

for attr in df.iloc[:, 1:]:
    encoder.fit(df[attr])
    label_mapping = dict(
        zip(encoder.classes_, encoder.transform(encoder.classes_)))
    encoded_answer.append(label_mapping.get(selected_answer[i]))
    i += 1


def predict_result(*array_to_predict):
    input = np.array([encoded_answer]).astype(np.float64)
    prediction = model.predict(input)

    if prediction == 'no-recurrence-events':
        st.write('This patient will not have breast cancer recurrence')
    else:
        st.write('This patient will have breast cancer recurrence')


if st.button('Predict'):
    predict_result(encoded_answer)
