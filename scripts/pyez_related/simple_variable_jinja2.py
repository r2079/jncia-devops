# Print hello <name> given the variable as name. 
from jinja2 import Template

template = "hello {{ name }}"
data = {'name': 'juniper'}

load_my_template_into_jinja = Template(template)
render_my_final_data = load_my_template_into_jinja.render(data)
print(render_my_final_data)
