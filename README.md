# Automatic_Traffic_Management_System







I divided this project into 4 parts but I will focus in particular on the part to calculate the speed of the vehicles:

1) Detect and track vehicles
2) Select the area where the vehicle is starting
3) Estimate the time for speed detection
4) Calculate average kilometer per hour

https://github.com/Ashutosh-AI/Automatic_Traffic_Management_System/assets/53949585/54ea1f34-5c89-4e18-b295-ba42e8f31ccd

# Detect and track vehicles

allowed_objects for Detection
(bicycle, car, motorcycle, bus, truck)




# Select the area where the vehicle is starting
To perform speed detection correctly it is necessary to identify areas where the machines start their motion and where it ends. In addition to tracing, we have to draw polygons with OpenCV where we can see the passage of the machines.

At the code level, it is enough to indicate 4 points for each area, one way to do it is this

![image](https://github.com/Ashutosh-AI/Automatic_Traffic_Management_System/assets/53949585/0ad2de31-28d1-41b6-ad84-0fc6cb0db7a8)


# Calculate average kilometer per hour
We have everything we need to calculate speed. With the time and space variable, a small mathematical calculation is enough to obtain the required result and therefore the speed detection for each vehicle.

![clip1](https://github.com/Ashutosh-AI/Automatic_Traffic_Management_System/assets/53949585/b7f78040-d380-4fbc-b803-138fbd0f3c8a)


# Final Output Video:

https://github.com/Ashutosh-AI/Automatic_Traffic_Management_System/assets/53949585/6143aedb-5739-4f98-a390-4d39a9b51d20




# Tech Stack:
Object Detection
Object Tracking
Counting
DeepSort
Yolo V5
OpenCV
