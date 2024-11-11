from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', name="lowe")
@app.route('/image/<path:filename>')
def send_image(filename):
    return send_from_directory('image', filename)

@app.route('/quit')
def quit():
    return render_template("quit.html")


@app.route('/search')
def search():
    search_term = request.args.get('q')
    if search_term:
        results = search_subscriptions(search_term)
        return render_template('search_results.html', results=results)
    else:
        return render_template('index.html', name="lowe")



app.run(debug=False, host='0.0.0.0')

subscriptions = [
    {'name': 'Яндекс Плюс', 'description': 'Яндекс подписка плюс', 'link': 'https://plus.yandex.ru/'},
    {'name': 'иви', 'description': 'иви', 'link': 'https://www.ivi.ru/'},
    {'name': 'мтс премиум', 'description': 'мтс премиум', 'link': 'https://premium.mts.ru/'},
    {'name': 'Телеграм премиум', 'description': 'Телеграм премиум', 'link': 'https://t.me/PremiumRussia'},
    {'name': 'сбер прайм', 'description': 'сбер прайм', 'link': 'https://www.sberbank.com/sberprime'},
    {'name': 'Старт', 'description': 'подписка на кинотеатр СТАРТ', 'link': 'https://start.ru/auth'},
    {'name': 'Premier', 'description': 'онлайн кинотиатор premier', 'link': 'https://premier.one/'},
    {'name': 'Wink', 'description': 'Онлайн кинотеаотр Wink', 'link': 'https://wink.ru/music-buy'},
    {'name': 'Mybook', 'description': 'Сервес для чтения книг Mybook', 'link': 'https://mtbook.ru/payments/'},
]

def search_subscriptions(search_term):
    results = []
    for subscription in subscriptions:
        if search_term.lower() in subscription['name'].lower() or search_term.lower() in subscription['description'].lower():
            results.append(subscription)
    return results
