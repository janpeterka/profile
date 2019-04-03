{% extends "base.tpl" %}
{% block title %}
    Portfolio
{% endblock %}

{% block style %} 
    <style type="text/css" media="screen">

    div.main {
        margin-left: 5%; 
    }

    div.row {
        margin-top: 20px;
    }

    span.file {
        border-radius: 6px;
        background-color: #eff6ff;
        box-shadow: 0 0 0 1px rgba(89,105,129,.1),0 1px 3px 0 rgba(89,105,129,.1),0 1px 2px 0 rgba(0,0,0,.05);
        padding: 6px 30px;
    }

/*    span.download {
        margin-right: 10px;
    }*/

    span.download {
        margin-right: 10px;
        /*margin-top: 30px;*/

        border-radius: 6px;
        background-color: #eff6ff;
        box-shadow: 0 0 0 1px rgba(89,105,129,.1),0 1px 3px 0 rgba(89,105,129,.1),0 1px 2px 0 rgba(0,0,0,.05);
        padding: 10px 30px;
    }

/*     span.download a i.fa-file-audio {
        color: red;
     }

     span.download a i.fa-file-video {
        color: blue;
     }*/

     video {
        border: 2px black solid;
        margin-top: 20px;
     }

    </style>  
{% endblock %}

{% block script %}
{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
    <div class="container main">
        <span class="stream col-6">
            <img src="http://jpeterka.cz:5500/video" alt="video_2" style="width: 700px; margin: 50px">
        </span>

        <span class="downloads col-6">
            {% for folder in folders %}
                <div class="row">
                    <span class="file col-6" >
                        {{ folder.name }}
                    </span>

                    <span class="col-6">
    
                        <!-- Video -->
                        <span class="download">
                            <a class="video" href="/mms/{{ folder.name }}.mkv" download> <i class="fas fa-file-video"></i> mkv (original)</a>
                        </span>

                        <span class="download">
                            <a class="video" href="/mms/{{ folder.name }}.flv" download> flv <i class="fas fa-file-video"></i> </a>
                        </span>

                        <!-- Audio -->
                        <span class="download">
                            <a class="audio" href="/mms/{{ folder.name }}.mp3" download> <i class="fas fa-file-audio"></i> mp3 </a>
                        </span>

                    </span>
                </div>
            {% endfor %}
        </span>

    </div>
{% endblock %}

