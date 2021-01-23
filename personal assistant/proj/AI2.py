import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from selenium import webdriver # to control browser operations 
from selenium.webdriver.common.keys import Keys
import time

num=1
def assistant_speaks(output):
    global num
    num +=1
    print("Friday : ",output)
    toSpeak=gTTS(text = output ,lang ='en' , slow =False )
    file = str(num)+".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    sobject= sr.Recognizer()
    audio= ''

    with sr.Microphone() as source:
        print("Talk to me....")

        audio = sobject.listen(source, phrase_time_limit = 5)
    print("Gotcha")

    try:

        text = sobject.recognize_google(audio, language = 'en-US')
        print("You : ", text)
        return text

    
    except:
        assistant_speaks("Sorry! pardon me")
        return 0

def process_text(input):
    try:
        if 'search' in input:
            search_web(input.lower())
            return
        
        elif "who are you" in input or "define yourself" in input:
            speak = "Hello, I am Friday. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications."
            assistant_speaks(speak)
            return
        
        elif "who made you" in input or "who created you" in input:
            speak="My creator is Mohammed Ismail."
            assistant_speaks(speak)
            return

        elif "Codewars" in input:
            speak="Codewars is the Online Coding Platform for learning and challenging yourself."""
            assistant_speaks(speak)
            return

        #elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            #app_id = "WOLFRAMALPHA_APP_ID" 
            #client = wolframalpha.Client(app_id) 
  
            #indx = input.lower().split().index('calculate') 
            #query = input.split()[indx + 1:] 
            #res = client.query(' '.join(query)) 
            #answer = next(res.results).text 
            #assistant_speaks("The answer is " + answer) 
            #return

        elif 'open' in input:
            open_application(input.lower())
            return


        else:
            assistant_speaks("I dint get you, I can browse in web if you want...")
            ans=get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans) or "fine browse for me" in str(ans) or "very well" in str(ans):
                search_web(input)
            else:
                return

    except:
        assistant_speaks("I don't understand, Can I search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


def search_web(input):

    driver = webdriver.Edge(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\edgedriver_win64\msedgedriver.exe')
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input:

        assistant_speaks("opening in youtube")
        #indx = input.lower().split().indx('youtube')
        #query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com")#results?search_query =" + '+'.join(query)) 
        driver.find_element_by_name("search_query").send_keys(input)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button").send_keys(Keys.ENTER)  
        time.sleep(3)
        return
    

    elif 'wikipedia' in input:
        assistant_speaks("Opening Wikipedia")
        #indx = input.lower().split()[indx + 1:]
        #query= input.split()[indx + 1:]
        driver.get("https://www.wikipedia.org/")
        driver.find_element_by_name("search").send_keys(input)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/form/fieldset/button").send_keys(Keys.ENTER)
        time.sleep(3)
        return
  
    else: 
  
        if 'google' in input: 
  
            #indx = input.lower().split().index('google') 
            #query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/")
            driver.find_element_by_name("q").send_keys(input)
            time.sleep(3)
            driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
            time.sleep(3)
            return
  
        elif 'search' in input: 
  
            #indx = input.lower().split().index('google') 
            #query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/")
            driver.find_element_by_name("q").send_keys(input)
            time.sleep(3)
            driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
            time.sleep(3)
            return 
  
        else: 
  
            driver.get("https://www.google.com/")
            driver.find_element_by_name("q").send_keys(input)
            time.sleep(3)
            driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
            time.sleep(3)
            return 
  
        return
  
  
# function used to open application 
# present inside the system.
def open_application(input):

    if 'microsoft edge' in input:
        assistant_speaks("Microsoft Edge")
        os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        return

    elif 'mp3 player' in input:
        assistant_speaks("Opening Windows Player")
        os.startfile(r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
        return

    elif 'vlc' in input:
        assistant_speaks("Opening vlc")
        os.startfile(r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe')
        return


    else:
        assistant_speaks("Apllication is not in this system")
        return


if __name__=="__main__":
    assistant_speaks("What is your name,human?")
    name='Human'
    name=get_audio()
    assistant_speaks("Hello, " + name + '.')

    while(1):

        assistant_speaks("What can I do for you?")
        text = get_audio().lower()

        if text == None:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye," + name + '.')
            break

        if "pleasure meeting you" in str(text):
            assistant_speaks("Same here," + name+'.')
            break

        process_text(text)
        

    

    


        

    

    



    
                

            

        
        
