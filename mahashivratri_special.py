import cv2
import turtle
import numpy as np

def draw_artistic_lines(image_path):
    # load img
    img=cv2.imread(image_path)
    
    if img is None:
        print("Error: image not found!Make sure image.png is in the floder.")
        return
    
    # Resizing
    width=900
    ratio=width/img.shape[1]
    height=int(img.shape[0]*ratio)
    img=cv2.resize(img,(width,height))
    
    # Extract line art colors
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # gold/orange lines
    lower_gold = np.array([0,50,50])
    upper_gold = np.array([30,255,255])
    mask_gold=cv2.inRange(hsv,lower_gold,upper_gold)
    
    # cyan,white
    
    lower_cyan=np.array([80,50,50])
    upper_cyan=np.array([130,255,255])
    mask_cyan=cv2.inRange(hsv,lower_cyan,upper_cyan)
    
    # combine masks
    full_mask=cv2.bitwise_or(mask_gold,mask_cyan)
    
    # detect Contours
    contours,_=cv2.findContours(
        full_mask,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE
    )
    
    # setup turtle screen
    screen=turtle.Screen()
    
    # padding
    screen.setup(width+50,height+50)
    screen.bgcolor("black")
    screen.colormode(255)
    
    # faster screen
    screen.tracer(25)
    
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.width(3)
    
    print(f"Contours found{len(contours)}")
    print("Drawing started...")
    
    
    # draw Contours with shift
    
    y_shift_down=80
    
    for contour in contours:
        if len(contour)<5:
            continue
        
        t.penup()
        
        for i,point in enumerate(contour):  
            p=point[0]
            
            tx=p[0]-width//2
            ty=(height // 2 -p[1])-y_shift_down
            
            if i==0:
                try:
                    b,g,r=img[p[1],p[0]]
                    t.pencolor(r,g,b)
                except IndexError:
                    t.pencolor(255,255,255)
                    
                t.goto(tx,ty)
                t.pendown()
            else:
                t.goto(tx,ty)
        
        screen.update()
                     
    screen.update()
    
    print("Masterpiece Completed!")
    turtle.done()
            
draw_artistic_lines("image.png")
    