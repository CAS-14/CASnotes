import pickle

savedir = "notes"

class Note():
    def __init__(self, name, content, title = None):
        self.name = name
        self.content = content
        self.title = title if title else name

        self.save()

    def save(self):
        pickle.dump(self, open(f"{savedir}/{self.name}.casnote", "wb"))

    def get(self):
        return f"{self.title}\n\n{self.content}\n"

def accessNote(name):
    return pickle.load(open(f"{savedir}/{name}.casnote", "rb"))

def test():
    note = Note("test note 1", "hello world", "testing 123")
    note.save()

    note = Note("test note 2", "hello world world owrrororooror")
    note.save()

    print(accessNote("test note 1").get())
    print(accessNote("test note 2").get())

if __name__ == "__main__":
    test()
