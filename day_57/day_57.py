from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    name = "John"
    age=21
    company="finstein"
    return render_template('index.html', 
                           name=name,age=age,company=company)

if __name__ == '__main__':
    app.run()
