from elasticsearch import Elasticsearch 
from elasticsearch.exceptions import NotFoundError 
from typing import Dict 


#docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:tag 


class ES_DRIVER: 
    #Basic CRUD: Create-read-update-delete 
    def __init__(self): 
        self.es = Elasticsearch(['http://localhost:9200'], basic_auth=("elastic", "text_moderator"))
        self.index_name = "comment" 
        # Create an index if it doesn't exist 
        if not self.es.indices.exists(index=self.index_name): 
            self.create_index()
    
    def create_index(self): 
        mapping: Dict[str, Dict[str, Dict[str,str]]] = {
            "mappings": {
                "properties": {
                    "text": {"type": "text"}, 
                    "label": {"type": "keyword"}
                }
            }
        }
        self.es.indices.create(index = self.index_name, body=mapping)

    def create(self, comment:str, class_label: int) -> Dict[str,int]: 
        data: Dict[str,int] = {
            "text": comment, "label": class_label
        }
        return self.es.index(index=self.index_name, body = data)
    
    def read(self, commend_id: str) -> Dict[str,int]: 
        res = self.es.get(index =self.index_name, id=commend_id)
        return res["_source"] if "found" in res and res["found"] else None 
    
    def update(self,comment_id: str, new_text: str, new_label:int) -> Dict[str, Dict[str,int]]: 
        data: Dict[str, Dict[str,int]] = {
            "doc": {
                "text": new_text, "label": new_label
            }
        }
        return self.es.update(index = self.index_name, id = comment_id, body=data)
    def delete(self,comment_id: str) -> str: 
        try: 
            comment = self.es.get(index= self.index_name, id=comment_id)["_source"]
            result = self.es.delete(index=self.index_name, id=comment_id)
            if result['result'] == 'deleted': 
                return f"Comment with ID '{comment_id}' is deleted"
            else: 
                return f"Comment not found"
        except NotFoundError: 
            return f"Comment not found, nothing to delete"

if __name__ == "__main__": 
    comment_crud = ES_DRIVER()
