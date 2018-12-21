{% extends "base.tpl" %}
{% block title %}
    Pexeso
{% endblock %}

{% block links %}
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='pexeso.css') }}">
{% endblock %}

{% block style %}  
{% endblock %}

{% block script %}
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
    <div class="container">
        <div class="main">
            <div class="col-sm-8 col-xs-12" id="container"></div>

            <div class="col-sm-4 col-xs-12">
                <div class="col-sm-12 col-xs-6" id="scoreboard" class="label label-info">
                    <strong><span id="diff_show"></span></strong>
                    <br>
                    <span id="moves_full"><span id="moves"></span> moves </span>
                    <br>
                    <span id="timer_full"><span id="timer"></span> seconds</span>
                    <br>
                    <span id="score_full"><span id="score"></span> points for you</span>
                    <br>
                    <span id="npc_score_full"><span id="npc_score"></span> points for npc</span>
                    <!-- <br> -->
                    <!-- <span id="logbook"></span> -->
                </div>
                <div class="col-sm-12 col-xs-5" id="settings">
                    <label for="size">Select size:</label>
                    <select id="size" class="form-control">
                        <option selected="selected" value=4>4</option>
                        <option value=5>5</option>
                        <option value=6>6</option>
                        <option value=7>7</option>
                        <option value=8>8</option>
                        <option value=9>9</option>
                        <option value=10>10</option>
                        <option value=11>11</option>
                        <option value=12>12</option>
                    </select>
                    <label for="difficulty">Select difficulty:</label>
                    <select id="difficulty" class="form-control">
                        <option selected="selected" value=0>Singleplayer</option>
                        <option value=1>Beginner</option>
                        <option value=2>Easy</option>
                        <option value=3>Advanced</option>
                        <!-- <option value=4>Expert</option> -->
                    </select>
                    <button class="btn btn-primary" id="newgame" onclick="restart()">New Game</button>
                </div>
                <div class="col-xs-1"></div>

            </div>
        	
        </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')
    </script>
    <script src={{ url_for('static', filename='pexeso.js') }}></script>

{% endblock %}

