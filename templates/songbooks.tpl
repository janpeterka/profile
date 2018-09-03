
{% extends "base.tpl" %}
{% block title %}
    Zpěvníky
{% endblock %}

{% block style %}
    <style type="text/css" media="screen">

    div.songbook{
        border-radius: 6px;
        padding: 10px 30px;
        margin: 5px;
        /*background-color: #fff;*/
        background-color: #eff6ff;

        box-shadow: 0 0 0 1px rgba(89,105,129,.1),0 1px 3px 0 rgba(89,105,129,.1),0 1px 2px 0 rgba(0,0,0,.05);
    }

    a.songbook{
        color: black;
    }

    a.songbook i{
        margin-right: 7px;
    }

    </style>    
{% endblock %}

{% block script %}

{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
    <div class="container" style="margin-top:20px">
        <div class="main">
            <table>
            <td class="col-2"></td>

            <td class="col-10">

            {% for folder in folders %}

            	<div class="row">

	                <div class="songbook col-5">
	                    <a class="songbook" href="/{{ folder.name }}.pdf" download> <i class="fas fa-download"></i> {{ folder.name }} [.pdf] </a>
	                </div>
	                <div class="songbook col-5">
	                    <a class="songbook" href="/{{ folder.name }}.docx" download> <i class="fas fa-download"></i> {{ folder.name }} [.docx] </a>
	                </div>

            	</div>
			
            {% endfor %}


            </td>

            <td class="col-2"></td>
            </table>
            
        </div>
    </div>
{% endblock %}