import pyautogui, time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

"""xcor = int(config[cor]['xcor'])
ycor = int(config['cor']['ycor'])
url = config['cor']['url']"""

xcor = 583
ycor = 538
#url for the engine you wish to use
url = "https://chat.openai.com/?model=text-davinci-002-render-sha"


def SearchNew(url):
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.typewrite(url)
    pyautogui.press("Enter")
    time.sleep(0.5)


def TimeStop(words):
    return 5 + words / 30


topics_input = input("Enter the list of topics separated by commas: ")
topics = [topic.strip() for topic in topics_input.split(',')]
words = int(input("Enter the number of words: "))

print("Switch to browser tab in 2 seconds")
time.sleep(2)
SearchNew(url)
time.sleep(5)

for topic in topics:
    x = words
    if x <= 500:
        query = f"Describe {topic} in {x} words\n"
        pyautogui.typewrite(query)
        time.sleep(TimeStop(x))

    elif x > 500:
        query = f"Describe {topic} in 500 words\n"
        pyautogui.typewrite(query)
        x -= 500
        time.sleep(10)
        while x >= 500:
            query = "Continue writing for 500 words\n"
            pyautogui.typewrite(query)
            x -= 500
            time.sleep(10)
        if x > 0:
            query = f"Continue writing for {x} words\n"
            pyautogui.typewrite(query)
            time.sleep(TimeStop(x))

time.sleep(1)

pyautogui.moveTo(xcor, ycor)
pyautogui.click()

pyautogui.mouseDown()
pyautogui.moveTo(xcor, 0, 2, pyautogui.easeInQuad)
time.sleep(2)

pyautogui.mouseUp()

pyautogui.hotkey('ctrl', 'c')
pyautogui.press('winleft')
time.sleep(0.5)
pyautogui.typewrite('word')
time.sleep(0.5)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)

pyautogui.hotkey('ctrl', 'v')
