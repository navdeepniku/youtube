from __future__ import unicode_literals
from flask import url_for
from flask import request, redirect, render_template, session

from youtube import app

@app.route('/', methods=['GET','POST'])
def index():
	try:
		if request.method == 'POST':
			session['video_url'] = request.form['video_url']
			return redirect(url_for('fetch_video'))
		return render_template('index.html')

	except:
		return "error occoured! Return to home: <a href='"+url_for('index')+"'>Home</a>"

@app.route('/fetch_video')
def fetch_video():
	try:
		import youtube_dl
		
		ydl_opts = {
		        'outtmpl': 'app.config["DOWNLOAD_FOLDER"]%(id)s.%(ext)s'
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			video_info = ydl.extract_info(session['video_url'])
			session['filename'] = video_info['id']+"."+video_info['ext']
			
		return redirect(url_for('play_video'))
		
	except: 
		return "error occoured in fetching Video! Make sure you entered correct URL. Return to home:<a href='"+url_for('index')+"'>Home</a> "

@app.route('/play_video')
def play_video():
	return render_template('play_video.html')
