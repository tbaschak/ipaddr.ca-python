import os
import json
from flask import Flask, request, jsonify, Response
from socket import gethostbyaddr, gaierror
from pierky.ipdetailscache import IPDetailsCache

cache = IPDetailsCache()
cache.UseIXPs(WhenUse=2)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "<h1 style='color:salmon'>Hello There!!!!</h1>"

@app.route("/ip", methods=["GET"])
def simple_ip():
    resp = Response(request.remote_addr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp

@app.route("/ptr", methods=["GET"])
def simple_ptr():
    try:
        tmpptr = gethostbyaddr(request.remote_addr)
        ptr = tmpptr[0]
    except gaierror:
        ptr = "none"
    resp = Response(ptr)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp

@app.route("/api/ip", methods=["GET"])
def json_ipaddr_ip():
    resp = jsonify({'ip': request.remote_addr})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp

@app.route("/api/ptr", methods=["GET"])
def json_ipaddr_ptr():
    try:
        tmpptr = gethostbyaddr(request.remote_addr)
        ptr = tmpptr[0]
    except gaierror:
        ptr = "none"
    resp = jsonify({'ptr': ptr })
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp

@app.route("/api/v1/bgp/", methods=["GET","POST"])
def get_bgp_myip():
    if request.method == "POST":
        ip = request.form["text"]
    else:
        ip = request.remote_addr
    result = cache.GetIPInformation(ip)
    resp = jsonify(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp

@app.route("/api/v1/bgp/<ip>", methods=["GET","POST"])
def get_bgp_ip(ip):
    result = cache.GetIPInformation(ip)
    resp = jsonify(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,Accept,Content-Type,Origin'
    return resp
