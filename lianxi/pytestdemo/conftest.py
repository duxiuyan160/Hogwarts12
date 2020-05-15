import pytest


# 不带参数的fixture默认参数为scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")


# def pytest_collection_modifyitems(session, config, items: list):
# # #     for item in items.count():
# # #         if "add" in item.nodeid:
# # #             item.add_marker(pytest.mark.add)
# # #         elif 'div' in item.nodeid:
# # #             item.add_marker(pytest.mark.add)

def pytest_collection_modifyitems(session, config, items:list):
    # print(items)
    # print(type(items))
    for item in items.nodeid:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
# def pytest_configure(config):
#     marker_list = ["search","login"]     #标签名集合
#     for markers in marker_list:
#         config.addinivalue_lin("markers",markers)
