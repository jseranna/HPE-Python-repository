import pyautogui
import time

## to loginto sap by bot

class saplogin(object):
	## to define class objects
    def __init__(self, user, pw, inst,trancode):
    	self.userid=user
    	self.password=pw
    	self.instance=inst
    	self.tcode=trancode

    def predata(self):
    	pyautogui.hotkey('win', 'd')


    def saplogon(self):
    	try:
    		pyautogui.hotkey('win','r')
    		pyautogui.typewrite('saplogon')
    		pyautogui.press('enter')
    		return True
    	except:
    		return False

    def logonselection(self):
    	try:
    		pyautogui.hotkey('win','up')
    		return True
    	except:
    		return False

    def openinstance(self):
    	try:
    		pyautogui.hotkey('ctrl','f')
    		pyautogui.typewrite(self.instance)
    		pyautogui.press('enter')
    		return True
    	except:
    		return False

    def saplog(self):
    	try:
    		pyautogui.typewrite(self.userid)
    		pyautogui.press('tab')
    		pyautogui.typewrite(self.password)
    		pyautogui.press('enter')
    		pyautogui.press('enter')
    		return True
    	except:
    		return False

    	    

    def saptcode(self):
    	try:
    		pyautogui.typewrite(self.tcode)
    		pyautogui.press('enter')
    		pyautogui.hotkey('shift','f8')
    		return True
    	except:
    		return False

    	    


### maincode to execute


if __name__ == "__main__":
	mysap = saplogin('xxx','xxx','PJ1','fb03')
	mysap.predata()
	time.sleep(7)
	mysap.saplogon()
	time.sleep(7)
	mysap.logonselection()
	time.sleep(7)
	mysap.openinstance()
	time.sleep(7)
	mysap.saplog()
	time.sleep(7)
	mysap.saptcode()
