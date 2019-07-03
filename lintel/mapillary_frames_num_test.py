import time
import lintel
import numpy as np
import cv2
import sys

def test_lintel_frames_num(filename, width=0, height=0):
    witdh = 0
    height = 0

    with open(filename, 'rb') as f:
        encoded_video = f.read()

        num_frames = 47
        start = time.perf_counter()

        i = 0
        frame_nums = []
        for _ in range(num_frames):
            frame_nums.append(i)
            i+=1

        result = lintel.loadvid_frame_nums(encoded_video,
                                        frame_nums=frame_nums,
                                        width=width,
                                        height=height,
                                        should_seek=False)

        if (width == 0) and (height == 0):
            decoded_frames, width, height = result
        else:
            decoded_frames = result

        decoded_frames = np.frombuffer(decoded_frames, dtype=np.uint8)
        decoded_frames = np.reshape(decoded_frames,
                                    newshape=(num_frames, height, width, 3))

        for idx,frame in enumerate(decoded_frames):
            cv2.imwrite("frame{}.jpg".format(idx), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        end = time.perf_counter()

        print('time: {}'.format(end - start))
        
if __name__ == '__main__':
    filename = sys.argv[1]
    test_lintel_frames_num(filename)