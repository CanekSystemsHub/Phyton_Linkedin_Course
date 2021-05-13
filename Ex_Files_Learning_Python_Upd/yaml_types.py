import yaml

with open("data_all.yml",'r') as f:

    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        for k, v in doc.items():
            print (k, type(v), v)
