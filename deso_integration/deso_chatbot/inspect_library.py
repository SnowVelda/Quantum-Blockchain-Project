from neocitizen import NeocitiesApi

# Initialize with the key to be safe
api = NeocitiesApi(api_key="e629db8800d43833d4724eb190fa8b7e")

print("--- Methods available on NeocitiesApi object ---")
# Print all attributes and methods of the api object
for attr in dir(api):
    if not attr.startswith('_'):
        print(attr)

print("\n--- Help on the NeocitiesApi class ---")
help(NeocitiesApi)
