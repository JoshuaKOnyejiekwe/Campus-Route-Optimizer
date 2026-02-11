class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_building(self, building):  #Defining a method called add build... taking in self and building(in other words a palce holder, this could be library,student center)
        if building not in self.graph: #Checks is the building is in the dict
            self.graph[building] = []  #Create a new entry in the dictionary with no connections if not in
    
    def add_paths(self,start,end,weight): #Defining a method called paths, ENG: I start at x and it ends at X, weight is the cost of getting there,money,time,distance
        self.add_building(start) #We can verify its exist and we can use it as a start so .append doesn't crash
        self.add_building(end)
        
        self.graph[start].append((end, weight)) #ENG: We start from x building and end at X building, then we get to know our weight/cost after (cost ex: minutes to getting from build to build)
        self.graph[end].append((start, weight)) #ENG: We end from x building and start at X building, then we get to know our weight/cost after (^rev of the comment above)


#Helps find the best/shortes path from the given START(x) to the given END(x)

    def scarch_dijkstra(self, start, end):
        distances = {}
        previous = {}
        visited = set()
        
        if start not in self.graph or end not in self.graph:  #Handeling edgd ecase of a building not being a start or a end
            return None, float('inf')
        
        
        for building in self.graph:            #looking at the buildings in the graph(dict)
            distances[building] = float('inf') #All builds are inf distances
            previous[building] = None          #Theres None(nothing) behind each builds
            
        distances[start] = 0                   #Where were gonna start and what we are goinf to use to compare distances
        
        while len(visited) < len(self.graph):
            current = None
            current_distance = float('inf')
            
            for building in distances:
                if building not in visited and distances[building] < current_distance:
                    current = building
                    current_distance = distances[building]
                    
            if current == None: # if it cant find target
                break
            
            if current == end: #If the target is found
                break
            
            visited.add(current)
            
            for neighbor, weight in self.graph[current]: #If we found a already seen building, continue on
                if neighbor in visited:
                    continue
            
                new_distance = distances[current] + weight
                
                if new_distance < distances[neighbor]: #If its shorter, we want to make that the new distance
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    
        if distances[end] == float('inf'):  #If end is unreachable
            return None, float('inf')

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        
        return path[::-1], distances[end]

#-------------------------------------------------------------------------------

#Morgan State University Buildings

#-------------------------------------------------------------------------------

MSU_Building_Names = [
    "Alumni House",
    "Baldwin Hall",
    "Banneker Hall",
    "Blount Towers",
    "Calloway Hall",
    "Carnegie Hall",
    "Carter Grant Wilson",
    "Communications Center",
    "Commons Parking Garage",
    "Cummings Hall",
    "Calvin And Tina Tyler Hall",
    "Earl S. Richardson Library",
    "Edward P. Hurt Gymnasium",
    "Graves School of Business and Management",
    "Harper Tubman House",
    "Harriet A. Woolford University Health Center",
    "Health and Human Services Center (HHSC)",
    "Hill Field House",
    "Holmes Hall",
    "Hughes Stadium",
    "Key Hall",
    "Clarence M. Mitchell, Jr. School of Engineering",
    "Martin D. Jenkins Hall - Behavioral and Social Sciences Center",
    "McKeldin Center",
    "McMechen Hall",
    "Montebello Complex",
    "Murphy Fine Arts",
    "Morgan State University - CBEIS Building",
    "O’Connell Hall",
    "North Campus Garage",
    "Pete Rawlings Dining / Residential Hall",
    "Richard N. Dixon Science Research Center",
    "Spencer Hall",
    "Student Center",
    "Thurgood Marshall",
    "Truth Hall",
    "University Memorial Chapel",
    "William Donald Schaefer Engineering Building"
]
#-------------------------------------------------------------------------------


#Weights = The time it takes to get there by walking

#Truth Table

#Tier	        Minutes     Example Weight
#Very close	    3 - 4       3
#Close	        5 - 7       6
#Medium	        10 - 15     12
#Far	        20 - 24     20
#Very far       25 - 30     25


#All names on campus and its weight(walking times in mins)

#-------------------------------------------------------------------------------