# Recommendation Algorithm
Recommendation Algorithm (Context: Uni Individual project) 

Part 1 - User ID-based Recommendation Algorithm:

In this first part, I will develop a recommendation algorithm that operates by processing unique user IDs. Each ID is simply an integer representing a user. The algorithm should iterate through all users, compare their IDs, and calculate the number of common friends between each pair of users. Then, for a user chosen by the program's user, the algorithm will recommend the user who is not already their friend but has the most common friends in the social network.

Part 2 - Using User Names:

In the second part, I will extend the algorithm to allow users to refer to users by their names rather than their IDs. This will make interaction with the program more user-friendly for human users. I will likely need to establish a mapping between user names and their IDs so that the algorithm can still operate internally with IDs.

Part 3 - Using the Program with a Large Number of Users and External Data:

The third part involves using the program with a social network that has a large number of users, with data sourced from external files. This means I will need to implement mechanisms to efficiently import and manage user data from these files. The recommendation algorithm developed in the previous parts will be used to recommend friends in this expanded social network.

In summary, my project aims to develop a recommendation system based on friendship relationships in a social network, starting with a basic implementation using user IDs and evolving into a user-friendly version with user names, and then managing a large number of users and external data.
