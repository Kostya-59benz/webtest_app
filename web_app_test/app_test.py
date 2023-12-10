import subprocess
from flask import Flask, render_template, request, flash

from web_test.config.links import Links
from web_test.config.choose_driver import browser_selector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fasd1hu312njdakj36990'

selected_options = []

link = None

@app.route("/", methods=['POST', 'GET'])
def get_url():
    global data, link
    input_url = ''
    if request.method == 'POST':
        input_url = request.form['url']
        if 'option1' in request.form:
            selected_options.append('Firefox')
        if 'option2' in request.form:
            selected_options.append('Edge')
        if 'option3' in request.form:
            selected_options.append('Chrome')
        link = Links()
        link.host = input_url
        browser_selector(selected_options)
        if data is not None:
            try:
                subprocess.run(['pytest', '../web_test/'])
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при запуске тестов: {e}")
            else:
                print("Тесты успешно выполнены")
        selected_options.clear()
    return render_template('index.html', selected_options=selected_options)
