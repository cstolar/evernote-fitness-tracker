# Import ID Generator
from IdGenerator.IdGenerator import idgenerator

# BS
from bs4 import BeautifulSoup


def noteParser(notecontent):
    soup = BeautifulSoup(notecontent, 'html.parser')
    return soup.find_all('td')

# TODO Fix the OOP Setup here
class Workout:
    def __init__(self):
        self.id = idgenerator()
        self.date = ""
        self.exercise = ""
        self.weight = 0
        self.reps = 0

    def addData(self, notecontent):
        finder = noteParser(notecontent)
        for element in finder:
            if element.text == "Date":
                print({element.text: finder[4].text})
            elif element.text == "Exercise":
                print({element.text: finder[5].text})
            elif element.text == "Weight":
                print({element.text: finder[6].text})
            elif element.text == "Reps":
                print({element.text: finder[7].text})
            else:
                pass
