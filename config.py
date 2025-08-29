from pathlib import Path

LOCAL_T5_PATH = Path(r"C:\Users\Pc\Desktop\ai interview coach\flan-t5-base")
LOCAL_EMB_PATH = Path(r"C:\Users\Pc\Desktop\ai interview coach\all-MiniLM-L6-v2")

GEN_KWARGS = dict(max_new_tokens=128, num_beams=4)


# Generation settings tuned to reduce repetition
GEN_KWARGS = dict(
max_new_tokens=256,
num_beams=4,
do_sample=False,
repetition_penalty=1.15,
no_repeat_ngram_size=3,
)


# Scoring weights
SCORE_WEIGHTS = {
'similarity': 0.6,
'keywords': 0.25,
'structure': 0.1,
'length': 0.05,
}


MIN_WORDS = 30 # minimum words for a substantive answer