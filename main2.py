import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pymongo import MongoClient
from datetime import datetime
import json


# # MongoDB Setup
# client = MongoClient("mongodb://localhost:27017")
# db = client["tenant_schemas"]
# collection = db["tenant_schemas"]

# --------------------------
# Dynamic Type Generation
# --------------------------
type_map = {
    "int": int,
    "str": str,
    "float": float
}  # Removed datetime

# Path to your document.json file
json_file_path = 'document.json'
print('test')
# Load the JSON data into the 'document' variable
with open(json_file_path, 'r') as file:
    document = json.load(file)


annotations = {
    field: type_map[field_type]
    for field, field_type in document["schema"]["fields"].items()
}

DynamicType = strawberry.type(
    type("DynamicData", (object,), {"__annotations__": annotations})
)

# --------------------------
# Schema Setup
# --------------------------
@strawberry.type
class Query:
    @strawberry.field
    def get_data(self) -> DynamicType:
        data = document["data"].copy()
        return DynamicType(**data)

schema = strawberry.Schema(query=Query)
app = FastAPI()
print('test2')
app.include_router(GraphQLRouter(schema), prefix="/graphql")
print('test3')

# {
#   getData {
#     friends
#     lastLoggedOn
#   }
# }
