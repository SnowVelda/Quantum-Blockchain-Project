class Chapter1: 
 def __init__(self): 
  self.name = "L0s7 M3m0ry" 
  self.year = 1984 
  self.story = "Y0u w4k3 up 1n 4n 0ld c0mpu73r r00m. Y0u d0n7 kn0w wh0 y0u 4r3." 
  self.puzzle = "F1nd th3 p4ssw0rd t0 th3 d00r." 
 
 def play_chapter(self, game): 
  print(self.story) 
  action = input("Wh4t d0 y0u d0? ") 
  if action == "l00k 4r0und": 
   print("Y0u s33 4n 0ld c0mpu73r w1th 4 p4ssw0rd pr0mpt.") 
   password = input("Wh4t 1s th3 p4ssw0rd? ") 
   if password == "3l0n": 
    print("Y0u 4r3 1n!") 
    game.player_data["year"] = 1985 
   else: 
    print("Y0u 4r3 n0t 1n!") 
  elif action == "h4ck": 
   print("Y0u h4v3 h4ck3d th3 c0mpu73r!") 
   game.blockchain.hack() 
