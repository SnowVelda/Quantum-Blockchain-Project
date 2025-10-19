import zlib 
import base64 

def compress(data): 
 return base64.b64encode(zlib.compress(data)) 
