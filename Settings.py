import numpy as np
import cv2

settings = {
            
            'Read': {

                     'interpolation_method' : cv2.INTER_CUBIC,
                     'interpolation_k' : 2.5,
  
                     'colors' : {    # Colors are [RGB_min,RGB_max,HSV_min,HSV_max] 
                                     'gray':np.array([[100,100,100],[255,255,255],[0,0,140],[110,100,220]]),  
                                     'white':np.array([[128,128,128],[255,255,255],[0,0,0],[0,0,255]]),
                                     'red':np.array([[65, 76, 136],[110, 110, 203],[0, 64, 64],[7, 206, 206]]),                    
                                     'green':np.array([[42, 70, 41],[70, 190, 90],[45, 64, 64],[60, 206, 206]]),                    
                                     'blue':np.array([[115, 80, 59],[200, 150, 101],[102, 64, 64],[110, 206, 206]]),
                                  },
                     #tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
                     #tessedit_char_whitelist=0123456789
                     'methods' : {    
                                     'single_word':"--psm 8 --oem 2",
                                     'single_textline':"--psm 7 --oem 2",
                                     'columns_text':"--psm 4 --oem 2",
                                     'only_digits':" --psm 7 --oem 2",                   
                                 },
                     
                     'mode' : {  
                                    'texte':'texte', 
                                    'kamas':'kamas',
                              },
                                 
                     'images' : {
                                    'kamas' : cv2.imread('template\kamas_logo.png'),
                                },
        
            
                      },
            
            'Check' : {
                            'Bonus' : ['% Critical','AP','Agility','Chance','Intelligence','MP','Range','Strengh','Summons', 
                    '% Air Resistance','% Critical Hits On The Spell','% Earth Resistance','% Fire Resistance',
                    '% Melee Damage','% Melee Resistance','% Neutral Resistance','% Power','% Ranged Damage',
                    '% Ranged Resistance','% Spell Damage','% Water Resistance','% Weapon Damage',
                    "'S Range Becomes Modificable",'% Melee Resistance','AP Loss Resistance','AP Reduction','Air Damage','Air Resistance',
                    'Changes Speech','Critical Damage','Critical Resistance','Damage','Damage On The Spell','Dodge',
                    'Earth Damage','Earth Resistance','Fire Damage','Fire Resistance','Heals',
                    "Increase's Basic Damage By",'Increase The Range Of By',
                    'Increase The Maximum Number Of Times Can Be Cast Per Target By'
                    'Increase The Maximum Number Of Times Can Be Cast Per Turn By','Initiative','Lock',
                    'MP Loss Resistance','MP Reduction','Neutral Damage','Neutral Resistance','Power (Traps)',
                    'Prospecting','Pushback Damage','Pushback Resistance',"Reduces's AP Cost By",
                    "Reduce's Cooldown Period By",'Reflects Damage','Title:','Trap Damage',
                    'Vitality','Water Resistance','Wisdom','Emote','Is No Longer Linear',
                    'No Longer Requires A Line Of Sight','pods','- AP','- AP Dodge','- AP Reduction','- Agility',
                    '- Air Damage','- Chance','- Critical Damage','- Critical Resistance','- Dodge','- Earth Damage',
                    '- Fire Damage','- HP','- Intelligence','- Lock','- MP','- MP Dodge','-MP Reduction',
                    '- Neutral Damage','- Prospecting','- Pushback Damage','- Range','- Strengh','- Vitality',
                    '- Water Damage','- Wisdom','-% Air Resistance','-% Critical','-% Earth Resistance',
                    '-% Fire Resistance','-% Melee Damage','-% Neutral Resistance',
                    '-% Ranged Damage','-% Ranged Resistance','-% Spell Damage','-% Water Resistance',
                    '-% Weapon Damage']
            
                    },
                    
            
            
            
            'DB' : {
            
                   'connection':'postgresql://postgres:gui@localhost:5432/HDV'
                       
                   },
            
            
            
            
            
            'Markets' : {
                            'location' : {
                                            'otype' : np.array([224,144,227,15]),
                                            'title' : np.array([622,238,300,32]),
                                            'un' : np.array([616,332,96,36]),
                                            'dix' : np.array([716,332,96,36]),
                                            'cent' : np.array([822,332,96,36]),
                                         },
                            'PNGs': {
                                       'Resources': {
                                                            'PNG':(848,427),
                                                            'Buy':(889,490),
                                                            'Sell':(875,474),
                                                            
                                                         }
                            
                                   }
            
                        },
                        
}

if __name__ == "__main__":
    pass
