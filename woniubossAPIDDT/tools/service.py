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
    Service.get_session('..\\conf\\base.conf')