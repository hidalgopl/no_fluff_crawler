from collections import OrderedDict


def create_output_dict(title, salary, requirements, specs):
    details = OrderedDict()
    names = ('title', 'salary', 'requirements', 'specs')
    for name in names:
        details[name] = locals()[name]
    return details
