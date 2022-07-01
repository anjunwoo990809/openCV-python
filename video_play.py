import cv2
import true_rotation

video_file = "/Users/junwooahn/Documents/OpenCV/img/rainyvideo.mp4"

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성

# checking wheter the video needs rotating
rotateCode = true_rotation.check_rotation(video_file, isHorizontal=True) # 가로로 찍은 사진 # isHorizontal=True

if cap.isOpened():
    # delaytime = 1000 / fps
    fps = cap.get(cv2.CAP_PROP_FPS) # 영상의 fps 값
    delay = int(1000/fps)
    print(f"FPS: {fps}, Delay: {delay}")
    
    while True:
        ret, img = cap.read()
        
        if rotateCode is not None:
            img = true_rotation.correct_rotation(img, rotateCode) # cv2.ROTATE_180
        
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
            
        else:
            break
        
        # if rotateCode is not None:
        #     frame = true_rotation.correct_rotation(img, cv2.ROTATE_180)
        
else:
    print("can't open video.")

cap.release()
cv2.destroyAllWindows()