{% extends "base.tpl" %}
{% block title %}
    Tady nemáte co pohledávat
{% endblock %}

{% block content %}
    {% include('navbar.html.j2') %}
    <div class="container">
        <div class="main">
            <table>
            <td class="col-2"></td>

            <td class="col-8">
                <h1>Na této stránce byste neměli být</h1>
                Radši se vraťte na <a href="/">hlavní stránku</a>
            </td>

            <td class="col-2"></td>
            </table>
        	
        </div>
    </div>
{% endblock %}

