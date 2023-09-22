class Diary:
    def __init__(self):
        self.all_entries = [] 

    def add_entry(self, entry):
        for i in self.all_entries:
            if i.date == entry.date:
                raise Exception("An entry for this date already exists.")
        self.all_entries.append(entry)


    def to_dict(self):
        for i in self.all_entries:
            entry_dict = {
                "Date": i.date,
                "Diary Entry": i.description,
            }
        return entry_dict

    def search_by_title(self, searched_date):
        for i in self.all_entries:
            if i.date == searched_date:
                entry_dict = {
                    "Date": i.date,
                    "Diary Entry": i.description
                }
        return entry_dict



    def reading_chunk(self, able_to_read):
        for i in self.all_entries:
            len_of_words = len(i.description.split())
            if len_of_words <= able_to_read: #if length o f words is => the number of words in diary 
                return  {"Date": i.date, "Diary Entry": i.description} #return diary entry 
            else:
                raise Exception("No entries can be read") #return no entries for you
