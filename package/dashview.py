import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from package import app
import base64
from routes import *
from package.display_formatting import democrat_blue, republican_red, layout, encoded_image, years, dropdown_options_obama, dropdown_options_trump, blurb

###IMPORTING DATA
obama_total_article_count=return_total_article_count_by_president(1)
obama_monthly_data = return_monthly_article_counts_by_pres(1)
obama_people_data = top_fifteen_people_keywords_obama()
obama_subject_data = top_fifteen_subject_keywords_obama()

trump_total_article_count=return_total_article_count_by_president(2)
trump_monthly_data=return_monthly_article_counts_by_pres(2)
trump_people_data=top_fifteen_people_keywords_trump()
trump_subject_data = top_fifteen_subject_keywords_trump()

article_tabs = dcc.Tabs(value=1, id='tabs', tabs=[
        {'label': 'Monthly Article Count', 'value': 1},
        {'label': 'Presidential Coverage', 'value': 2},
        {'label': 'Breakdown by Section', 'value': 3},
        {'label': 'Keyword Overview', 'value': 4},
        {'label': 'Obama Top Keywords', 'value': 5},
        {'label': 'Trump Top Keywords', 'value': 6}
        ])
article_div=html.Div(id='tab-output1')


#in here, we also need to set up our layout via app.layout
app.layout = html.Div([
        html.H1("THE NEW YORK TIMES API PROJECT"),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
        html.H2("Welcome to our visualization of New York Times presidential coverage!"),
        html.P(blurb),
        article_tabs,
        article_div], style={'width': '90%','fontFamily': 'Sans-Serif', 'margin-left': 'auto', 'margin-right': 'auto'})

@app.callback(Output('tab-output1', 'children'), [Input('tabs', 'value')])
def display_content(value):
    data1 = [
        {'x': years, 'y': obama_monthly_data, 'name': 'President Obama 2007-2009', 'marker': {'color': democrat_blue}, 'type': ['bar'][int(value) % 1]},
        {'x': years, 'y': trump_monthly_data, 'name': 'President Trump 2016-2018', 'marker': {'color': republican_red}, 'type': ['bar'][int(value) % 1]}]
    data2 = [
        {'values': [obama_total_article_count, trump_total_article_count], 'name':'Article Chart by President', 'marker': {'colors': [democrat_blue, republican_red]}, 'type': 'pie', 'labels': ['President Obama', 'President Trump'],  'textfont': {'size': 20}}]
    data3 = [
        {'values': obama_sec_values, 'name': 'Obama top 15 sections pie', 'type': 'pie', 'labels': obama_sec_labels}]
    data4=[
        {'values': trump_sec_values, 'name': 'Trump top 15 sections pie', 'type': 'pie', 'labels': trump_sec_labels}]
    data5 = [
        {'x': [i[0] for i in top_fifteen_people_keywords_obama()+top_fifteen_subject_keywords_obama()], 'y': [i[1] for i in top_fifteen_people_keywords_obama()+top_fifteen_subject_keywords_obama()],'name': 'President Obama 2016-2018', 'marker': {'color': democrat_blue}, 'type': ['bar'][int(value) % 1]}]
    data6 = [
        {'x': [i[0] for i in top_fifteen_people_keywords_trump()+top_fifteen_subject_keywords_trump()], 'y': [i[1] for i in top_fifteen_people_keywords_trump()+top_fifteen_subject_keywords_trump()],'name': 'President Trump 2016-2018', 'marker': {'color': republican_red}, 'type': ['bar'][int(value) % 1]}]

    if value == 1:
        return html.Div([
            dcc.Graph(id='graph', figure={'data': data1, 'layout': {'title': 'Number of Articles Written by Month','margin-left': 'auto', 'margin-right': 'auto', 'legend': {'x': 0, 'y': 1}}}), html.Div(' '.join('created: by: Catherine Huang, Christopher Pease'))
            ])
    elif value == 2:
        return html.Div([
            dcc.Graph(id='graph', figure={'data': data2, 'layout': {'title': 'Article Breakdown by President'}}), html.Div(' '.join('created by: Catherine Huang, Christopher Pease'))
            ])
    elif value==3:
        return html.Div([
            html.Div([
            html.P('President Obama Articles'),
            dcc.Graph(id='graph', figure={'data': data3, 'layout':{'margin-left': 'auto', 'margin-right': 'auto'}})],className="six columns"),
            html.Div([
            html.P('President Trump Articles'),
            dcc.Graph(id='graph2', figure={'data': data4, 'layout':{'margin-left': 'auto', 'margin-right': 'auto'}})], className="six columns")])
    elif value==4:
        return html.Div([
            html.Div([dcc.Dropdown(value='all', id='obama-dropdown', options=dropdown_options_obama, className="six columns")],className="row"),
            html.Div(id='obama_output-container'),
            html.Div([dcc.Dropdown(value='all', id='trump-dropdown', options=dropdown_options_trump, className="six columns")], className="row"),
            html.Div(id='trump_output-container')])
    elif value == 5:
        return html.Div([
            dcc.Graph(id='graph',
            figure={'data': data5,
            'layout': {'title': 'Top Keywords for President Obama: People and Subjects',
            'margin': {'l': 50, 'r': 100, 'b': 200, 't':100}, 'legend': {'x': 0, 'y': 1}}}), html.Div(' '.join('created: by: Catherine, Christopher'))
            ])
    elif value == 6:
        return html.Div([
            dcc.Graph(id='graph',
            figure={'data': data6,
            'layout': {'title': 'Top Keywords for President Trump: People and Subjects',
            'margin': {'l': 50, 'r': 100, 'b': 230, 't':100},
            'legend': {'x': 0, 'y': 1}}}), html.Div(' '.join('created: by: Catherine, Christopher'))
            ])


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.config['suppress_callback_exceptions']=True

@app.callback(dash.dependencies.Output('obama_output-container', 'children'), [dash.dependencies.Input('obama-dropdown', 'value')])
def update_output_obama(value):
    keyword_data_all_o=[go.Bar(x=obama_allkeyword_values, y=obama_allkeyword_labels, orientation = 'h')]
    ppl_keyword_data_o=[go.Bar(x=obama_pplkeyword_values, y=obama_pplkeyword_labels, orientation = 'h')]
    sub_keyword_data_o=[go.Bar(x=obama_subkeyword_values, y=obama_subkeyword_labels, orientation = 'h')]
    org_keyword_data_o=[go.Bar(x=obama_orgkeyword_values, y=obama_orgkeyword_labels, orientation = 'h')]
    loc_keyword_data_o=[go.Bar(x=obama_lockeyword_values, y=obama_lockeyword_labels, orientation = 'h')]

    if value == 'all':
        return html.Div([dcc.Graph(id='graph_o1', figure={'data': keyword_data_all_o,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'people':
        return html.Div([dcc.Graph(id='graph_o2', figure={'data': ppl_keyword_data_o,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'subject':
        return html.Div([dcc.Graph(id='graph_o3', figure={'data': sub_keyword_data_o,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'organization':
        return html.Div([dcc.Graph(id='graph_o4', figure={'data': org_keyword_data_o,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value=='location':
        return html.Div([dcc.Graph(id='graph_o5', figure={'data': sub_keyword_data_o})])


@app.callback(dash.dependencies.Output('trump_output-container', 'children'), [dash.dependencies.Input('trump-dropdown', 'value')])
def update_output_trump(value):
    keyword_data_all_t=[go.Bar(x=trump_allkeyword_values, y=trump_allkeyword_labels, orientation = 'h')]
    ppl_keyword_data_t=[go.Bar(x=trump_pplkeyword_values, y=trump_pplkeyword_labels, orientation = 'h')]
    sub_keyword_data_t=[go.Bar(x=trump_subkeyword_values, y=trump_subkeyword_labels, orientation = 'h')]
    org_keyword_data_t=[go.Bar(x=trump_orgkeyword_values, y=trump_orgkeyword_labels, orientation = 'h')]
    loc_keyword_data_t=[go.Bar(x=trump_lockeyword_values, y=trump_lockeyword_labels, orientation = 'h')]

    if value == 'all':
        return html.Div([
        dcc.Graph(id='graph_t1', figure={'data': keyword_data_all_t,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'people':
        return html.Div([dcc.Graph(id='graph_t2', figure={'data': ppl_keyword_data_t,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'subject':
        return html.Div([dcc.Graph(id='graph_t3', figure={'data': sub_keyword_data_t,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value == 'organization':
        return html.Div([dcc.Graph(id='graph_t4', figure={'data': org_keyword_data_t,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])

    elif value=='location':
        return html.Div([dcc.Graph(id='graph_t5', figure={'data': loc_keyword_data_t,
                'layout':{'margin': {'l': 450, 'r': 600, 'b': 50, 't':0}}})])
