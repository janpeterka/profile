cvlc http://192.168.1.30:8080/video --sout "#transcode{vcodec=theo,vb=800,scale=Auto,acodec=vorb,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=http{mux=ogg,dst=127.0.0.1:8080/webcam.ogg},dst=display}" --no-sout-all --sout-keep