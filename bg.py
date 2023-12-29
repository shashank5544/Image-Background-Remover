import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': "https://user-images.githubusercontent.com/76609302/172825370-c323b652-ad37-4244-94ff-51105516039f.png",
        'size': 'auto'
    },
    headers={'X-Api-Key': 'NhgR4Vez3twLwkFJmoUxC51Q'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)