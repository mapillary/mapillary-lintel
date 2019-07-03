import time
import lintel
import numpy as np
import sys



def test_lintel_frames_num(filename, width=0, height=0):
    witdh = 0
    height = 0

    with open(filename, 'rb') as f:
        encoded_video = f.read()

        num_frames = 296
        start = time.perf_counter()

        i = 0
        frame_nums = []
        for _ in range(num_frames):
            frame_nums.append(i)
            i+=1
            #i += int(random.uniform(1, 4))
        output_dir = '.'.encode()
        result = lintel.saveframes_frame_nums(encoded_video,
                                        output_dir=output_dir,
                                        frame_nums=frame_nums,
                                        width=width,
                                        height=height,
                                        should_seek=False)

        end = time.perf_counter()

        print('time: {}'.format(end - start))
        
if __name__ == '__main__':
    filename = sys.argv[1]
    test_lintel_frames_num(filename)