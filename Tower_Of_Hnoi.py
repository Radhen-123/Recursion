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

# Both code hase same output but Secondone is easy to understand

print("------------------------Another code-------------------------------")
def Tower_Hnoi(NumberOfPeg, Source, Destination, Spare):
    if NumberOfPeg == 1:
        print("Move From ",Source," To ",Destination )
    else:
        Tower_Hnoi(NumberOfPeg-1, Source, Spare, Destination)
        Tower_Hnoi(1, Source, Destination, Spare)
        Tower_Hnoi(NumberOfPeg-1, Spare, Destination,Source)
Tower_Hnoi(3, 'A', 'C', 'B')
