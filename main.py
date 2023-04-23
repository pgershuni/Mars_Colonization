from flask import Flask,  url_for, request

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
# Часть 1. Колонизация Марса
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

@app.route('/promotion')
# Часть 2. Рекламная кампания
def p3():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <b>Человечество вырастает из детства.</b>
                    <br><b>Человечеству мала одна планета.</b>
                    <br><b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
                    <br><b>И начнем с Марса!</b>
                  </body>
                </html>"""


@app.route('/image_mars')
# Часть 3. Изображение Марса
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='data/mars.jpg')}"  alt="здесь должна была быть картинка, но не нашлась">
                    <br>Вот она какая, красная планета!
                  </body>
                </html>"""

# https://bootstrap-4.ru/docs/5.1/components/alerts/
@app.route('/promotion_image')
# Часть 4. Реклама с картинкой
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert"><b>Человечество вырастает из детства.</b></div>
                    <div class="alert alert-success" role="alert"><b>Человечеству мала одна планета.</b></div>
                    <div class="alert alert-light" role="alert"><b>Мы сделаем обитаемыми безжизненные пока планеты.</b></div>
                    <div class="alert alert-warning" role="alert"><b>И начнем с Марса!</b></div>
                    <div class="alert alert-danger" role="alert"><b>Присоединяйся!</b></div>
                  </body>
                </html>"""

@app.route('/astronaut_selection', methods=['POST', 'GET'])
# Часть 5. Отбор астронавтов
def astrunaut_selection():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h2>Анкета претендента</h2>
                    <h3>на участие в миссии</h3>
                     <div>
                        <form class="astronaut_form" method="post" enctype="multipart/form-data")
                        <label for="form-control">  </label>
                        <input type="astro_sname" class="form-control" id="astro_sname" placeholder="Введите фамилию" name="astro_sname">
                        <input type="astro_name" class="form-control" id="name" placeholder="Введите имя" name="astro_name">
                        <label for="form-control">  </label>
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                        <div class="form-group">
                            <label for="form-control">Какое у Вас образование</label>
                            <select class="form-control" id="form-control" name="class">
                            <option>Высшее</option>
                            <option>Высшее неоконченное</option>
                            <option>Среднее специальное</option>
                            <option>Среднее основное</option>
                            <option>9 классов</option>
                            <option>Начальное</option>
                            </select>
                       </div>        
                       <div class="form-group">
                            <label for="form-control">Ваша профессия</label>
                             <div class="form-check">
                                <input class="form-check-input" type="radio" name="profession" id="engeneer1" value="engeneer1" checked>
                                <label class="form-check-label" for="engeneer1">
                                    Инженер - исследователь
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="profession" id="engeneer2" value="engeneer2">
                                <label class="form-check-label" for="engeneer2">
                                    Инженер - строитель
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="profession" id="pilot" value="pilot">
                                <label class="form-check-label" for="pilot">
                                    Пилот
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="profession" id="exobiolog" value="exobiolog">
                                <label class="form-check-label" for="exobiolog">
                                    Экзобиолог
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="profession" id="doctor" value="doctor">
                                <label class="form-check-label" for="doctor">
                                    Врач
                                </label>
                            </div>
                       </div>        
                        <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                    Мужской
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                <label class="form-check-label" for="female">
                                    Женский
                                </label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="form-control">Почему Вы хотите принять участие в миссии</label>       
                            <textarea class="form-control" id="motivation" rows="3" name="about"></textarea>
                        </div>    
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                         <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="stayOnMars" name="stay" checked>
                            <label class="form-check-label" for="stayOnMars">Готов остаться на Марсе</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                  </body>
                </html>"""
    elif request.method == 'POST':
        res = request.files['file']
        print('file=', res.read())
        print('astro_sname=', request.form.get('astro_sname'))
        print('astro_name=', request.form.get('astro_name'))
        print('profession=', request.form.get('profession'))
        print('sex=', request.form.get('sex'))
        print('about=', request.form.get('about'))
        print('stay=', request.form.get('stay'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
# Часть 6. Ва   рианты выбора
def planet_variants(planet_name):
    if planet_name == "Меркурий":
        stroka = """
        <div class ="alert alert-dark" role="alert"><b>Шанс побывать близко к солнцу.</b></div>
        <div class ="alert alert-success" role="alert"><b>Самая маленькая планета - легко обойдете пешком.</b></div>
        <div class ="alert alert-light" role="alert"><b>В году всего 1.5 меркурианских суток - как тебе пожить в таких условиях?</b></div>
        <div class ="alert alert-info" role="alert"><b>Среди геологов есть мнение, что он покрыт алмазами. Хочешь проверить?</b></div>
        <div class ="alert alert-warning" role="alert"><b>Ждем на Меркурии!</b></div>"""
    elif planet_name == "Венера":
        stroka = """
        <div class ="alert alert-dark"  role="alert"><b>Испытай парниковый эффект на себе.</b></div>
        <div class ="alert alert-success" role="alert"><b>Если ты всегда шел против толпы,то Венера - твой выбор!</b></div>
        <div class ="alert alert-light"  role="alert"><b>(как известно, она вращается в другую сторону, чем другие планеты)</b></div>
        <div class ="alert alert-info"  role="alert"><b>Овеянная легендами Утренняя Звезда</b></div>
        <div class ="alert alert-warning"  role="alert"><b>Ждем на Венере!</b></div>"""
    elif planet_name == "Марс":
        stroka = """
         <div class ="alert alert-dark"  role="alert"><b>Эта планета близка к Земле.</b></div>
         <div class ="alert alert-success"  role="alert"><b>На ней много необходимых ресурсов</b></div>
         <div class ="alert alert-light"  role="alert"><b>На ней есть вода и атмосфера</b></div>
         <div class ="alert alert-info"  role="alert"><b>Есть даже небольшое магнитное поле</b></div>
         <div class ="alert alert-warning"  role="alert"><b>Начни строить будущее сегодня - лети на Марс!</b></div>"""
    else:
        stroka = """
                 <div class ="alert alert-warning"  role="alert"><b>Такая планета не найдена</b></div>"""
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Твое предложение: {planet_name}</h1>
                    {stroka}
                    <div class="alert alert-danger" role="alert"><b>Присоединяйся!</b></div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
# Часть 7. Результаты отбора
def otbor_result(nickname, level, rating):
    if rating > 50:
        if level== 10:
            stroka1 = "Поздравляем, ты успешно завершил отбор на миссию."
        else:
            stroka1 = "Поздравляем, ты успешно прошел на следующий уровень."
    else:
        stroka1 = "К сожалению, твой результат недостаточен, ты сошел с дистанции"
    if rating > 50:
        stroka = f"""<div class ="alert alert-success" role="alert"><b>{stroka1}</b></div>"""
    else:
        stroka = f"""<div class ="alert alert-danger" role="alert"><b>{stroka1}</b></div>"""

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результат отбора</h1>
                    <h3>претендента на участие в миссии {nickname}</h3>
                    {stroka}
                    <div class="alert alert-dark" role="alert"><b>Твой рейтинг после {level} этапа отбора</b></div>
                    <div class="alert alert-info" role="alert"><b>составляет {rating}</b></div>
                    <div class="alert alert-success" role="alert"><b>Желаем удачи!</b></div>
                  </body>
                </html>"""

app.run(debug=True, port=8080)