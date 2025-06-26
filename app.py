# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posters')
def posters():
    return render_template('posters.html')

@app.route('/banners')
def banners():
    return render_template('banners.html')

@app.route('/illustrations')
def illustrations():
    return render_template('illustrations.html')

@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/mockup')
def mockup():
    return render_template('mockup.html')

@app.route('/ui-designs')
def ui_designs():
    return render_template('ui_designs.html')

@app.route('/prototypes')
def prototypes():
    return render_template('prototypes.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
