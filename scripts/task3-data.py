from tasks.mmlu import MMLU
from tasks.smoltalk import SmolTalk

mmlu = MMLU(subset="all", split="auxiliary_train")
smoltalk = SmolTalk(split="train")

print("mmlu size:", len(mmlu))
print("smoltalk size:", len(smoltalk))

print(f"mmlu example")
print(mmlu[1])

print("\n \n \n \n \n")

print(f"smoltalk example")
print(smoltalk[1])