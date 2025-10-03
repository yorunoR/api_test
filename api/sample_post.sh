#!/bin/bash

curl -X POST http://localhost:8888/recipes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "トマトスープ",
    "making_time": "15分",
    "serves": "5人",
    "ingredients": "玉ねぎ, トマト, スパイス, 水",
    "cost": "450"
  }'
