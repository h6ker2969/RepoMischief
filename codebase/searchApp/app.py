from flask import Flask, render_template, request
from main import Navigate
from map import MAP

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    obstacles = eval(request.form['obstacles'])
    nrow = eval(request.form['rows'])
    ncol = eval(request.form['columns'])
    start = eval(request.form['start'])
    goal = eval(request.form['goal'])

    print("Obstacles:", obstacles)
    print("Rows:", nrow)
    print("Columns:", ncol)
    print("Start:", start)
    print("Goal:", goal)

    maps = MAP(nrow, ncol, start, goal, obstacles)
    navigation = Navigate(maps)
    fig = navigation.search_BFS()

    # Return some response or render a template
    plot_html = fig.to_html(full_html=False)
    return render_template('plot_display.html', plot_html=plot_html)

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
