from flask import Flask, render_template, url_for, request, Response
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

@app.route('/' , methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if 'https://www.linkedin.com/posts' in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text,'lxml')
            video = soup.find('video')['data-sources']
            links = re.search("(?P<url>https?://[^\s]+)", video).group("url")
            download_link = re.search(r'^(.+?)"' , links)[0].replace('"', '')
            req = requests.get(download_link)
            return Response(
                    req,
                    mimetype="video/mp4",
                    headers={"Content-disposition":
                            "attachment; filename=videp.mp4"})     
        else:
            return render_template('index.html')
           
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)