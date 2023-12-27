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
# import callbacks  # Uncomment if you have callbacks


app = dash.Dash(__name__)
app.layout = get_layout()

if __name__ == '__main__':
    app.run_server(debug=True)