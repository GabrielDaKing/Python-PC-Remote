from flask import Flask, render_template, redirect
import qrcode
import keyboard
import socket 


import os
import threading

app = Flask(__name__)
app.secret_key = "gabriel"

@app.route('/remote')
def base():

	return render_template('remote.html')

@app.route('/previous')
def previous():
	keyboard.press_and_release('previous track')
	return redirect("/remote")
@app.route('/play_pause')
def play():
	keyboard.press_and_release('play/pause media')
	return redirect("/remote")
@app.route('/next')
def next():
	keyboard.press_and_release('next track')
	return redirect("/remote")
@app.route('/volume_up')
def volume_up():
	keyboard.press_and_release('volume up')
	return redirect("/remote")
@app.route('/volume_down')
def volume_down():
	keyboard.press_and_release('volume down')
	return redirect("/remote")
@app.route('/mute')
def mute():
	keyboard.press_and_release('volume mute')
	return redirect("/remote")

@app.route('/')
def connect():
	
	return render_template('connect.html')

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	s.connect(("192.168.0.1", 80))

	IPAddr = (s.getsockname()[0]) 
	s.close()

	return IPAddr

if __name__ == "__main__":
	
	img = qrcode.make('http://'+get_ip()+':25802/remote')
	img.save('static/images/connect.png')
	app.run(debug=True,host='0.0.0.0',port=25802)