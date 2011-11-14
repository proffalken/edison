{% extends 'base.tpl' %}
{% block main %}
    {% if section_item_name %}
        <h5>Welcome to {{ title }}</h5>
        <p>Please select an action from the list below:</p>
        <ul>
            <li><a href="list/">List all {{ section_item_name }}s</a></li>
        </ul>
    {% else %}
        <p> Welcome to Edison, Please choose an action from the list on your left...</p> 
    {% endif %}
{% endblock %}
