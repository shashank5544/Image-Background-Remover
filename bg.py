import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': "Url of image you want to remove background of",
        'size': 'auto'
    },
    headers={'X-Api-Key': 'Your Api_key paste here'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
