from flask import Flask, render_template, request
import requests

app = Flask(__name__)

IMAGES = [
    "https://static.bandainamcoent.eu/high/dragon-ball/dragonball-project-z/00-page-setup/dbzk_game-thumbnail.jpg",
    "https://i.pinimg.com/564x/ae/58/76/ae5876ced7178ab2086107252e459599.jpg",
    "https://bnetcmsus-a.akamaihd.net/cms/blog_header/yr/YRN3K8WPLESY1663891400581.jpg"
]

IMAGGA_API_KEY = "acc_73a7a1e8a8b83c4"
IMAGGA_API_SECRET = "93a1d0e208187c26397d62e5d9134fc6"

@app.route('/')
def index():
    return render_template('index.html', images=IMAGES)

@app.route('/analyze', methods=['GET'])
def analyze():
    results = []
    for image_url in IMAGES:
        response = requests.get(
            'https://api.imagga.com/v2/tags',
            auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET),
            params={'image_url': image_url}
        )
        if response.status_code == 200:
            data = response.json()
            tags = data['result']['tags']  
            top_tags = tags[:2] 
            results.append({'url': image_url, 'tags': top_tags})
        else:
            results.append({'url': image_url, 'tags': [{'tag': {'en': 'Error al analizar imagen'}, 'confidence': 0}]})

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
