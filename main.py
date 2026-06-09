import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="✨ MBTI 직업 추천 | Career Guide",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── MBTI Data ─────────────────────────────────────────────────────────────────
MBTI_DATA = {
    "INTJ": {
        "nickname": "전략가 🧠",
        "emoji": "♟️",
        "color": "#6C63FF",
        "gradient": "linear-gradient(135deg, #6C63FF 0%, #3F3D56 100%)",
        "desc": "독립적이고 결단력 있는 전략가. 복잡한 문제를 체계적으로 해결하는 능력이 탁월합니다.",
        "traits": ["🎯 목표 지향적", "🔍 분석적 사고", "📐 체계적", "💡 혁신적"],
        "careers": [
            {"job": "소프트웨어 아키텍트", "icon": "🏗️", "desc": "시스템 전체 구조를 설계하는 전문가"},
            {"job": "데이터 과학자", "icon": "📊", "desc": "빅데이터를 분석해 인사이트를 도출"},
            {"job": "경영 컨설턴트", "icon": "💼", "desc": "기업 전략과 운영 효율을 개선"},
            {"job": "외과 의사", "icon": "🔬", "desc": "정밀한 판단과 집중력이 필요한 직업"},
            {"job": "투자 분석가", "icon": "📈", "desc": "시장을 분석하고 투자 전략 수립"},
            {"job": "AI 연구원", "icon": "🤖", "desc": "인공지능 알고리즘 연구 및 개발"},
        ],
    },
    "INTP": {
        "nickname": "논리술사 🔭",
        "emoji": "⚗️",
        "color": "#00BCD4",
        "gradient": "linear-gradient(135deg, #00BCD4 0%, #0D47A1 100%)",
        "desc": "지식에 대한 끝없는 갈증을 가진 철학자. 이론과 아이디어의 세계에서 살아갑니다.",
        "traits": ["🧩 논리적", "🌐 창의적", "📚 지식 탐구", "🤔 비판적 사고"],
        "careers": [
            {"job": "철학자 / 연구원", "icon": "📖", "desc": "지식의 본질을 탐구하는 학자"},
            {"job": "프로그래머", "icon": "💻", "desc": "알고리즘과 코드로 세상을 만들어가는 직업"},
            {"job": "물리학자", "icon": "⚛️", "desc": "우주와 자연의 법칙을 연구"},
            {"job": "수학자", "icon": "🔢", "desc": "추상적 개념과 패턴을 탐구"},
            {"job": "게임 개발자", "icon": "🎮", "desc": "창의적 세계관과 시스템을 구현"},
            {"job": "사이버 보안 전문가", "icon": "🔐", "desc": "디지털 세계의 방어를 담당"},
        ],
    },
    "ENTJ": {
        "nickname": "통솔자 👑",
        "emoji": "🦁",
        "color": "#FF6B35",
        "gradient": "linear-gradient(135deg, #FF6B35 0%, #C0392B 100%)",
        "desc": "타고난 리더십으로 목표를 향해 돌진하는 통솔자. 큰 그림을 그리고 실현시킵니다.",
        "traits": ["🚀 리더십", "💪 결단력", "🌟 카리스마", "🎯 목표 달성"],
        "careers": [
            {"job": "CEO / 창업가", "icon": "🏢", "desc": "기업을 이끄는 최고 의사결정자"},
            {"job": "정치인", "icon": "🏛️", "desc": "국가와 사회를 이끄는 지도자"},
            {"job": "법률가", "icon": "⚖️", "desc": "정의를 실현하는 법의 수호자"},
            {"job": "투자 은행가", "icon": "💰", "desc": "대규모 금융 거래를 주도"},
            {"job": "군사 장교", "icon": "🎖️", "desc": "조직을 통솔하는 리더"},
            {"job": "프로젝트 매니저", "icon": "📋", "desc": "팀과 프로젝트를 성공으로 이끄는 역할"},
        ],
    },
    "ENTP": {
        "nickname": "변론가 🎭",
        "emoji": "💬",
        "color": "#FF9800",
        "gradient": "linear-gradient(135deg, #FF9800 0%, #E65100 100%)",
        "desc": "아이디어의 불꽃이 튀는 토론가. 도전과 논쟁을 즐기며 혁신을 이끕니다.",
        "traits": ["💡 아이디어 뱅크", "🗣️ 토론 즐김", "🔄 유연한 사고", "🚀 혁신적"],
        "careers": [
            {"job": "스타트업 창업가", "icon": "🚀", "desc": "새로운 아이디어로 시장을 개척"},
            {"job": "변호사", "icon": "⚖️", "desc": "논리와 설득으로 의뢰인을 변호"},
            {"job": "마케터", "icon": "📣", "desc": "창의적 전략으로 브랜드를 알림"},
            {"job": "UX 디자이너", "icon": "🎨", "desc": "사용자 경험을 혁신적으로 설계"},
            {"job": "언론인 / 기자", "icon": "📰", "desc": "세상의 이야기를 발굴하고 전달"},
            {"job": "광고 크리에이티브 디렉터", "icon": "✨", "desc": "브랜드의 창의적 방향을 이끔"},
        ],
    },
    "INFJ": {
        "nickname": "옹호자 🌸",
        "emoji": "🔮",
        "color": "#9C27B0",
        "gradient": "linear-gradient(135deg, #9C27B0 0%, #4A148C 100%)",
        "desc": "깊은 통찰과 이상주의로 세상을 더 나은 곳으로 만들려는 조용한 완벽주의자.",
        "traits": ["💫 통찰력", "❤️ 공감 능력", "🌱 이상주의", "🎯 사명감"],
        "careers": [
            {"job": "심리상담사", "icon": "🧠", "desc": "마음의 상처를 치유하는 전문가"},
            {"job": "작가 / 소설가", "icon": "✍️", "desc": "깊은 통찰을 글로 표현하는 예술가"},
            {"job": "사회복지사", "icon": "🤝", "desc": "취약계층의 삶을 지원하는 직업"},
            {"job": "의사 / 치료사", "icon": "🏥", "desc": "몸과 마음을 치유하는 의료 전문가"},
            {"job": "교수 / 교육자", "icon": "🎓", "desc": "다음 세대에게 지식과 가치를 전달"},
            {"job": "NGO 활동가", "icon": "🌍", "desc": "세상을 더 나은 곳으로 만드는 활동"},
        ],
    },
    "INFP": {
        "nickname": "중재자 🌈",
        "emoji": "🦋",
        "color": "#E91E63",
        "gradient": "linear-gradient(135deg, #E91E63 0%, #880E4F 100%)",
        "desc": "이상과 가치를 소중히 여기는 몽상가. 인류에 대한 사랑과 창의성이 넘칩니다.",
        "traits": ["🎨 창의적", "💖 공감 능력", "🌟 이상주의", "🕊️ 평화 추구"],
        "careers": [
            {"job": "시인 / 작가", "icon": "📝", "desc": "감성과 상상력으로 글을 쓰는 예술가"},
            {"job": "그래픽 디자이너", "icon": "🎨", "desc": "시각적 아름다움을 창조하는 직업"},
            {"job": "음악가", "icon": "🎵", "desc": "감정을 음악으로 표현하는 예술가"},
            {"job": "심리치료사", "icon": "💆", "desc": "내면의 상처를 치유하는 전문가"},
            {"job": "영화 감독", "icon": "🎬", "desc": "이야기를 영상으로 표현하는 예술가"},
            {"job": "환경 운동가", "icon": "🌿", "desc": "지구 환경을 지키는 활동가"},
        ],
    },
    "ENFJ": {
        "nickname": "선도자 🌟",
        "emoji": "🌠",
        "color": "#4CAF50",
        "gradient": "linear-gradient(135deg, #4CAF50 0%, #1B5E20 100%)",
        "desc": "타인의 성장을 돕는 카리스마 넘치는 리더. 사람들에게 영감을 주고 변화를 이끕니다.",
        "traits": ["🌟 카리스마", "❤️ 따뜻함", "🚀 영감 부여", "🤝 협력"],
        "careers": [
            {"job": "교사 / 강사", "icon": "🍎", "desc": "학생들의 잠재력을 꽃피우는 교육자"},
            {"job": "HR 매니저", "icon": "👥", "desc": "인재를 발굴하고 조직 문화를 만듦"},
            {"job": "코치 / 멘토", "icon": "🏆", "desc": "개인과 팀의 성장을 이끄는 전문가"},
            {"job": "배우 / 공연 예술가", "icon": "🎭", "desc": "감동을 전하는 무대의 예술가"},
            {"job": "사회운동가", "icon": "✊", "desc": "사회 변화를 위해 목소리를 높이는 활동가"},
            {"job": "커뮤니케이션 전문가", "icon": "📡", "desc": "메시지를 효과적으로 전달하는 전문가"},
        ],
    },
    "ENFP": {
        "nickname": "활동가 🎉",
        "emoji": "🌈",
        "color": "#FF4081",
        "gradient": "linear-gradient(135deg, #FF4081 0%, #F50057 100%)",
        "desc": "자유로운 영혼의 열정가! 사람과 아이디어를 연결하며 세상을 축제로 만듭니다.",
        "traits": ["🎊 열정적", "💫 창의적", "🌍 호기심", "💃 사교적"],
        "careers": [
            {"job": "크리에이티브 디렉터", "icon": "✨", "desc": "창의적 비전으로 프로젝트를 이끔"},
            {"job": "유튜버 / 콘텐츠 크리에이터", "icon": "📹", "desc": "개성 넘치는 콘텐츠로 세상과 소통"},
            {"job": "이벤트 플래너", "icon": "🎪", "desc": "특별한 순간을 기획하고 연출"},
            {"job": "홍보 전문가", "icon": "📣", "desc": "브랜드와 사람을 연결하는 전문가"},
            {"job": "여행 작가", "icon": "✈️", "desc": "세상을 돌아다니며 이야기를 전달"},
            {"job": "상담사 / 코치", "icon": "💬", "desc": "사람들의 가능성을 이끌어내는 전문가"},
        ],
    },
    "ISTJ": {
        "nickname": "현실주의자 📋",
        "emoji": "🏛️",
        "color": "#607D8B",
        "gradient": "linear-gradient(135deg, #607D8B 0%, #263238 100%)",
        "desc": "신뢰와 책임감의 화신. 전통과 규칙을 존중하며 묵묵히 맡은 바를 완수합니다.",
        "traits": ["✅ 책임감", "📏 체계적", "🔒 신뢰성", "📚 성실함"],
        "careers": [
            {"job": "회계사 / 세무사", "icon": "🧾", "desc": "숫자와 법규를 다루는 재무 전문가"},
            {"job": "법무사 / 행정사", "icon": "📜", "desc": "법적 절차를 돕는 전문 직업"},
            {"job": "공무원", "icon": "🏢", "desc": "국가와 사회를 위해 일하는 직업"},
            {"job": "군인 / 경찰", "icon": "🛡️", "desc": "사회 질서와 안전을 수호"},
            {"job": "IT 시스템 관리자", "icon": "🖥️", "desc": "시스템의 안정적 운영을 책임짐"},
            {"job": "품질 관리 전문가", "icon": "🔎", "desc": "제품과 서비스의 품질을 보장"},
        ],
    },
    "ISFJ": {
        "nickname": "수호자 🛡️",
        "emoji": "🌻",
        "color": "#795548",
        "gradient": "linear-gradient(135deg, #795548 0%, #3E2723 100%)",
        "desc": "따뜻한 마음으로 타인을 돌보는 수호자. 헌신과 배려로 주변을 행복하게 합니다.",
        "traits": ["❤️ 헌신적", "🌿 배려심", "🏠 안정 추구", "🤝 협력적"],
        "careers": [
            {"job": "간호사", "icon": "💊", "desc": "환자를 돌보는 의료 현장의 핵심"},
            {"job": "초등학교 교사", "icon": "🍎", "desc": "아이들의 첫 배움을 이끄는 교육자"},
            {"job": "사회복지사", "icon": "🤲", "desc": "도움이 필요한 사람을 지원"},
            {"job": "영양사", "icon": "🥗", "desc": "건강한 식생활을 안내하는 전문가"},
            {"job": "도서관 사서", "icon": "📚", "desc": "지식과 문화를 관리하는 전문가"},
            {"job": "행정 관리자", "icon": "📁", "desc": "조직이 원활하게 돌아가도록 지원"},
        ],
    },
    "ESTJ": {
        "nickname": "경영자 📊",
        "emoji": "🏆",
        "color": "#F44336",
        "gradient": "linear-gradient(135deg, #F44336 0%, #B71C1C 100%)",
        "desc": "질서와 효율의 화신. 규칙과 전통을 바탕으로 조직을 이끄는 타고난 관리자.",
        "traits": ["📋 조직력", "⚡ 실행력", "🎯 목표 달성", "👔 리더십"],
        "careers": [
            {"job": "기업 관리자 / 임원", "icon": "🏢", "desc": "조직의 방향을 이끄는 경영진"},
            {"job": "판사 / 검사", "icon": "⚖️", "desc": "정의를 실현하는 법조인"},
            {"job": "군 장교", "icon": "🎖️", "desc": "규율과 명령으로 조직을 이끔"},
            {"job": "재무 관리자", "icon": "💹", "desc": "기업의 재무 건전성을 책임짐"},
            {"job": "학교 교장", "icon": "🏫", "desc": "교육 기관을 이끄는 관리자"},
            {"job": "공급망 관리자", "icon": "🚚", "desc": "물류와 공급 시스템을 최적화"},
        ],
    },
    "ESFJ": {
        "nickname": "집정관 🤗",
        "emoji": "🌺",
        "color": "#FF5722",
        "gradient": "linear-gradient(135deg, #FF5722 0%, #BF360C 100%)",
        "desc": "공동체의 화목을 이끄는 따뜻한 조력자. 다른 사람의 행복이 자신의 기쁨입니다.",
        "traits": ["🤗 사교적", "💖 배려심", "🎊 협력적", "🌟 헌신적"],
        "careers": [
            {"job": "간호사 / 의료 코디네이터", "icon": "🏥", "desc": "환자와 의료진을 연결하는 중추"},
            {"job": "이벤트 매니저", "icon": "🎉", "desc": "특별한 행사를 기획하고 운영"},
            {"job": "항공 승무원", "icon": "✈️", "desc": "고객 서비스의 최전선에서 활약"},
            {"job": "호텔리어", "icon": "🏨", "desc": "최고의 환대를 제공하는 서비스 전문가"},
            {"job": "영업 관리자", "icon": "🤝", "desc": "관계를 바탕으로 비즈니스를 이끔"},
            {"job": "유치원 교사", "icon": "🧸", "desc": "아이들의 성장을 돌보는 교육자"},
        ],
    },
    "ISTP": {
        "nickname": "장인 🔧",
        "emoji": "⚙️",
        "color": "#009688",
        "gradient": "linear-gradient(135deg, #009688 0%, #004D40 100%)",
        "desc": "손재주와 논리로 무장한 실용주의자. 어떤 도구든 완벽하게 다루는 고요한 장인.",
        "traits": ["🔧 실용적", "🧩 문제 해결", "⚡ 즉흥적", "🔍 관찰력"],
        "careers": [
            {"job": "엔지니어 / 기계공학자", "icon": "⚙️", "desc": "기계와 시스템을 설계하고 제작"},
            {"job": "파일럿", "icon": "✈️", "desc": "하늘을 나는 항공기 조종 전문가"},
            {"job": "외과 의사", "icon": "🩺", "desc": "정교한 손기술이 요구되는 의사"},
            {"job": "포렌식 전문가", "icon": "🔬", "desc": "범죄 현장의 증거를 분석하는 전문가"},
            {"job": "자동차 엔지니어", "icon": "🚗", "desc": "자동차 기술을 연구하고 개발"},
            {"job": "건축 기술자", "icon": "🏗️", "desc": "건물과 구조물을 설계하고 건설"},
        ],
    },
    "ISFP": {
        "nickname": "모험가 🎨",
        "emoji": "🦚",
        "color": "#8BC34A",
        "gradient": "linear-gradient(135deg, #8BC34A 0%, #33691E 100%)",
        "desc": "섬세한 감성과 유연함을 가진 예술가. 현재 이 순간의 아름다움을 만끽합니다.",
        "traits": ["🎨 예술적", "💚 자유로움", "🌿 자연 친화", "🦋 유연성"],
        "careers": [
            {"job": "패션 디자이너", "icon": "👗", "desc": "아름다움을 옷으로 표현하는 예술가"},
            {"job": "사진작가", "icon": "📸", "desc": "순간의 아름다움을 포착하는 전문가"},
            {"job": "인테리어 디자이너", "icon": "🏠", "desc": "공간을 아름답게 꾸미는 전문가"},
            {"job": "수의사", "icon": "🐾", "desc": "동물의 건강을 돌보는 의료 전문가"},
            {"job": "셰프 / 요리사", "icon": "👨‍🍳", "desc": "맛과 예술을 요리로 표현"},
            {"job": "플로리스트", "icon": "💐", "desc": "꽃으로 감성을 표현하는 전문가"},
        ],
    },
    "ESTP": {
        "nickname": "사업가 💥",
        "emoji": "⚡",
        "color": "#FFC107",
        "gradient": "linear-gradient(135deg, #FFC107 0%, #E65100 100%)",
        "desc": "행동이 말보다 앞서는 현실주의 모험가. 위기를 기회로 바꾸는 타고난 감각을 보유합니다.",
        "traits": ["⚡ 행동력", "🎯 현실적", "🃏 순발력", "🌍 사교적"],
        "careers": [
            {"job": "세일즈 전문가", "icon": "💼", "desc": "뛰어난 설득력으로 영업을 이끔"},
            {"job": "응급의학과 의사", "icon": "🚨", "desc": "위기 상황에서 빠른 판단을 내림"},
            {"job": "기업가 / 사업가", "icon": "💰", "desc": "위험을 감수하며 사업을 펼침"},
            {"job": "스포츠 선수", "icon": "🏅", "desc": "신체 능력을 최고로 발휘하는 직업"},
            {"job": "형사 / 수사관", "icon": "🕵️", "desc": "현장에서 직감과 관찰력으로 수사"},
            {"job": "파이낸셜 트레이더", "icon": "📊", "desc": "순간적 판단으로 금융 시장에서 활약"},
        ],
    },
    "ESFP": {
        "nickname": "연예인 🎤",
        "emoji": "🎊",
        "color": "#E040FB",
        "gradient": "linear-gradient(135deg, #E040FB 0%, #6A1B9A 100%)",
        "desc": "삶 자체가 무대인 자유로운 엔터테이너! 사람들에게 에너지와 기쁨을 선사합니다.",
        "traits": ["🎉 활기참", "🌟 매력적", "💃 즉흥적", "❤️ 따뜻함"],
        "careers": [
            {"job": "배우 / 엔터테이너", "icon": "🎬", "desc": "무대와 스크린을 누비는 예술가"},
            {"job": "이벤트 호스트 / MC", "icon": "🎤", "desc": "행사를 빛나게 하는 사회자"},
            {"job": "플라이트 어텐던트", "icon": "✈️", "desc": "하늘 위에서 최고의 서비스 제공"},
            {"job": "피트니스 트레이너", "icon": "💪", "desc": "사람들의 건강과 활력을 책임짐"},
            {"job": "유아 교육 전문가", "icon": "🧒", "desc": "아이들과 함께하는 에너지 넘치는 교육자"},
            {"job": "뷰티 크리에이터 / 메이크업 아티스트", "icon": "💄", "desc": "아름다움을 만들어내는 아티스트"},
        ],
    },
}

MBTI_GROUPS = {
    "🔵 분석가형 (NT)": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "🟣 외교관형 (NF)": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "🟢 관리자형 (SJ)": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "🟡 탐험가형 (SP)": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Space+Grotesk:wght@400;600;700&display=swap');

* { font-family: 'Noto Sans KR', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    min-height: 100vh;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem 3rem; max-width: 1200px; margin: 0 auto; }

.hero-section {
    text-align: center;
    padding: 3rem 1rem 2rem 1rem;
    position: relative;
}
.hero-section::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse, rgba(140,100,255,0.25) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(90deg, #a78bfa, #f472b6, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 0.5rem;
}
.hero-sub {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.65);
    margin-bottom: 2rem;
    font-weight: 300;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 50px;
    padding: 0.4rem 1.2rem;
    font-size: 0.85rem;
    color: rgba(255,255,255,0.7);
    margin: 0 0.3rem;
    backdrop-filter: blur(10px);
}
.section-header {
    font-size: 1.3rem;
    font-weight: 700;
    color: rgba(255,255,255,0.9);
    margin: 2rem 0 1rem 0;
    padding-left: 0.8rem;
    border-left: 4px solid #a78bfa;
}
.group-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: rgba(255,255,255,0.6);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 1.5rem 0 0.6rem 0;
}
div[data-testid="stButton"] button {
    width: 100%;
    background: rgba(255,255,255,0.07);
    border: 1.5px solid rgba(255,255,255,0.15);
    border-radius: 14px;
    color: white;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.7rem 0.5rem;
    transition: all 0.25s ease;
    backdrop-filter: blur(8px);
}
div[data-testid="stButton"] button:hover {
    background: rgba(167,139,250,0.25);
    border-color: #a78bfa;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(167,139,250,0.3);
}
.result-hero {
    border-radius: 24px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.result-hero::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 60%);
    pointer-events: none;
}
.result-mbti-name {
    font-size: 4rem;
    font-weight: 900;
    color: white;
    letter-spacing: 0.05em;
    font-family: 'Space Grotesk', sans-serif;
    text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.result-nickname {
    font-size: 1.5rem;
    color: rgba(255,255,255,0.85);
    font-weight: 500;
    margin-bottom: 1rem;
}
.result-desc {
    font-size: 1rem;
    color: rgba(255,255,255,0.8);
    line-height: 1.7;
    font-weight: 300;
    max-width: 600px;
}
.result-big-emoji {
    font-size: 5rem;
    position: absolute;
    right: 2.5rem;
    top: 2rem;
    opacity: 0.85;
    text-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.trait-chip {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border-radius: 50px;
    padding: 0.3rem 0.9rem;
    font-size: 0.85rem;
    color: white;
    margin: 0.2rem;
    font-weight: 500;
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255,255,255,0.2);
}
.career-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.career-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 1.3rem 1.4rem;
    transition: all 0.25s ease;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
}
.career-card:hover {
    background: rgba(255,255,255,0.10);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}
.career-icon {
    font-size: 2.2rem;
    margin-bottom: 0.6rem;
    display: block;
}
.career-job-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: white;
    margin-bottom: 0.3rem;
}
.career-job-desc {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.6);
    line-height: 1.5;
}
.career-rank {
    position: absolute;
    top: 0.9rem;
    right: 1rem;
    font-size: 0.75rem;
    color: rgba(255,255,255,0.3);
    font-weight: 600;
}
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.4), rgba(244,114,182,0.4), transparent);
    margin: 2rem 0;
}
.tip-box {
    background: rgba(167,139,250,0.1);
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-top: 1.5rem;
    color: rgba(255,255,255,0.75);
    font-size: 0.9rem;
    line-height: 1.6;
}
.footer {
    text-align: center;
    padding: 2rem 0 1rem 0;
    color: rgba(255,255,255,0.3);
    font-size: 0.82rem;
}
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.4); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────────────────
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🔮 MBTI 직업 추천</div>
    <div style="font-size:2rem; margin-bottom:0.5rem;">✨ Career Guide ✨</div>
    <div class="hero-sub">나의 성격 유형에 딱 맞는 직업을 발견해보세요 🚀</div>
    <div>
        <span class="hero-badge">🧠 16가지 유형</span>
        <span class="hero-badge">💼 96가지 직업</span>
        <span class="hero-badge">🌟 진로 탐색</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

# ── MBTI Selector ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">👇 나의 MBTI를 선택하세요</div>', unsafe_allow_html=True)

for group_name, types in MBTI_GROUPS.items():
    st.markdown(f'<div class="group-label">{group_name}</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, mbti in enumerate(types):
        with cols[i]:
            d = MBTI_DATA[mbti]
            label = f"{d['emoji']} {mbti}\n{d['nickname']}"
            if st.button(label, key=f"btn_{mbti}", use_container_width=True):
                st.session_state.selected_mbti = mbti

st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

# ── Result ────────────────────────────────────────────────────────────────────
if st.session_state.selected_mbti:
    mbti = st.session_state.selected_mbti
    data = MBTI_DATA[mbti]

    st.markdown('<div class="section-header">🌟 나의 MBTI 분석 결과</div>', unsafe_allow_html=True)

    traits_html = "".join([f'<span class="trait-chip">{t}</span>' for t in data["traits"]])
    st.markdown(f"""
    <div class="result-hero" style="background: {data['gradient']};">
        <span class="result-big-emoji">{data['emoji']}</span>
        <div class="result-mbti-name">{mbti}</div>
        <div class="result-nickname">{data['nickname']}</div>
        <div style="margin-bottom:1rem;">{traits_html}</div>
        <div class="result-desc">{data['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="section-header">💼 {mbti} 유형에게 추천하는 직업 TOP 6</div>', unsafe_allow_html=True)

    careers = data["careers"]
    cards_html = '<div class="career-grid">'
    for idx, c in enumerate(careers):
        top_badge = "🥇" if idx == 0 else ("🥈" if idx == 1 else ("🥉" if idx == 2 else f"#{idx+1}"))
        cards_html += f"""
        <div class="career-card" style="border-top: 3px solid {data['color']}80;">
            <span class="career-rank">{top_badge}</span>
            <span class="career-icon">{c['icon']}</span>
            <div class="career-job-name">{c['job']}</div>
            <div class="career-job-desc">{c['desc']}</div>
        </div>
        """
    cards_html += '</div>'
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="tip-box">
        💡 <strong>진로 탐색 TIP!</strong><br>
        추천 직업은 {mbti} 유형의 강점과 성향을 기반으로 선정된 것입니다.
        실제 직업 선택 시에는 개인의 관심사, 역량, 환경을 종합적으로 고려하세요.
        🔍 각 직업에 대해 더 깊이 알아보고 싶다면 관련 학과, 자격증, 현직자 인터뷰를 참고해보세요!
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center; padding: 4rem 2rem; color: rgba(255,255,255,0.3);">
        <div style="font-size:4rem; margin-bottom:1rem;">🔮</div>
        <div style="font-size:1.2rem; font-weight:500;">위에서 MBTI를 선택하면</div>
        <div style="font-size:1rem; margin-top:0.5rem;">나에게 맞는 직업 추천이 나타납니다 ✨</div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="fancy-divider"></div>
<div class="footer">
    ✨ MBTI Career Guide &nbsp;|&nbsp; 🎓 진로 교육용 서비스 &nbsp;|&nbsp; 💜 Made with Streamlit
</div>
""", unsafe_allow_html=True)
