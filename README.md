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

App Overview
I created a riddle generator which returns a random riddle from a list of 49 possible riddles

Service 1 sends a GET request to Service 4.
Service 4 sends a GET request to Services 2 and 3.
Service 2 receives the GET request and generates a random number between 1 and 7 (inclusive).
Service 3 receives the GET request and generates a random letter between A and G (inclusive).
Service 4 receives responses from Services 2 and 3, and concatenates them into a single result. This result is actually a dictionary key which will return a value... the riddle assigned to that specific key. At this point, the result is commited to the MySQL database.
Service 1 receives the result from Service 4 to display it on the page and also shows a list of the last 10 riddles generated.

![Imgur](https://i.imgur.com/rk21u5h.png)

Trello Board
To keep track of my project and the tasks required for its completion I made us of Trello project management. This was to track the tasks of each sprint and understand the minimum requirements for the MVP. This was broken down to a backlog of tasks which were split into seperate sprints, and user stories to understand the Minimum Viable Product.




Database
The database in use for the application uses a very simple table, as seen below. This was used to hold the result of previously opened loot boxes.




Technologies Used
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

CI Pipeline

![Imgur](https://i.imgur.com/o7wnwx3.jpg)

The image above details the CI Pipeline implemented for this project.
Source Code - Written and tested locally while being commited to preestablished GitHub Repo making use of the feature branch model.
Project Tracking - We then look to Trello to confirm our previous job from project backlog was complete, and look to take on the next.
Version Control System - Git is used to branch from the functioning app repository when developing each job from Trello, before being merged back into the main branch. (See screenshot below)
CI Server - When a new commit has been made, Jenkins will run a job to replace the old version with the new from GitHub, and rerun the Docker Compose and Ansible Playbook. This would also cause new docker images to be built and pushed to Docker Hub.
NGINX is also implemented at this stage to act as a reverse proxy to allow us to access the web app without requiring to specify a port.
This is all deployed on Ubuntu Servers hosted on GCP.



Front-End Design
The first implementation of the application simply generated a piece of equipment.




The second implementation of the application generated the piece of equipment and saved it to the database. The previous pieces of equipment



Risk Assessment



Difficulties Faced
NGINX Reverse Proxy
I had encountered an issue with the NGINX Reverse Proxy with a port conflict which was overhanging from previous configuration during development. This tripped me up for a while and through all my troubleshooting I ended up renaming and mispelling a part of my configuration. I had confirmed all parts of the configuration were correct and in place, but that one spelling mistake cost me a couple of hours. This has really enforced that I need to be diligent in spellchecking myself.

Environment Variables
Figuring out how to pass environment variables into the docker containers was just within reach for a long time but I couldn't quite figure it out. In this case I tunnel visioned on one approach and spent too long on it, where as trying something just a little different would have lead me to the correct answer.


Current Issues
List of opened loot currently goes on forever meaning the page can end up incredibly long. This should be limited by only showing the last 50 results in the DB query.

Future Improvements
User sign in to track individual users luck.
Colour each quality of item.
A board showing each item slot and the best quality item found so far for each slot.

Author
Gary Forrow


Resources:
Trello - https://trello.com/b/9hLtft5c/sfia2
Link to app - http://35.189.124.167