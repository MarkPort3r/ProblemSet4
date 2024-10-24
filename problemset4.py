#API 호출용
import requests
import matplotlib.pyplot as plt

# API 키와 기본 URL 설정
API_KEY = '724b9d38864a9a7537f1a8ce0726bb77'
BASE_URL = 'http://api.weatherstack.com/current'

# 요청할 도시 설정
city = 'Seoul'

# API 호출 URL 구성
params = {
    'access_key': API_KEY,
    'query': city
}

# API 호출 및 응답 처리
response = requests.get(BASE_URL, params=params)
data = response.json()

# 응답이 정상인지 확인
if 'current' in data:
    current_weather = data['current']

    # 유용한 정보 추출
    temperature = current_weather['temperature']
    feels_like = current_weather['feelslike']
    humidity = current_weather['humidity']
    wind_speed = current_weather['wind_speed']

    # 결과 출력
    print(f"도시: {city}")
    print(f"현재 온도: {temperature}°C")
    print(f"체감 온도: {feels_like}°C")
    print(f"습도: {humidity}%")
    print(f"풍속: {wind_speed} km/h")

    # 시각화: 온도와 체감 온도 비교 그래프
    labels = ['Actual Temperature', 'Feels Like']
    values = [temperature, feels_like]

    plt.bar(labels, values, color=['skyblue', 'lightcoral'])
    plt.title(f'Temperature Comparison in {city}')
    plt.ylabel('Temperature (°C)')
    plt.show()

else:
    print(f"데이터를 가져오지 못했습니다: {data.get('error', {}).get('info', 'Unknown error')}")