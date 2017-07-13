from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "sharpie7"))

# Add User
def add_user(tx, name):
    tx.run("CREATE (n: User { name: $name })", name=name)

# Test User Was Added
# Was User Removed
def find_user(tx, name):
    user = tx.run("MATCH (n: User {name: $name})"
           "RETURN n.name as name",
           name=name)
    for record in user:
        print record["name"]

# Remove User
def delete_user(tx, name):
    tx.run("MATCH (n:User {name: $name})"
           "DETACH DELETE n",
           name=name)

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
    session.write_transaction(add_user, "Test User")
    session.write_transaction(find_user, "Test User")
    session.write_transaction(delete_user, "Test User")
    session.write_transaction(find_user, "Test User")
