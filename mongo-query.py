import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Cluster78180:fpirulinesm@cluster78180.mwv8wrj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster78180")
mydb = myclient["test"]
mycol = mydb["Nicolasito"]
a=0
for x in mycol.find({"status": "A"}):
 print(x)
 a=a+1

print("Cantidad:", a)
