**DevOps Core Practical Project**

Riddle Generator

Michael McGarrigle

**ReadMe Content**

1. The Brief
2. Scope
2. App Overview
3. Trello Board
4. Data
5. Technologies Used
6. CI Pipeline
7. Front-End Design
8. Risk Assessment
9. Difficulties Faced
10. Current Issues
11. Improvements To Be Made
12. Authors

**The Brief**

The brief set out for the DevOps Core Practical Project was to create an application that generates "Objects" upon a set of predefined rules. There was a requirement to create a service-orientated architecture for the application and a stipulation that the application must consist of at least 4 services that work together.

**Scope**

The minimum set of requirements for the project were:

A Kanban Board with full expansion on tasks needed to complete the project
Risk assessment and any issues faced during the project
An application fully integrated into a Version Control System using Feature-Branch model, subsequently making use of webhooks through a CI server and deployed to cloud-based virtual machines
The project must follow the Service Oriented architecture that has been asked for
The project must be be deployed using containterisation and use an orchestration tool
The project must make use of a reverse proxy
The project must make use of an Ansible Playbook to provision the environment the application needs to run

**App Overview**

I created a riddle generator which returns a random riddle from a list of 49 possible riddles

Service 1 sends a GET request to Service 4.
Service 4 sends a GET request to Services 2 and 3.
Service 2 receives the GET request and generates a random number between 1 and 7 (inclusive).
Service 3 receives the GET request and generates a random letter between A and G (inclusive).
Service 4 receives responses from Services 2 and 3, and concatenates them into a single result. This result is actually a dictionary key which will return a value... the riddle assigned to that specific key. At this point, the result is commited to the MySQL database.
Service 1 receives the result from Service 4 to display it on the page and also shows a list of the last 10 riddles generated.

![Imgur](https://i.imgur.com/rk21u5h.png)

**Trello Board**

To keep track of my project and the tasks required for its completion I made us of Trello project management. This was to track the tasks of each sprint and understand the minimum requirements for the MVP. This was broken down to a backlog of tasks which were split into seperate sprints, and user stories to understand the Minimum Viable Product. I also prioritised the User Stories as per MoSCoW methodology.




**Database**

The database in use for the application uses a very simple table, as seen below. This was used to hold all riddles generated and assign them an ID.

![Imgur](https://i.imgur.com/IADKqId.png)


**Technologies Used**

To keep in line with the brief I made us of the following technologies that were learned during my training:

Trello - Project Management / Kanban Board
Google Cloud Platform - Cloud hosting
mySQL - Database technology implemented via GCP
Linux - Server OS used for hosting web app in GCP
Docker - Used for containerisation of application. Making use of Docker Compose and Docker Swarm.
Python - Application Back-End
HTML - Application Front-End
Flask - As applications Web Framework
Git - Version Control also making use of GitHub
Jenkins - CI Server
Ansible - Used as the configuration management, making use of ansible playbooks for deployment configuration.
NGINX - Used as web server utilising reverse proxy to access site without specifying ports.

**CI Pipeline**

![Imgur](https://i.imgur.com/o7wnwx3.jpg)

The image above details the CI Pipeline implemented for this project.
Source Code - Written and tested locally while being commited to preestablished GitHub Repo making use of the feature branch model.
Project Tracking - We then look to Trello to confirm our previous job from project backlog was complete, and look to take on the next.
Version Control System - Git is used to branch from the functioning app repository when developing each job from Trello, before being merged back into the main branch. (See screenshot below)
CI Server - When a new commit has been made, Jenkins will run a job to replace the old version with the new from GitHub, and rerun the Docker Compose and Ansible Playbook. This would also cause new docker images to be built and pushed to Docker Hub.
NGINX is also implemented at this stage to act as a reverse proxy to allow us to access the web app without requiring to specify a port.
This is all deployed on Ubuntu Servers hosted on GCP.


**Risk Assessment**

![Imgur](https://i.imgur.com/fbyv6bT.png)

**Difficulties Faced**

**Cataclysmic failure of PC**

Unfortunately, just over halfway through the project, my PC failed. I had to replace both motherboard and CPU which resulted in a large loss of time to work on the project while awaiting delivery. I found that following the videos on MS Teams did help to get me through most of what had to be completed but the biggest difficulty was getting answers to my questions quickly and I feel my uderstanding of some of the work carried out has suffered due to this. I also put too much pressure on myself to catch up which led to further mistakes.

**Not pushing to GitHub enough**

Also partially due to getting through as much work as possilble, as quickly as possible, I failed to carry out enough pushes to Github. On occassion, this led to me losing work after the failure of my PC thus doubling some of my workload due to my own mistake.


**Current Issues**

App is not currently functioning.

**Future Improvements**

Adding more riddles to the dictionary.
Allowing users to login to track answers.
Persisting data for answers provided by users.

Author
Michael McGarrigle