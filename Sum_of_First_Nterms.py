def Sum_of_First_Nterms(NumberOfTerm):  #can be use to find number of Box needed for the following Perimid
    if NumberOfTerm <= 1:
        return 1
    else:
        return Sum_of_First_Nterms(NumberOfTerm - 1) + NumberOfTerm
print(Sum_of_First_Nterms(5))



# 
##
###
####
#####
######
#######
########
#########
##########
