import requests
import bittensor as bt

def get_TTS():
    url = "https://api.corcel.io/v1/text/cortext/chat"
    headers = {
        "Authorization": "9be319e8-c45e-4f8d-aba6-",
        "accept": "application/json",
        "content-type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": "random meaningful text phrase in less than 32 words"}],
        "miners_to_query": 1,
        "top_k_miners_to_query": 40,
        "ensure_responses": True,
        "model": "cortext-ultra",
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    # Check the HTTP status code
    status_code = response.status_code
    if status_code == 200:
        # If status code is 200, parse the response
        json_data = response.json()
        content = json_data[0]['choices'][0]['delta']['content']
        return content
    else:
        # Handle other failure codes
        bt.logging.error("Request failed to fetch prompt from corcel with status code:", status_code)
        return None
    
def get_VC():
    url = "https://api.corcel.io/v1/text/cortext/chat"
    headers = {
        "Authorization": "9be319e8-c45e-4f8d-aba6-",
        "accept": "application/json",
        "content-type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": "random meaningful text phrase in less than 32 words"}],
        "miners_to_query": 1,
        "top_k_miners_to_query": 40,
        "ensure_responses": True,
        "model": "cortext-ultra",
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    # Check the HTTP status code
    status_code = response.status_code
    if status_code == 200:
        # If status code is 200, parse the response
        json_data = response.json()
        content = json_data[0]['choices'][0]['delta']['content']
        return content
    else:
        # Handle other failure codes
        bt.logging.error("Request failed to fetch prompt from corcel with status code:", status_code)
        return None
    
def get_TTM():
    url = "https://api.corcel.io/v1/text/cortext/chat"
    headers = {
        "Authorization": "9be319e8-c45e-4f8d-aba6-",
        "accept": "application/json",
        "content-type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": "random Music generation phrase for AI music generation model in less than 32 words"}],
        "miners_to_query": 1,
        "top_k_miners_to_query": 40,
        "ensure_responses": True,
        "model": "cortext-ultra",
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    # Check the HTTP status code
    status_code = response.status_code
    if status_code == 200:
        # If status code is 200, parse the response
        json_data = response.json()
        content = json_data[0]['choices'][0]['delta']['content']
        return content
    else:
        # Handle other failure codes
        bt.logging.error("Request failed to fetch prompt from corcel with status code:", status_code)
        return None
    
    