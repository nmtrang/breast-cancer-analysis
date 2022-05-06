

# Breast Cancer Analysis & Prediction
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nmtrang/breast-cancer-analysis/app.py)







## Appendix
- [Introduction](#Introduction)
- [Re-organizing the dataset](#Reorganizing-the-dataset)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Tackle imbalanced dataset](#Tackle-imbalanced-dataset)
- [Model stacking](#Model-stacking)
- [Deploy to streamlit](#Deploy-to-streamlit)



## Introduction

### Data source: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer

### Attributes description:
- ``menopause`` (nominal): the time that marks the end of a person's menstrual cycle.
- ``age`` (range): the age of the patient.
- ``tumor-size`` (in mm) (range): the size of the tumor in the patient.
- ``inv-nodes`` (range): the number of axillary lymph nodes that contain metastatic breast cancer visible on histological examination.
- ``node-caps`` (binary): 
- ``deg-malig`` (numerical): the histological grade of the tumor. Tumors that a grade 1 predominantly consist of cells that, while neoplastic, retain many of their usual characteristics. Grade 3 tumors predominately consist of cells that are highly abnormal.
- ``breast`` (nominal): the side of breast that the patient has had the most malignant tumor, may occur in either breast.
- ``breast-quad`` (nominal): the quadrant of the breast that the patient has had the most malignant tumor.
- ``irradiate`` (binary): whether the patient has had radiation therapy to destroy cancer cells.

## Reorganizing the dataset

This dataset is of file type ``.data`` which we will see it'll become like this if reading with pandas - ``read_fwf()``
![image]()

After re-organizing the value, final result will look like this:
![image]()

## Exploratory Data Analysis
We notice abitruary values in some columns so let's clean it.

There are 3 range data columns: ``age``, ``tumor-size``, ``inv-nodes``.

There are 5 nominal data columns: ``menopause``, ``node-caps``, ``irradiat``, ``breast``, ``breast-quad``.

There is only 1 numerical data column: ``def-malig``.

The class/label is ``class`` with ``no-recurrence-events`` and ``recurrence-events``.

## Tackle imbalanced dataset

## Model stacking

## Deploy to streamlit
