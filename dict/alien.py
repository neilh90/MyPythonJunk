alien0 = {"color": "green", "speed": "medium", "x_pos": 0, "y_pos": 25}

print("Alien original x postion: " + str(alien0["x_pos"]))

if alien0["speed"] == "slow":
    x_inc = 1
elif alien0["speed"] == "medium":
    x_inc = 2
else:
    #Alien must be "fast"
    x_inc = 3

alien0["x_pos"] = alien0["x_pos"] + x_inc

print("The alien's new X position is: %s" %str(alien0["x_pos"]))