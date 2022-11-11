import dash
import dash_core_components as dcc
import dash_html_components as html

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

app.layout = html.Div([
    html.H1('aftermath test')])
