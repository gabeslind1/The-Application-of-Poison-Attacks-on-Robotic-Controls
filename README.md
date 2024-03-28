# The Application-of-Poison-Attacks-on-Robotic-Controls

This project contains files developed in the USNA Cyber Capstone 2024 project of the same name as listed above. The collaborators of this project are Jeff Edwards, Alex Gannon, Gabriel Slind, and Josh Temeles. The simulation used for this project was part of Oude Vrielink, Jeoren's work (2021), which was further built off of the network proposed by Kumra et al. (2020). Our attacks used the Cornell dataset and the "isolated" experiment of the simulation.


Link to the simulation: https://github.com/JeroenOudeVrielink/ur5-robotic-grasping?tab=readme-ov-file

Link to the network: https://github.com/skumra/robotic-grasping

The three main programs in this repository are killer.py, killerv2.py, and killerv3.py. Each program is a different attack on the UR5 simulation and are described in our paper which is linked below.

The images folder contains images from the Cornell dataset which we targeted in our final attack on spherical objects. The images are named in accordance with the Cornell dataset.

The networks folder contains all of the networks that we poisoned throughout the project. Each is labelled with the type of poisoning that the network was trained on. We used each of these networks to run on the simulation and recorded our results, which can be found in our paper.
