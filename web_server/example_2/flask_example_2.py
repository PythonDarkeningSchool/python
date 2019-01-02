from flask import Flask, request

app = Flask(__name__)


@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    framework = request.args.get('framework')
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language:<br>
                  <input type="text" name="language"><br>
                  Framework:<br>
                  <input type="text" name="framework"><br>                  
                  <br><input type="submit" value="Submit"><br>
              </form>'''


@app.route('/json-example',  methods=['POST'])
def json_example():
    req_data = request.get_json()

    return req_data
    language = req_data['language']
    framework = req_data['framework']

    return '''
           The language value is: {}
           The framework value is: {}'''.format(language, framework)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
