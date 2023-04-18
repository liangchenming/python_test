import os
import yaml




class YamlUtil:
    # 读取extract.yml文件
    def read_extract_yaml(self, value_yaml):
        with open("/Users/motong/PycharmProjects/pythontest/testcase/yaml/" + value_yaml, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value;

    # 写入extract.yml文件
    def write_extract_yaml(self, data, value_yaml):
        with open(os.getcwd() + "/yaml/" + value_yaml, mode='w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
