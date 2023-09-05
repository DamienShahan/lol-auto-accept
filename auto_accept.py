import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time
import yaml

# Settings
pyautogui.FAILSAFE = False
TIMELAPSE = 1
with open("resources/settings.yaml", "r") as yamlfile:
    settings = yaml.safe_load(yamlfile)

# Images
acceptButtonImg = f'./resources/{settings["launcherSize"]}/queue-pop.png'
acceptedButtonImg = f'./resources/{settings["launcherSize"]}/queue-accepted.png'
championSelectionImg_flash = f'./resources/{settings["launcherSize"]}/flash-icon.png'
championSelectionImg_emote = f'./resources/{settings["launcherSize"]}/emote-icon.png'
playButtonImg = f'./resources/{settings["launcherSize"]}/play-button.png'

def checkGameAvailableLoop():
    while True:
        print("looking 6")
        pos = imagesearch(acceptButtonImg, 0.8)
        pos = imagesearch(acceptButtonImg)
        print(f"pos 0:{pos[0]}")
        print(f"pos 1:{pos[1]}")
        if not pos[0] == -1:
            pyautogui.click(x=pos[0], y=pos[1])
            print("Game accepted!")
            break
        
        time.sleep(TIMELAPSE)
    
pyautogui.moveTo(2835, 1091)
pyautogui.position()

def checkChampionSelection():
    flash = imagesearch(championSelectionImg_flash)
    emote = imagesearch(championSelectionImg_emote)

    if not emote[0] == -1 or not flash[0] == -1:
        return True
    else:
        return False

def checkGameCancelled():
    accepted = imagesearch(acceptedButtonImg)
    play = imagesearch(playButtonImg)

    if accepted[0] == -1 and not play[0] == -1:
        return True
    else:
        return False


def main():
    run = True
    print("looking 1")
    while run is True:
        print("looking 2")
        checkGameAvailableLoop()
        time.sleep(TIMELAPSE)

        while True:
            print("looking 3")
            cancelled = checkGameCancelled()
            if cancelled is True:
                print("Game has been cancelled, waiting...")
                break
            
            csResult = checkChampionSelection()
            if csResult is True:
                print("Champion selection! Good Luck :D")
                time.sleep(TIMELAPSE)
                run = False
                break

            time.sleep(TIMELAPSE)
        

if __name__ == '__main__':
    print("Running...")
    main()