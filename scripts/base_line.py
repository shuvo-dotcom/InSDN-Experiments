# ✅ Imports
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

# 📦 Load dataset (you can replace this with your custom dataset)
dataset = load_dataset("Abirate/english_quotes")
dataset = dataset["train"].train_test_split(test_size=0.1)
