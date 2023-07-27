from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_jobs():
    api_key = 'AIzaSyCgn_YK7927yAncAl_z4ObaCHkuFzIgOow'  # Replace with your actual Google API key
    cse_id = '832834dab627040ba'  # Replace with your actual CSE ID

    keyword = request.args.get('web developer')
    location = request.args.get('toronto')

    # Construct the Google CSE search query
    search_query = f'site:https://www.linkedin.com jobs {keyword} {location}'  # Replace 'example.com' with the desired job search website

    # Make a request to the Google CSE API
    api_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={search_query}'
    response = requests.get(api_url)
    data = response.json()

    # Extract relevant job information from the API response
    job_listings = []
    if 'items' in data:
        for item in data['items']:
            job_title = item['title']
            job_url = item['link']
            snippet = item['snippet']

            job_listings.append({
                'job_title': job_title,
                'job_url': job_url,
                'snippet': snippet
            })

    return jsonify(job_listings)

if __name__ == '__search_jobs__':
    app.run(host='localhost', port=5000, debug=True)