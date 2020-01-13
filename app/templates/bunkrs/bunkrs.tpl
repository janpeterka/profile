{% extends "base.tpl" %}
{% block title %}
    Bunkrs
{% endblock %}

{% block links %}
    {{ super() }}
{% endblock %}

{% block script %}
    {{ super() }}
    {# <script src="https://unpkg.com/bootstrap-table@1.14.2/dist/bootstrap-table.min.js"></script> #}
{% endblock %}

{% block content %}
    {% include('navbar.html.j2') %}
    <div class="container">
        <div class="main">
            
            <button class="btn"><a href="/get_bunkrs">Načíst nové</a></button>

            <table
              class="table"
              data-toggle="table"
              data-sort-class="table-active"
              data-sortable="true"
              {# data-height="460" #}
              >
              <thead>
                <tr>
                    <th data-field="name">název</th>
                    <th data-sortable="true">datum prodeje</th>
                    <th>katastr</th>
                    <th>obec</th>
                    <th>kraj</th>
                    <th>území</th>
                    <th>minimální cena</th>
                    <th data-sortable="true">přidáno dne</th>
                    <th data-sortable="true">zdroj</th>
                </tr>
              </thead>

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

