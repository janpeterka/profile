cvlc http://192.168.1.24:8080/video --sout "#transcode{vcodec=theo,vb=800,scale=Auto,acodec=vorb,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=http{mux=ogg,dst=:8080/},dst=display}" --no-sout-all --sout-keep &
export FLASK_APP=Dropbox/Programming/profile/app.py
python -m flask run
