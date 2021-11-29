import argparse
import json
import yaml

def json2yaml(jsonFile, yamlFile):
    with open(jsonFile,'r') as json_file:
        jsonObj = json.load(json_file)
        with open(yamlFile,'w') as yaml_file:
            yaml.safe_dump(jsonObj, yaml_file, default_flow_style=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFile", help="JSON file to parse", type=str)
    parser.add_argument("yamlFile", help="YAML file to produce from JSON", type=str)
    args = parser.parse_args()
    json2yaml(args.jsonFile,args.yamlFile)
    print(f'File {args.jsonFile} was successfully converted to {args.yamlFile}.')
