import unittest

from parameterized import parameterized

from woniubossAPIDDT.lib.training import Training
from woniubossAPIDDT.tools.service import Service
from woniubossAPIDDT.tools.uiti import uiti

test_info = uiti.get_json('..\\conf\\testdata.conf')
train_infos=uiti.trans_dict_tup(test_info[1])
follow_infos = uiti.trans_dict_tup(test_info[2])
query_infos = uiti.trans_dict_tup(test_info[3])
edit_infos = uiti.trans_dict_tup(test_info[4])
abandon_infos = uiti.trans_dict_tup(test_info[5])
transQuery_infos = uiti.trans_dict_tup(test_info[6])
see_infos = uiti.trans_dict_tup(test_info[7])
commit_infos = uiti.trans_dict_tup(test_info[8])
allQuery_infos = uiti.trans_dict_tup(test_info[9])
submit_infos = uiti.trans_dict_tup(test_info[10])
allot_infos = uiti.trans_dict_tup(test_info[11])
pubQuery_infos = uiti.trans_dict_tup(test_info[12])
owner_infos = uiti.trans_dict_tup(test_info[13])
class trainingTest(unittest.TestCase):

    def setUp(self):
        print("begin test")

    def tearDown(self):
        print("test over")

    #新增资源测试
    @parameterized.expand(train_infos)
    def test_train_add(self,add_url,METHOD,DATA,CODE,CONTENT,expect):
        add_data =  {'cus.tel':DATA['cus.tel' ], 'cus.name': DATA['cus.name' ], 'cus.sex': DATA['cus.sex' ], 'cus.last_status': DATA['cus.last_status' ], 'cus.email': DATA['cus.email' ], 'cus.qq': DATA['cus.qq' ], 'cus.school':  DATA['cus.school' ], 'cus.education': DATA['cus.education'], 'cus.major': DATA['cus.major'], 'cus.intent': DATA['cus.intent'], 'cus.workage':  DATA['cus.workage'], 'cus.salary': DATA['cus.salary'], 'cus.source': DATA['cus.source'], 'cus.applposition': DATA['cus.applposition'], 'cus.age': DATA['cus.age'], 'cus.eduexp':DATA['cus.eduexp'], 'cus.experience':DATA['cus.experience'], 'cus.last_tracking_remark': DATA['cus.last_tracking_remark']}
        resp = Training('..\\conf\\base.conf').do_add(add_url,add_data)
        if '新增成功' in resp.text:
            actual = 'add success'
        elif  '该资源现属于测试账号名下,已更新该资源的信息.' in resp.text:
            actual = 'already added'
        else:
            actual = 'add fail'
        self.assertEqual(actual,expect)
    
    #跟踪资源测试
    @parameterized.expand(follow_infos)
    def test_train_follow(self, follow_url, METHOD, DATA, CODE, CONTENT, expect):
        follow_data = {'fee': DATA['fee'], 'remark': DATA['remark'], 'status': DATA['status'],
                    'id': DATA['id'], 'nextTime': DATA['nextTime'],
                    'priority': DATA['priority']}
        resp = Training('..\\conf\\base.conf').do_follow(follow_url, follow_data)
        print(resp.text)
        if resp.text == '':
            actual = 'flow  fail'
        else:
            actual = 'flow ok'
        self.assertEqual(actual,expect)
    
    # 查询资源测试
    @parameterized.expand(query_infos)
    def test_train_query(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'], 'status': DATA['status'],
                       'cusInfo': DATA['cusInfo'], 'lastStatus': DATA['lastStatus'],'empName':DATA['empName'],
                       'source': DATA['source'],'s_time':DATA['s_time'],'e_time':DATA['e_time'],'poolType':DATA['poolType']}
        resp = Training('..\\conf\\base.conf').do_query(query_url, query_data)
        num = resp.text.split(':')[1].split(',')
        if int(num[0]) != 0:
            if DATA['poolType'] == 'temp':
                counts = uiti.query_one('..\\conf\\base.conf','SELECT COUNT(customer_id) FROM customer WHERE pool_type = "temp"')
                if counts[0] == int(num[0]):
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['lastStatus'] == '已报名':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(customer_id) FROM customer WHERE last_status = "已报名"')
                if counts[0] == int(num[0]):
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual,expect)
    
    # 编辑资源测试
    @parameterized.expand(edit_infos)
    def test_train_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'cus.customer_id': DATA['cus.customer_id'], 'cus.name': DATA['cus.name'], 'cus.sex': DATA['cus.sex'],
                       'cus.last_status': DATA['cus.last_status'], 'cus.tel': DATA['cus.tel'],'cus.email': DATA['cus.email'],
                       'cus.qq': DATA['cus.qq'],'cus.school':DATA['cus.school'],'cus.education':DATA['cus.education'],
                        'cus.major':DATA['cus.major'],'cus.intent':DATA['cus.intent'],'cus.workage':DATA['cus.workage'],
                         'cus.age':DATA['cus.age'],'cus.source':DATA['cus.source'],'cus.applposition':DATA['cus.applposition'],
                        'cus.eduexp':DATA['cus.eduexp'],'cus.experience':DATA['cus.experience'],'cus.last_tracking_remark':DATA['cus.last_tracking_remark']}
        resp = Training('..\\conf\\base.conf').do_edit(edit_url, edit_data)
        print(resp.text)
        if '修改成功' in resp.text:
            actual = 'edit success'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)
    
    # 废弃资源测试
    @parameterized.expand(abandon_infos)
    def test_train_abandon(self, abandon_url, METHOD, DATA, CODE, CONTENT, expect):
        abandon_data = {'arr[]': DATA['arr[]']}
        resp = Training('..\\conf\\base.conf').do_abandon(abandon_url, abandon_data)
        print(resp.text)
        if '废弃资源完成' in resp.text:
            actual = 'abandon success'
        else:
            actual = 'abandon fail'
        self.assertEqual(actual, expect)
    

    # 转交责任人查询资源测试
    @parameterized.expand(transQuery_infos)
    def test_train_transQuery(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data ={'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'], 'cusInfo': DATA['cusInfo'],
                    'workId': DATA['workId'], 'region': DATA['region'],
                    'source': DATA['source'],'status': DATA['status']}
        resp = Training('..\\conf\\base.conf').do_transQuery(query_url, query_data)
        print(resp.text)
        num = resp.text.split(':')[1].split(',')
        if int(num[0]) != 0:
            if DATA['status'] == '已报名':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(customer_id) FROM customer WHERE last_status = "已报名"')
                if counts[0] == int(num[0]):
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['workId'] == 'WNCD004':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(customer_id) FROM customer WHERE work_id = "WNCD004"')
                if counts[0] == int(num[0]):
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    # 转交责任人查看资源测试
    @parameterized.expand(see_infos)
    def test_train_see(self, see_url, METHOD, DATA, CODE, CONTENT, expect):
        see_data = {'cusId': DATA['cusId']}
        resp = Training('..\\conf\\base.conf').do_abandon(see_url, see_data)
        print(resp.text)
        if resp.text == '':
            actual = 'see fail'
        else:
            actual = 'see ok'
        self.assertEqual(actual, expect)
    
    # 转交责任人提交资源测试
    @parameterized.expand(commit_infos)
    def test_train_see(self, commit_url, METHOD, DATA, CODE, CONTENT, expect):
        commit_data = {'arr[]': DATA['arr[]'],'workId': DATA['workId']}
        resp = Training('..\\conf\\base.conf').do_abandon(commit_url, commit_data)
        print(resp.text)
        if resp.text == '':
            actual = 'commit fail'
        else:
            actual = 'commit ok'
        self.assertEqual(actual, expect)
    
    # 分配资源查询测试
    @parameterized.expand(allQuery_infos)
    def test_train_allQuery(self, allot_url, METHOD, DATA, CODE, CONTENT, expect):
        allot_data = {'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'],
                      'source': DATA['source'],'info': DATA['info']}
        URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
        login_info = {'userName': 'WNCD011', 'userPass': 'woniu123', 'checkcode': '0000'}
        self.session = Service.get_session('..\\conf\\base.conf')
        login_resp = self.session.post(URL, login_info)
        resp = self.session.post(allot_url, allot_data)
        num = resp.text.split(':')[1].split(',')
        if int(num[0]) == 1:
            actual = 'query ok'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    # 分配资源提交测试
    @parameterized.expand(submit_infos)
    def test_train_submit(self, submit_url, METHOD, DATA, CODE, CONTENT, expect):
        submit_data = {'arr[]': DATA['arr[]'], 'work_id': DATA['work_id']}
        URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
        login_info = {'userName': 'WNCD011', 'userPass': 'woniu123', 'checkcode': '0000'}
        self.session = Service.get_session('..\\conf\\base.conf')
        login_resp = self.session.post(URL, login_info)
        resp = self.session.post(submit_url, submit_data)
        print(resp.text)
        if resp.text == '':
            actual = 'submit fail'
        else:
            actual = 'submit ok'
        self.assertEqual(actual, expect)
    
    # 分配资源按比例分配测试
    @parameterized.expand(allot_infos)
    def test_train_allot(self, allot_url, METHOD, DATA, CODE, CONTENT, expect):
        allot_data = {'length': DATA['length'], 'work_id0': DATA['work_id0'],'proportion0': DATA['proportion0'],
                      'work_id1': DATA['work_id1'],'proportion1': DATA['proportion1'],'work_id2': DATA['work_id2'],
                      'proportion2': DATA['proportion2'],'work_id3': DATA['work_id3'],'proportion3': DATA['proportion3'],
                      'work_id4': DATA['work_id4'],'proportion4': DATA['proportion4'],'work_id5': DATA['work_id5'],
                      'proportion5': DATA['proportion5']}
        URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
        login_info = {'userName': 'WNCD011', 'userPass': 'woniu123', 'checkcode': '0000'}
        self.session = Service.get_session('..\\conf\\base.conf')
        login_resp = self.session.post(URL, login_info)
        resp = self.session.post(allot_url, allot_data)
        print(resp.text)
        if resp.text == '':
            actual = 'allot fail'
        else:
            actual = 'allot ok'
        self.assertEqual(actual, expect)
    
    #公共资源查询测试
    @parameterized.expand(pubQuery_infos)
    def test_train_pubQuery(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'],
                      'workId': DATA['workId'], 'lastStatus': DATA['lastStatus'],
                      'source': DATA['source'], 'cusInfo': DATA['cusInfo']}
        resp = Training('..\\conf\\base.conf').do_pubQuery(query_url, query_data)
        print(resp.text)
        num = resp.text.split(':')[1].split(',')
        if int(num[0]) != 0:
            if DATA['lastStatus'] == '无意向':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(customer_id) FROM customer WHERE last_status = "无意向"')
                if counts[0] == int(num[0]):
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['cusInfo'] == '姚茜':
                if int(num[0]) == 1:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)

    # 公共资源认领测试
    @parameterized.expand(owner_infos)
    def test_train_owner(self, owner_url, METHOD, DATA, CODE, CONTENT, expect):
        owner_data = {'arr[]': DATA['arr[]']}
        resp = Training('..\\conf\\base.conf').do_owner(owner_url, owner_data)
        print(resp.text)
        if resp.text == '':
            actual = 'owner fail'
        else:
            actual = 'owner ok'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)