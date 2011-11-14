<ul id="nav">
    <li><a href="/cmdb/">Configuration Management</a>
        <ul>
            <li><a href="/cmdb/list">List</a></li>
            <li><a href="/cmdb/add">Add</a></li>
            <li><a href="/cmdb/edit">Edit</a></li>
        </ul>
    </li>
    <li><a href="/changemanagement/">Change Management</a>
        <ul>
            <li><a href="/changemanagement/list">List</a></li>
            <li><a href="/changemanagement/add">Add</a></li>
            <li><a href="/changemanagement/edit">Edit</a></li>
        </ul>
    </li>
    <li><a href="/orchestra/">Orchestration</a>
        <ul>
            <li><a href="/orchestra/list">List</a></li>
            <li><a href="/orchestra/add">Add</a></li>
            <li><a href="/orchestra/edit">Edit</a></li>
        </ul>
    </li>
    <li>
        {% if user.is_authenticated %}
            <a href='/accounts/logout'>Logout</a>
        {% else %}
            <a href='/accounts/login'>Login</a>
        {% endif %}
    </li>
</ul>
<div  class='clear'></div>
