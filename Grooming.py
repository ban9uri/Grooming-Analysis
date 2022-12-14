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

st.info('This is a purely informational message', icon="ℹ️")

st.subheader('그루밍족 감성분석')
labels1 = ['POSITIVE', 'NEGATIVE']
frequency1 = [17.8, 82.2]
explode1 = [0.2, 0.2]
colors1 = ['#8fd9b6', '#d395d0']
fig1, ax1 = plt.subplots()
ax1.pie(frequency1, explode=explode1, labels=labels1, autopct='%1.1f%%',
        shadow=True, startangle=260, colors=colors1)
ax1.axis('equal')
st.pyplot(fig1)

st.subheader("인구 천 명당 연간 성형수술 건수")
surgery_data = load_data("data/인구 천 명당 연간 성형수술 건수.xlsx")
st.bar_chart(surgery_data, x='국가', y='number', height=500)

st.subheader('남성 최근 1년 내 외모 관리 경험')
labels2 = ['YES', 'NO']
frequency2 = [92.6,7.4]
explode2 = [0.2, 0.2]
colors2 = ['#ff9999', '#ffc000']
fig2, ax2 = plt.subplots()
ax2.pie(frequency2, explode=explode2, labels=labels2, autopct='%1.1f%%',
        shadow=True, startangle=260, colors=colors2)
ax2.axis('equal')
st.pyplot(fig2)

source2 = pd.DataFrame({"Response": ['YES', 'NO'], "value": [92.6, 7.4]})
pie2=alt.Chart(source2).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="Response", type="nominal"),
)
st.altair_chart(pie2, use_container_width=True)

st.subheader("남성 외모 관리 방법")
how_data = load_data("data/남성 외모 관리 방법 (가로 막대그래프).xlsx")
how_chart = alt.Chart(how_data).mark_bar().encode(
    x='Rate',
    y='Type'
    ).properties(height=400)
st.altair_chart(how_chart, use_container_width=True)

st.subheader("남성 외모 관리 요인")
factor_data = load_data("data/남성 외모 관리 요인 (가로 막대그래프).xlsx")
factor_chart = alt.Chart(factor_data).mark_bar().encode(
    x='Rate',
    y='Factor'
    ).properties(height=300)
st.altair_chart(factor_chart, use_container_width=True)

st.subheader("제품 사용 경험")
exp_data = load_data("data/제품 사용 경험 (가로 막대그래프).xlsx")
exp_chart = alt.Chart(exp_data).mark_bar().encode(
    x='percentage',
    y='item',
    color='Type'
    ).properties(height=500)
st.altair_chart(exp_chart, use_container_width=True)


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