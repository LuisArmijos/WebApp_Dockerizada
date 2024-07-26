from flask import Flask, render_template, request
import requests

app = Flask(__name__)

IMAGES = [
    "https://dragonball-api.com/transformaciones/goku_ultra.jpg",
    "https://dragonball-api.com/transformaciones/gogeta__bm__ssb_evolution___1__con_aura__by_ssjrose890_df682g0-fullview.jpg",
    "https://dragonball-api.com/transformaciones/beast_gohan___dragon_ball_super_super_hero_by_rmrlr2020_dfbqvta-pre.jpg"
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
