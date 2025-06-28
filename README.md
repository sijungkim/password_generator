# 🔒 시너지 OS: 파이썬 OOP 암호 생성기

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-ff69b4.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Synergy OS와 함께 진행한 첫 번째 포트폴리오 프로젝트입니다. Python의 객체 지향 프로그래밍(OOP) 원칙을 깊이 있게 학습하고 적용하는 것을 목표로 제작한 웹 기반 암호 생성 애플리케이션입니다.

---

## 🚀 주요 기능 (Features)

-   **다양한 암호 모델:** Simple, Strong, Very Strong 세 가지 모델 선택 가능
-   **동적 UI:** 선택된 암호 모델에 따라 필요한 옵션(슬라이더)이 동적으로 변경됨
-   **사용자 정의 옵션:** 비밀번호 길이, 대문자/특수문자 포함 개수를 슬라이더로 조절
-   **클립보드 복사:** 생성된 비밀번호를 원클릭으로 복사하는 기능

## 🛠️ 기술 스택 (Tech Stack)

-   **언어:** Python
-   **웹 프레임워크:** Streamlit
-   **라이브러리:** pyperclip
-   **핵심 설계:** 객체 지향 프로그래밍 (상속, 다형성, 캡슐화)

## ⚙️ 로컬 환경에서 실행하기 (Getting Started)

1.  **저장소 복제:**
    ```bash
    git clone [https://github.com/YourUsername/repository-name.git](https://github.com/YourUsername/repository-name.git)
    cd repository-name
    ```

2.  **가상 환경 생성 및 활성화:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **필요한 라이브러리 설치:**
    ```bash
    pip install -r requirements.txt
    ```
    (아래의 '추가 작업 제안'을 참고하여 `requirements.txt` 파일을 먼저 생성해주세요.)

4.  **애플리케이션 실행:**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 주요 학습 내용 (Key Learnings)

이 프로젝트는 단순한 기능 구현을 넘어, 다음과 같은 깊이 있는 소프트웨어 설계 원칙을 체득하는 과정이었습니다.

-   **객체 지향 설계:**
    -   `pwGenerator` -> `strongGenerator` -> `extremeGenerator`로 이어지는 **상속(Inheritance)** 구조를 설계하고 `super()`를 활용했습니다.
    -   UI 렌더링 과정에서 상속의 한계를 인지하고, **다형성(Polymorphism)**을 이용해 `pw.renderGUI()`와 같이 문제를 해결하며 '상속이 만능은 아님'을 배웠습니다.

-   **상태 관리 (State Management):**
    -   `self` 변수를 이용한 '스테이트풀(Stateful)' 설계의 잠재적 위험(상태 누적)을 파악했습니다.
    -   '인자와 반환값'으로만 통신하는 **'스테이트리스(Stateless)' 설계**의 견고함과 예측 가능성에 대해 깊이 학습했습니다.

-   **프레임워크와의 상호작용:**
    -   Streamlit의 '매번 재실행'되는 렌더링 모델을 이해하고, 이것이 객체의 생명주기와 상태 관리에 어떤 영향을 미치는지 분석했습니다.
    -   `st.session_state`를 활용하여 재실행 사이클 간에도 데이터를 유지하는 방법을 적용했습니다.

-   **개발 환경 및 버전 관리:**
    -   `.gitignore`의 중요성을 이해하고, Python 프로젝트에 맞는 템플릿을 적용했습니다.
    -   Git과 GitHub를 이용해 코드를 버전 관리하고 공유하는 기본적인 워크플로우를 익혔습니다.

## 📜 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.