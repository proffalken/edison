<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
    <title>Edison - {{ title }}</title>
    <style type='text/css' media='all'>
        @import url('/media/css/edison.css');
    </style>
    <script type="text/javascript" src="/media/js/jquery-1.4.3.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            $(" #nav ul ").css({display: "none"}); // Opera Fix
            $(" #nav li").hover(function(){
                    $(this).find('ul:first').css({visibility: "visible",display: "none"}).show(400);
                    },function(){
                    $(this).find('ul:first').css({visibility: "hidden"});
                });
        });
    </script>
</head>
<body>
<div id='page'>
    <div id='header'>
        <div id='logo'>
            <img src='/media/images/edison_small.jpg' />
        </div>
        <div id='branding'>
            <h1>Edison</h1>
            <p><i>"The Hamster that keeps your infrastructure running..."</i></p>
        </div>
        <div id='section_heading'>
            {% block title %}
                <h5>
                    {% if section_item_name %}
                        Viewing: {{ title }}
                    {% else %}
                        Welcome to Edison, Please choose an action from the navigation below...
                    {% endif %}
                </h5>
            {% endblock %}
        </div>
        {% if user.is_authenticated %}
            <p>Welcome {{ user.first_name }} {{ user.last_name }}</p>
        {% endif %}
        <div  class='clear'></div>
    </div>
    <div id='content'>
        {% block navigation %}
            {% include 'nav.tpl' %}
        {% endblock %}
        {% block main %}
            <div id='main'>
                <h2>{{ title }}</h2>
            </div>
        {% endblock %}
        <div  class='clear'></div>
    </div>
</div>
</body>
</html>

