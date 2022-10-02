import csv
import numpy as np
import math
counter = 0
customer_list = []
super = []
vector_list = []
sub_vector = []
angles = []
average_angle = []
end_of_item = 0
start = 0
check_end = True
item_id = 0
match_id = 0
min_angle = 0
item_angle_list = []
mini_angle_list = []
angle_list_ordered = []
candidate_list = []
Recommended_list = []
loop_done = False





def calc_angle(x,y): #From the lecture notes
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x,y)/(norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

with open("history.txt") as csvfile:
    rdr = csv.reader(csvfile)
    for line in rdr:
        if counter == 0:
            customer_list = line[0].split()
            numberOfItems = customer_list[1]
            numberOfCustomers = customer_list[0]
            numberOfItems = int(numberOfItems)
            numberOfCustomers = int(numberOfCustomers)
            counter = counter + 1
            continue
        line = line[0].split(" ")
        if not(line in super):
            super.append(line)

    #print(super) # prints the list containing positive entries
    for item in range(1, numberOfItems+1): #number of items actually to go through
        for customer in range(1,numberOfCustomers+1):
            if [str(customer), str(item)] in super:
                sub_vector.append(1)
            else:
                sub_vector.append(0)
        vector_list.append(np.array(sub_vector))
        sub_vector = []
    print("Positive entries: "+str(len(super)))
    #prints the vectors for the items

    #Get and average angles of all items
    for v1 in range(0,len(vector_list)):
        for v2 in range(0,len(vector_list)):
            if v1 == v2:
                continue
            angles.append(calc_angle(vector_list[v1],vector_list[v2]))
            if check_end: #Calculates the number gap between items 1 and 2
                    end_of_item = end_of_item + 1
        check_end = False
    end_of_item = end_of_item - 1 #CHANGES
    end  = end_of_item
    average_angle = sum(angles)/len(angles)
    print("Average angle: "+str(round(average_angle,2)))
    #print(angles)
    #print("End of item: ",end_of_item)
    file = open("queries.txt","r")
    for line in file:

        print("Shopping cart:",line,end="")
        line = line.strip()
        line = line.split(" ")

        #print("LINE: "+str(line))
        for item in line: #CHANGE SO IT'S A LIST***
            item_id = item.strip()
            #print("Item id: ",item_id)
            item_index = int(item_id) - 1
            end_of_item = end
            #print("item_id: ",item_id)
            #print("Start before convert: ",start,end_of_item)

            start = (end_of_item + 1) * (item_index)
            end_of_item = start + end_of_item
            item_angle_list = list(range(start,end_of_item+1))
            #print("Start after: ",start,end_of_item)


            for index in item_angle_list: #Append angles to list so we can check for minimum angle
                mini_angle_list.append(angles[index])
            #print("Mini angle extracted: ",mini_angle_list)
            #print("item angle list: ",item_angle_list)
            angle_list_ordered = mini_angle_list[:] #duplicate list so we can add our item_id to it to get match_id
            angle_list_ordered.insert(item_index, "P") #Indicates position of item id in list
            # sort list in order of increasing angles
            mini_angle_list.sort()
            #print("Mini angle FINAL: ",mini_angle_list)
            #print("New angle list: ",angle_list_ordered)
            #print("item currently looking at: ",line[item])


            for angle in mini_angle_list:
                if loop_done == True:
                    break
                indices = [index for index, element in enumerate(angle_list_ordered) if element == angle]
                #print("angle: ",angle)
                #print(angle_list_ordered)
                #print(indices)
                for anglet in indices:
                    #print("Anglet: ",anglet+1)
                    #print("Angle looking at: ",angle)
                    #print("Index in angle list: ",anglet)
                    #CHECK IF THE ITEM IS ALREADY IN THE BASKET
                    if angle < 90 and not(str(anglet+1) in line): #anglet is an index
                        #print("Anglet: ",anglet+1)
                        #print("item in SHOPPING CART?: ", str(anglet+1) in line)
                        #print("LINE ",line)
                        #print("MATCHED!")
                        #print("anglet: ",anglet)
                        angle_end = angle
                        match_id = anglet + 1
                        loop_done = True
                        break

            if match_id == 0:
                match_id = "no match"
            if match_id == "no match":
                print("Item:",item_id,match_id)
            else:
                print("Item:",str(item_id)+"; match: "+str(match_id)+"; angle: "+"{:.2f}".format(angle_end))
                candidate_list.append((match_id,angle_end))
                #print("Before sort: ",candidate_list)


            mini_angle_list = []
            item_angle_list = []
            match_id = 0
            start = 0
            end_of_item = 0
            loop_done = False
            candidate_add = True
        candidate_list.sort(key=lambda x : x[1])
        duplicate_Reccomended = []


        #print("After sort: ",candidate_list)
        #print(candidate_list)
        for rec in candidate_list:
            if not(rec[0] in Recommended_list):
                Recommended_list.append(rec[0])
        print("Recommend:",*Recommended_list, sep=" ")

        #print(Recommended_list)
        candidate_list.clear()
        Recommended_list.clear()




    #print(Item: item_id; match: match_id; angle: min_angle)
