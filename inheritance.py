# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:16:57 2021

@author: vignesh jaishankar
"""

class Team:

    def __init__(self, Name = "Name", Origin = "Origin"):             
        self.TeamName = Name
        self.TeamOrigin = Origin                                      

    def DefineTeamName(self, Name):                                  
        self.TeamName = Name


    def DefineTeamOrigin(self, Origin):                              
        self.TeamOrigin = Origin

class Player(Team):
    def __init__(self,PlayerName,PPoints,TeamName,TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PPoints
    
    def ScoredPoint(self):
        self.PlayerPoints += 1 
    
    def setName(self,Name):
        self.PlayerName = Name
    
    def __str__(self):#str helps to diredtly call player 1
        return self.PlayerName + " has scored : " + str(self.PlayerPoints) + "Points"

Player1 = Player("Hitman",10,"mumbai indians","mumbai") #object

print(Player1.PlayerName)
print(Player1.PlayerPoints)
#Player1.DefineTeamName("Sharks")
print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.ScoredPoint()
print(Player1.PlayerPoints)

Player1.setName("pandaya")
print(Player1.PlayerName)

print(Player1)