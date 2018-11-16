from flask import Flask, request, json
import requests
import docker
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/AlorenaP/exam2/api/v1/images", methods=['POST'])
def image_merge():
    contentData=request.get_data()
    contentString=str(content, 'utf-8')
    jsonFile=json.loads(contentString)
    merged=jsonFile["pull_request"]["merged"]
    if merged:
        sha_id=jsonFile["pull_request"]["head"]["sha"]
        imageUrl="https://raw.githubusercontent.com/AlorenaP/sd2018b-exam2/"+sha_id+"/image.json"
        imageResponse=requests.get(imageUrl)
        image=json.loads(imageResponse.content)

        dockerFileUrl="https://raw.githubusercontent.com/AlorenaP/sd2018b-exam2/"+sha_id+"/Dockerfile"
        dockerFileResponse=requests.get(dockerfileUrl)
        file = open("Dockerfile","w")
        file.write(str(dockerFileResponse.content, 'utf-8')) 
        file.close()
        image_tag="192.168.99.100:5000/"+image["service_name"]+":"+image["version"]

        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        client.images.build(path="./", tag=image_tag)
        client.images.push(image_tag)
        client.images.remove(image=image_tag, force=True)
        return image_tag
    else:
        return "Pull request is not merged"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
