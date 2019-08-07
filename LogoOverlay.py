import numpy as np
import cv2


cap = cv2.VideoCapture(0)

img_path = 'test.png'
logo = cv2.imread(img_path, -1)
dim=(100,100)
watermark = cv2.resize(logo, dim,interpolation=cv2.INTER_AREA)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_h, frame_w, frame_c = frame.shape
    # overlay with 3 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 3), dtype='uint8')
    watermark_h, watermark_w, watermark_c = watermark.shape
    # replace overlay pixels with watermark pixel values
    for i in range(0, watermark_h):
        for j in range(0, watermark_w):
            if watermark[i,j][2] != 0:
                offset = 10
                h_offset = frame_h - watermark_h - offset
                w_offset = frame_w - watermark_w - offset
                overlay[h_offset + i, w_offset+ j] = watermark[i,j]

    cv2.addWeighted(overlay, 1, frame, 0.75, 0, frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()