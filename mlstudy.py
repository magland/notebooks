import numpy
import requests
import json
from mdaio import mda_from_bytes

class MLStudyScript:
    def __init__(self):
        self._object={}
        self._results_object={}
    def setObject(self,obj):
        self._object=obj
    def setResultsObject(self,obj):
        self._results_object=obj
    def result(self,name):
        return self._results_object[name]['value']

class MLStudy:
    _docstor_url='https://docstor1.herokuapp.com'
    def __init__(self,id):
        self._study={}
        if id:
            self.load(id)
    def setDocStorUrl(self,url):
        self._docstor_url=url
    def load(self,id):
        req=requests.post(self._docstor_url+'/api/getDocument',json={"id":id,"include_content":True})
        if (req.status_code != 200):
            raise ValueError('Unable to load study with id: '+id)
        self._study=json.loads(req.json()['content'])
        return True
    def description(self):
        return self._study['description']
    def scriptNames(self):
        return self._study['scripts'].keys()
    def script(self,script_name):
        X=MLStudyScript()
        X.setObject(self._study['scripts'][script_name])
        X.setResultsObject(self._study['results_by_script'][script_name])
        return X;
    def datasetIds(self):
        return self._study['datasets'].keys()

class MLUtils:    
    def load(obj):
        if 'prv' in obj:
            url='https://kbucket.flatironinstitute.org/download/'+obj['prv']['original_checksum']
            req=requests.get(url)
            return req.content
    def loadText(obj):
        return MLUtils.load(obj).decode('utf-8')
    def loadJson(obj):
        return json.loads(MLUtils.loadText(obj))
    def loadMda(obj):
        return mda_from_bytes(MLUtils.load(obj))
