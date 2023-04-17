# A doubly linked list is a type of linked list where each node has two pointers: one that points 
# to the next node in the list and another that points to the previous node. This allows for 
# efficient traversal in both forward and backward directions. It can be thought of as a 
# sequence of connected nodes where each node has a value and two pointers, one pointing 
# to the next node and one pointing to the previous node. The first node in the list is called the 
# head, and the last node is called the tail.

import random

class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Playlist:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0
        self.current_song = -1

    def iter(self):
        # Iterate through the list.
        currentent = self.head
        while currentent:
            val = currentent.data
            currentent = currentent.next
            yield val

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node
        self.count += 1

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        current = self.head
        index = 0
        while current:
            if current.data.title == data:
                return index
            current = current.next
            index += 1
        return -1

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.
        if (index > (self.count)):
            return
            
        current = self.head
        prev = self.head

        for n in range(index):
            prev = current
            current = current.next
            
        prev.next = current.next
        current.prev = prev
        self.count -= 1

        if (current == self.head):
            self.head = current.next
            current.prev = None
        elif (current == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def play(self) -> None:
        if (self.current_song < 0):
            self.current_song = 0
            print(f"Playing: {self[self.current_song]}")
        else:
            print(f"Playing: {self[self.current_song]}")

    def skip(self) -> None:
        if self.current_song + 1 >= self.count:
            print("No songs left to skip.")
            return
        self.current_song += 1
        self.play()

    def go_back(self) -> None:
        if self.current_song - 1 < 0:
            print("Can't go back. Already at the first song.")
            return
        self.current_song -= 1
        self.play()
    
    def to_list(self):
        return [song for song in self.iter()]

    def shuffle(self):
        songs_list = self.to_list()
        random.shuffle(songs_list)
        self.clear()
        for song in songs_list:
            self.add_node(song)
        self.current_song = 0

    def show_current_song(self) -> None:
        if self.current_song > -1:
            print(f"Currently playing: {self[self.current_song]}")
        else:
            print("No song is currently playing.")

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        currentent = self.head
        for n in range(index):
            currentent = currentent.next
        return currentent.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        currentent = self.head
        for n in range(index):
            currentent = currentent.next
        currentent.data = value

    def __str__(self):
        song_list = [song for song in self.iter()]
        song_str = "\n".join([str(song) for song in song_list]) #new code to be able to list songs out in list formation. 
        return song_str

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

#4 Create list
playlist = Playlist()
playlist.add_node(Song("For Whom the Bell Tolls", "Metallica"))
playlist.add_node(Song("Enter Sandman", "Metallica"))
playlist.add_node(Song("Master of Puppets", "Metallica"))
playlist.add_node(Song("One", "Metallica"))
playlist.add_node(Song("The Unforgiven", "Metallica"))
playlist.add_node(Song("Fade to Black", "Metallica"))
playlist.add_node(Song("Nothing Else Matters", "Metallica"))

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        # Add song to playlist
        playlist.add_node(Song(title, artist))
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        title = input("Enter song title to remove: ")
        # Remove song from playlist
        index = playlist.indexOf(title)
        if index != -1:
            playlist.deleteAtIndex(index)
            print("Song Removed from Playlist")
        else:
            print("Song not found in Playlist")
    elif choice == 3:
        playlist.play()       
    elif choice == 4:
        playlist.skip()                   
    elif choice == 5:
        playlist.go_back()
    elif choice == 6:
        playlist.shuffle()
        print("Shuffling....")          
    elif choice == 7:
        playlist.show_current_song() 
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(playlist)
    elif choice == 0:
        print("Goodbye.")
        break
