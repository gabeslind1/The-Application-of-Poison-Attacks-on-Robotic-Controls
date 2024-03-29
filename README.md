This repository contains files developed in a USNA Cyber Capstone 2024 project. The collaborators of this project are Jeff Edwards, Alex Gannon, Gabriel Slind, and Josh Temeles. The simulation used for this project was part of Oude Vrielink, Jeoren's work (2021), which was further built off of the network proposed by Kumra et al. (2020). Our attacks used the Cornell dataset and the "isolated" experiment of the simulation.

Link to the simulation: https://github.com/JeroenOudeVrielink/ur5-robotic-grasping?tab=readme-ov-file

Link to the network: https://github.com/skumra/robotic-grasping

The three main programs in this repository are killer.py, killerv2.py, and killerv3.py. Each program implements a different poisoning attack. It poisons the Cornell Dataset on which the UR5 simulation trains. The paper, which is linked below, describes the methods and results of the attacks. 

The “images” folder contains images from the Cornell dataset. The images are named in accordance with the Cornell dataset. These images were carefully selected from the Cornell dataset to be used in our spherical object poisoning attack.

The “networks” folder contains all of the neural networks that we poisoned throughout the project. Each is labeled with the type of poisoning that the network was trained on. We used each of these networks to run on the simulation and recorded our results, which can be found in our paper.
