import cv2
import numpy as np

def cartoon_effect(image_path, median_blur_ksize, bilateral_filter_d, bilateral_filter_sigma_color, bilateral_filter_sigma_space):
    """
    이미지를 카툰 효과로 변환합니다.

    Args:
        image_path (str): 이미지 파일 경로.
        median_blur_ksize (int): Median Blur 커널 크기.
        bilateral_filter_d (int): Bilateral Filter 직경.
        bilateral_filter_sigma_color (int): Bilateral Filter 색 공간 시그마.
        bilateral_filter_sigma_space (int): Bilateral Filter 좌표 공간 시그마.

    Returns:
        numpy.ndarray: 카툰 효과가 적용된 이미지. None 반환 시 오류 발생.
    """
    # Load the image (use the correct file path)
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None  # 오류 발생 시 None 반환

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, median_blur_ksize)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to color image
    color = cv2.bilateralFilter(img, bilateral_filter_d, bilateral_filter_sigma_color, bilateral_filter_sigma_space)

    # Combine the color image with the edges mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

if __name__ == "__main__":
    image_path = "/Users/tuychievjavokhirbek/Library/Mobile Documents/com~apple~CloudDocs/Downloads/rsz_4a57bb9b-8370-44cf-a98f-4c65d52db60a.jpg" # 이미지 경로
    output_path = "cartoon_output.jpg" # 저장할 이미지 경로

    # Adjust filter parameters here
    median_blur_ksize = 5          # Median Blur 커널 크기 (홀수, 클수록 흐려짐)
    bilateral_filter_d = 9         # Bilateral Filter 직경 (클수록 흐려짐)
    bilateral_filter_sigma_color = 100 # Bilateral Filter 색 공간 시그마 (클수록 색이 넓게 퍼짐)
    bilateral_filter_sigma_space = 100 # Bilateral Filter 좌표 공간 시그마 (클수록 영역이 넓게 퍼짐)
    #카툰 효과 적용
    cartoon_image = cartoon_effect(image_path, median_blur_ksize, bilateral_filter_d, bilateral_filter_sigma_color, bilateral_filter_sigma_space)
    #성공적으로 변환시 이미지 저장 및 출력
    if cartoon_image is not None:
        cv2.imwrite(output_path, cartoon_image)
        print(f"Cartoon image saved to {output_path}")
        cv2.imshow("Cartoon", cartoon_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to generate cartoon effect.") #오류 메시지 출력
