{% extends "base.tpl" %}
{% block title %}
    Portfolio
{% endblock %}

{% block style %}
<style>
.portfolio-item { 
    font-family: Nunito; 
}
</style>
{% endblock %}

{% block script %}
{% endblock %}

{% block content %}
    {% include('navbar.html.j2') %}
    <div class="container">
        <div class="main">
            {% import "portfolio-item.tpl" as item %}

            <div class="portfolio-item">
                {{ item.title(
                    "ketocalc"
                    )
                }}

                {{ item.about(
                    "Aplikace pro výpočet a správu surovin, receptů a diet ketogenní diety"
                    )
                }}

                {{ item.motivation([
                    "projekt na předmět Databázové aplikace",
                    "na žádost známé, které podobný nástroj chyběl",
                    "možnost vytvořit první větší projekt a naučit se, co všechno je pro něj třeba"
                    ])
                }}

                {{ item.technology({
                    "Databáze": [
                        "MySQL"
                        ],
                    "Backend": [
                        "Python 3",
                        "Flask",
                        "SQLAlchemy"
                        ],
                    "Frontend": [
                        "jQuery",
                        "Bootstrap",
                        "stimulus"
                        ],
                    "Administrace": [
                        "Heroku",
                        "gunicorn",
                        "nginx, Apache", 
                        "FreeBSD->Debian",
                        "git (via github)"
                        ]
                 })
                }}

                {{ item.functions([
                        "výpočet receptu (pomocí numpy)",
                        "registrace a přihlašování"
                    ])
                }}

                {{ item.learned([
                    "Napojení na MySQL pomocí ORM SQLAlchemy",
                    "Framework Flask",
                    "prevence SQL injection ve Flasku",
                    "Google OAuth",
                    "základy AJAX",
                    "posílání emailů z webové aplikace",
                    "deploy over Heroku",
                    "deploy na Flask-Gunicorn webserveru na domácím FreeBSD/Debian serveru"
                    ])
                }}

                {{ item.time(
                    "cca 150 hodin"
                    )
                }}
            </div>
        </div>
    </div>
{% endblock %}

