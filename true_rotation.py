# true_rotation.py
# help from stackoverflow
# https://stackoverflow.com/questions/53097092/frame-from-video-is-upside-down-after-extracting

import ffmpeg
import cv2

# 이 방식의 단점은 휴대폰 가로모드와 세로모드를 구분하지 못한다는 점이다.
# 이를 개선하기 위해 isHorizontal 이라는 변수를 설정하여 해당 값이 True인경우 연산상의 변화가 있도록 개선해볼 수 있다.

def check_rotation(path_video_file, isHorizontal=False):
    # this returns meta-data of the video file in form of a dictionary
    meta_dict = ffmpeg.probe(path_video_file) # dictionary

    # from the dictionary, meta_dict['streams'][0]['tags']['rotate'] is the key
    # we are looking for
    rotateCode = None
    
    print(f"meta_dict keys : {meta_dict.keys()}") # dict_keys(['streams', 'format'])
    
    print(f"streams'][0] : {meta_dict['streams'][0]}")
    
    # problem was the value of rotation was -90 and also there were some indexes that didn't actually match
    
    test = int(meta_dict['streams'][0]['side_data_list'][0]['rotation'])
    
    print(test) # -90
    
    theAngle = (test + 360) % 360
    
    # horizontal perspective
    if isHorizontal:
        if theAngle == 180:
            rotateCode = cv2.ROTATE_90_CLOCKWISE
        elif theAngle == 270:
            rotateCode = cv2.ROTATE_180
        elif theAngle == 0:
            rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE
        
    else:
        # vertical perspective
        if theAngle == 90:
            rotateCode = cv2.ROTATE_90_CLOCKWISE
        elif theAngle == 180:
            rotateCode = cv2.ROTATE_180
        elif theAngle == 270:
            rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE

    return rotateCode

def correct_rotation(frame, rotateCode):  
    return cv2.rotate(frame, rotateCode)