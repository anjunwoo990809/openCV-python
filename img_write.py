# color image를 grayscale로 저장하는 코드
import cv2

img_file = "/Users/junwooahn/Documents/OpenCV/img/Pokemon.jpg"
save_file = "/Users/junwooahn/Documents/OpenCV/img/Pokemon_gray.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) # format은 확장자를 따름
cv2.waitKey()
cv2.destroyAllWindows()