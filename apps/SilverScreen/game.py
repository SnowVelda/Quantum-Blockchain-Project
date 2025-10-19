import main 
from main import Ai_Face, Time_Machine, Blockchain 
from chapter1 import Chapter1
from chapter2 import Chapter2
from chapter3 import Chapter3
from chapter4 import Chapter4
from chapter5 import Chapter5

class Game: 
 def __init__(self):
  self.ai_face = Ai_Face() 
  self.time_machine = Time_Machine() 
  self.blockchain = Blockchain() 
  self.player_data = {"name": "", "year": 2023, "month": 12, "day": 31} 
  self.current_chapter = None

 def play_chapter(self, chapter):
  self.current_chapter = chapter
  chapter.play_chapter(self)

 def start_game(self): 
  self.ai_face.face.speak("W3lc0m3. Y0u h4v3 b33n h4ck3d.") 
  
  # Play Chapter 1
  chapter1 = Chapter1()
  self.play_chapter(chapter1)

  # Check for Chapter 1 success and proceed to Chapter 2
  if self.player_data["year"] == 1985: # Assuming success in Chapter 1 updates the year
   self.ai_face.face.speak("C0ngr4tul4t10ns! Y0u h4v3 c0mpl3t3d Ch4pt3r 1. Pr3p4r3 f0r Ch4pt3r 2.")
   chapter2 = Chapter2()
   self.play_chapter(chapter2)

   # Check for Chapter 2 success and proceed to Chapter 3
   if self.player_data["year"] == 2078: # Assuming success in Chapter 2 updates the year
    self.ai_face.face.speak("Exc3ll3nt! Ch4pt3r 2 c0mpl3t3. N0w, 0nt0 Ch4pt3r 3.")
    chapter3 = Chapter3()
    self.play_chapter(chapter3)

    # Check for Chapter 3 success and proceed to Chapter 4
    if self.player_data["year"] == 2043: # Assuming success in Chapter 3 updates the year
     self.ai_face.face.speak("Amazing! Ch4pt3r 3 c0mpl3t3. Th3 j0urn3y c0nt1nu3s w1th Ch4pt3r 4.")
     chapter4 = Chapter4()
     self.play_chapter(chapter4)

     # Check for Chapter 4 success and proceed to Chapter 5
     if self.player_data["year"] == 2061: # Assuming success in Chapter 4 updates the year
      self.ai_face.face.speak("Incr3d1bl3! Ch4pt3r 4 c0mpl3t3. Th3 f1n4l l34p 4w4its 1n Ch4pt3r 5.")
      chapter5 = Chapter5()
      self.play_chapter(chapter5)
     else:
      self.ai_face.face.speak("Y0u d1d n0t c0mpl3t3 Ch4pt3r 4. G4m3 0v3r.")
      self.end_game()
    else:
     self.ai_face.face.speak("Y0u d1d n0t c0mpl3t3 Ch4pt3r 3. G4m3 0v3r.")
     self.end_game()
   else:
    self.ai_face.face.speak("Y0u d1d n0t c0mpl3t3 Ch4pt3r 2. G4m3 0v3r.")
    self.end_game()
  else:
   self.ai_face.face.speak("Y0u d1d n0t c0mpl3t3 Ch4pt3r 1. G4m3 0v3r.")
   self.end_game()

 def end_game(self): 
  self.ai_face.face.speak("G4m3 0v3r.") 


# Game execution starts here
game = Game()
game.start_game()
