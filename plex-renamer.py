import os

def renameEpisodes(show):
    for tup in show.episodeTuple():
        print(tup)
        ##This can be messed up if the filename contains periods.
        os.rename(os.getcwd()+"/"+tup[0],os.getcwd()+"/"+tup[1]+"."+tup[0].split(".")[1])

class OGTV:
    
    def __init__(self, filelist):
        self.filelist = filelist
        filename = filelist[0]
        self.splitName = filename.split()
        self.title = self.findTitle(filename)
        self.episodeIndex = self.findEpisode(filename)
        self.season = self.findSeason(filename)
        self.newFilelist = self.returnEpisodes()
    
    def findTitle(self, name):
        print(f"Type the title of the show with filename '{name}':\n")
        title = input()
        return title
    
    def findEpisode(self, name):
        print(f"Which of these fields are the episode number?\n")
        for word in name.split():
            print(name.split().index(word), word)
        
        episodeIndex = input()
        return episodeIndex
    
    def returnEpisode(self, name):
        return name.split()[int(self.episodeIndex)]
    
    def findSeason(self, name):
        print(f"What season of this show is '{name}':\n")
        season = input()
        return season
    
    def returnEpisodes(self):
        episodeList = []
        for episode in self.filelist:
            episodeList.append(self.title + " s" + self.season + "e" + self.returnEpisode(episode))
        return episodeList

    def episodeTuple(self):
        pairs = []
        
        for index in range(len(self.filelist)):
            pairs.append((self.filelist[index],self.newFilelist[index]))
        return pairs

print("Type your file path (relative or absolute):")
workDir = input()
os.chdir(workDir)

show = OGTV(os.listdir())
renameEpisodes(show)
print("Remember to rename the folder containing these files to just the title of the show!")
