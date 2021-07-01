import cv2
import numpy as np

def process_image(mask, img):

    #print(np.unique(mask)) #return an array of lengtfh having unique elemts

    kernel2=np.ones((10,10),np.uint8)
    #kernel = np.ones((5,5),np.uint8)
    #mask = cv2.erode(mask, kernel,iterations = 1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)
    coloured_mask = cv2.bitwise_and(img, img, mask=mask)
    return coloured_mask,mask

def trackobj(img,mask,coloured_mask):

    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #finds contour

    for c in contours:
        
        M= cv2.moments(c)

        if M['m00']!=0 :

            Cx=int (M['m10']/M['m00'])
            Cy=int (M['m01']/M['m00'])

            cv2.circle(img,(Cx,Cy),5,(123,123,32),-1)

            cv2.drawContours(coloured_mask,[c],-1,(3,200,44),3)
            cv2.putText(img, "center ({},{}) ".format(str(Cx),str(Cy)) , (Cx + 20, Cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

   # cv2.drawContours(img,contours,-1,(3,200,44),3)

    return coloured_mask,img