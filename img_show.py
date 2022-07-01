import cv2

img_file = "/Users/junwooahn/Documents/OpenCV/img/Pokemon.jpg" # 표시할 이미지 경로
img = cv2.imread(img_file) # 읽은 이미지를 img에 할당
# imread에 의해 return되는 타입은 numpy

if img is not None:
    # 문자열 'IMG'는 창의 제목부분에 나타남
    cv2.imshow('IMG', img) # 읽은 이미지 화면에 표시
    cv2.waitKey() # 키가 입력될 때까지 대기
    cv2.destroyAllWindows() # 창 모두 닫기
else:
    print("No image file.")