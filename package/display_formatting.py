import base64



image_filename = 'nyt_img.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
layout = {'margin': {'l': 30, 'r': 00, 'b': 30, 't': 0},'legend': {'x': 0, 'y': 1}}


democrat_blue = 'rgb(0, 21, 188)'
republican_red= 'rgb(233,29,14)'

years=['August Year 1', 'September Year 1', 'October Year 1', 'November Year 1', 'December Year 1', 'January Year 1', 'February Year 1', 'March Year 1', 'April Year 1', 'May Year 1', 'June Year 1', 'July Year 1','August Year 2', 'September Year 2', 'October Year 2', 'November Year 2', 'December Year 2', 'January Year 2', 'February Year 2','March Year 2', 'April Year 2', 'May Year 2', 'June Year 2', 'July Year 2']

dropdown_options_obama=[
    {'label': 'Top Obama Keywords', 'value': 'all'},
    {'label': 'Obama People Keywords', 'value': 'people'},
    {'label': 'Obama Subject Keyowrds', 'value': 'subject'},
    {'label': 'Obama Organization Keyowrds', 'value': 'organization'},
    {'label': 'Obama Location Keyowrds', 'value': 'location'}]

dropdown_options_trump=[
    {'label': 'Top Trump Keywords', 'value': 'all'},
    {'label': 'Trump People Keywords', 'value': 'people'},
    {'label': 'Trump Subject Keyowrds', 'value': 'subject'},
    {'label': 'Trump Organization Keyowrds', 'value': 'organization'},
    {'label': 'Trump Location Keyowrds', 'value': 'location'}]

blurb = "In this mini-project, we used the article search API provided by the New York Times to pull data for articles related to Presidents Obama and Trump. Our queries looked at comparable time frames, which we decided would be a two-year period starting from 6 months before taking office. This allowed us to consider the (current) entirety of the Trump Administration, and yielded nearly 6000 articles to work with! We hope you enjoy looking through our visualizations of this data."
