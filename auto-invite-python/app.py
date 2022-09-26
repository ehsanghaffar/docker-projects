import requests
import time
import json
# import redis

# r = redis.Redis(
#     host='localhost',
#     port='6379',
#     db=1
# )


url = "https://www.clubhouseapi.com/api/"
ch = "m7Kk7X31"
t = "4c721c9c2f7d18b463c83a5e61df4d3d34e39d71"

user_list = []


def get_room(channel, token):
    headers = {
        'CH-Languages': 'en-US',
        'CH-Locale': 'en_US',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'CH-AppBuild': '2576',
        'CH-AppVersion': '0.1.8',
        'CH-UserID': '1928455578',
        'User-Agent': 'clubhouse/2576 (iPhone; iOS 14.4; Scale/2.00)',
        'Connection': 'close',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token ' + token,
    }
    data = {
        "channel": channel
    }
    api_url = url + 'get_channel'
    req = requests.request("POST", api_url,
                           headers=headers, json=data)
    res = req.json()
    dump_res = json.dumps(res, indent=2)
    loads_res = json.loads(dump_res)
    user_list = loads_res['users']
    return user_list


def invate_speaker(t, ch, id):
    headers = {
        'CH-Languages': 'en-US',
        'CH-Locale': 'en_US',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'CH-AppBuild': '2576',
        'CH-AppVersion': '0.1.8',
        'CH-UserID': '1928455578',
        'User-Agent': 'clubhouse/2576 (iPhone; iOS 14.4; Scale/2.00)',
        'Connection': 'close',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token ' + t,
    }
    payload = {
        "channel": ch,
        "user_id": id
    }
    api_url = url + 'invite_speaker'
    response = requests.request("POST", api_url, json=payload, headers=headers)
    print(response.text)


def add_to_dict(user):
    user_dict = {}
    user_id = user['user_id']
    user_state = user['is_speaker']
    is_invate = user['is_invited_as_speaker']
    user_dict = {1: user_id, 2: user_state, 3: is_invate}
    return user_dict


while True:
    all_users = get_room(ch, t)
    for i in all_users:
        all_user_dict = add_to_dict(i)
        # print(all_user_dict)
        if all_user_dict[2] == False:
            if all_user_dict[3] == False:
                id = all_user_dict[1]
                print(all_user_dict)
                invate_speaker(t, ch, id)
    time.sleep(5)
