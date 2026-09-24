LAST_NAME = "DAVID" 
SEED_NUM = 0
FAVORITE_ARTIST = "OLIVIA"

# telemetry itels
def telemetry_stream():
    data = [
        SEED_NUM * 10,
        len(LAST_NAME) * 5,
        len(FAVORITE_ARTIST) * 4,
        SEED_NUM + 25,
        "invalid",
        55
    ]

    for value in data:
        yield value

# RECURSION: Trace abnormal condition
def trace_abnormal(value, limit, steps=0):
    if value <= limit:
        return [f"Step {steps}: Value {value} is within limit"]

    if steps >= 3:
        return [
            f"Step {steps}: Value {value} remains above limit {limit}",
            "Base condition reached"
        ]

    return [
        f"Step {steps}: Value {value} exceeds limit {limit}"
    ] + trace_abnormal(value - 5, limit, steps + 1)

# DECORATOR: Monitor processing function
def monitor(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("Executing:", func.__name__)

        result = func(*args, **kwargs)

        print("Completed:", func.__name__)
        return result

    wrapper.calls = 0
    return wrapper

@monitor
def process_telemetry(data_stream):
    processed = valid = invalid = abnormal = 0
    traces = []

    for raw in data_stream:
        processed += 1

        try:
            if not isinstance(raw, (int, float)):
                raise ValueError('non-numeric reading')

            val = float(raw)

            if val < 0:
                raise ValueError('negative reading')

            valid += 1

            if val > 40:
                abnormal += 1
                traces.append(trace_abnormal(val, 40))

        except (TypeError, ValueError):
            invalid += 1

    status = 'UNSAFE' if abnormal > 0 else 'SAFE'

    return {
        'processed': processed,
        'valid': valid,
        'invalid': invalid,
        'abnormal': abnormal,
        'status': status,
        'traces': traces
    }
# Generate & process
generated_data = list(telemetry_stream())

print("Generated Telemetry Data:", generated_data)

transformed = map(
    lambda x: x if isinstance(x, (int, float)) else x,
    generated_data
)

report = process_telemetry(transformed)

# Report
print('=' * 50)
print('      EXERCISE 3: TELEMETRY MONITORING')
print('=' * 50)
print(f'Student   : {LAST_NAME}')
print(f'Seed No.  : {SEED_NUM}')
print(f'Artist    : {FAVORITE_ARTIST}')
print('-' * 50)
print(f'Processed : {report["processed"]}')
print(f'Valid     : {report["valid"]}')
print(f'Invalid   : {report["invalid"]}')
print(f'Abnormal  : {report["abnormal"]}')
print(f'Status    : {report["status"]}')
print(f'Monitored : {process_telemetry.calls} call(s)')
print('-' * 50)

for i, trace in enumerate(report['traces'], 1):
    print(f'\nAbnormal Trace {i}:')
    for step in trace:
        print(f'  {step}')

print('\n=== END OF REPORT ===') 