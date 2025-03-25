# hw2-Cartoon-Rendering
필터 강도를 조절하는 기능을 추가하여, Median Blur와 Bilateral Filter의 강도를 조절할 수 있도록 했습니다.
함수 분리: 카툰 효과 생성 로직을 cartoon_effect() 함수로 분리하여 재사용성을 높였습니다.
필터 파라미터 추가: cartoon_effect() 함수에 median_blur_ksize, bilateral_filter_d, bilateral_filter_sigma_color, bilateral_filter_sigma_space 매개변수를 추가하여 필터 강도를 조절할 수 있도록 했습니다.
main문 수정: if __name__ == "__main__": 블록에서 필터 파라미터를 설정하고, cartoon_effect() 함수를 호출하여 카툰 이미지를 생성하고, 결과를 화면에 표시하고 저장합니다.
오류 처리: cartoon_effect 함수에서 이미지 로드 실패 시 None을 반환하고, 호출하는 쪽에서 None을 받았을 경우 오류 메시지를 출력하도록 했습니다.
코드 가독성 향상: 변수 이름을 더 명확하게 변경하고, 주석을 추가하여 코드의 가독성을 높였습니다.
이제 median_blur_ksize, bilateral_filter_d, bilateral_filter_sigma_color, bilateral_filter_sigma_space 변수를 조절하여 카툰 효과의 강도를 변경할 수 있습니다
