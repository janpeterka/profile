

            {% macro title(text) %}
                <h1>{{ text }}</h1>
            {% endmacro %}

            {% macro about(text) %}
                <div class="portfolio-about">
                    <h2>O co jde?</h2>
                    {{ text }}
                </div>
            {% endmacro %}

            {% macro motivation(items) %}
            <div class="portfolio-motivation">
                <h2>Motivace</h2>
                <ul>
                    {% for item in items %}
                        <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endmacro %}


            {% macro technology(dict) %}
            <div class="portfolio-technology">
                <h2>Použité technologie</h2>
                {% for key, value in dict.items() %}
                    <h3>{{ key }}</h3>
                    <ul>
                    {% for item in value %}
                        <li>{{ item }}</li>
                    {% endfor %}
                    </ul>
                {% endfor %}
            </div>
            {% endmacro %}

            {% macro functions(items) %}
            <div class="portfolio-functions">
                <h2>Klíčové funkce</h2>
                <ul>
                    {% for item in items %}
                        <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endmacro %}

            {% macro learned(items) %}
            <div class="portfolio-learned">
                <h2>Co jsem se naučil</h2>
                <ul>
                    {% for item in items %}
                        <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            {% endmacro %}
 
            {% macro time(text) %}
                <div class="portfolio-time">
                    <h2>Čas</h2>
                    {{ text }}
                </div>
            {% endmacro %}
