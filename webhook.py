import requests
import json

acces_token='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'
webhook_url='https://your-development-store.myshopify.com/admin/api/2021-10/webhooks.json'
data={
    'name':'Akash',
    'Shop':'Test'
}
r=requests.post(webhook_url,data=json.dumps(data),headers={'Content-Type':'application/json'})