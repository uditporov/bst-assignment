

### Major Modules/Classes
- DataStore (a singleton class)- It acts as a primary module which stores all the data in-memory, all the storage related operations goes from this entity. For each entity it creates a map.
- BaseEntity - Parent class for all the entities, it provides basic CRUD operations to the entity and it handles all the integeration with the DataStore. It also adds "id" attribute to the entities which is UUID value, used as a key in the DataStore.
- app/__init__.py - This module automatically registers all the entities to the DataStore, even if a new entity is created it will register it too, which any changes in it.
   

### Initially loaded data

- Users

        "Admin" user with admin-role (all resource & action access)
        "User1" user with read-role (all resource with read action access)

- Resources
        
        "People"
        "Product"

- ActionType

        "CREATE"
        "DELETE"
        "READ"
        "UPDATE"

- Role

        "admin-role" with all operations access
        "read-role" with read access to all resource
        "create-role" with create access to all resource
        "delete-role" with delete access to all resource


###Assumption
- Role assignment is allowed to all users, right now. No permissions over that.
- Considering the main purpose of assignment, focused more on structural and quality of core parts of application, rather then opening all operations on command line like - creation/updation/deletion of entities


### Frameworks Used
> None


### How to run?
    >>> from app.run import *
    >>> run()

### Working Snaps

- Main Menu

        Hi! You are logged in as Admin
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -

- Switch User with Option 1

        Your choice -1
        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -

- Access resource with proper roles

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -2
        Press 1 to select Resource - People
        Press 2 to select Resource - Product
        Your choice - 1
        Press 1 to select ActionType - CREATE
        Press 2 to select ActionType - DELETE
        Press 3 to select ActionType - UPDATE
        Press 4 to select ActionType - READ
        Your choice - 4
        You are allowed to perform this operation

- Access resource without proper permission

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -2
        Press 1 to select Resource - People
        Press 2 to select Resource - Product
        Your choice - 2
        Press 1 to select ActionType - CREATE
        Press 2 to select ActionType - DELETE
        Press 3 to select ActionType - UPDATE
        Press 4 to select ActionType - READ
        Your choice - 1
        You don't have permission to perform this operation

- Assign Create role to User1

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -3
        Press 1 to select User - User1
        Press 2 to select User - Admin
        Your choice - 1
        Press 1 to select Role - admin-role
        Press 2 to select Role - read-role
        Press 3 to select Role - delete-role
        Press 4 to select Role - create-role
        Your choice - 4

- Check last assigned role

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -2
        Press 1 to select Resource - People
        Press 2 to select Resource - Product
        Your choice - 1
        Press 1 to select ActionType - CREATE
        Press 2 to select ActionType - DELETE
        Press 3 to select ActionType - UPDATE
        Press 4 to select ActionType - READ
        Your choice - 1
        You are allowed to perform this operation

- Remove Create role from User1 
        
        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -4
        Press 1 to select User - User1
        Press 2 to select User - Admin
        Your choice - 1
        Press 1 to select Role - admin-role
        Press 2 to select Role - read-role
        Press 3 to select Role - delete-role
        Press 4 to select Role - create-role
        Your choice - 4

- Remove role which doesn't exists for a User

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -4
        Press 1 to select User - User1
        Press 2 to select User - Admin
        Your choice - 1
        Press 1 to select Role - admin-role
        Press 2 to select Role - read-role
        Press 3 to select Role - delete-role
        Press 4 to select Role - create-role
        Your choice - 4
        This role is not assigned to this user.

- List roles for a User

        Hi! You are logged in as User1
        Press 1 for Login as another user
        Press 2 to access resource
        Press 3 to assign role to a user
        Press 4 to remove role from a user
        Press 5 to list roles of a user
        Your choice -5
        Press 1 to select User - User1
        Press 2 to select User - Admin
        Your choice - 1
        read-role
