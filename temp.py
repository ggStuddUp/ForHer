import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_center.settings")# project_name 项目名称
django.setup()
from django.utils import timezone
from data.models import DataCenter

# dc = DataCenter()
# dc.eid = '2222'
# dc.stime = timezone.now()
# dc.save

demo_list = [{'eid': 'startup', 'stime': '2020-04-29 23:59:53', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7986b4a81f7475a5', 'id': 'AXHGqo2rLS0XJov-iJWb', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:59:40', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7986b4a81f7475a5', 'id': 'AXHGqldXLS0XJov-iJKN', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:55:34', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7986b4a81f7475a5', 'id': 'AXHGppKPLS0XJov-iF6j', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:06:14', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeWojLS0XJov-hapk', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:06:14', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeWo8QvbXa9dl-ehR', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:05:59', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeS5eQvbXa9dl-eTA', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:05:40', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeOM0QvbXa9dl-eAf', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:05:17', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeIyzLS0XJov-hZyt', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 23:05:16', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': '7f7b653b4615f050', 'id': 'AXHGeITKQvbXa9dl-dp9', 'ip': '154.213.3.116'}, {'eid': 'startup', 'stime': '2020-04-29 22:04:59', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': 'a957fcab4c194ef1', 'id': 'AXHGQVFBQvbXa9dl9nJH', 'ip': '154.213.3.113'}, {'eid': 'startup', 'stime': '2020-04-29 21:47:32', 'product': 'nimo_android', 'iver': '1.9.7', 'mid': 'e61a810fed43fc11', 'id': 'AXHGMV7RLS0XJov-gRsB', 'ip': '154.213.3.116'}]


for demo in demo_list:
    dc = DataCenter(eid=demo['eid'],
                    stime=demo['stime'],
                    product=demo['product'],
                    iver=demo['iver'],
                    mid=demo['mid'],
                    uid=demo['id'],
                    ip=demo['ip'])
    dc.save()

data_list = DataCenter.objects.all()
for data in data_list:
    print(data.stime)
