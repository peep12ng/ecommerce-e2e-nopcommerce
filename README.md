nopCommerce, OpenCart public demo has CAPTCHA -> E2E target moved to OpenCart

CI (GitHub Actions)

The workflow runs smoke tests in headless mode on every push/PR to main.

Test artifacts:

pytest-html-report (always uploaded)

screenshots (uploaded on failure only)

## Run (Local)

```bash
# Smoke (GUI)
python -m pytest -m smoke

# Smoke (Headless)
python -m pytest -m smoke --headless

# Smoke + HTML report
python -m pytest -m smoke --headless --html=reports/pytest_reports.html --self-contained-html

## Scope & Notes

 - 본 레포는 Selenium + pytest 기반의 E2E 스모크 테스트 구현을 목표로 합니다.

 - 로컬/CI에서 안정적으로 반복 실행하기 위해 메인 대상은 SauceDemo로 선택했습니다.

 - 공개 데모 스토어(nopCommerce/OpenCart)는 환경에 따라 사람 확인(CAPTCHA/봇체크) 이 발생해 테스트가 불안정해질 수 있어, 관련 시나리오는 legacy로 분리했습니다.

 - 스모크 범위: 로그인 → 상품 1개 담기 → 장바구니 → 체크아웃(1단계) 화면 로드 확인

 - 실패 시 자동으로 스크린샷을 저장하며, CI에서는 HTML 리포트(항상) 와 스크린샷(실패 시) 을 업로드합니다.
