from graph import Graph, MSU_Building_Names

campus = Graph()


for building in MSU_Building_Names:
    campus.add_building(building)
    
campus.add_paths("Alumni House", "Student Center", 12)
campus.add_paths("Alumni House", "Baldwin Hall", 12)
campus.add_paths("Baldwin Hall", "Calloway Hall", 6)
campus.add_paths("Banneker Hall", "Carnegie Hall", 3)
campus.add_paths("Blount Towers", "Cummings Hall", 12)
campus.add_paths("Calloway Hall", "Key Hall", 3)
campus.add_paths("Carnegie Hall", "Earl S. Richardson Library", 6)
campus.add_paths("Carter Grant Wilson", "Murphy Fine Arts", 12)
campus.add_paths("Communications Center", "Hill Field House", 12)
campus.add_paths("Cummings Hall", "McKeldin Center", 3)
campus.add_paths("Calvin And Tina Tyler Hall", "Earl S. Richardson Library", 3)
campus.add_paths("Earl S. Richardson Library", "Student Center", 3)
campus.add_paths("Edward P. Hurt Gymnasium", "Hughes Stadium", 3)
campus.add_paths("Graves School of Business and Management", "Student Center", 6)
campus.add_paths("Harper Tubman House", "Truth Hall", 3)
campus.add_paths("Harriet A. Woolford University Health Center", "Earl S. Richardson Library", 3)
campus.add_paths("Health and Human Services Center (HHSC)", "Earl S. Richardson Library", 6)
campus.add_paths("Hill Field House", "Hughes Stadium", 3)
campus.add_paths("Holmes Hall", "Calvin And Tina Tyler Hall", 3)
campus.add_paths("Key Hall", "Clarence M. Mitchell, Jr. School of Engineering", 12)
campus.add_paths("Martin D. Jenkins Hall - Behavioral and Social Sciences Center", "Spencer Hall", 12)
campus.add_paths("McKeldin Center", "Montebello Complex", 12)
campus.add_paths("McMechen Hall", "Alumni House", 12)
campus.add_paths("Montebello Complex", "Pete Rawlings Dining / Residential Hall", 15)
campus.add_paths("Murphy Fine Arts", "University Memorial Chapel", 6)
campus.add_paths("Morgan State University - CBEIS Building", "Clarence M. Mitchell, Jr. School of Engineering", 3)
campus.add_paths("O’Connell Hall", "Thurgood Marshall", 12)
campus.add_paths("North Campus Garage", "Commons Parking Garage", 20)
campus.add_paths("Pete Rawlings Dining / Residential Hall", "Spencer Hall", 3)
campus.add_paths("Richard N. Dixon Science Research Center", "Cummings Hall", 12)
campus.add_paths("Spencer Hall", "Calvin And Tina Tyler Hall", 6)
campus.add_paths("Student Center", "Truth Hall", 6)
campus.add_paths("Thurgood Marshall", "University Memorial Chapel", 12)
campus.add_paths("Truth Hall", "Calvin And Tina Tyler Hall", 3)
campus.add_paths("University Memorial Chapel", "Harper Tubman House", 6)
campus.add_paths("William Donald Schaefer Engineering Building", "Clarence M. Mitchell, Jr. School of Engineering", 3)
    
while True:
    print('Building Options')
    for building in campus.graph:
        print('->' , building)
        
    start = input('Starting location: ').strip()  #Must Have a Start Point / .strip() handels empty spcaes
    end = input('Ending location: ').strip()      #Must End somewhere / .strip() handels empty spcaes
    
    if start not in MSU_Building_Names or end not in MSU_Building_Names: #Inpute Validater check, if spelled wrong or doesnt not exist catch
        print("Invalid building name, please look at the map closely again.")
        continue  #If typed wrong, this here will restart the program back to the top agn  (everything below this gets skipped if wrong)


    path, cost = campus.scarch_dijkstra(start, end)  #Running Search Dijkstra Here
    

    #Either the buildings are not in the graph Or they are disconnected
    if path is None:
        print("\nNo path found between {} and {}.".format(start, end)) #fills in the building names from user input

    else:
        print("\nShortest Path:")
        print(" → ".join(path))
        print("Total Cost:", cost)
    
    looping_the_program = input("Have you found your destination?").lower()
    if looping_the_program != "yes": # if anything but yes is said
        break # Exit running