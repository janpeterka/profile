{% extends "base.tpl" %}
{% block title %}
    Zpěvníky
{% endblock %}

{% block style %}
    <style type="text/css" media="screen">
    div.songbook{
        border-radius: 20px;
        padding: 10px 30px;
        margin: 5px;
        border: 2px solid black;

    }

    a.songbook{
        color: black;
    }
    </style>    
{% endblock %}

{% block script %}

{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
    <div class="container">
        <div class="main">
            <table>
            <td class="col-2"></td>

            <td class="col-8">
                <div class="songbook">
                    <a class="songbook" href="/static/files/songbooks/songbook_main.pdf" download> Hlavní zpěvník [PDF] </a>
                </div>
            </td>

            <td class="col-2"></td>
            </table>
            
        </div>
    </div>
{% endblock %}