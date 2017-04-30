import pyautogui
import random
import time
import numpy



import Markets
import Read
import Settings

from multiprocessing import Pool
  
  
from pykeyboard import PyKeyboardEvent


class keyevent(PyKeyboardEvent):
    def __init__(self):
        super(keyevent, self).__init__()

    def pause(self, keycode, character, press):
        if character == 'p':
            print('Pause, cb de temps ? (valeur entiere en seconde).!!! Ne pas oublier de cliquer sur l item en cours à la fin!!')
            tm = int(input())
            time.sleep(tm)
            return character


   

    
    
    
pyautogui.FAILSAFE = True
        
        
def checkColor2(x,y,tupleColor,tolerance):
    return pyautogui.pixelMatchesColor(x, y, tupleColor, tolerance=tolerance)

def moveMouseToAndClick(x,y,tm):
    pyautogui.moveTo(x,y)
    time.sleep(round(random.uniform(0.1, tm),2))
    pyautogui.click()

def restart():
    while (not (checkColor2(530,401,(101,101,101),tolerance=5)) or not bool(pyautogui.pixel(515, 398) == (101,101,101))):
        pyautogui.press('up')
        delay = random.uniform(0.0, 0.1)
        time.sleep(delay)   

def loopOverMarket(marketName):

    #Sort de la liste du type d'objet
    moveMouseToAndClick(247,124,0.3)

    #Reviens en haut de la liste avec une methode bourrin ...
    moveMouseToAndClick(268,159,0.3)
    stop=(0,0,0)
    restart()
            
    #On regarde si la liste des types ne possède pas de scroll 
    if (not checkColor2(530,194,(104,104,104),tolerance=5)):
        pass
        #~ print('No scroll')
        #~ #Sort de la liste du type d'objet
        #~ moveMouseToAndClick(247,124,0.3)
        #~ print(range(len(Read.readingFrom([235,169,265,472],Settings.settings['Read']['mode']['texte'])[0])))
        #~ while (not (checkColor2(530,401,(101,101,101),tolerance=5)) or not bool(pyautogui.pixel(515, 398) == (101,101,101)))::
           
           #
           
            #~ loopOverItems(marketName)
           #~ #Reviens en haut de la liste avec un methode bourrin ...
            #~ moveMouseToAndClick(268,159,0.3)
            #~ #On descend d'un
            #~ pyautogui.press('down')
           #~ #Sort de la listeq
            #~ moveMouseToAndClick(250,154,0.3)
        #~ loopOverMarket(marketName)
    else:
        while (not (checkColor2(530,401,(101,101,101),tolerance=5)) or not bool(pyautogui.pixel(515, 398) == (101,101,101))):
            #Sortir de la liste
            moveMouseToAndClick(247,124,0.3)
            
            #Fait le tour des items.
            loopOverItems(marketName)
            
            #Clique de liste
            moveMouseToAndClick(250,154,0.3)            
            delay = round(random.uniform(0.1, 0.2),2)
            time.sleep(delay)
            
            #On descend d'un
            pyautogui.press('down')
            delay = round(random.uniform(0.1, 0.2),2)
            time.sleep(delay)
    moveMouseToAndClick(247,124,0.3)        
    loopOverItems(marketName)   #last row     
    loopOverMarket(marketName)            





def loopOverItems(marketName):
    results = {'title':'a'}
    lastObject= 'b'
    count = 0   
     
    pyautogui.moveTo(263,176)
    pyautogui.click()
    restart()
    if not (checkColor2(536,175,(104,104,104),tolerance=5)):
        for n in range(len(Read.readingFrom([265,173,265,472],Settings.settings['Read']['mode']['texte'])[0])):
            pause()
            results = Markets.launch(marketName)['title']
            count = count +1
            if not (results['title'] == lastObject):            
                count = count +1
                Markets.launch('commitDB')
            else :
                Markets.launch('RollBack')
                moveMouseToAndClick(1207,82,0.3)
                time.sleep(0.5)
                moveMouseToAndClick(Settings.settings['Markets']['PNGs'][marketName]['PNG'][0],Settings.settings['Markets']['PNGs'][marketName]['PNG'][1],0.3)
                time.sleep(0.5)
                moveMouseToAndClick(Settings.settings['Markets']['PNGs'][marketName]['Buy'][0],Settings.settings['Markets']['PNGs'][marketName]['Buy'][1],0.3)
                time.sleep(2)
                moveMouseToAndClick(267,173,0.3)
                for i in range(count-1):
                    time.sleep(0.5)
                    pyautogui.press('down')
                    
                results = Markets.launch(marketName)
                lastObject = results['title']
                
            lastObject = results['title']
            pyautogui.press('down')
        count = 0
        return
        
    else :
        stop = (0,0,0)
        while ( not (checkColor2(536,649,(104,104,104),tolerance=5)) or not (pyautogui.pixel(526, 640) == (97,97,97) )):
            pause()
            results = Markets.launch(marketName)
            if not ( results['title'] == lastObject):            
                count = count +1
                Markets.launch('commitDB')
            else :
                Markets.launch('RollBack')
                moveMouseToAndClick(1207,82,0.3)
                time.sleep(0.5)
                moveMouseToAndClick(Settings.settings['Markets']['PNGs'][marketName]['PNG'][0],Settings.settings['Markets']['PNGs'][marketName]['PNG'][1],0.3)
                time.sleep(0.5)
                moveMouseToAndClick(Settings.settings['Markets']['PNGs'][marketName]['Buy'][0],Settings.settings['Markets']['PNGs'][marketName]['Buy'][1],0.3)
                time.sleep(2)
                moveMouseToAndClick(267,173,0.3)
                for i in range(count-1):
                    time.sleep(0.5)
                    pyautogui.press('down')

                results = Markets.launch(marketName)
                lastObject = results['title']
                
            lastObject = results['title']
            print(lastObject)
            
            pyautogui.press('down')
        count = 0
            
        Markets.launch(marketName)  #last 
        return
            
            
    #~ pool = Pool(processes=1)
    #~ result = pool.apply_async(Markets.launch, '{marketName}'.format(marketName=marketName), callback=finish)           
    #Loop over item for sale


if __name__ == '__main__':
    k = keyevent()
    k.daemon = False
    k.start()
    loopOverMarket('Resources')
    
    
    
    
    
    
    
    
    
    
    #Debug
    #~ while (True):
      #~ time.sleep(5) 
      #~ x,y = pyautogui.position()
      #~ print(x,y)
      #~ print(pyautogui.pixel(x, y))
      #~ stop = pyautogui.pixel(515, 398)
      #~ print(not (checkColor2(530,401,(101,101,101),tolerance=5)) or not bool(stop == (101,101,101)))
      #~ print(not (checkColor2(530,401,(101,101,101),tolerance=5)),not bool(stop == (101,101,101)))
      
