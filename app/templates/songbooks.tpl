{% extends "base.tpl" %}
{% block title %}
    Zpěvníky
{% endblock %}

{% block style %}
    <style type="text/css" media="screen">

    div.main {
        margin-left: 5%; 
    }

    div.row {
        margin-top: 5px;
    }

    span.songbook {
        border-radius: 6px;
        background-color: #eff6ff;
        box-shadow: 0 0 0 1px rgba(89,105,129,.1),0 1px 3px 0 rgba(89,105,129,.1),0 1px 2px 0 rgba(0,0,0,.05);
        padding: 6px 30px;
    }

    span.download {
        margin-right: 10px;
    }

    span.download a.songbook i{
        border-radius: 6px;
        background-color: #eff6ff;
        box-shadow: 0 0 0 1px rgba(89,105,129,.1),0 1px 3px 0 rgba(89,105,129,.1),0 1px 2px 0 rgba(0,0,0,.05);
        padding: 10px 30px;
    }

     span.download a.songbook i.fa-file-pdf {
        color: red;
     }

     span.download a.songbook i.fa-file-word {
        color: blue;
     }

    </style>    
{% endblock %}

{% block script %}

{% endblock %}

{% block content %}
    {% include('navbar.html.j2') %}
    <div class="container" style="margin-top:20px">
        <div class="main">

            {% for folder in folders %}

            	<div class="row col-8">
                    <span class="songbook col-8" >
                        {{ folder.name }}
                    </span>

                    <span class="col-4">
                        
                        <span class="download">
                            <a class="songbook" href="/songbooks/{{ folder.name }}.pdf" download> <i class="fas fa-file-pdf"></i></a>
                        </span>

                        <span class="download">
                            <a class="songbook" href="/songbooks/{{ folder.name }}.docx" download><i class="fas fa-file-word"></i></a>
                        </span>

                    </span>
            	</div>
			
            {% endfor %}

        <div style="margin-left: 10px; margin-top: 10px">
            a další zpěvníky, které mám rád: <br>
            <a href="https://nerez.szm.com/nerez.pdf">Nerez</a> <br>
            <a href="https://navarova.szm.com/navarova.pdf">Navarová</a> <br>
        </div>
            
        </div>
    </div>
{% endblock %}
