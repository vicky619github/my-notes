class Team:

    def __init__(self, Name = "Name", Origin = "Origin"):             
        self.TeamName = Name
        self.TeamOrigin = Origin                                      

    def DefineTeamName(self, Name):                                  
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):                              
        self.TeamOrigin = Origin

Team1 = Team("Tigers", "Chicago")                                   
Team2 = Team("Hawks", "Newyork")                                   
Team3 = Team()                                                      
print(Team1.TeamName)                                               
Team1.DefineTeamName("Tigers")
print(Team1.TeamName)                                               
print(Team1.TeamOrigin)                                             
Team1.DefineTeamOrigin("Chicago")
print(Team1.TeamOrigin)                                             
print(Team2.TeamName)                                              
print(Team2.TeamOrigin)                                           
print(Team3.TeamName)                                               
print(Team3.TeamOrigin)                                           