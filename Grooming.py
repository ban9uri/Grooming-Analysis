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

###### 1. 외모지상주의 
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
###### 2. 아이돌과 대중매체의 영향
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

###### *국내 남성 화장품 시장 규모*
"""
)
kor_data = load_data("data/국내 남성 화장품 시장 규모 (선그래프).xlsx")
kor_data.year=kor_data.year.astype(str)
st.line_chart(kor_data, x='year', y='amount', height=500)
st.caption("**<그래프 7>** *출처: Euromonitor / 단위: 억 원*")

if st.button('참고'):
    st.markdown("""
    ###### *해외 남성 그루밍 시장 성장세*
    이하는 전세계 남성 그루밍 시장 규모 1, 2위를 차지하고 있는 미국과 브라질과, 인근 동아시아 국가인 일본과 중국의 시장 규모 변화를 보인 그래프이다.
    """)
    col1, col2 = st.columns(2)
    with col1:
        world_data1 = load_data("data/아메리카.xlsx")
        world_data1.year=world_data1.year.astype(str)
        st.line_chart(world_data1, x='year', y=['브라질', '미국'], height=500)
        st.caption("**<그래프 8>** *출처: Euromonitor / 단위: 백만 달러*")
    with col2:
        world_data2 = load_data("data/동아시아.xlsx")
        world_data2.year=world_data2.year.astype(str)
        st.line_chart(world_data2, x='year', y=['일본', '중국'], height=500)
        st.caption("**<그래프 9>** *출처: Euromonitor / 단위: 백만 달러*")
else:
    st.write('전세계적인 남성 그루밍 시장 상황을 보고 싶다면 버튼을 클릭하시오.')

st.markdown(
"""
##### ▶ 남성 그루밍 관련 소셜 미디어 성장세
설명

###### *그루밍 관련 유튜브 채널 구독자 수 추이*
"""
)
youtube_data = load_data("data/youtuber.xlsx")
youtube_data.date=youtube_data.date.astype(str)
st.line_chart(youtube_data, x='date', y=['화장', '헤어', '패션', '헬스'], height=500)
st.caption("**<그래프 10>** *출처: ㅇ / 단위: 명*")

st.markdown("""
###### *그루밍 관련 키워드 트위터 언급량 추이*
설명
""")
tweet_data = load_data("data/tweet.xlsx")
tweet_data.date=tweet_data.date.astype(str)
st.line_chart(tweet_data, x='date', y='tweet', height=500)
st.caption("**<그래프 11>** *출처: Twitter / 단위: 명*")

st.markdown(
"""
##### ▶ 남성 그루밍에 대한 사회적 인식: 소셜 미디어를 중심으로
###### - 긍정/부정 인식 간 비교
설명
###### *유튜브 내 긍정/부정 인식*
"""
)
col3, col4 = st.columns(2)
with col3:
    image1 = Image.open('img/youtube_positive_wordcloud.png')
    st.image(image1, caption='<그림 1> Youtube Positive WordCloud')
    st.caption("*출처: 영상제목 / n=*")
with col4:
    image2 = Image.open('img/youtube_negative_wordcloud.png')
    st.image(image2, caption='<그림 2> Youtube Negative WordCloud')
    st.caption("*출처: 영상제목 / n=*")

st.markdown(
"""
###### - 남성/여성 인식 간 비교
남성의 그루밍 행위에 대한 남성과 여성의 인식을 비교하고자, 남성 유저 위주의 커뮤니티 ‘디시인사이드’, 여성 유저 위주의 커뮤니티 ‘트위터’를 선정하였다.
"""
)
st.caption("""
디시인사이드의 경우 1990년대부터 2020년대에 이르기까지 인터넷 커뮤니티 1위를 유지하고 있으며, 2022년 10월 기준 네이버, 구글, 유튜브에
이은 한국 전체 인터넷 사이트 4위에 오른 국내 최대 포털 사이트인바 사회적 인식을 충분히 반영할 수 있다고 판단하였다. 디시인사이드를 남초
커뮤니티로 규정한 근거는 2022년 기준 ‘디시인사이드’ 어플리케이션의 유저 중 남성 비율이 79%라는 통계자료에 기반한 것이다(Dighty).
""")
st.caption("""
트위터의 경우 2022년 4월 기준 ‘페이스북’에 이은 전세계 방문자 2위 소셜 미디어 사이트이고, 동년 기준 국내 SNS·커뮤니티 앱 사용자 순위
TOP 7에 선정된바 역시 사회적 인식을 충분히 반영할 수 있다고 판단하였다. 트위터를 여초 커뮤니티로 규정한 근거는 ‘트위터’ 어플리케이션 유저 
중 여성 비율이 63.8%라는 통계자료에 기반한 것이다. 
""")
st.markdown(
"""
이하는 남성 그루밍 행위 관련 키워드의 게시글 내용을 크롤링한 결과에서 형용사를 추출하여 워드클라우드 형태로 제작한 것이다.
###### *디시인사이드/트위터 내 인식*
"""
)
col5, col6 = st.columns(2)
with col5:
    image3 = Image.open('img/dc wordcloud.png')
    st.image(image3, caption='<그림 3> DC WordCloud')
    st.caption("*출처: 디시인사이드 '남자 관리' 키워드 검색 결과(정확도순), n=1000*")
with col6:
    image4 = Image.open('img/twitter wordcloud.png')
    st.image(image4, caption='<그림 4>Twitter WordCloud')
    st.caption("*출처: 트위터 '남자(화장OR외모 관리OR자기 관리)' 검색 결과, n=2000*")
st.markdown(
"""
디시인사이드와 트위터 모두 공통적으로 ‘좋다’, ‘좋아하다’, ‘잘생기다’, ‘많다’, ‘중요하다’, ‘필요하다’, ‘예쁘다’ 등의 긍정적 성격의 형용사가 
‘싫다’, ‘싫어하다’ 등의 부정적 성격의 형용사에 비해 더 많은 종류가 더 높은 빈도로 추출되었음을 확인할 수 있다.
"""
)
st.markdown(
"""
디시인사이드의 경우. 특징적으로  ‘적당하다’, ‘깔끔하다’ 등의 키워드가 도출된 것을 통해 남성들은 과하지 않은 자연스러운 그루밍 행위를 추구함을
엿볼 수 있다. ‘철저하다’, ‘꾸준하다’, ‘당연하다’ 등의 키워드를 통해서는 남성의 외모 관리가 과거에 비해 보편화된 현상임을 엿볼 수 있다. 크롤링
결과를 분석하는 과정에서 그루밍 행위에 대한 회의론도 적지 않게 발견되었는데, 이러한 여론은 ‘똑같다’, ‘필요없다’, ‘어렵다’, ‘힘들다’, ‘이상하다’,
(여성들이)‘싫어하다’ 등의 키워드를 통해 확인되었다.
"""
)
st.markdown(
"""
트위터의 경우,
"""
)

st.markdown(
"""
##### ▶ 남성 그루밍 제품 마케팅 방식 분석: 쿠팡을 중심으로
앞선 분석에서, 남성들은 그루밍 행위에 있어서 간편함, 자연스러움 등의 가치를 추구함을 보였다. 이를 바탕으로, 남성들이 중시하는 이러한 가치들이
실제로 남성 화장품의 마케팅에도 반영이 되는지를 보고자 한다. 이를 위해 국내 쇼핑 사이트인 ‘쿠팡(Coupang)’을 분석 대상으로 선정하였다.  이하는
쿠팡 ‘남성화장품’ 카테고리에서 ‘남성 스킨케어’ 제품과 ‘남성 메이크업’ 제품을 분석한 내용이다.
"""
)
st.caption("""
2021년 10월 기준 연령별 쇼핑 어플리케이션 설치 순위 통계에서 10대부터 60대까지 전부 1위를 차지(출처: Dighty)하고 그루밍족이 주로 
분포하는 MZ세대가 가장 선호하는 종합 온라인 쇼핑몰 1위를 차지(출처: 대학내일20대연구소)했다는 점을 고려하였다.
""")
st.markdown("스킨케어/메이크업 상품 기업의 마케팅 방식")
col7, col8 = st.columns(2)
with col7:
    image5 = Image.open('img/skincare wordcloud.png')
    st.image(image5, caption='<그림 5> Skincare Marketing WordCloud')
    st.caption("*출처: 쿠팡 / 대상: 남성 스킨케어 제품 판매량 상위 120개 제품의 상품명*")
with col8:
    image6 = Image.open('img/makeup wordcloud.png')
    st.image(image6, caption='<그림 6> Makeup Marketing WordCloud')
    st.caption("*출처: 쿠팡 / 대상: 남성 메이크업 제품 판매량 상위 15개 제품의 제품 설명 문구*")
st.markdown("""
<그림 5>은 ‘남성 스킨케어’ 제품 중 판매량이 높은 순대로 120개를 선정하여 그 제품명을 크롤링하고 명사를 추출하여 WordCloud 형태로 제작한 것이다.
<그래프 6>(제품사용)에서 보인 바와 같이 스킨, 로션, 에센스, 크림 등이 등이 중요한 비중을 차지함을 알 수 있고, ‘올인원’, ‘세트’라는 키워드가 제일 높은
빈도로 등장했다는 점에서 남성들이 그루밍 행위에 있어서 간편함, 실용성을 추구한다는 것을 재확인할 수 있었다. 또한 ‘모이스처’ 키워드를 통해 기업들이
중시하는 남성 스킨케어 제품의 강점이 ‘보습’임을 도출할 수 있었다.
""")
st.markdown("""
<그림 6>은 ‘남성 메이크업’ 제품 중 판매량이 높은 순대로 15개를 선정하여 그 제품 상세설명 문구를 분석하고 형용사를 추출하여 WordCloud 형태로
제작한 것이다. 쿠팡의 특성상 제품 설명 문구가 모두 사진 형태로 되어 있어, 사진들을 OCR 기법으로 분석하여 텍스트만을 추출하였다. 가장 높은 빈도로
등장한 ‘자연스럽다’, ‘가볍다’, ‘깔끔하다’, ‘얇다’ 등의 키워드를 통해, 앞서 확인한 남성들이 그루밍 행위에 있어서 중시하는 ‘자연스러움’이라는 가치가
제품 마케팅에 활용된 것을 확인할 수 있었다. ‘촉촉하다’ 키워드를 통해서는 앞서 스킨케어에서 확인한 대로 보습력이 주요 마케팅 포인트임을 확인할 수 있었다. 
""")


st.markdown("긍정적/부정적 상품평 분석")
col9, col10 = st.columns(2)
with col9:
    image7 = Image.open('img/cosmetic_star45.png')
    st.image(image7, caption='Cosmetic 4-5 Review WordCloud')
    st.caption("*출처: 쿠팡 / 대상: *")
with col10:
    image8 = Image.open('img/cosmetic_star12.png')
    st.image(image8, caption='Cosmetic 1-2 Review WordCloud')
    st.caption("*출처: 쿠팡 / 대상: *")


st.markdown("***")

st.header("결(結)")
st.markdown(
"""
##### ▶ 남성 그루밍 시장 성장세
이하는 통계청에서 발표한 여성 경제활동 인구 및 참가율이다. 2012년 이후로 지속적으로 상승세를 보임을 알 수 있다.
앞서 <그래프 7>에서 본 한국 남성 화장품 시장 규모의 변화 추이 또한 2010년대 내내 지속적인 상승세를 보여주었다. 이 두
그래프를 통해 본 11조는 여성의 사회·경제적 진출과 남성의 그루밍 행위 간의 상관관계가 존재할 가능성을 엿보았다.

본 11조는 앞서 제시한 미시적 원인들 외에, 그루밍족 등장에 대한 거시적 원인으로서 성 역할(gender role)의 변화를 제시한다.
성 역할이란 남성 및 여성의 특징으로서 적합하다고 여겨지는 가치 내지는 고정관념이 일상생활의 역할에 반영된 것(Shaffer:2005, Berk:2009)을 의미한다.
수렵·채집 사회 이래로, 동서고금을 막론하고 남성에게는 생물학적 힘을 바탕으로 가정의 생계를 책임지는 역할이 부여되었다. 하지만 현대 사회에서 여성
인권의 신장과 함께 여성들이 기존 남성들의 역할로 여겨졌던 사회 진출과 경제 활동 등을 수행하는 비율이 증가함에 따라 전통적인 남녀 성 역할 구분이
모호해졌고, 이로 인해 유사한 맥락에서 남성은 여성의 역할로 여겨졌던 외모 관리, 화장에 참여하는 비율이 증가한 것으로 그루밍족의 증가 현상을 해석해볼
수 있겠다. 한국 사회의 경우에는, 이러한 성 역할을 남녀에게 부여하였었던, 오랜 세월 동안 사회 저변에 뿌리내린 채 행동 양식에 영향을 미친 유교적 사상과
문화가 최근 들어 2030세대를 중심축으로 변화하고 있음을 시사한다고 볼 수 있겠다. 오늘날 여성의 경제 활동 진출을 남성 그루밍족 증가의 거시적 원인으로
본다면, 미래에도 남성 그루밍 시장은 꾸준히 성장하리라고 예측해볼 수 있겠다.

###### *여성경제활동인구 및 참가율*
"""
)

col11, col12 = st.columns(2)
fem_data = load_data("data/C 여성경제활동인구 및 참가율 (통계청).xlsx")
fem_data.year=fem_data.year.astype(str)
with col11:
    st.bar_chart(fem_data, x='year', y='people', height=500)
    st.caption("**<그래프 12>** *출처: 통계청 / 단위: 명*")
with col12:
    st.line_chart(fem_data, x='year', y='rate', height=500)
    st.caption("**<그래프 13>** *출처: 통계청 / 단위: %*")