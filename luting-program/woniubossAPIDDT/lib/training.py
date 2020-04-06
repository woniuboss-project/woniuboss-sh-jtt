
from woniubossAPIDDT.tools.service import Service


class Training:
    def __init__(self,base_path):
        self.session = Service.get_session(base_path)
        URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
        login_info = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode': '0000'}
        login_resp = self.session.post(URL, login_info)

     #培训资源新增功能
    def do_add(self,add_url,add_data):
        resp = self.session.post(add_url,add_data)
        return resp

    #培训资源跟踪功能
    def  do_follow(self,follow_url,follow_data):
        resp = self.session.post(follow_url,follow_data)
        return  resp

    #培训资源查询功能
    def  do_query(self,query_url,query_data):
        resp = self.session.post(query_url,query_data)
        return resp


    #培训资源修改功能
    def  do_edit(self,edit_url,edit_data):
        resp = self.session.post(edit_url,edit_data)
        return resp

    # 培训资源废弃功能
    def do_abandon(self, abandon_url, abandon_data):
        resp = self.session.post(abandon_url, abandon_data)
        return resp

    # 转交责任人查询功能
    def do_transQuery(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp

    # 转交责任人查看功能
    def do_see(self, see_url, see_data):
        resp = self.session.post(see_url, see_data)
        return resp

    # 转交责任人提交功能
    def do_commit(self, commit_url, commit_data):
        resp = self.session.post(commit_url, commit_data)
        return resp

    # 公共资源查询功能
    def do_pubQuery(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp



    # 公共资源认领功能
    def do_owner(self, owner_url, owner_data):
        resp = self.session.post(owner_url, owner_data)
        return resp