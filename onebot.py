import requests
from requests.compat import urljoin, urlencode, quote_plus
import sys

if len(sys.argv) < 4:
    print("Usage: computer_name user_name ip_ex ip_in")
    exit()

api_host = "127.0.0.1"
api_port = 8083
api_group = 114514
access_token = "changeme"

computer_name = sys.argv[1]
user_name = sys.argv[2]
user_ip = sys.argv[3]
user_ip_internal = sys.argv[4]

msg = f"有主机上线了喵! 注意查收哦\n主机名:{computer_name}\n用户名:{user_name}\nIP: {user_ip} (外网) / {user_ip_internal} (内网)"
try:
    response = requests.get(
        urljoin("http://" + api_host + f":{api_port}".format(api_port=api_port), quote_plus("send_group_msg")),
        {
            "group_id": str(api_group),
            "message": f"[CQ:text,text={msg}]".format(msg=msg),
            "auto_escape": "false",
            "access_token": access_token
        },
    )
    if response.status_code == 401:
        print("wrong token.")
except Exception as e:
    print(e)