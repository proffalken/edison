{% extends 'base.tpl' %}
{% block main %}
    <div class='span-10 last'>
        {% if messages %}
            {% for message in messages %}
                {{message}}
            {% endfor %}
        {%endif %}
    </div>
    <div class='span-10 last'>
        <form method="post" action="">
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Owner'>Owner:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Owner }} {{ form.Owner.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Class'>Class:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Class }} {{ form.Class.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Hostname:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Hostname }} {{ form.Hostname.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Location:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Rack }} {{ form.Rack.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>IP Address:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.NetworkInterface }} {{ form.NetworkInterface.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Asset Number:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Asset }} {{ form.Asset.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Support Tag:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.SupportTag }} {{ form.SupportTag.errors }}
	    </div>
	</div>
	<div class='span-8 last'>
                <button class="button positive">
                <img src="/media/images/icons/tick.png" alt=""/>Update
                </button>
                <input type="hidden" name="next" value="/" />
            </div>
        </form>
    </div>
{% endblock %}
