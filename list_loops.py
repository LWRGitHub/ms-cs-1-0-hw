
#Q1 list of songs
songs = ["ROCKSTAR", "Do It", "For The Night"]

#Q2 print out 1st & 2nd items in list
print(songs[1])
print(songs[2])

#Q2 printed "Do It"and "For The Night"
print(songs[1:3])

#Q3 update the last element
songs[2] = "Treat You Better"
print(songs)

#Q4 three songs added
songs.append("If I Was a Man")
# songs.prepend("Happy") # .prepend() not working sent Jess a slack mesage about it
songs.extend(["Happy"])
songs.insert(0, "Musice Is My Hot Hot Sex")
print(songs)

#Q4 Delete a song
del songs[2]
print(songs)