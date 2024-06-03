
from jinja2 import Template 

template = """
{% for router in routers %}
Router Name is {{ router.name }}
Router location is {{ router.loc }}
{% endfor %}
"""

data = {'routers': [{'name':'r1','loc':'l1'},{'name':'r2','loc':'l2'},{'name':'r3','loc':'l3'}]}

load_my_template = Template(template)
render_my_data_into_template = load_my_template.render(data)
print(render_my_data_into_template)