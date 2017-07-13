from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "sharpie7"))


user_id_counter = 0
item_id_counter = 0
store_id_counter = 0


# -------------- User ---------------
def add_user(tx, name, id):
    tx.run("CREATE (n: User { "
           "name: $name,"
           "id: $id"
           "})",
           name=name,
           id=id
    )

    
def find_user(tx, id):
    result = tx.run("MATCH (n: User {id: $id})"
                    "RETURN n.name as name, n.id as id",
                    id=id)
    for record in result:
        print record["name"] + " " +  str(record["id"])


def delete_user(tx, id):
    result = tx.run("MATCH (n:User {id: $id})"
                    "DETACH DELETE n",
                    id=id)
    if result.single() == None:
        return True
    else:
        return False

    
# ------------- Item ------------
    
def add_item(tx, name, id):
    result = tx.run("CREATE (n :Item {"
                    "name: $name,"
                    "id: $id"
                    "})",
                    name=name,
                    id=id)

def find_item(tx, id):
    result = tx.run("MATCH (n:Item {id: $id})"
                    "RETURN n.name as name, n.id as id",
                    id=id)
    
    
def delete_item(tx, id):
    result = tx.run("MATCH (n:Item {id: $id})"
                    "DETACH DELETE n",
                    id=id)
    if result.single() == None:
        return True
    else:
        return

    
# ----------- Store -----------

def add_store(tx, name, id):
    result = tx.run("MATCH(n:Store {"
                    "name: $name,"
                    "id: $id"
                    "})",
                    name=name,
                    id=id)

def find_store(tx, id):
    result = tx.run("MATCH (n:Store {id: $id}"
                    "RETURN n.name as name, n.id as id",
                    id=id)

def delete_store(tx, id):
    result = tx.run("MATCH (n:Store {id: $id}"
                    "DETACH DELETE n",
                    id=id)
    if result.single() == None:
        return True
    else:
        return False

    
# --------- Follows -----------


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
    session.write_transaction(add_user, "Test User", user_id_counter)
    user_id_counter += 1
    session.write_transaction(find_user, 0)
    session.write_transaction(delete_user, 0)
    session.write_transaction(find_user, 0)
