"""회사 블로그 3개의 역할. 주제(topics.csv의 blog 칸), 표지 색, 검수 기준이 여기서 갈립니다."""

BLOGS = {
    "donginensis3047": {
        "name": "동인엔시스 지능형 제어반",
        "role": "지능형 제어반: 이상감지(전류·온도·진동), 유지보수, 도입 가이드",
        "reader": "제조기업 설비·보전 담당자, 공장장",
        "kicker": "INTELLIGENT CONTROL PANEL",
        "theme": "panel",
        "brand_tags": ["동인엔시스", "지능형제어반"],
    },
    "donginensis": {
        "name": "동인엔시스 데이터 인프라",
        "role": "산업설비 데이터 인프라: 수집·표준화, MQTT·OPC UA, MES·AI·디지털트윈 연동",
        "reader": "MES·AI·디지털트윈 IT기업, 스마트공장 추진 담당자",
        "kicker": "INDUSTRIAL DATA INFRA",
        "theme": "data",
        "brand_tags": ["동인엔시스", "설비데이터"],
    },
    "bmk3037": {
        "name": "동인엔시스 현장 이야기",
        "role": "적용 현장(조선·해양, 수소·에너지, 데이터센터), 납품 사례, 회사 이야기",
        "reader": "조선소·선주사·발주처 엔지니어, 협력사, 구직자",
        "kicker": "FIELD STORY",
        "theme": "field",
        "brand_tags": ["동인엔시스", "제어반제작"],
    },
}
ORDER = ["donginensis3047", "donginensis", "bmk3037"]


def get(blog_id):
    if blog_id not in BLOGS:
        raise KeyError(f"모르는 블로그입니다: {blog_id} (가능: {', '.join(ORDER)})")
    return BLOGS[blog_id]
