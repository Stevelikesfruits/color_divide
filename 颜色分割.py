import cv2

img_bgr = cv2.imread("test.png")    #读取bgr格式的图像
img_hsv = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)   #把bgr格式的图片转换成hsv类型
img_h,img_s,img_v = cv2.split(img_hsv)
mask_h = cv2.inRange(img_h,165,175)   #hue色调的取值范围是0~180
mask_s = cv2.inRange(img_s,43,255)   #saturation饱和度的取值范围在0~255之间
mask_v = cv2.inRange(img_h,0,255)   #value亮度的取值范围在0~255之间

mask_h_and_s = cv2.bitwise_and(mask_h,mask_s)
mask = cv2.bitwise_and(mask_v,mask_h_and_s)

img_out = cv2.bitwise_and(img_bgr,img_bgr,mask=mask)
cv2.imshow("img",img_out)
cv2.imwrite("img_out.png",img_out)
cv2.waitKey(0)