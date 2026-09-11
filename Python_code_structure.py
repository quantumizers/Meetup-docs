from anuastra import Client

astra = Client(api_key='API Key')

# Define industry-standard OpenQASM 2.0
qasm_str = """
// Paste your QASM code here

"""

result = astra.execute_qasm(qasm_str, shots=1024)
print("Results Counts:", result['results']['counts'])
