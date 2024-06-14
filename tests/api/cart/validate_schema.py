from utils import assertions as a


def validate_schema(data):
    schema = {
          "type": "object",
          "properties": {
            "addBonuses": {
              "type": "integer"
            },
            "cost": {
              "type": "integer"
            },
            "costGiftWrap": {
              "type": "null"
            },
            "costWithBonuses": {
              "type": "integer"
            },
            "costWithSale": {
              "type": "integer"
            },
            "disabledProducts": {
              "type": "array",
              "items": {}
            },
            "discount": {
              "type": "integer"
            },
            "gifts": {
              "type": "array",
              "items": {}
            },
            "preorderProducts": {
              "type": "array",
              "items": {}
            },
            "products": {
              "type": "array",
              "items": {}
            },
            "promoCode": {
              "type": "null"
            },
            "weight": {
              "type": "integer"
            }
          },
          "required": [
            "addBonuses",
            "cost",
            "costGiftWrap",
            "costWithBonuses",
            "costWithSale",
            "disabledProducts",
            "discount",
            "gifts",
            "preorderProducts",
            "products",
            "promoCode",
            "weight"
          ]
        }
    a.validate_schema(schema, data)
