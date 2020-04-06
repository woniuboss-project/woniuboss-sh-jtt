# -*- coding: utf-8 -*-
import requests

from woniubossAPIDDT.tools.uiti import uiti


class Service:
    @classmethod
    def get_session(cls,base_path):
        content=uiti.get_json(base_path)
        URL='%s://%s:%s/%s'%(content['PROTOCOL'],content['HOST'],content['PORT'],content['AURL'])
        data = {'userName':content['username'],'userPass':content['password'],'checkcode':content['checkcode']}
        session = requests.session()
        resp=session.post(URL,data)
        return session

if __name__ == '__main__':
    session = Service.get_session('..\\conf\\base.conf')
    print(session)

    URL = 'http://192.168.101.135:8080/WoniuBoss2.5/log/userLogin'
    data = {"userName":"WNCD000","userPass":"woniu123","checkcode":"0000"}

    resp = session.post(URL, data)
    print(resp.text)






if __name__ == '__main__':
    Service.get_session('..\\conf\\base.conf')