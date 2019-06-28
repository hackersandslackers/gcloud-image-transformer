"""Endpoint for optimizing images."""
from flask import Flask, request, jsonify, make_response
from images import optimize_images


def main(request):
    """Entry point."""
    response = jsonify(optimize_images())
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST'
    }
    return make_response(response, 200, headers)
