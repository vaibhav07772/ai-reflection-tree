import json

with open("../tree/reflection-tree.json") as f:
    tree_list = json.load(f)

tree = {node["id"]: node for node in tree_list}

state = {
    "answers": {},
    "signals": {}
}

current = "START"

while True:
    node = tree[current]
    print("\n" + node["text"])

    if node["type"] == "end":
        break

    elif node["type"] == "question":
        for i, opt in enumerate(node["options"]):
            print(f"{i+1}. {opt}")

        choice = int(input("Choose: ")) - 1
        selected = node["options"][choice]
        state["answers"][current] = selected

        # Signal tracking
        if "signal" in node:
            key = node["signal"]
            state["signals"][key] = state["signals"].get(key, 0) + 1

        current = node["next"]

    elif node["type"] == "decision":
        prev_q = list(state["answers"].keys())[-1]
        prev_ans = state["answers"][prev_q]
        current = node["rules"][prev_ans]

    else:
        current = node.get("next")

# final summary
print("\n--- SUMMARY ---")
print("Your signals:", state["signals"])