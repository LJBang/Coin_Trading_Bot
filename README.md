# Coin_Trading_Bot
업비트에서 코인을 자동 매매하는 봇을 만들자  

## 기술
- Python  
- Jupyter Notebook  
- AWS EC2  

## 전략
1. pyupbit 라이브러리를 사용하여 매매  
2. 간이 RSI지표를 이용하여 RSI가 0.3이하로 떨어지면 매수  
3. 특정 지점 (3%, 5%)수익 나면 익절, 손절  

## 부족한 점
1. 정확한 RSI지표가 아니다.  
    - 과거로부터 계속 계산해 온 RSI값이 아니라 계산한 한 시점의 RSI값  
2. 코드 리팩토링 할 필요가 있음.  
3. 여러개의 서로 다른 봇을 돌려 비교분석 할 필요가 있음.  
 
## 개선 사항  
1. 코드 리팩토링  
2. 매수, 매도에 대한 다양한 전략  
    - 코인간 상관관계분석 -> 안정적인 모델  
    - 모멘텀, 다른 지표 등 여러가지 전략을 코드화  
3. ec2에 jupyter notebook을 켜놓는 대신 다른 서버 프로그램 사용?  

## 사용해볼만한 전략
- RSI(2) 
    - 15일 RSI값이 아닌 2일 RSI값과 200일 이평선값을 사용해 단기 급락에서 수익을 내는 역추세 매매.  
    - 코인장에서 생각보다 괜찮은 효과를 보인다고 함.  
- 모멘텀 전략
    - 추세추종 전략
    - 이 역시 코인 시장에서 효과있는 전략
    - 어떤 모멘텀 전략을 쓸지는 더 고민해보거나 모두 사용해봐야 할 것