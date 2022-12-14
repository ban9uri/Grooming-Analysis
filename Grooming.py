import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image

@st.cache(allow_output_mutation=True)

def load_data(filename):
    data = pd.read_excel(filename)
    return data

st.title('💁🏻‍♂꾸미는 남자들:')
st.header('그루밍족 톺아보기💄💇🏻‍♂💅🏻💪🏻👔💆🏻‍♂')
st.markdown(
"""
***
데이터 저널리즘 11조: 김가연, 안민규, 장진
***
"""
)

st.subheader('서문')
st.write(
"""
오늘날 그루밍족은 통계적으로 2030 남성들의 40% 이상을 차지한다. 국내 남성 그루밍 시장은 어
떻게 진화해왔으며, 남성들의 그루밍에 대한 사회적 인식은 어떠한가? 또 기업들은 어떠한 마케팅 
전략을 활용하여 그루밍족들을 소구하고 있는가?
"""
)

st.info("""
차례

**1. 기(起)**
 - 그루밍족이란?
**2. 서(序)**
 - 남성 그루밍 시장 현황
 - 그루밍족에 대한 사회적 인식
 - 그루밍족을 겨냥한 마케팅 방식
**3. 결(結)**
 - 결론 및 시사점
""", icon="ℹ️")
st.markdown("***")

st.header("기(起)")
st.markdown(
"""
##### ▶ 용어 정의
**그루밍족(Grooming-族):** 외모를 경쟁력이라 여기고 외모 관리에 시간과 비용을 아낌없이 투자하는 
남성. 마부가 말을 목욕시키고 빗질하는 것을 뜻하는 그룸(groom)에서 유래한 단어이다.
"""
)
st.markdown(
"""
##### ▶ 용어 등장 시기
그루밍족이라는 단어가 처음 등장한 것은 2007년으로 추정된다.
"""
)
with st.expander("상세설명 참조"):
    st.write("""
        - 2007년 이전: 고려대학교 코퍼스분석도구, NAVER Database 등에서 용례 확인 불가
        - 2007년:〈한국경제〉8월 15일 기사《남성 패션시대… ‘그루밍族’ 뜬다》발간
        - 2008년: 한경 경제용어사전 ‘그루밍족’ 등재

           … 중략 …

        - 2022년: 언론, 방송 등 다양한 분야에서 활발히 사용
    """)
st.markdown(
"""
##### ▶ 용어의 용례
흥미로운 것은, 외모관리에 대한 남성들의 관심은 지속적으로 긍정적인 방향으로 증가하였
고 언론에서는 그루밍족이라는 용어의 긍정적 용례가 확인되는 것이 대부분이나, 남성 인터
넷 커뮤니티상에서 그루밍족이라는 용어는 그 내용을 감성분석한 결과, 대체로 부정적인 용
례로 사용됨을 확인할 수 있었다.

###### *'그루밍족' 용례 감성분석 결과*
"""
)
source1 = pd.DataFrame({"Response": ['POSITIVE', 'NEGATIVE'], "value": [17.8, 82.2]})
pie1=alt.Chart(source1).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Response", type="nominal"),
)
st.altair_chart(pie1, use_container_width=True)
st.caption("**<그래프 1>** *출처: 디시인사이드 갤러리 ‘그루밍족’ 키워드 검색, n=343*")

st.markdown(
"""
##### ▶ 그루밍족 등장의 미시적 원인

1. 외모지상주의 
지난 수십 년간 한국 사회에 뿌리 내린 외모지상주의가 그루밍족 등장의 원인 중 하나로 지목될 
수 있다. 이하는 한국의 외모지상주의를 보여줄 수 있는 통계자료이다. 인구 천 명당 연간 성형수술 
건수는 한국이 23건으로, 조사 대상이 된 다른 국가들과 비교하여 유의미하게 높은 수치를 보인다.

###### *인구 천 명당 연간 성형수술 건수*
"""
)
surgery_data = load_data("data/인구 천 명당 연간 성형수술 건수.xlsx")
st.bar_chart(surgery_data, x='국가', y='number', height=500)
st.caption("**<그래프 2>** *출처: ISAPS / 단위: 건*")

st.markdown(
"""
2. 아이돌과 대중매체의 영향
방탄소년단(BTS)로 대표되는 한국의 K-POP 산업은 전세계적으로 큰 성공을 거두고 있다. 이러한 
K-POP의 초기 해외 시장 진출 과정에서 진입 장벽으로 작용한 것은 바로 남성 가수 또한 여성 가
수 못지않은 수준의 메이크업을 한다는 점이었다. 하지만 메이크업을 하는 남성 가수들의 모습을 대
중매체를 통해 보며 유년기를 보낸 2030세대에게 남성의 화장에 대한 인식은 기성세대에 비해 우호
적이다. 대중매체의 본질적 기능은 수용자들의 행동 양식에 영향을 미치는 것이라는 **문화 규범 이론
(the Culture Norms Theory)** 과, 매스미디어에서 묘사하는 모델적인 사람들의 행동은 수용자들에게 
새로운 행동양식으로 채택되게 된다는 **모델링 이론(the Modeling Theory)** 은 이를 뒷받침한다. 
"""
)


st.markdown(
"""
##### ▶ 그루밍족 관련 통계

통계청의 조사에 따르면, 최근 1년 내 외모 관리를 경험해본 남성의 비율은 92.6%로 그렇지 않은 7.4%보다 
12배 이상 높은 수치를 기록하였다.

###### *남성 최근 1년 내 외모 관리 경험*
"""
)
source2 = pd.DataFrame({"Response": ['YES', 'NO'], "value": [92.6, 7.4]})
pie2=alt.Chart(source2).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Response", type="nominal"),
)
st.altair_chart(pie2, use_container_width=True)
st.caption("**<그래프 3>** *출처: 통계청 / 단위: %*")

st.markdown(
"""
구체적인 외모 관리의 방법은 아래 그래프와 같다. 에 따르면 기초화장품을 통해 피부 관리를 한다고 응답한 
남성은 조사 대상의 79.8%였다. 39.6%를 차지한 눈썹 관리, 19.4%를 차지한 체모 관리, 18.9%를 차지한 손
톱/발톱 관리, 7.6%를 차지한 성형수술/시술이 그 뒤를 이었다. 
###### *남성 외모 관리 방법*
"""
)
how_data = load_data("data/남성 외모 관리 방법 (가로 막대그래프).xlsx")
how_chart = alt.Chart(how_data).mark_bar(color = 'palegreen').encode(
    x='Rate',
    y='Type'
    ).properties(height=400)
st.altair_chart(how_chart, use_container_width=True)
st.caption("**<그래프 4>** *출처: <2022 남성 그루밍 트렌드 리포트>, 오픈서베이 / 단위: %*")

st.markdown(
"""
남성들이 외모를 관리하는 요인은 자신감 획득(78.8%), 자기만족(73.4%), 대인관계 유지(67.8)% 순으로 많
은 응답을 기록하였다.
###### *남성 외모 관리 요인*
"""
)
factor_data = load_data("data/남성 외모 관리 요인 (가로 막대그래프).xlsx")
factor_chart = alt.Chart(factor_data).mark_bar().encode(
    x='Rate',
    y='Factor'
    ).properties(height=300)
st.altair_chart(factor_chart, use_container_width=True)
st.caption("**<그래프 5>** *출처: 통계청 / 단위: %*")

st.markdown(
"""
구체적으로 사용하는 외모관리 제품의 종류와 비율은 다음과 같다. 생필품의 성격을 가진 폼클렌저, 로션, 스
킨 등을 제외하면 기초 화장품 부문에서는 올인원 제품, 자외선차단 제품, 에센스, 마스크팩이 50% 이상을 차
지하였다. 색조화장품 부문에서 가장 높은 비율을 기록한 것은 23.2%의 BB크림/CC크림이었다. 또한, 1인당
평균 사용하는 남성 그루밍 제품 개수가 7.7개였다.
###### *제품 사용 경험*
"""
)
exp_data = load_data("data/제품 사용 경험 (가로 막대그래프).xlsx")
exp_chart = alt.Chart(exp_data).mark_bar().encode(
    x='percentage',
    y='item',
    color='Type'
    ).properties(height=500)
st.altair_chart(exp_chart, use_container_width=True)
st.caption("**<그래프 6>** *출처: <2022 남성 그루밍 트렌드 리포트>, 오픈서베이 / 단위: %*")
st.markdown("***")

st.header("서(序)")
st.markdown(
"""
##### ▶ 남성 그루밍 시장 성장세
국내 남성 화장품 시장은 매년 10% 이상의 성장률을 기록하며 꾸준히 성장 중이다. 2020년 기준 이미 1조 4천억 이상의
규모를 달성하였고, 이러한 성장세는 앞으로도 지속될 것으로 전망된다.
"""
)


st.subheader("국내 남성 화장품 시장 규모")
kor_data = load_data("data/국내 남성 화장품 시장 규모 (선그래프).xlsx")
kor_data.year=kor_data.year.astype(str)
st.line_chart(kor_data, x='year', y='amount', height=500)

st.subheader("국가별 남성 화장품 시장 규모")
col3, col4 = st.columns(2)
with col3:
    world_data1 = load_data("data/아메리카.xlsx")
    world_data1.year=world_data1.year.astype(str)
    st.line_chart(world_data1, x='year', y=['브라질', '미국'], height=500)
with col4:
    world_data2 = load_data("data/동아시아.xlsx")
    world_data2.year=world_data2.year.astype(str)
    st.line_chart(world_data2, x='year', y=['일본', '중국'], height=500)

st.subheader("트위터 언급량 추이")
tweet_data = load_data("data/tweet.xlsx")
tweet_data.date=tweet_data.date.astype(str)
st.line_chart(tweet_data, x='date', y='tweet', height=500)

st.subheader("유튜브 구독자 수 추이")
youtube_data = load_data("data/youtuber.xlsx")
youtube_data.date=youtube_data.date.astype(str)
st.line_chart(youtube_data, x='date', y=['화장', '헤어', '패션', '헬스'], height=500)


st.subheader("유튜브 내 긍정/부정 인식")
col1, col2 = st.columns(2)
with col1:
    image1 = Image.open('img/youtube_positive_wordcloud.png')
    st.image(image1, caption='Youtube Positive WordCloud')
with col2:
    image2 = Image.open('img/youtube_negative_wordcloud.png')
    st.image(image2, caption='Youtube Negative WordCloud')


st.subheader("DC 내 인식(남성의 인식)")
image3 = Image.open('img/dc wordcloud.png')
st.image(image3, caption='DC WordCloud')

st.subheader("트위터 내 인식(여성의 인식)")
image4 = Image.open('img/twitter wordcloud.png')
st.image(image4, caption='Twitter WordCloud')

st.subheader("스킨케어 상품 기업의 마케팅 방식")
image5 = Image.open('img/skincare wordcloud.png')
st.image(image5, caption='Skincare Marketing WordCloud')

st.subheader("메이크업 상품 기업의 마케팅 방식")
image6 = Image.open('img/makeup wordcloud.png')
st.image(image6, caption='Makeup Marketing WordCloud')

st.subheader("소비자 선호 상품")
image7 = Image.open('img/cosmetic_star45.png')
st.image(image7, caption='Cosmetic 4-5 Review WordCloud')

st.subheader("소비자 불호 상품")
image8 = Image.open('img/cosmetic_star12.png')
st.image(image8, caption='Cosmetic 1-2 Review WordCloud')


st.subheader("여성경제활동인구 및 참가율")
fem_data = load_data("data/C 여성경제활동인구 및 참가율 (통계청).xlsx")
fem_data.year=fem_data.year.astype(str)
base = alt.Chart(fem_data).encode(x='year')
bar = base.mark_bar().encode(y='여성경제 활동인구')
line =  base.mark_line(color='red').encode(y='여성경제 활동참가율')
fem_chart=(bar + line).properties(width=500)
st.altair_chart(fem_chart, use_container_width=True)