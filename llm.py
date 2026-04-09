from bytez import Bytez
import os
from dotenv import load_dotenv

load_dotenv()

sdk = Bytez(os.getenv("BYTEZ_API_KEY"))

model = sdk.model("zai-org/GLM-4.7")

def generate(prompt):
    results = model.run([
        {
            "role": "user",
            "content": prompt
        }
    ])

    if results.error:
        return f"Error: {results.error}"
    
    return results.output