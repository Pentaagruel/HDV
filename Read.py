# -*- coding: utf-8 -*-
from pyautogui import screenshot,locate
import numpy as np
from PIL.Image import fromarray, open
import pytesseract
import cv2    
import Settings

pytesseract.pytesseract.tesseract_cmd = 'C:///Program Files (x86)///Tesseract-OCR///tesseract'

def readingFrom(coords,mode,colors=['white'],method='columns_text'):
    """
        Capture et lit une chaine de caractère depuis l'image selon couleur
    """  
    rgbScreen = np.asarray(screenshot(region=(coords[0],coords[1],coords[2],coords[3])))
    hsvScreen = cv2.cvtColor(rgbScreen,cv2.COLOR_BGR2HSV)
    #Declaration a l'avance de l'image sur laquelle on merge chaque threshold, peut etre optimisee        
    hsvBinary = np.zeros((rgbScreen.shape[0],rgbScreen.shape[1]),dtype=np.uint8)
    rgbBinary = np.zeros((rgbScreen.shape[0],rgbScreen.shape[1]),dtype=np.uint8)
    
    if (mode == 'kamas'):
        # A convertir directement
        kamas = cv2.cvtColor(Settings.settings['Read']['images']['kamas'],cv2.COLOR_BGR2GRAY)
        temp_rgbScreen = cv2.cvtColor(rgbScreen,cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(temp_rgbScreen, kamas, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        h,w = kamas.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        rgbScreen.setflags(write=1)
        rgbScreen[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]].fill(0)
            
    for color in colors:
        if (color == 'white'):            
            b,g,r = cv2.split(rgbScreen)
            thresh,hsvBinary_b = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            thresh,hsvBinary_g = cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            thresh,hsvBinary_r = cv2.threshold(r,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            hsvBinary = cv2.bitwise_or(cv2.bitwise_or(b,r),g)          
            rgbThreshold = cv2.inRange(rgbScreen, Settings.settings['Read']['colors'][color][0],Settings.settings['Read']['colors'][color][1])
            rgbBinary = cv2.bitwise_or(rgbBinary,rgbThreshold)
        else:
            hsvThreshold = cv2.inRange(hsvScreen, Settings.settings['Read']['colors'][color][2],Settings.settings['Read']['colors'][color][3])    
            hsvBinary = cv2.bitwise_or(hsvBinary,hsvThreshold)
            rgbThreshold = cv2.inRange(rgbScreen, Settings.settings['Read']['colors'][color][0],Settings.settings['Read']['colors'][color][1])
            rgbBinary = cv2.bitwise_or(rgbBinary,rgbThreshold)

        
    hsvBinary = cv2.resize(hsvBinary,None,fx=Settings.settings['Read']['interpolation_k'], fy=Settings.settings['Read']['interpolation_k'], interpolation = Settings.settings['Read']['interpolation_method'])
    rgbBinary = cv2.resize(rgbBinary,None,fx=Settings.settings['Read']['interpolation_k'], fy=Settings.settings['Read']['interpolation_k'], interpolation = Settings.settings['Read']['interpolation_method'])
    
    #~ cv2.imshow('image',hsvBinary)
    #~ cv2.waitKey(0)
    #~ cv2.destroyAllWindows()
    
    return list(filter(None, pytesseract.image_to_string(fromarray(hsvBinary),lang="eng",config=Settings.settings['Read']['methods'][method]))),list(filter(None, pytesseract.image_to_string(fromarray(hsvBinary),lang="eng",config=Settings.settings['Read']['methods'][method])))    


if __name__ == "__main__":
    pass
