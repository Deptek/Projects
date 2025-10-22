import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import random
#pip install pocketsphinx
recognizer = sr.Recognizer()


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def processcommand(c):
    if c.lower().startswith("open"):  #yaah agar c.lower likha to command c ka lower mange ga lekin likhna hame c.lower() jisse c ki value ka liower aye
        website=c.lower().split(" ")[1]  #usi valu ka split space ke hisab se karke 1st index pe ane wale word ko website le liya
        webbrowser.open(f"https://{website}.com")
    # elif c.lower().startswith("play song"):
    #     song=c.lower().split(" ")[2]  
    #     webbrowser.open(f"https://www.youtube.{song}.com")
    #     pass , koi tarika dhudo yt ke kisi bhi song ko play karne ka websit ki tarah    
    elif "task" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=gwWKnnCMQ5c&t=2s")
    else:
        #let open ai handle this take the api or ues copilet
        pass


if __name__=="__main__":
    speak("Initialising alfred....")
    
 # speech : listen for the wake word
    while True:

        # obtain audio from the microphone
        r = sr.Recognizer()
            
        #instead of sphinx we will ues google
        # recognize speech using Sphinx (a suite of speech recognition systems developed, open-source nature and its ability to perform speaker-independent, continuous speech recognition)
        
        try:         #this line means listen(from r= recocognize) from the source= microphone and store it in audio
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source ,timeout=2,phrase_time_limit=1) #timeout is time till then system will wait foe an input 
                                                      #and phrase_time is limit that how much time you can wait between saying words   
            word= r.recognize_google(audio) # type: ignore
            print(word)
            
            if (word.lower()=="alfred"):
                z=["ya","yes"] #add more sounds and fine tune the timming

                engine.say(random.choice(z))  #yaha speak wala function nahi chal raha to direct call kardiya h
                
            
                time.sleep(0.5)
                with sr.Microphone() as source:
                    print("alfred active...")
                    audio = r.listen(source ,timeout=2,phrase_time_limit=1)
                    command= r.recognize_google(audio) # type: ignore
                    
                processcommand(command)


        except sr.UnknownValueError:
            print(" could not understand audio")
        except Exception as e:
            print("error; {0}".format(e))