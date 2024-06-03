
from jinja2 import Template 

template = """
{% for router in routers %}
Router Name is {{ router }}
{% endfor %}
"""

data = {'routers': ['r1','r2','r3','r4']}

load_my_template = Template(template)
render_my_data_into_template = load_my_template.render(data)
print(render_my_data_into_template)