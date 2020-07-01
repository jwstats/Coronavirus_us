
import plots
from plots import fig, daily_totals
import json
import plotly.graph_objects as go
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# CSS Styling
# app.css.append_css(
#     {'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#### App ####
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H1(children='US Covid-19 Dashboard'),
                    html.H5(children='Created by Jonathan Williams'),
                    html.Hr()
                ])
            ], className="row"),
            html.Div([
                html.H4(children='Hover the graph below to Update Results')
            ], className="row"),
            html.Div([
                html.Div([
                    dcc.Graph(id="main_graph",
                              figure=fig)
                ])
            ], className="row"),
            html.Div([
                html.Div([
                    dcc.Graph(id='hover-Bar',
                              figure=dict(data=[go.Bar(x=[0, 1], y=[1, 1])],
                                          layout=go.Layout(title='Daily Totals')))
                ], className="four columns"),
                html.Div([
                    dcc.Graph(id='hover-Gauge',
                              figure=dict())
                ], className="four columns"),
                html.Div([
                    html.H4(
                        children='Metric Description: What We Still Don\'t Know'),
                    html.Hr(),
                    html.H6(
                        children='The purple gauge represents the number of (Unresolved) cases that we still don\'t know the status of.\nWe want the purple gauge to fall below the black target line.'),
                    html.H6(
                        children='The black target line is a reference point marked at 30% of all cases, on a specific day.'),
                    html.H6(html.B(
                            "This metric tracks the percentage of active cases that we don't have conclusions for, on a specific day."))
                ], className="four columns")
            ], className="row"),
            html.Hr(),
            html.Div([
                html.Div([
                    html.H2(children="Acknowledgments"),
                    dcc.Markdown('''
            * Johns Hopkins University for making the data available for educational and academic research purposes
            * Sudalai Raj Kumar for global covid-19 data distribution.
            ''')
                ], className="eight columns"),
                html.Div([
                    html.H4(children='Data Source and More Information'),
                    html.Hr(),
                    html.H6(html.A(href='https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset',
                                   children='Original Data Source',
                                   n_clicks=2)),
                    html.H6(children="Email Jonathan @: j.will.3993@gmail.com")
                ], className="four columns")
            ], className="row")
        ], style=dict(backgroundColor='#f2f2f2'))
    ])
])


@app.callback(
    [Output('hover-Bar', 'figure'),
     Output('hover-Gauge', 'figure')],
    [Input('main_graph', 'hoverData')])
def display_hover(hoverData):
    # Grab 'index' to access dataset
    index = hoverData['points'][0]['pointIndex']

    # Define Graph Categories and Values
    category = ['Deaths', 'Recovered']
    val = [round(daily_totals.iloc[index]['Deaths']),
           round(daily_totals.iloc[index]['Recovered'])]

    # Bar Graph
    figure = dict(data=[go.Bar(x=category,
                               y=[round(val[0])],
                               text=round(val[0]),
                               textposition='auto',
                               textfont=dict(family='Arial', size=20),
                               name='Deaths',
                               width=0.4,
                               marker=dict(color='#EA2916')),
                        go.Bar(x=category,
                               y=[round(val[1])],
                               text=round(val[1]),
                               textposition='auto',
                               textfont=dict(family='Arial', size=20),
                               name='Recovered',
                               width=0.4,
                               marker=dict(color='#35C33E'))],
                  layout=go.Layout(title='Daily Totals on {}'.format(daily_totals.iloc[index]['ObservationDate']),
                                   xaxis=dict(visible=False)))

    # Gauge Indicator
    gauge = dict(data=[go.Indicator(
        mode='gauge+number+delta',
        title=dict(text='Unresolved Cases Indicator',
                   font=dict(size=24)),
        delta=dict(reference=round(max(daily_totals.iloc[:index+1]["Confirmed"]*.30)),
                   increasing=dict(color="darkorange"),
                   decreasing=dict(color="darkorange")),
        domain=dict(x=[0, 1], y=[0, 1]),
        value=daily_totals.iloc[index]["Confirmed"] -
        daily_totals.iloc[index]["Deaths"] -
        daily_totals.iloc[index]["Recovered"],
        gauge=dict(axis=dict(range=[None, max(daily_totals.iloc[:index+1]["Confirmed"])]),
                   bar=dict(color="purple"),
                   bgcolor="white",
                   borderwidth=2,
                   bordercolor="darkorange",
                   steps=[dict(range=[0, max(daily_totals.iloc[:index+1]["Confirmed"]*.25)],
                               color='gray'),
                          dict(range=[max(daily_totals.iloc[:index+1]["Confirmed"]*.25), max(daily_totals.iloc[:index+1]["Confirmed"]*.50)],
                               color='darkgray'),
                          dict(range=[max(daily_totals.iloc[:index+1]["Confirmed"]*.50), max(daily_totals.iloc[:index+1]["Confirmed"]*.75)],
                               color='lightgray')],
                   threshold=dict(line=dict(color="black", width=6),
                                  thickness=0.75,
                                  value=max(daily_totals.iloc[:index+1]["Confirmed"]*.30))))]
                 )

    return figure, gauge


if __name__ == '__main__':
    app.run_server(debug=True)
