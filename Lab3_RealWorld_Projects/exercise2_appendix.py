LAST_NAME = "DAVID"
SEED_NUM = 0 
FAVORITE_ARTIST = "OLIVIA"

call_counter = 0

def create_fault_code():
    name_sum = sum(ord(c) for c in LAST_NAME)
    artist_len = len(FAVORITE_ARTIST)
    return (name_sum * SEED_NUM) % 100 + artist_len

def trace_fault(code, level=1):
    global call_counter 
    call_counter<= 1
    print(f"Level {level}: Checking fault code -> {code}")

    if code <= 10:
        print(f"level {level}: returning from level {level +1}")
        return code

    new_code = code // 2 + code % 2
    result = trace_fault(new_code, level +1)
    print(f"Level {level}: Returning from level {level+1}")
    return result

def run_fault_diagnostic():
    print("=" * 45)
    print("        RECURSIVE FAULT TRACE SYSTEM")
    print("=" * 45)
    print(f"Student: {LAST_NAME} | Seed: {SEED_NUM}")
    print(f"Reference: {FAVORITE_ARTIST}\n")

    fault_code = create_fault_code()
    print(f"Generated Fault Code: {fault_code}\nStarting trace...\n")

    final_result = trace_fault(fault_code)

    print("\n" + "=" * 45)
    print("         TRACE SUMMARY")
    print("=" * 45)
    print(f"Initial Fault Code:     {fault_code}")
    print(f"Final Resolved Value: {final_result}")
    print(f"Total Recursive Calls: {call_counter}")
    print("=" * 45)

run_fault_diagnostic()






