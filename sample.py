from datetime import datetime
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt","w") as myfile:
    myfile.write("Hi there")
