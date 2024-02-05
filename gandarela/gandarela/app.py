"""
import app
import layout
import callbacks

app.layout = layout.get_layout()

if __name__ == '__main__':
    app.server.run(debug=True, port=8080)
"""

import dash
from layout import get_layout
from callbacks import register_callbacks
import data


app = dash.Dash(__name__)
server = app.server

# Load and preprocess data
lamina_data, cad_data = data.load_data()
lamina_data = data.prepare_data_for_performance_graph(lamina_data)

# Set layout with DataFrame
app.layout = get_layout(lamina_data, cad_data)

# Register callbacks
register_callbacks(app,lamina_data, cad_data)

if __name__ == '__main__':
    app.run_server(debug=True)

# 
