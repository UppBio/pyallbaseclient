graphql-generate:
	echo "Generating graphql client library files..."
	python -m sgqlc.introspection http://localhost:8080/query allbase.schema.json
	sgqlc-codegen schema ./allbase.schema.json ./pyallbaseclient/allbase_schema.py
