from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "sharpie7"))

id = 0

# Add User
def add_user(tx, name, id):
    tx.run("CREATE (n: User { "
           "name: $name,"
           "id: $id"
           "})",
           name=name,
           id=id
    )

# Test User Was Added
# Was User Removed
def find_user(tx, name):
    result = tx.run("MATCH (n: User {name: $name})"
                     "RETURN n.name as name, n.id as id",
                     name=name)

    for record in result:
        print record["name"] + " " +  str(record["id"])

def find_user(tx, id):
    result = tx.run("MATCH (n: User {id: $id})"
                     "RETURN n.name as name, n.id as id",
                     id=id)

    for record in result:
        print record["name"] + " " +  str(record["id"])

# Remove User
def delete_user(tx, id):
    tx.run("MATCH (n:User {id: $id})"
           "DETACH DELETE n",
           id=id)

    result = driver.session().find_user(id)
    

    
# Add Item
def add_item(tx, name):
    tx.run("CREATE (n :Item { name: $name })", name=name)
    
# Was Item Added
# Remove Item
# Was Item Removed
# Add Store
# Was Store Added
# Remove Store
# Was Store Removed
# Add User Follows Item
# Was Follows Added
# Remove User Follows Item
# Was User Follows Item Removed
# Add User Follows Store
# Was Add User Follow Store Added 
# Remove User Follows Store
# Was User Follow Store Removed


# Print All Users
def print_users(tx, name):
    for record in tx.run(" "
                         "", name=name):
        print(record["friend.name"])

        
with driver.session() as session:
    session.write_transaction(add_user, "Test User", id)
    id += 1
    session.write_transaction(find_user, "Test User")
    session.write_transaction(delete_user, 0)
    session.write_transaction(find_user, "Test User")
