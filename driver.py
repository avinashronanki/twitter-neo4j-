from neo4j import GraphDatabase

uri = "neo4j://35.242.245.2:7473"
driver = GraphDatabase.driver(uri, auth=("neo4j", "ne04j-gcp"))

def create_friend_of(tx, name, friend):
    tx.run("CREATE (a:Person)-[:KNOWS]->(f:Person {name: $friend}) "
           "WHERE a.name = $name "
           "RETURN f.name AS friend", name=name, friend=friend)

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Bob")

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()



#from py2neo import Graph

#Graph("http://mydomain.com:7474", auth=(NEO4J_USERNAME, NEO4J_PASSWORD))