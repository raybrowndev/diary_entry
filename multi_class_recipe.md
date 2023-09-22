# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem


As a user
So that I can record my experiences
I want to keep a regular diary

    #add entry to dictionary
    #arguments: title date, diary text
    #added to a class just for entry and text 

Diary Entry = {"01/09/2023": "Today I had an amazing day. My life is just perfect"}
    
As a user
So that I can reflect on my experiences
I want to read my past diary entries

    #return all entries from the diary 
    #1 - return full dictionary
    #2 - return entries by day


As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

    #return all entries that have a length of text sufficent for reading speed
    #arguments: time alloted, words per minute
    #sum the total lenth of text by the words per minute 


As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
    #CLASS - list of tasks 
    #list of todo's attached to the key of diary date 
    #adding a dictionary key value to entry date 

self._full_entry = {
        "Date" : 01/09/2023,
        "Diary Entry" : "Today I had an amazing day. My life is just perfect", 
        "To Do's: ["walk the cat", "paint the grass"],
        "Contacts": 
            {   "Sarah": 07900000000, 
                "John": 07800000000
            }
        }

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
    #CLASS - name and phone 
    #when i meet a person on a specific day - i add their name and phone number to my diary entry 
    #return a list of all phone numbers and names

final return all details of a diary entry
text, todo, contacts, word 


<!-- nice additions:
#mood tracker by numbets 1-3 (happy, ok, sad) to be added to each date 
#return all to-dos and date added/ diary date title 
#nice date time format -->


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```


                                                     Diary
                                     ┌───────────────────────────────────────┐
                                     │                                       │
                                     │         self._full_entry = {}         │
                                     │                                       │
                                     │                                       │
                                     └───────────────────────────────────────┘

                 DiaryEntry                                                             Contacts
                                                       ToDo
       ┌────────────────────────────┐          ┌──────────────────────────┐       ┌────────────────────────────┐
       │                            │          │                          │       │                            │
       │  self.diary_title          │          │  self.todo               │       │   self.contact_name        │
       │  self.diary_text           │          │                          │       │   self.contact_number      │
       │                            │          │                          │       │                            │
       │                            │          │                          │       │                            │
       │                            │          │                          │       │                            │
       │                            │          │                          │       │                            │
       │                            │          │                          │       │                            │
       └────────────────────────────┘          └──────────────────────────┘       └────────────────────────────┘



                                                         OUTPUT

                ┌──────────────────────────────────────────────────────────────────────────────────────────┐
                │                                                                                          │
                │                                                                                          │
                │   September 1st 2023                                                                     │
                │                                                                                          │
                │                                                                                          │
                │   Diary Entry: I had an amazing day, everything was just perfect and I love my life      │
                │                                                                                          │
                │   To Do: walk the cat, paint the grass, clean the groceries                              │
                │                                                                                          │
                │   Contacts Made: Sarah: 07900000000, John: 07800000000                                   │
                │                                                                                          │
                │   Word Count: 14                                                                         │
                │                                                                                          │
                │                                                                                          │
                └──────────────────────────────────────────────────────────────────────────────────────────┘


```

_Also design the interface of each class in more detail._

self._full_entry = {
        entry1  = {
            "Date" : 01/09/2023,
            "Diary Entry" : "Today I had an amazing day. My life is just perfect", 
            "To Do's: ["walk the cat", "paint the grass"],
            "Contacts": 
                {   "Sarah": 07900000000, 
                    "John": 07800000000
                }
            }

    entry2  = {
            "Date" : 02/09/2023,
            "Diary Entry" : "Today I had an amazing day. My life is just perfect", 
            "To Do's: ["walk the cat", "paint the grass"],
            "Contacts": 
                {   "Sarah": 07900000000, 
                    "John": 07800000000
                }
            }
    }  



entry1  = {
            "Date" : 01/09/2023,
            "Diary Entry" : "Today I had an amazing day. My life is just perfect", 
            }
entry2  = {
            "Date" : 02/09/2023,
            "Diary Entry" : "Today I had an amazing day. My life is just perfect", 
            "To Do's: ["walk the cat", "paint the grass"],
            } 

```python
class FullDiary(Entry, Words, Todo):

    def __init__(self):

    def add_diary(self, diary_entry):
        for i in self._full_entry:
            self._full_entry[i.title] = i.text

    def read_diary(self):
        return self._full_entry
    
    def search_by_title(self, title):
        if title == key in self._full_entry:
            return key value pair 

    def able_to_read()
    pass

    def add_todo(self, todo):
        for existing_todo in self._all_things:
            if existing_todo.task == todo.task:
                raise Exception("task already added")
        self._all_things.append(todo)

    def add_contact(self,contact)


OTHERS

class DiaryEntry:
    def __init__(self, title, text):
        self.title = title
        self.text = text
       


class WordMinute:
    def __init__(self,wpm,minutes)
        self.wpm = wpm
        self.minutes = minutes 

    def reading_time(self, wpm):
        words_to_be_read = self._contents #text
        num_of_words = len(words_to_be_read.split()) #20 words
        time = num_of_words / wpm #20/10
        return time #number of minutes 2
        #if time taken < time avalible return dict 

class Todo:
    def __init__(self, task):
        self.task = task

class Contacts:
    def __init__(self, name, number):
        self.name = name
        self.number = number


entry1 = 

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
add a title and entry
return dict of title and entry 

"""

"""
add a title and entry
search by title
return dict of title and entry 
"""

"""
add a title and entry
search by title
return full dict
"""

"""
add a title and entry
add reading time and time avalible
return dict of entry within reading time
"""

"""
add a title and entry
add todo item 1
add todo item 2
search by title
return dict of title, entry and tasks 
"""

"""
add a title and entry
add contact name and number
add a title and entry
add contact name and number
return all numbers from all dict

"""

"""
add a title and entry
add todo item 1
add todo item 2
add contact and name
add wpm reading time 
search by title
return dict of title, entry and tasks and only text that can be read 
"""

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._