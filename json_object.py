import twint
import sys
module = sys.modules["twint.storage.write"]

def Json(obj, config):
    tweet = obj.__dict__
    #print(tweet)

module.Json = Json

c = twint.Config()
c.Search = "neo4j OR \"graph database\" OR \"graph databases\" OR graphdb OR graphconnect OR @neoquestions OR @Neo4jDE OR @Neo4jFr OR neotechnology"
c.Store_json = True
c.Custom["user"] = ["id", "tweet", "user_id", "username", "hashtags", "mentions"]
c.User_full = True
c.Output = "tweets_obj.json"
c.Since = "2020-05-20"
c.Hide_output = True

twint.run.Search(c)