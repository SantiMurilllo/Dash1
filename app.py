import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.H1("Hola Dash"),#H1 es heather 1 y es el texto mas grande 
    html.Hr(),
    html.H3("mi primera app en Dash"),
    html.P("esta es la primera ocasión en que estoy modificando mi página web"),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ]),
    html.H5("Lista sin numeros"),
    html.Ul([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    html.H5("Lista enumerada"),
    html.Ol([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    ])

if __name__ == '__main__':
    app.run_server()

    app.layout = html.Div([
    html.H1("Hola Dash!"),
    html.H3("Mi primera app de Dash"),
    html.P("Esta es la muestra de una aplicacion de dash, no hemos creado gráficos pero estamos poniendo información"),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ])
    ])