from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .utils import Converter


def main(request):
    target_cur = request.GET.get('target_cur', None)
    conv = Converter(target_cur)
    result = conv.get_rub_coef()
    print(result)
    # result = 0.015
    dict = {
        'ratio': result
    }
    json_response = JsonResponse(dict)
    return json_response
