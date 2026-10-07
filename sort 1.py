scores = [(85, "Rohit"), (85, "Aditi")]
count = [0] * 101

for score, name in scores:
    count[score] += 1
for i in range(1, 101):
    count[i] += count[i - 1]

output = [None] * len(scores)
for i in range(len(scores) - 1, -1, -1):
    score, name = scores[i]
    output[count[score] - 1] = (score, name)
    count[score] -= 1

for score, name in output:
    print(f"{score} - {name}")