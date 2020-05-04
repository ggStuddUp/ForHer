import configparser
import os


class Config:
    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        self.conf_path = os.path.join(cur_path, "spider.ini")
        self.conf = configparser.ConfigParser()
        self.conf.read(self.conf_path, encoding='utf-8')

    def get_conf_data(self):
        """
        返回配置文件的配置信息
        :return: dict
        """
        dic = {}
        dic['product'] = self.conf.get('bug', 'product')
        dic['iver'] = self.conf.get('bug', 'iver')
        return dic

    def change_conf_data(self, conf_dict):
        """
        更新配置文件信息
        :param conf_dict: 字典类型
        :return:
        """
        try:
            self.conf.set('bug', 'product', conf_dict['product'])
            self.conf.set('bug', 'iver', conf_dict['iver'])
        except Exception as e:
            print(e, "\n配置文件传入参数有误，请传入字典类型，且包含'product'和'iver'这两个key")
        self.conf.write(open(self.conf_path, 'w', encoding='utf-8'))


if __name__ == "__main__":
    conf = Config()
    conf_data = conf.get_conf_data()
    print(conf_data)
    conf_dic = {}
    conf_dic['product'] = 'nimo_ios'
    conf_dic['iver'] = '1.9.0'
    conf.change_conf_data(conf_dict=conf_dic)
    new_conf_data = conf.get_conf_data()
    print(new_conf_data)

    conf.change_conf_data(conf_dict={'product': 'nimo_android', 'iver': '1.8.0'})
    print(conf.get_conf_data())
