# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import string
import itertools
import Settings

    #~ flagsToQuery : {
                    #~ 'empty?': { 'title':False,}   
                    
    #~ }
                    
    #~ flagsToQuery = [    'Title is not empty', 
            #~ 'HSV is not empty', 
            #~ 'RVB is not empty', 
            #~ 'No ascii character found in hsv', 
            #~ 'No ascii character found in rgb', 
            #~ 'No minus,tilt or equal character found',
            #~ 'Lists are same lenght',  
            #~ 'Bonus well written', 
            #~ 'No differences between each String',   
            
            #~ ]

def removeNumbers(string):
    acceptable_characters = "-0123456789"
    return ''.join(list(filter(lambda c: c in acceptable_characters, string)))
    
#Convert each List of String into list before processing
def listToString(li):
    return [ ''.join(i) for i in li ]

def checkResources(results):
    dataToQuery = {}
            
    
    results = listToString(results)    
            
    dataToQuery = checkStringEquality(results[0],results[1],'otype',dataToQuery)
    dataToQuery = checkStringEquality(results[2],results[3],'title',dataToQuery)
    keys = {1:'X1',3:'X10',5:'X100'}
    for i,result in enumerate(results[4:]):        
        if (i%2):
            dataToQuery = checkPrice(results[(i-1)+4],results[i+4],keys[i],dataToQuery)
    return dataToQuery
 
def checkStringEquality(str1,str2,key,dataToQuery):
    """
    Faire du fuzzy matching sur le titre un fois bdd remplie
    """
    if (str1 == str2):
        #~ flagsToQuery[0]='Title are the same'
        dataToQuery[key] = str1 
    else:
        dataToQuery[key] = str1
        #~ flagsToQuery[0]='!!! Title are NOT the same'
    return dataToQuery

def checkCharacterInString(str1):
    for i in str1:
        if (i.isalpha()):
            return True
    return False        

def checkPrice(price1,price2,key,dataToQuery):
    price1 = removeNumbers(price1)
    price2 = removeNumbers(price2)
    #Si a=b et que les deux ne sont pas vides
    if ((price1 == price2) and (bool(price1) and bool(price2))):
        #~ flagsToQuery[0]='Title are the same'
        dataToQuery[key]= price2
    #Sinon on regarde si l'n des deux contient une chaine de caractères. On vérifie egalement la taille entre les deux. 
    elif (bool(price1) and bool(price2)):
    
        equalSize = checkListsEqualSize   (price1,price2)
        charIn1 = checkCharacterInString(price1)
        charIn2 = checkCharacterInString(price2)
        charAscii1 = checkAscii(price1)
        charAscii2 = checkAscii(price2)
        
        if (equalSize):
            if (not(charIn1) and not (charAscii1)) :
                if (not(charIn2) and not (charAscii2)):
                    dataToQuery[key]= price2
                    # Faire d'autres test ici comme l'écart max en les 2 deux nombres
                else :
                    dataToQuery[key]= price1
            else :
                if (not(charIn2) and not (charAscii2)):
                    dataToQuery[key]= price2
                    # Faire d'autres test ici comme l'écart max en les 2 deux nombres
                else : 
                    dataToQuery[key]= ''                  
        else :
            dataToQuery[key]= ''
            #~ if (not(charIn1) and not (charAscii1)) :
                #~ if (not(charIn2) and not (charAscii2)):
                    #~ dataToQuery[key]= price2
                    #~ # Faire d'autres test ici comme l'écart max en les 2 deux nombres
                #~ else :
                    #~ dataToQuery[key]= price1
            #~ else :
                #~ # Faire d'autres test ici comme l'écart max en les 2 deux nombres
                #~ dataToQuery[key]= price1
            
    else :                
        dataToQuery[key]= ''
        #~ flagsToQuery[0]='!!! Title are NOT the same'
        ##Faire un test sur le contenu : Lettre ou non, ecart entre chaque string detecte. Essayer avec autre paramètres ?
    
    return dataToQuery
    
    
def checkEmpty(results,dataToQuery):
    for i,result in results:
        if not (result):
            pass
        #~ flagsToQuery[i]='!!! RGB empty or object with no charac'. Pour savoir si rbg ou hsv, on peut utilser i%2
    return dataToQuery
        
# Retire les signes - ~ = et rajoute - au debut de la string si un (ou plus) des 3 existait    dans cette string
def checkMinus(listCaract):
    toRemove = ['~','=','-'];            
    # Check if there is ~ or =, remove it and add -
    for i,car in enumerate(listCaract):
        removed = False                
        for e in car :
            if e in toRemove:
                removed = True
                listCaract[i] = car.replace(e,'')
                #~ flagsToQuery[5] = '!!! found:'+e+' '                  
        if(removed):
            listCaract[i] = "-"+ listCaract[i]
            
    return listCaract
    
# Verifie si il y a le même un nombre dans chaque string et renvoit la string ou il a le plus grand si ce n'est pas le cas.
def checkDigits(str1,str2):
    try:
        hsvValue = int(''.join(list(filter(str.isdigit, str1))))
    except ValueError:
        hsvValue = 0
    try:
        rgbValue = int(''.join(list(filter(str.isdigit, str2))))
    except ValueError:
        rgbValue = 0
         
    if (hsvValue > rgbValue):
        return str1
    elif(hsvValue > rgbValue):
        return str2
    else :
        return False
# Verifie la presence de caracteres non ascii
def checkAscii(str1):        
    try:
        str1.encode('ascii')
    except UnicodeEncodeError:
        return True
        #log
        #~ flagsToQuery[3]='!!! Ascii character in hsv'
    return False        
            
# Trouve qui a la plus longue et donne au flags
def checkListsEqualSize(list1,list2):
    """
    if false, return false,longuestlist
    else return true,list1
    """    
    if (len(list1)>len(list2)):
        #~ flagsToQuery[6]= 'HSV > RBG'
        return False
    elif(len(list1)<len(list2)):
        #~ flagsToQuery[6]= 'HSV < RBG'
        return False
    else :
        return True

def checkItem(results):
    # Vérifie si l'algo renvoit bien du contenu pour le titre et les resultats de tesseract


    dataToQuery = []
    #~ flagsToQuery = [    'Title is not empty', 
            #~ 'HSV is not empty', 
            #~ 'RVB is not empty', 
            #~ 'No ascii character found in hsv', 
            #~ 'No ascii character found in rgb', 
            #~ 'No minus,tilt or equal character found',
            #~ 'Lists are same lenght',  
            #~ 'Bonus well written', 
            #~ 'No differences between each String',   
            
            #~ ]
            
    checkEmpty(results,dataToQuery)
    checkAscii(results)        
             
    #Perform Minus Check + cleaning
    results[1] = checkMinus(results[1])
    results[2] = checkMinus(results[2])
    

    # Trouve qui a la plus longue et donne au flags
    ran = checkListsEqualSize   (results,flagsToQuery)
       
    for hsv,rgb in itertools.zip_longest(results[1],results[2]):        
           # Si les listes ne sont pas de la même longueur alors on leve un exception
        try :
            # Deux tests ici, 1) on cherche a savoir si, malgré que les strings soient identiques, 
            # elles appartiennent bien à la liste des bonus sinon on corrige avec un fuzzy matching avec une string seulement
       
            if(hsv==rgb):
            #Remoove digits to perform bottom check
                charWithoutDigitsHSV=''.join([i for i in hsv if not i.isdigit()])
            #Get also digits
                try:
                    DigitsHSV = int(''.join(list(filter(str.isdigit, hsv))))
                except ValueError:
                    DigitsHSV = ''
                
                #At least one belongs to well written bonus list ?
                if (charWithoutDigitsHSV) in Check.Bonus:
                    dataToQuery.append(hsv)
                else:
                    #~ flagsToQuery[7]="Bonus no well written"
                    # On cherche la valeur la plus proche dans la liste pour chaque string detectee
                    hsvString = process.extract(charWithoutDigitsHSV, Check.Bonus,scorer=fuzz.ratio ,limit=2)
                    if '-' in charWithoutDigitsHSV:
                        dataToQuery.append("-"+str(DigitsHSV)+" "+hsvString[1][0].replace('-',''))
                    else:
                        dataToQuery.append(str(DigitsHSV)+" "+hsvString[0][0])

            #Sinon , c'est qu'elles ne collent déjà pas : on regarde si une string a un nombre plus grand que l'autre 
            #Si c'est le cas on fuzzy uniquement dessus sinon on fuzzy les 2
            else:
                #~ flagsToQuery[8]="Differences found in string"
                ownNumber = checkDigits(hsv,rgb)
                if (ownNumber):
                    charWithoutDigitsOwnNumber = ''.join([i for i in ownNumber if not i.isdigit()])
                    #Get also digits
                    try:
                        DigitsOwnNumber = int(''.join(list(filter(str.isdigit,ownNumber))))
                    except ValueError:
                        DigitsOwnNumber = ''
                    
                    #At least one belongs to well written bonus list ?
                    if (charWithoutDigitsOwnNumber) in Check.Bonus:
                        dataToQuery.append(ownNumber)
                    else :
                        #~ flagsToQuery[7]="Bonus no well written"
                        # On cherche la valeur la plus proche dans la liste pour chaque string detectee
                        hsvString = process.extract(charWithoutDigitsOwnNumber, Check.Bonus,scorer=fuzz.ratio ,limit=2)
                        if '-' in charWithoutDigitsOwnNumber:
                            dataToQuery.append("-"+str(DigitsOwnNumber)+" "+hsvString[1][0].replace('-',''))
                        else:
                            dataToQuery.append(str(DigitsOwnNumber)+" "+hsvString[0][0])
                
                else:
                    
                    #Remoove digits to perform bottom check
                    charWithoutDigitsHSV = ''.join([i for i in hsv if not i.isdigit()])
                    #Get also digits
                    try:
                        DigitsHSV = int(''.join(list(filter(str.isdigit, hsv))))
                    except ValueError:
                        DigitsHSV = ''
                    
                    # On cherche la valeur la plus proche dans la liste pour chaque string detectee
                    hsvString = process.extract(charWithoutDigitsHSV, Check.Bonus,scorer=fuzz.ratio ,limit=2)
                    
                    #Remoove digits to perform bottom check
                    charWithoutDigitsRGB = ''.join([i for i in rgb if not i.isdigit()])
                    #Get also digits
                    try:
                        DigitsRGB = int(''.join(list(filter(str.isdigit, rgb))))
                    except ValueError:
                        DigitsRGB = ''
                    
                    # On cherche la valeur la plus proche dans la liste pour chaque string detectee
                    rgbString = process.extract(charWithoutDigitsHSV, Check.Bonus,scorer=fuzz.ratio ,limit=2)
                    
                    #On chercche le meilleur match
                    if (hsvString[0][1]>=rgbString[0][1]):
                        #On Envoit
                        if '-' in charWithoutDigitsHSV:
                            dataToQuery.append("-"+str(DigitsHSV)+" "+hsvString[1][0].replace('-',''))
                        else:
                            dataToQuery.append(str(DigitsHSV)+" "+hsvString[0][0])
                    else:
                        if '-' in charWithoutDigitsRGB:
                            dataToQuery.append("-"+str(DigitsRGB)+" "+rgbString[1][0].replace('-',''))
                        else:
                            dataToQuery.append(str(DigitsRGB)+" "+rgbString[0][0])
                            
        except IndexError:
            #normalement déjà marqué avec la fonction lenght
            pass
        
    return dataToQuery


if __name__ == "__main__":
    pass
            
