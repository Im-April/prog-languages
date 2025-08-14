# 온도 변환기

def celsius_to_fahrenheit(celsius):
    '''
    섭씨를 화씨로 변환
    '''
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    '''
    화씨를 섭씨로 변환
    '''
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(f'31°C는 {celsius_to_fahrenheit(31):.1f}°F입니다')
print(f'77°F는 {fahrenheit_to_celsius(77):.1f}°C입니다')