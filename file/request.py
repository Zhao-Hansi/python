import requests


def main():
    resp = requests.get('https://apis.tianapi.com/guonei/index?key=6348f8b66f9f95e386ef0d4157271e89&num=100')
    print(type(resp))
    data_model = json.loads(resp.text)
    print(type(data_model))
    print(data_model)
    context = data_model['newslist']
    for news in context['newslist']:
        print(news)
        print(news['title'])


if __name__ == '__main__':
    main()




