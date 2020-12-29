# import pytest
#
# def pytest_collection_modifyitems(session, config, items:list):
#     print(items)
#     print(type(items))
#     for item in items:
#         if 'add' in item.nodeid:             #指定mark标签   Terminal: pytest -m add test_calc.py -vs
#             item.add_marker(pytest.mark.add)
#
#         elif 'div' in item.nodeid:
#             item.add_marker(pytest.mark.div)
#
#     items.reverse()    #reverse：反向执行