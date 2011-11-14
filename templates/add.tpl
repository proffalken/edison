{% extends 'base.tpl' %}
{% block main %}
    <div>
        {% if messages %}
            {% for message in messages %}
                {{message}}
            {% endfor %}
        {%endif %}
    <div>
        <form method="post" action="">
            {{ formset.management_form }}
            {% for form in formset.forms %}
                {% for field in form %}
                    <div>
                        <div>{{ field.label_tag }}:</div>
                        <div> {{ field }}</div>
                    </div>
                {% endfor %}
                <div>
                    <button class="button positive">
                    <img src="/media/images/icons/tick.png" alt=""/>Add
                    </button>
                    <input type="hidden" name="next" value="/" />
                </div>
            {% endfor %}
        </form>
    </div>
{% endblock %}
