from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


app = FastAPI()

# Load model and tokenizer
model_name_or_path = "./fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path).to("cuda" if torch.cuda.is_available() else "cpu")

class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50

@app.post("/generate/")
def generate_text(request: TextGenerationRequest):
    inputs = tokenizer(request.prompt, return_tensors='pt').to(model.device)
    outputs = model.generate(inputs['input_ids'], max_length=request.max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": generated_text}
