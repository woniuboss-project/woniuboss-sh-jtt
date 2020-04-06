import unittest

from parameterized import parameterized

from woniubossAPIDDT.lib.backs import Backs
from woniubossAPIDDT.tools.uiti import uiti

test_info = uiti.get_json('..\\conf\\testdata.conf')
train_infos=uiti.trans_dict_tup(test_info[14])
edit_infos = uiti.trans_dict_tup(test_info[15])
del_infos = uiti.trans_dict_tup(test_info[16])
setup_infos = uiti.trans_dict_tup(test_info[17])
rolAdd_infos = uiti.trans_dict_tup(test_info[18])
licen_infos = uiti.trans_dict_tup(test_info[19])
query_infos = uiti.trans_dict_tup(test_info[20])
dicAdd_infos = uiti.trans_dict_tup(test_info[21])
status_infos = uiti.trans_dict_tup(test_info[22])
dicEdit_infos = uiti.trans_dict_tup(test_info[23])
class backsTest(unittest.TestCase):

    def setUp(self):
        print("begin test")

    def tearDown(self):
        print("test over")

    # 菜单管理新增资源测试
    @parameterized.expand(train_infos)
    def test_back_add(self, add_url, METHOD, DATA, CODE, CONTENT, expect):
        add_data = {'resUrl': DATA['resUrl'], 'des': DATA['des'], 'pid': DATA['pid'],
                    'name': DATA['name']}
        resp = Backs('..\\conf\\base.conf').do_add(add_url, add_data)
        print(resp.text)
        if 'success' in resp.text:
            actual = 'add success'
        else:
            actual = 'add fail'

        self.assertEqual(actual,expect)
    
    # 菜单管理修改资源测试
    @parameterized.expand(edit_infos)
    def test_back_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'id': DATA['id'], 'name': DATA['name']}
        resp = Backs('..\\conf\\base.conf').do_edit(edit_url, edit_data)
        print(resp.text)
        if resp.text == '':
            actual = 'edit fail'
        else:
            actual = 'edit ok'
        self.assertEqual(actual,expect)
    
    # 菜单管理删除资源测试
    @parameterized.expand(del_infos)
    def test_back_del(self, del_url, METHOD, DATA, CODE, CONTENT, expect):
        del_data = {'id': DATA['id']}
        resp = Backs('..\\conf\\base.conf').do_del(del_url, del_data)
        print(resp.text)
        if resp.text == '':
            actual = 'del fail'
        else:
            actual = 'del ok'
        self.assertEqual(actual, expect)
    
    # 菜单管理设置资源测试
    @parameterized.expand(setup_infos)
    def test_back_setup(self, setup_url, METHOD, DATA, CODE, CONTENT, expect):
        setup_data = {'roleId': DATA['roleId']}
        resp = Backs('..\\conf\\base.conf').do_setup(setup_url, setup_data)
        print(resp.text)
        if resp.text == '':
            actual = 'set fail'
        else:
            actual = 'set ok'
        self.assertEqual(actual, expect)
    
    # 角色管理新增资源测试
    @parameterized.expand(rolAdd_infos)
    def test_back_rolAdd(self, add_url, METHOD, DATA, CODE, CONTENT, expect):
        add_data = {'role.name': DATA['role.name'],'role.des': DATA['role.des']}
        resp = Backs('..\\conf\\base.conf').do_rolAdd(add_url, add_data)
        print(resp.text)
        if 'success' in resp.text:
            actual = 'rolAdd ok'
        else:
            actual = 'rolAdd fail'

        self.assertEqual(actual, expect)
    
    # 角色管理授权资源测试
    @parameterized.expand(licen_infos)
    def test_back_licen(self, licen_url, METHOD, DATA, CODE, CONTENT, expect):
        licen_data = {'roleId': DATA['roleId']}
        resp = Backs('..\\conf\\base.conf').do_licen(licen_url, licen_data)
        print(resp.text)
        if resp.text == '':
            actual = 'licen fail'
        else:
            actual = 'licen ok'
        self.assertEqual(actual, expect)
    


    # 用户管理查询资源测试
    @parameterized.expand(query_infos)
    def test_back_query(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'],'pageIndex': DATA['pageIndex'],'userName': DATA['userName']}
        resp = Backs('..\\conf\\base.conf').do_query(query_url, query_data)
        num = resp.json()
        if num['totalRow'] != 0:
            if DATA['userName'] == 'admin':
                counts = uiti.query_one('..\\conf\\base.conf','SELECT COUNT(id) FROM system_user  WHERE name = "admin"')
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['userName'] == '':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(id) FROM system_user')
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual,expect)
    
    # 字典管理新增资源测试
    @parameterized.expand(dicAdd_infos)
    def test_back_dicAdd(self, add_url, METHOD, DATA, CODE, CONTENT, expect):
        add_data = {'dd.dict_type_id': DATA['dd.dict_type_id'], 'dd.dict_value': DATA['dd.dict_value'], 'dd.dict_key': DATA['dd.dict_key']
                    ,'dd.sort': DATA['dd.sort'],'dd.remarks': DATA['dd.remarks']}
        resp = Backs('..\\conf\\base.conf').do_dicAdd(add_url, add_data)
        print(resp.text)
        if 'success' in resp.text:
            actual = 'add ok'
        else:
            actual = 'add fail'

        self.assertEqual(actual, expect)
    
    # 角色管理启停用资源测试
    @parameterized.expand(status_infos)
    def test_back_status(self, status_url, METHOD, DATA, CODE, CONTENT, expect):
        status_data = {'typeId': DATA['typeId'], 'status': DATA['status']}
        resp = Backs('..\\conf\\base.conf').do_status(status_url, status_data)
        print(resp.text)
        if 'success' in resp.text:
            actual = 'statu ok'
        else:
            actual = 'statu fail'

        self.assertEqual(actual, expect)

     # 字典管理编辑资源测试
    @parameterized.expand(dicEdit_infos)
    def test_back_dicEdit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'dd.dict_type_id': DATA['dd.dict_type_id'], 'dd.dict_data_id': DATA['dd.dict_data_id'],
                    'dict_typename': DATA['dict_typename']
            , 'dd.dict_value': DATA['dd.dict_value'], 'dd.sort': DATA['dd.sort'],'dd.remarks': DATA['dd.remarks']}
        resp = Backs('..\\conf\\base.conf').do_dicEdit(edit_url, edit_data)
        print(resp.text)
        if 'success' in resp.text:
            actual = 'edit ok'
        else:
            actual = 'edit fail'

        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)