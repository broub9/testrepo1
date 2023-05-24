# Made by tq148 (rblxdeve) don't say you made this code bruv.
import requests

target_id = # Made by tq148 (rblxdeve) don't say you made this code bruv.
import requests

target_id = 1885942045
cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_3570BE80ABA3B26E9F999D6AE2136D7915BD1153A365491E4B97815824854198FE8B67624CC7A3891E680ED1113606064A5D22A3AAA51022F03832558F7A9AD5E17B32696CDCAE1C76B5D73331344B530CC30204EC955726DFA1E2467000400F4C815A13632E6A791231E3D4372477EBF1E6821AF80C3CBF67C0AE6B338D639BECB5580F1DEEFFB05D448FAF8B1AA3B55C52B77EAEF30FA3E688ADC668F304685EB7C70D907862F852B78FD118B925CC999ED2B2F9414455BA5890B21D007A392035A157FCE37320BF0B00DF74B3981CBB4F88B831E7A0EF006479D8C50B14B14741FDFEF9B40492E85D09A490D68EC542712D5FE702CA3D50D7D63A41F680903DA159950BC51345DB7D6F3EB46865CA6CCF8A10C865837ED9D2460886129750EB2C2A1D5ACF37C5FDD7743EADF917676D111E78F14ADA076AF778511E59544E86A5975C329CD216993AA323EF48EFC089B37F829915DD9A255DD8B70CB47E9C66823D3C"
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

userid= requests.get('https://www.roblox.com/my/settings/json', headers=headers).json()['UserId']

data = {
    "userId": userid, # your user id
    "subject": "hello",
    "body": "you've been struck by tq148",
    "recipientId": target_id # recipient's user Id
}
import time, os
while True:
    message_response = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers = headers, data = data)
    print(f"{message_response.json()} , {message_response.status_code}")   
    if message_response.status_code == 429:
        time.sleep(60)
    if message_response.status_code ==403:
        os.system('python 9000RTE.py')
    time.sleep(5)


cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_3570BE80ABA3B26E9F999D6AE2136D7915BD1153A365491E4B97815824854198FE8B67624CC7A3891E680ED1113606064A5D22A3AAA51022F03832558F7A9AD5E17B32696CDCAE1C76B5D73331344B530CC30204EC955726DFA1E2467000400F4C815A13632E6A791231E3D4372477EBF1E6821AF80C3CBF67C0AE6B338D639BECB5580F1DEEFFB05D448FAF8B1AA3B55C52B77EAEF30FA3E688ADC668F304685EB7C70D907862F852B78FD118B925CC999ED2B2F9414455BA5890B21D007A392035A157FCE37320BF0B00DF74B3981CBB4F88B831E7A0EF006479D8C50B14B14741FDFEF9B40492E85D09A490D68EC542712D5FE702CA3D50D7D63A41F680903DA159950BC51345DB7D6F3EB46865CA6CCF8A10C865837ED9D2460886129750EB2C2A1D5ACF37C5FDD7743EADF917676D111E78F14ADA076AF778511E59544E86A5975C329CD216993AA323EF48EFC089B37F829915DD9A255DD8B70CB47E9C66823D3C"
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

userid= requests.get('https://www.roblox.com/my/settings/json', headers=headers).json()['UserId']

data = {
    "userId": userid, # your user id
    "subject": "hello",
    "body": "you've been struck by tq148",
    "recipientId": target_id # recipient's user Id
}
import time, os
while True:
    message_response = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers = headers, data = data)
    print(f"{message_response.json()} , {message_response.status_code}")   
    if message_response.status_code == 429:
        time.sleep(60)
    if message_response.status_code ==403:
        os.system('python 9000RTE.py')
    time.sleep(5)

