# 21.02.18 코드

import pyupbit
import time

# 원화로 거래할 수 있는 코인 목록을 tickers에 저장
# 앞으로 tickers에 있는 코인들을 돌면서 거래할 예정
tickers=pyupbit.get_tickers("KRW")

# api키를 이용해 업빝 로그인
access_key = ''
secret_key = ''
upbit = pyupbit.Upbit(access_key, secret_key)

while True:
    print('start!')
    for ticker in tickers:
        keyw = ticker.split('-')[1]  # 티커에서 'krw-' 떼고 코인 키만
	      try:    # 현재가 불러오는데 한 번씩 JSON에러나서 에러 잡아줌
            cur_price = pyupbit.get_current_price(ticker)
            vol = 5600/cur_price # 최소거래금액이 5천원이라 손절가 포함 5600원어치 코인 개수
						# 3분봉 14개의 값을 데이터 프레임형태로 저장
            df = pyupbit.get_ohlcv(ticker, interval="minute3", count=14)
            # print(ticker)

            UU = 0    # 증가분 합
            DD = 0    # 감소분 합
            diff = 0  # 전종가와 현종가의 차
            rsi = 0   # rsi지표 값

            for i in range(13):   # 14개의 봉 마다 종가를 봐서 증분, 감소분 계산
                diff = df['close'][i+1] - df['close'][i]
                if diff >= 0:
                    DD += diff
                else:
                    UU += (-diff)

            rsi=UU/(UU+DD) # rsi계산

            # print("rsi = ", rsi)
            
            # 매수
						# rsi가 25퍼 이하일 때 매수
            if rsi < 0.25: 
                print(keyw, 'rsi = ', rsi, '산닷!')
                upbit.buy_limit_order(ticker,cur_price,vol)

            # 매도
						# 3퍼익절 5퍼손절
            else: 
                for i in upbit.get_balances(): # 잔고를 돌면서
                    if i['currency'] == keyw: # ticker에 해당하는 코인이 잔고에 있는지 확인
                        # print(keyw, "평단: ", upbit.get_balances()[i]['avg_buy_price'], '현재가: ', cur_price)
                        if (cur_price >= float(i['avg_buy_price'])*1.03) or (cur_price <= float(i['avg_buy_price'])*0.95):
                            print('현재가', cur_price, '평단', i['avg_buy_price'])
                            print(keyw, '매도')
                            upbit.sell_market_order(ticker, i['balance'])
                        
        except TypeError:
            pass
        
    # 3분 대기
    print(upbit.get_balances())
    time.sleep(180)