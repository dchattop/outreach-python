import json
import http.client

def get_access_token(
        client_id_,
        client_secret_,
        redirect_url_,
        refresh_token_,
        grant_type_='refresh_token'
):
    config_ = {
        'client_id': client_id_,
        'client_secret': client_secret_,
        'redirect_uri': redirect_url_,
        'refresh_token': refresh_token_,
        'grant_type': grant_type_,
    }
    conn_ = http.client.HTTPSConnection("api.outreach.io")
    conn_.request("POST", "/oauth/token", json.dumps(config_), {'Content-Type': 'application/json'})
    res_ = conn_.getresponse()
    if res_.status == 200:
        data_ = res_.read()
        data_json_ = json.loads(data_)
        access_token_ = data_json_.get("access_token")
        return access_token_

