from woniubossAPIDDT.tools.service import Service


class Backs:
    def __init__(self,base_path):
        self.session = Service.get_session(base_path)
        URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
        login_info = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode': '0000'}
        login_resp = self.session.post(URL, login_info)

     #菜单管理资源树新增功能
    def do_add(self,add_url,add_data):
        resp = self.session.post(add_url,add_data)
        return resp

    #菜单管理资源树修改功能
    def do_edit(self,edit_url,edit_data):
        resp = self.session.post(edit_url,edit_data)
        return resp



    # 菜单管理资源树删除功能
    def do_del(self, del_url, del_data):
        resp = self.session.post(del_url, del_data)
        return resp

    # 菜单管理设置功能
    def do_setup(self, setup_url, setup_data):
        resp = self.session.post(setup_url, setup_data)
        return resp

    # 角色管理新增功能
    def do_rolAdd(self, add_url, add_data):
        resp = self.session.post(add_url, add_data)
        return resp

    # 角色管理授权功能
    def do_licen(self, licen_url, licen_data):
        resp = self.session.post(licen_url, licen_data)
        return resp

    # 用户管理查询功能
    def do_query(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp

    # 字典管理新增功能
    def do_dicAdd(self, add_url, add_data):
        resp = self.session.post(add_url, add_data)
        return resp

    # 字典管理启用/停用功能
    def do_status(self, status_url, status_data):
        resp = self.session.post(status_url, status_data)
        return resp

    # 字典管理编辑功能
    def do_dicEdit(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp