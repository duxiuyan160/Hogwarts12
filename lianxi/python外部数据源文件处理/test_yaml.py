import yaml

#yaml.load 后可以是文件，也可以是yaml格式
def test_loadyaml():
    print(yaml.load(open("demo.yaml")))
    # print(yaml.load("""
    # - Hesperiidae
    # - Papilionidae
    # - Apatelodidae
    # - Epiplemidae
    # """))

#将字典或列表格式转换成yaml格式
def test_dumpyaml():
    with open("demo3.yml","w") as f:
        yaml.dump({'a': [1, 2]},stream=f)