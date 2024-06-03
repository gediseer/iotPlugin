import os
import subprocess
from flask import Flask, Response, request, jsonify, send_from_directory  
  
app = Flask(__name__)  
  
    # 'cmd1': 'python ..\MiService\micli.py -did477054694 2-1=#false',  
    # 'cmd2': 'python ..\MiService\micli.py -did477054694 2-1=#true',  
    # 'cmd3': 'python ..\MiService\micli.py -did434455491 2-2=#0',#日光
    # 'cmd4': 'python ..\MiService\micli.py -did434455491 2-2=#1',  
    
@app.route('/', methods=['GET'])  
def get_nationality():  
    print("invoked!!!")
    name = request.args.get('name') 
    print(f"name : {name}")
    return jsonify(name=name, country=[{'country_id': 'US', 'probability': 1.0}]) 

@app.route('/file/api.yaml')  
def serve_static_file():  
    print("yaml !!!")
    file_path = os.path.abspath('iotServer/static/api.yaml')  
    with open(file_path, 'r') as file:  
        file_content = file.read()  
    return Response(file_content, mimetype='text/plain') 

@app.route('/ac/close', methods=['GET'])  
def get_closeac():  
    print(f"close AC")
    subprocess.run('python .\MiService\micli.py -did477054694 2-1=#false', shell=True)  
    return jsonify(result=0,message="success")  

@app.route('/ac/open', methods=['GET'])  
def get_openac():  
    print(f"open AC")
    subprocess.run('python .\MiService\micli.py -did477054694 2-1=#true', shell=True)  
    return jsonify(result=0,message="success")  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0') 
