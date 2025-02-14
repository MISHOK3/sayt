from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <a href="/random_fact">Посмотреть случайный факт!</a><br>
        <a href="/secret">Secret Google Maps</a>
    '''


@app.route('/random_fact')
def random_fact():
    facts_list = [
        ' Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. '
        ' Он утверждает, что социальные сети собирают огромное количество информации о нас, '
        ' которую потом можно использовать для манипулирования нашими мыслями и поведением. ',

        ' Согласно исследованию, проведенному в 2019 году, '
        ' более 60% людей отвечают на рабочие сообщения в своих смартфонах в '
        ' течение 15 минут после того, как они вышли с работы. ',

        ' Социальные сети имеют как позитивные, так и негативные стороны, '
        ' и мы должны быть более осознанными в использовании этих платформ.'

    ]

    return f'<p>{random.choice(facts_list)}</p>'

@app.route('/secret')
def secret():
    secret_coordinates = [
        'кординаты: 32°10\'15.7"N 110°51\'00.4"W',

        'кординаты: 38°43\'27.7"N 93°32\'55.0"W ',

        'кординаты: 24°35\'40.0"N 76°48\'35.4"W ',

        'кординаты: 40°27\'28.5"N 93°18\'48.1"E'

    ]

    return f'<p>{random.choice(secret_coordinates)}</p>'



app.run(debug=True)
