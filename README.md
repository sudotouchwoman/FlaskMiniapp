# _FlaskMiniapp_
---
Flask app to handle requests from this [Streamlit app](https://github.com/sudotouchwoman/PythonSandbox)
Now it responses to **GET** requests from the app and loads files with some contents. The whole thing was done to test how app would behave when the server is _unreachable_ (it should load data from its local filesystem). The problem is that data management actually _should be independent from the data source_. That is what i consider myself working on later.