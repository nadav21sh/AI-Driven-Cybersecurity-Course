
import pandas as pd
import numpy as np

np.random.seed(42)

N_SAMPLES = 1000
ATTACK_RATIO = 0.03

users = ["alice", "bob", "charlie", "david", "eve"]
countries = ["US", "IL", "DE", "FR", "CN"]
normal_ips = [f"192.168.1.{i}" for i in range(1, 50)]
attack_ips = [f"10.0.0.{i}" for i in range(1, 5)]

normal_size = int(N_SAMPLES * (1 - ATTACK_RATIO))

normal_data = {
    "hour": np.random.randint(8, 19, normal_size),
    "login_attempts": np.random.randint(1, 4, normal_size),
    "session_duration": np.random.normal(300, 50, normal_size).astype(int),
    "user": np.random.choice(users, normal_size),
    "source_ip": np.random.choice(normal_ips, normal_size),
    "country": np.random.choice(countries, normal_size),
    "label": np.zeros(normal_size, dtype=int)
}

attack_size = N_SAMPLES - normal_size

attack_data = {
    "hour": np.random.randint(0, 24, attack_size),
    "login_attempts": np.random.randint(20, 60, attack_size),
    "session_duration": np.random.normal(30, 10, attack_size).astype(int),
    "user": np.random.choice(users, attack_size),
    "source_ip": np.random.choice(attack_ips, attack_size),
    "country": np.random.choice(countries, attack_size),
    "label": np.ones(attack_size, dtype=int)
}

df = pd.concat(
    [pd.DataFrame(normal_data), pd.DataFrame(attack_data)],
    ignore_index=True
)

df.to_csv("login_events.csv", index=False)

print("Dataset generated: login_events.csv")
print(df["label"].value_counts(normalize=True))
