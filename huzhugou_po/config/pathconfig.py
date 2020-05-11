import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取测试数据文件所在路径
CONFIG_DIR = os.path.join(BASE_DIR,"config")
USERCONFIG_FILE_PATH = os.path.join(CONFIG_DIR,"userconfig.yaml")