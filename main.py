from flask import Flask

app = Flask('my web app')


@app.route('/')
def p1():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <b>Миссия Колонизация Марса<b>
                  </body>
                </html>"""

@app.route('/index')
def p2():

    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <b>И на Марсе будут яблони цвести!</b>
                  </body>
                </html>"""

app.run(debug=True, port=8080)

