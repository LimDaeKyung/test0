import os
import requests
from bs4 import BeautifulSoup

# 웹 페이지의 소스코드를 가져오기
URL = 'https://www.google.com/search?q=%EB%9D%BC%EB%B2%A8%EC%9D%B4+%EC%9E%88%EB%8A%94+%EC%9E%AC%ED%99%9C%EC%9A%A9%EC%93%B0%EB%A0%88%EA%B8%B0&tbm=isch&ved=2ahUKEwjr0vz5sML_AhWwm1YBHdnkCTUQ2-cCegQIABAA&oq=%EB%9D%BC%EB%B2%A8%EC%9D%B4+%EC%9E%88%EB%8A%94+%EC%9E%AC%ED%99%9C%EC%9A%A9%EC%93%B0%EB%A0%88%EA%B8%B0&gs_lcp=CgNpbWcQAzoECCMQJzoFCAAQgAQ6BwgAEBgQgAQ6BggAEAgQHjoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgcIIxDqAhAnUIcDWLChAWDKoQFoHXAAeAiAAa4BiAHOJZIBBDQuMzmYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=mX-JZKuiC7C32roP2cmnqAM&bih=725&biw=1365&client=safari&hl=ko'
# print(URL)
response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# 웹 페이지에서 모든 이미지 태그(<img>)를 찾기
# print(soup)
img_tags = soup.find_all('img')
print(img_tags)

# 이미지 URL을 저장할 디렉터리 생성
SAVE_DIR = './saved_images_라벨있는 패트병'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# 이미지 태그에서 이미지 URL을 추출하고 이미지 저장하기
for img in img_tags:
    img_url = img.get('src')
    print(img_url)
    if not img_url.startswith('http'): 
        img_url = URL + img_url
    response = requests.get(img_url, stream=True)

    # 이미지 파일을 저장할 경로 지정
    filename = os.path.join(SAVE_DIR, img_url.split('/')[-1])+".jpg"
    
    # 이미지 파일을 저장
    with open(filename, 'wb') as file_out:
        for chunk in response.iter_content(chunk_size=8192):
            file_out.write(chunk)

