class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(tracks)
        self.score = float(score)
        
    def change_name(self, new_name):
        self.name = str(new_name)
        print(f"Your new name is: {new_name}")

    def change_age(self, new_age):
        self.age = int(new_age)
        print(f"Your new age is: {new_age}")
    
    def add_track(self, add_track):
        self.track = str(add_track)
        print(f"Your added track is: {add_track}")
    
    def get_score(self, get_score):
        self.score = str(get_score)
        print(f"Your score is: {get_score}")
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)
        

# # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20)