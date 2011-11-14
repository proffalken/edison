{% extends 'base.tpl' %}
{% block main %}
    <div>
        {% if messages %}
            {% for message in messages %}
                {{message}}
            {% endfor %}
        {%endif %}
    </div>
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
            {% endfor %}
            <div>
                <button class="button positive">
                <img src="/media/images/icons/tick.png" alt=""/>Update
                </button>
                <input type="hidden" name="next" value="/" />
            </div>
        </form>
    </div>
{% endblock %}
