import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")


# 스타일 설정
st.markdown(
    """
    <style>
        .main { background-color: #F2F4F7 !important; }

        h1 {
            font-weight: 800 !important;
            color: #2F3A4A !important;
        }

        h2, h3 {
            color: #334155 !important;
            font-weight: 700 !important;
        }

        .section-box {
            background: white;
            padding: 1.8rem;
            border-radius: 15px;
            margin-bottom: 1.2rem;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .emoji-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #1E293B;
        }

        .highlight {
            background: #EEF2FF;
            padding: 4px 8px;
            border-radius: 6px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 메인 제목
st.title("📊 통합 상권 BI 분석 플랫폼")
st.subheader("AI 기반 정성·정량 상권 분석 자동화 서비스")

st.markdown(
    """
    이 플랫폼은 **상권 트렌드 보고서 생성**과 **매출 데이터 분석**을 제공하는 통합 분석 도구입니다.

    좌측 메뉴에서 기능을 선택해 시작하세요! 👈
    """
)

st.divider()

# 주요 기능 설명
st.markdown("<div class='emoji-title'>📌 주요 기능 안내</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="section-box">

        <h3>🔎 BI 트렌드 보고서 생성 기능</h3>
        <ul>
            <li>자연어로 요청 입력 → AI가 자동 분석</li>
            <li>웹 검색 기반 최신 정보 수집</li>
            <li>실제 문서 기반 RAG로 신뢰도 강화</li>
            <li>BI 전문가 수준의 전략 분석 보고서 출력</li>
            <li>Markdown + PDF 저장 지원</li>
        </ul>

        <p>→ 사용 위치: <b>사이드바 → “BI report generator” 페이지</b></p>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="section-box">

        <h3>📊 상권 매출 분석 대시보드</h3>
        <ul>
            <li>상권·업종별 매출 Top10</li>
            <li>성별/연령대/시간대 매출 분포</li>
            <li>업종별 상권 비교 분석</li>
            <li>미래 분기별 매출 예측</li>
            <li>연도/분기 기준 비교 기능</li>
        </ul>

        <p>→ 사용 위치: <b>사이드바 → “Sales Analysis Dashboard” 페이지</b></p>

        </div>
        """,
        unsafe_allow_html=True
    )




# 데이터 출처 및 처리 흐름 설명
st.markdown("<div class='emoji-title'>📂 데이터 출처 및 처리 흐름</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="section-box">

        <h3>🧩 웹 기반 정성 데이터</h3>
        <ul>
            <li>DuckDuckGo 검색 API로 최신 상권 관련 문서 수집</li>
            <li>WebBaseLoader로 웹페이지 콘텐츠 직접 로딩</li>
            <li>Chroma Vector DB(text-embedding-3-large 사용)에 저장</li>
            <li>RAG 기반 문서 유사도 검색 후 GPT 분석에 활용</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="section-box">

        <h3>📘 정량 매출 데이터</h3>
        <ul>
            <li>서울시 전역 상권 매출 CSV 데이터 사용</li>
            <li>업종/성별/연령대/시간대별 매출 포함</li>
            <li>예측 모델: Exponential Smoothing</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
<div class="section-box" style="text-align:center;">

### ✔ 개인정보 또는 내부 DB는 전혀 사용하지 않습니다.
오직 **공개 웹 데이터 + 제공된 CSV 데이터만 활용**하여 분석합니다.

</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="section-box" style="text-align:center;">
    <h3>이제 시작해볼까요? 😊</h3>
    <p>왼쪽 메뉴에서 원하는 기능을 선택해주세요.</p>
</div>
    """,
    unsafe_allow_html=True
)

