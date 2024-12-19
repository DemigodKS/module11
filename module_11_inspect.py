import inspect

def  introspection_info(*obj):

    count = []

    for i in obj:
        if i % 2:
            count.append(i)
    return len(count), count

infooo_ = introspection_info(3, 5, 2)
print(infooo_)
results_search = []
type_ = type(infooo_)
results_search.append(type_)

has_attr = hasattr(infooo_, 'count')
results_search.append(has_attr)

dir_ = dir(infooo_)
results_search.append(dir_)

module_ = inspect.ismodule(introspection_info)
results_search.append(module_)

inspect_1 = ['type', 'result of hasattr', 'results of dir', 'ismodule']
inspect_2 = results_search

results_search_1 = dict(zip(inspect_1, inspect_2))
print(results_search_1)

