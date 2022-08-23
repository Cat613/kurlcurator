from flask import request
from flask_restx import Resource, Api, Namespace
from recipe_dao import RecipeDao
import json


Recipe = Namespace(
    name="user",
    description="user API.",
)

@Recipe.route('')
class GetRecipe(Resource):
    def get(self):
        """recipe 목록을 가져옵니다."""
        
        li = RecipeDao().getRecipe()
        res = json.dumps(li, ensure_ascii=False, indent=4).encode('utf8')

        print(res)

        return li
    

    def post(self):
        """recipe를 추가합니다."""
        RECIPE_ID = request.json.get('id')
        RECIPE_SN = request.json.get('sn')
        RECIPE_CONT = request.json.get('cont')
        IMAGE_FILE_NM = request.json.get('image')
        RecipeDao().insRecipe(RECIPE_ID, RECIPE_SN, RECIPE_CONT,IMAGE_FILE_NM)
        return {
            "insert" : "success"
        }

