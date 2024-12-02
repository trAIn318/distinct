
import os
from supabase import create_client, Client

def crate_ciente():
    url: str = os.environ.get("aws-0-us-east-1.pooler.supabase.com")
    key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtqdmNjbWtkaG1ocHlmbnJid252Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI4MDc5NDYsImV4cCI6MjA0ODM4Mzk0Nn0.yT6KhakBB7JseiD2tAsI8W5Sn4RX642bkJ2yR8vEQ-E")
    supabase: Client = create_client(url, key)
    return supabase

def test_func(conect):
  try:
    resp = conect.functions.invoke("hello-world", invoke_options={'body':{}})
    return resp
  except (FunctionsRelayError, FunctionsHttpError) as exception:
    err = exception.to_dict()
    print(err.get("message"))

def query(conect):
    response = conect.table("users").select("*").execute()
    # Assert we pulled real data.
    assert len(response.data) > 0
    # Assert we pulled real data.
    return response