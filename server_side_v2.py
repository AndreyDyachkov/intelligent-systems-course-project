import socket
from rdflib import Graph
import os

def perform_sparql_query(query):
    # file_location = os.path.dirname(os.path.abspath(__file__))
    KB_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Project_knowledge_base_v2.n3")
    knowledge_base = Graph()
    knowledge_base.parse(file=open(KB_path, "r"), format="text/n3")

    # Perform SPARQL query on the knowledge base
    result = knowledge_base.query(query)
    dict ={}
    for row in result:
        label = str(row.asdict()['label'].toPython())
        threshold = str(row.asdict()['threshold'].toPython())
        dict[label] = threshold
    return dict

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    data = client_socket.recv(1024)
    print(f"Received request from client: {data.decode()}")

    # Check if the client's request is a SPARQL query
    if data.decode().startswith("SPARQL:"):
        sparql_query = data.decode()[7:]  # Extract the SPARQL query from the request

        # Perform the SPARQL query on the knowledge base
        result = perform_sparql_query(sparql_query)

        # Send the result back to the client
        client_socket.sendall(str(result).encode())
    else:
        response = "Sorry, I don't understand that request."

        # Send a general response back to the client
        client_socket.sendall(response.encode())

    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server_host = '127.0.0.1'  # localhost
    server_port = 12345

    start_server(server_host, server_port)
