
import requests
import json
def test_li():
    url="http://www.fratelloinnotech.com/getusersall.php"
    reep=requests.get(url)
    j=json.loads(reep.text)
    assert reep.status_code==200, 'Responce code should be 200 but came '+str(reep.status_code)
    assert j[0]['id']=='63226', reep.text
    assert j [0]['name']== 'vivek', reep.text

def test_kk():
    url= 'http://www.fratelloinnotech.com/insertuser.php'
    data="('name':'rajayya','address':'hyd')"
    reep=requests.post(url,data=data)
    j=json.loads(reep.text)
    assert reep.status_code== 200, reep.status_code
    assert j['result']=='success ok', reep.text

def test_delr():
    url= 'http://www.fratelloinnotech.com/insertuser.php?id=62340'
    reep=requests.post(url)
    j=json.loads(reep.text)
    assert reep.status_code == 200, 'Responce code should be 200 but came ' + str(reep.status_code)
    assert j['result'] == 'success ok' , reep.text

def test_tt():
    url="https://catfact.ninja/fact"
    raep=requests.get(url)
    j=json.loads(raep.text)
    assert raep.status_code==200,raep.status_code

def test_air():
    url="https://api.instantwebtools.net/v1/airlines"
    reap=requests.get(url)
    j=json.loads(reap.text)
    assert reap.status_code == 200, reap.status_code
    assert j[1]['id'] == 2, reap.text
    assert j[1]['name'] == 'Singapore Airlines', reap.text
    assert j[1]['country'] == 'Singapore', reap.text
    assert j[1]['website'] == 'www.singaporeair.com', reap.text
    assert j[1]['established'] == '1947'

def test_tr():
    url="https://jsonplaceholder.typicode.com/users"
    reap=requests.get(url)
    j=json.loads(reap.text)
    assert reap.status_code==200, reap.status_code
    assert j[0]['name']=='Leanne Graham',reap.text
    assert j[0]['username']=='Bret',reap.text
    assert j[0]['email']=='Sincere@april.biz',reap.text



