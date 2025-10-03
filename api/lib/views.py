import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from lib.models import Recipe

failed_response = {"message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost"}


@csrf_exempt
def recipes(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        title = body.get("title")
        making_time = body.get("making_time")
        serves = body.get("serves")
        ingredients = body.get("ingredients")
        cost = body.get("cost")
        try:
            recipe = Recipe.objects.create(title=title, making_time=making_time, serves=serves, ingredients=ingredients, cost=cost)
            json_data = {
                "message": "Recipe successfully created!",
                "recipe": [
                    {
                        "id": recipe.id,
                        "title": recipe.title,
                        "making_time": recipe.making_time,
                        "serves": recipe.serves,
                        "ingredients": recipe.ingredients,
                        "cost": recipe.cost,
                        "created_at": recipe.created_at,
                        "updated_at": recipe.updated_at,
                    }
                ],
            }
        except Exception as e:
            print(e)
            json_data = failed_response
        return JsonResponse(json_data)
    elif request.method == "GET":
        recipes = Recipe.objects.all()
        recipes_data = [
            {
                "id": recipe.id,
                "title": recipe.title,
                "making_time": recipe.making_time,
                "serves": recipe.serves,
                "ingredients": recipe.ingredients,
                "cost": recipe.cost,
            }
            for recipe in recipes
        ]
        return JsonResponse({"recipes": recipes_data})


@csrf_exempt
def recipe(request, id):
    print(request.method)
    if request.method == "GET":
        recipe = Recipe.objects.get(id=id)
        json_data = {
            "message": "Recipe details by id",
            "recipe": [
                {
                    "id": recipe.id,
                    "title": recipe.title,
                    "making_time": recipe.making_time,
                    "serves": recipe.serves,
                    "ingredients": recipe.ingredients,
                    "cost": recipe.cost,
                }
            ],
        }
        return JsonResponse(json_data)
    elif request.method == "PATCH":
        body = json.loads(request.body.decode("utf-8"))
        print(body)

        recipe = Recipe.objects.get(id=id)
        recipe.title = body.get("title")
        recipe.making_time = body.get("making_time")
        recipe.serves = body.get("serves")
        recipe.ingredients = body.get("ingredients")
        recipe.cost = body.get("cost")

        recipe.save()

        json_data = {
            "message": "Recipe successfully updated!",
            "recipe": [
                {
                    "id": recipe.id,
                    "title": recipe.title,
                    "making_time": recipe.making_time,
                    "serves": recipe.serves,
                    "ingredients": recipe.ingredients,
                    "cost": recipe.cost,
                    "created_at": recipe.created_at,
                    "updated_at": recipe.updated_at,
                }
            ],
        }
        return JsonResponse(json_data)
    elif request.method == "DELETE":
        try:
            Recipe.objects.get(id=id).delete()
            return JsonResponse({"message": "Recipe successfully removed!"})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "No Recipe found"})
