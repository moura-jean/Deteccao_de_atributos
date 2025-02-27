import google.generativeai as genai

# Configurar sua chave de API
API_KEY = "AIzaSyARwgO5v4XA3LxT5mTvOarQSHE-7wscrK0"
genai.configure(api_key=API_KEY)

# Listar todos os modelos disponíveis
for model in genai.list_models():
    print(f"Nome: {model.name}")
    print(f"Suporta imagens: {('image' in model.supported_generation_methods)}")
    print(f"Métodos suportados: {model.supported_generation_methods}")
    print("---------------------------")

# O modelo recomendado para processar imagens é o gemini-1.5-flash
print("\nModelo recomendado para imagens: gemini-1.5-flash")