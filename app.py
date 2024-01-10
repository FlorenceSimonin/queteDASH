from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# initialisation de l'app Dash
app = Dash(__name__)

# Création de la base de donnée
link = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'
df = pd.read_csv(link, sep=',', on_bad_lines='skip')

bar_chart= px.bar(df.head(10), x='title', y='  num_pages', title= '10 first books with number of pages')

app.layout = html.Div([
    html.H1("Book's lover", style= {'textAlign': 'center'}),
    html.P("Welcome !! you will find here information on books 📚", style= {'textAlign': 'center'}),
    html.Div([dcc.Graph(id='bar_chart', figure=(bar_chart)),
              html.P('Veuillez choisir un auteur:'),
             dcc.Dropdown(id='dropd_authors', options=[{'label':i, 'value': i} for i in df['authors'].unique()]),
             html.P('Veullez entrer un nombre de pages maximales:'),
             dcc.Input(id='Input_nb_pages', type='number')
             ])
])
if __name__ == '__main__':
    app.run_server(debug=True)