"""
import app
import layout
import callbacks

app.layout = layout.get_layout()

if __name__ == '__main__':
    app.server.run(debug=True, port=8080)
"""