Step = 1
def Tower_Of_Hnoi(NumberOfPices, From_Source, Destination_Rode, Extra_Rode):
    global Step
    if NumberOfPices == 1:
        print("Step:",Step," Move disk 1 from", From_Source, " Rode to", Destination_Rode, " Rode")
        Step +=1
    else:
        Tower_Of_Hnoi(NumberOfPices - 1, From_Source, Extra_Rode, Destination_Rode)
        print("Step:",Step," Move disk", NumberOfPices,  "from", From_Source, " Rode to", Destination_Rode, " Rode")
        Step += 1
        Tower_Of_Hnoi(NumberOfPices-1, Extra_Rode, Destination_Rode, From_Source)
Tower_Of_Hnoi(3, "A", "C", "B")
