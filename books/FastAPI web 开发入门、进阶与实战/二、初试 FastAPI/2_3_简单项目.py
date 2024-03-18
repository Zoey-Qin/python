#!/usr/bin/env python3
from fastapi import FastAPI, APIRouter
from typing import Optional

# create app object
app = FastAPI(
		title = 'hello test',
        description = 'this is a test',
        version = '0.1.0',
        docs_url = '',
        redoc_url = ''
		)

prefix = '/api/v1'
# create a route 
@app.get('{prefix}/hello')
def app_hello(name: Optional[str] = None):
	return {'hello': name}