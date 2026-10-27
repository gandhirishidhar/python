Score = {
    "Sonu" : 100,
    "Munmun" : 25,
    "Shantanu" : 54,
    0: "IT"
}

#print(Score.items())
#print(Score.keys())
#print(Score.values())
Score.update({"Sonu" : 250, "Sonu kumar" : 254})
#print(Score)

print(Score.get( "Munmun"))