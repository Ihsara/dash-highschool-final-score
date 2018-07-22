# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from pathlib import Path



__file__ = "../nhse-dataset/province_code.xlsx"

p = Path(__file__).parents[1]

def get_data(ref_province):
    data_wrapper = {}
    for province_id in range(64):
        try:
            data_wraper[ref_province[ref_province["SỐ TT CỤM THI"] == province_id]["ĐIẠ PHƯƠNG"].values[0]] = pd.read_csv(BASE_DIR_DATA.format(province_id))
        except FileNotFoundError:
            pass
    return data_wrapper

province_ref = pd.read_excel(p)
data_wrapper = get_data(province_ref)


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.p(children='''
        This is the test paragraph
    '''),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                        go.Histogram(x=data_wraper["TP.HCM"]['LÝ'],  histnorm='probability')
            ],
            'layout': {
                'title': 'Điểm thi Toán THPT của TP.HCM 2018'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)