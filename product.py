input_data= {
        "Product_Id":6599003177022
    }

import requests,json
from html.parser import HTMLParser
Product_Id = input_data.get('Product_Id')

url = f"https://cowhides-direct.myshopify.com/admin/api/2023-04/products/{Product_Id}.json"
print(url)
headers = {
  'Content-Type': 'application/json',
  'X-Shopify-Access-Token': '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',
  'Cookie': '_master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxWmpJME5UaGhNUzFrTURnMUxUUTFNemd0WWpZMk1TMDBZekJrWldWbU0yWTFNR1VHT2daRlJnPT0iLCJleHAiOiIyMDI1LTA0LTE5VDExOjI3OjUzLjg5MloiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--3c431b30a45d9932abb8f2606bf6720c5fa2204b; _secure_admin_session_id=ec02c5a7fea623f0e5d1da5a662a73f0; _secure_admin_session_id_csrf=ec02c5a7fea623f0e5d1da5a662a73f0; identity-state=BAhbBkkiJTkyMTBiMDNlMThhMjczOTEyODk0NmVlNjFiYWY0ZTgwBjoGRUY%3D--cfd08268a598858e2bd36d0fb4af18a743de886f; identity-state-9210b03e18a2739128946ee61baf4e80=BAh7DEkiDnJldHVybi10bwY6BkVUSSI7aHR0cHM6Ly9jb3doaWRlcy1kaXJlY3QubXlzaG9waWZ5LmNvbS9hZG1pbi9hdXRoL2xvZ2luBjsAVEkiEXJlZGlyZWN0LXVyaQY7AFRJIkdodHRwczovL2Nvd2hpZGVzLWRpcmVjdC5teXNob3BpZnkuY29tL2FkbWluL2F1dGgvaWRlbnRpdHkvY2FsbGJhY2sGOwBUSSIQc2Vzc2lvbi1rZXkGOwBUOgxhY2NvdW50SSIPY3JlYXRlZC1hdAY7AFRmFzE2ODE5MDM2NzMuOTAzMjg2NUkiCm5vbmNlBjsAVEkiJWM4MjJhMzBjNzhkYzgwZDI3ZTc4ZTAzNWYxZWFkMjMxBjsARkkiCnNjb3BlBjsAVFsPSSIKZW1haWwGOwBUSSI3aHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9kZXN0aW5hdGlvbnMucmVhZG9ubHkGOwBUSSILb3BlbmlkBjsAVEkiDHByb2ZpbGUGOwBUSSJOaHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9wYXJ0bmVycy5jb2xsYWJvcmF0b3ItcmVsYXRpb25zaGlwcy5yZWFkb25seQY7AFRJIjBodHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL2JhbmtpbmcubWFuYWdlBjsAVEkiQmh0dHBzOi8vYXBpLnNob3BpZnkuY29tL2F1dGgvbWVyY2hhbnQtc2V0dXAtZGFzaGJvYXJkLmdyYXBocWwGOwBUSSI8aHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9zaG9waWZ5LWNoYXQuYWRtaW4uZ3JhcGhxbAY7AFRJIjdodHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL2Zsb3cud29ya2Zsb3dzLm1hbmFnZQY7AFRJIj5odHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL29yZ2FuaXphdGlvbi1pZGVudGl0eS5tYW5hZ2UGOwBUSSIPY29uZmlnLWtleQY7AFRJIgxkZWZhdWx0BjsAVA%3D%3D--19007e2e30dc357993b80da3fa3f651009b8d3a1'
}
response = json.loads(requests.request("GET", url, headers=headers).text).get('product')

Product_Title = response.get('title')
Product_Description = response.get('body_html')

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data.strip())

    def get_text(self):
        return '\n'.join(line for line in self.text if line)
parser = TextExtractor()
parser.feed(str(Product_Description))
Desctiption = parser.get_text()
x = str(Desctiption.strip().split('\n')).replace('[','').replace(']','').replace(',',' ')
output = {"Production Description":length_dess}


