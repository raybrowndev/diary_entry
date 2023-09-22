import pytest 
from lib.child_diary import Diary
from lib.entry import Entry
from lib.word import Word


"""
add a title and entry
return dict of title and entry 

"""
def test_add_entry_return_entry():
    entry1 = Entry("Jan 1st 2023", "Today was a great day!")

    my_diary = Diary()

    my_diary.add_entry(entry1)
    result = my_diary.to_dict()
    assert result == [{'Date': 'Jan 1st 2023', 'Diary Entry': 'Today was a great day!'}]

"""
add a title and entry
search by title
return dict of title and entry 
"""

def test_search_by_title():
    entry1 = Entry("Jan 1st 2023", "Today was a great day!")
    entry2 = Entry("Jan 2nd 2023", "Work was so boring. I want better days")

    my_diary = Diary()
    
    my_diary.add_entry(entry1)
    my_diary.add_entry(entry2)
    result = my_diary.search_by_title("Jan 2nd 2023")
    assert result == {'Date': "Jan 2nd 2023", 'Diary Entry': "Work was so boring. I want better days"}


"""
add a title and entry
add reading time and time avalible
return dict of entry within reading time
"""

def test_reading_chunk():
    entry3 = Entry("Jan 3rd 2023", "I've had a very lucky day which I have enjoyed") #10 words

    my_diary = Diary() 
    my_diary.add_entry(entry3) 

    my_wpm = Word(10,1) 
    able_to_read = my_wpm.able_to()

    result = my_diary.reading_chunk(able_to_read)
    assert result == {'Date':"Jan 3rd 2023", 'Diary Entry': "I've had a very lucky day which I have enjoyed"}


"""
add a title and entry
add reading time and time avalible
return dict of entry within reading time
"""

def test_reading_chunk_higher_wpm():
    entry4 = Entry("Jan 4th 2023", "What a wonderful day! A blessing to be alive on a planet called Earth") #14 words

    my_diary = Diary() 
    my_diary.add_entry(entry4) 

    my_wpm = Word(20,1) 
    able_to_read = my_wpm.able_to()

    result = my_diary.reading_chunk(able_to_read)
    assert result == {'Date':"Jan 4th 2023", 'Diary Entry': "What a wonderful day! A blessing to be alive on a planet called Earth"}



"""
EDGE CASE
add reading time less than time avalible
return dict of entry within reading time
"""


def test_reading_chunk_not_able_to_read():
    entry5 = Entry("Jan 5th 2023", "I'm learning a lot about life and I need to learn more") #12 words

    my_diary = Diary() 
    my_diary.add_entry(entry5)

    my_wpm = Word(20,0.5) 
    able_to_read = my_wpm.able_to()

    with pytest.raises(Exception) as e:
        my_diary.reading_chunk(able_to_read)
    error_message = str(e.value)
    assert error_message == 'No entries can be read'



"""
add a title and entry
add todo item 1
add todo item 2
search by title
return dict of title, entry and tasks 
"""


def test_add_enty_todo_return_all():
    entry6 = Entry("Jan 6th 2023", "Work was amazing, I got so much done. I'm proud of all my achievements")


    entry6.add_task("walk the cat")
    entry6.add_task("paint the grass")
    entry6.add_task("feed the laundry")

    my_diary = Diary()
    
    my_diary.add_entry(entry6)

    result = my_diary.to_dict()
    assert result == [{'Date': 'Jan 6th 2023', 'Diary Entry': "Work was amazing, I got so much done. I'm proud of all my achievements", "To Do's": ['walk the cat', 'paint the grass', 'feed the laundry']}]




"""
add a title and entry
add contact name and number
add a title and entry
add contact name and number
return all numbers from all dict

"""



def test_add_entry_todo_contact():
    entry7 = Entry("Jan 7th 2023", "I'm grateful for everything in my life")


    entry7.add_task("walk the cat")
    entry7.add_task("paint the grass")
    entry7.add_contact("Sarah", +4403433882038)
    entry7.add_contact("John", +4403435682039)

    my_diary = Diary()
    
    my_diary.add_entry(entry7)

    result = my_diary.to_dict()
    assert result == [{'Date': 'Jan 7th 2023', 'Diary Entry': "I'm grateful for everything in my life", "To Do's": ['walk the cat', 'paint the grass'], "Contacts": {"Sarah": +4403433882038, "John": +4403435682039}}]
