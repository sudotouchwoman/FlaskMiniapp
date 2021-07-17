## _FlaskMiniapp_
## 
Flask app to handle requests from this [Streamlit app](https://github.com/sudotouchwoman/PythonSandbox). The whole thing was done to test how app would behave when the server is _unreachable_ (if so, it should load data from its local filesystem).
## 
**Development notes**
+ **Update 1.1** Now it responses to **GET** requests from the app and loads files with some contents.  The problem is that data management actually _should be independent from the data source_. That is what i consider myself working on later.
+ **Update 1.2** Added _Docker_ integration. Tested out connection within compose network. The yaml can be found [here](https://github.com/sudotouchwoman/PythonSandbox/blob/master/st-app-docker-compose.yaml).