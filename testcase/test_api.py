import pytest as pytest
import os
import sys
object_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(object_path)
from common.send_requests import SendRequests
from common.yaml_util import YamlUtil


class TestApi:

    # ubmp登录接口
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_extract_yaml('web_login_case.yml'))
    def test_post_token(self, caseinfo):
        method = caseinfo['web_method']
        url = caseinfo['web_url']
        jsons = caseinfo['web_data']
        res = SendRequests().all_send_requests(method, url=url, json=jsons)
        datas = res.json()
        cookie = res.headers
        assert datas['message'] == '登录成功'
        return cookie

    @pytest.mark.parametrize('sampleinfo', YamlUtil().read_extract_yaml('out_sample.yml'))
    def test_out_sample(self, sampleinfo):
        case_name = sampleinfo['name']
        method = sampleinfo['method']
        url = sampleinfo['url']
        out_data = sampleinfo['out_data']
        res = SendRequests().all_send_requests(method=method, url=url, data=out_data)
        samplejson = res.json()
        assert samplejson['success']  == True
        print(res.text)


if __name__ == '__main__':
    pytest.main()
