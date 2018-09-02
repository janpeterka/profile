{% extends "base.tpl" %}
{% block title %}
    Portfolio
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
            <table>
            <td class="col-2"></td>

            <td class="col-8">
                <h1>Na portfoliu se usilovně pracuje</h1>
            </td>

            <td class="col-2"></td>
            </table>
        	
        </div>
    </div>
{% endblock %}

