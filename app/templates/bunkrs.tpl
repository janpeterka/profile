{% extends "base.tpl" %}
{% block title %}
    Bunkrs
{% endblock %}

{% block style %}
    <style type="text/css" media="screen">
    .main{
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px;
    }
    </style>    
{% endblock %}

{% block script %}

{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
    <div class="container">
        <div class="main">
            
            <button class="btn"><a href="/get_bunkrs">Načíst nové</a></button>

            <table class="table">
                <tr>
                    <th>název</th>
                    <th>datum prodeje</th>
                    <th>katastr</th>
                    <th>obec</th>
                    <th>kraj</th>
                    <th>území</th>
                    <th>minimální cena</th>
                    <th>přidáno dne</th>
                    <th>offer_type</th>
                </tr>
            {% for bunkr in bunkrs %}
                <tr>
                    <td><a href="{{ bunkr.link }}">{{ bunkr.name }}</a></td>
                    <td>{{ bunkr.sale_date}}</td>
                    <td>{{ bunkr.katastr }}</td>
                    <td>{{ bunkr.obec }}</td>
                    <td>{{ bunkr.kraj }}</td>
                    <td>{{ bunkr.uzemi }}</td>
                    <td>{{ bunkr.min_sale_price }}</td>
                    <td>{{ bunkr.created_at.strftime('%d.%m.%Y') }}</td>
                    <td>{{ bunkr.offer_type }}</td>
                </tr>
            {% endfor %}   
            </table>
        </div>
    </div>
{% endblock %}

