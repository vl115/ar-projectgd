from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 確保 index.html 放在 templates 資料夾內

if __name__ == '__main__':
    app.run(debug=True)
