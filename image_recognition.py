import pyautogui
# Enter your directory that leads to the pictures folder containing all the files needed.
ss = 'C:/Users/user/Documents/Programs/Bloons/image_recognition/pictures/'

play = ss + 'play-button.png'
easy = ss + 'easy-button.png'
home = ss + 'home-button.png'
nextbtn = ss + 'next-button.png'
okbtn = ss + 'ok-button.png'
deflation = ss + 'deflation-button.png'
expert = ss + 'expert-button.png'
infernal = ss + 'infernal.png'



def locateImage(image):
    try:
        imagelocation = pyautogui.locateOnScreen(image, confidence=0.75)
        imagecenter = pyautogui.center(imagelocation)
        return imagecenter
    except pyautogui.ImageNotFoundException:
        # print('[ERROR] Image not found')
        return 0
        
def clickImage(pos):
    pyautogui.click(pos)